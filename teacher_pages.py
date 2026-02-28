# ============================================================
# teacher_pages.py — Optimized Version
# High performance / scalable
# ============================================================

import os
import json
import random
import sqlite3
import streamlit as st

from config import SUBJECT_OPTIONS, GRADE_CONFIG
from teacher_manager import (
    save_teacher_exam, get_teacher_exams,
    delete_teacher_exam, get_exam_questions
)
from assignment_manager import (
    create_assignment, deactivate_assignment,
    delete_assignment, toggle_required,
    get_all_assignments, get_all_submission_stats
)
from user_manager import (
    get_user_exams, get_user_stats, get_all_users
)

# ============================================================
# CONFIG
# ============================================================

PAGE_SIZE = 10

_MON_MAP = {
    "Toán": "toan",
    "Ngữ Văn": "van",
    "Tiếng Anh": "anh",
    "Vật Lý": "ly",
    "Hóa Học": "hoa",
    "Sinh Học": "sinh",
}

_LOP_MAP = {
    "Lớp 9 (THCS)": "l9",
    "Lớp 10 (THPT)": "l10",
    "Lớp 11 (THPT)": "l11",
    "Lớp 12 (THPT)": "l12",
    "Đại học / Nâng cao": "dh",
}

# ============================================================
# BANK HANDLING (JSON — FAST)
# ============================================================

def _bank_path(subject: str, grade: str):
    mon = _MON_MAP.get(subject)
    lop = _LOP_MAP.get(grade)
    if not mon or not lop:
        return None
    return f"banks/{mon}_{lop}.json"


@st.cache_data(ttl=120)
def _read_bank(path):
    if not path or not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _write_bank(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    _read_bank.clear()


# ============================================================
# CACHE DB (BATCH)
# ============================================================

@st.cache_data(ttl=30)
def _cached_assignments():
    return get_all_assignments()

@st.cache_data(ttl=30)
def _cached_submission_stats():
    return get_all_submission_stats()

@st.cache_data(ttl=30)
def _cached_teacher_exams():
    return get_teacher_exams()

@st.cache_data(ttl=30)
def _cached_users():
    return get_all_users()

def _clear_cache():
    _cached_assignments.clear()
    _cached_submission_stats.clear()
    _cached_teacher_exams.clear()
    _cached_users.clear()


# ============================================================
# DASHBOARD ENTRY
# ============================================================

def show_teacher_dashboard():

    st.title("👩‍🏫 Dashboard Giáo viên")
    st.caption(f"Xin chào, {st.session_state.username}")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "➕ Thêm câu hỏi",
        "📝 Ngân hàng",
        "📋 Đề thi riêng",
        "📢 Giao đề",
        "📊 Thống kê"
    ])

    with tab1:
        _tab_add()

    with tab2:
        _tab_manage()

    with tab3:
        _tab_exam()

    with tab4:
        _tab_assign()

    with tab5:
        _tab_stats()


# ============================================================
# TAB 1 — ADD QUESTION
# ============================================================

def _tab_add():

    subject = st.selectbox("Môn", SUBJECT_OPTIONS)
    grades = [g for g, cfg in GRADE_CONFIG.items() if subject in cfg["subjects"]]
    grade = st.selectbox("Lớp", grades)

    path = _bank_path(subject, grade)
    questions = _read_bank(path)

    st.caption(f"Hiện có {len(questions)} câu")

    question = st.text_area("Câu hỏi")

    options = []
    cols = st.columns(2)
    for i in range(4):
        col = cols[i % 2]
        options.append(col.text_input(f"Đáp án {['A','B','C','D'][i]}"))

    answer = st.selectbox("Đáp án đúng", options)
    explanation = st.text_area("Giải thích")

    if st.button("Lưu", use_container_width=True):

        if not question or len(set(options)) != 4:
            st.error("Dữ liệu chưa hợp lệ")
            return

        questions.append({
            "question": question.strip(),
            "options": options,
            "answer": answer,
            "explanation": explanation.strip()
        })

        _write_bank(path, questions)
        st.success("Đã lưu")
        st.rerun()


# ============================================================
# TAB 2 — MANAGE (PAGINATION + SEARCH)
# ============================================================

def _tab_manage():

    subject = st.selectbox("Môn", SUBJECT_OPTIONS, key="m_sub")
    grades = [g for g, cfg in GRADE_CONFIG.items() if subject in cfg["subjects"]]
    grade = st.selectbox("Lớp", grades, key="m_grade")

    path = _bank_path(subject, grade)
    questions = _read_bank(path)

    if not questions:
        st.info("Chưa có câu hỏi")
        return

    search = st.text_input("Tìm kiếm")
    if search:
        questions = [q for q in questions if search.lower() in q["question"].lower()]

    total_pages = (len(questions) - 1) // PAGE_SIZE + 1
    page = st.number_input("Trang", 1, total_pages, 1)

    start = (page - 1) * PAGE_SIZE
    end = start + PAGE_SIZE

    for i, q in enumerate(questions[start:end], start=start):

        with st.expander(f"{i+1}. {q['question'][:60]}"):

            if st.button("Xóa", key=f"del_{i}"):
                questions.pop(i)
                _write_bank(path, questions)
                st.rerun()


# ============================================================
# TAB 3 — EXAM (NO MASS CHECKBOX)
# ============================================================

def _tab_exam():

    exams = _cached_teacher_exams()

    subject = st.selectbox("Môn", SUBJECT_OPTIONS, key="ex_sub")
    grades = [g for g, cfg in GRADE_CONFIG.items() if subject in cfg["subjects"]]
    grade = st.selectbox("Lớp", grades, key="ex_grade")

    path = _bank_path(subject, grade)
    pool = _read_bank(path)

    if not pool:
        st.warning("Ngân hàng trống")
        return

    num_q = st.slider("Số câu", 1, len(pool), min(10, len(pool)))

    if st.button("Tạo đề random"):

        selected = random.sample(pool, num_q)
        ids = []

        from teacher_manager import add_question, approve_question

        for q in selected:
            qid = add_question(subject, grade,
                               q["question"],
                               q["options"],
                               q["answer"],
                               q["explanation"],
                               created_by=st.session_state.username)
            approve_question(qid, True)
            ids.append(qid)

        save_teacher_exam("Đề random", subject, grade, ids)
        _clear_cache()
        st.success("Đã tạo đề")
        st.rerun()


# ============================================================
# TAB 4 — ASSIGN (BATCH STATS)
# ============================================================

def _tab_assign():

    assignments = _cached_assignments()
    all_stats = _cached_submission_stats()

    for a in assignments:

        stats = all_stats.get(a["id"], {
            "count": 0,
            "avg_pct": 0,
            "subs": []
        })

        with st.expander(f"{a['title']} — {stats['count']} nộp"):

            st.metric("Đã nộp", stats["count"])
            st.metric("TB điểm", f"{stats['avg_pct']}%")

            if st.button("Xóa", key=f"a_{a['id']}"):
                delete_assignment(a["id"])
                _clear_cache()
                st.rerun()


# ============================================================
# TAB 5 — STATS (LOAD ONE USER ONLY)
# ============================================================

def _tab_stats():

    users = _cached_users()

    if not users:
        st.info("Chưa có dữ liệu")
        return

    selected = st.selectbox("Chọn học sinh", users)

    exams = get_user_exams(selected)
    stats = get_user_stats(selected)

    st.write(stats)

    for e in exams:
        st.write(e)
