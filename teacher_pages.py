# ============================================================
# teacher_pages.py — FULL OPTIMIZED SAFE VERSION
# ============================================================

import os
import json
import random
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

PAGE_SIZE = 10


# ============================================================
# JSON BANK
# ============================================================

def _bank_path(subject, grade):
    mon = subject.lower().replace(" ", "")
    lop = grade.split()[1].lower()
    return f"banks/{mon}_{lop}.json"


@st.cache_data(ttl=120)
def _read_bank(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _write_bank(path, data):
    os.makedirs("banks", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    _read_bank.clear()


# ============================================================
# CACHE
# ============================================================

@st.cache_data(ttl=30)
def _cached_assignments():
    return get_all_assignments()

@st.cache_data(ttl=30)
def _cached_submission_stats():
    return get_all_submission_stats()

@st.cache_data(ttl=30)
def _cached_users():
    return get_all_users()

def _clear_cache():
    _cached_assignments.clear()
    _cached_submission_stats.clear()
    _cached_users.clear()


# ============================================================
# DASHBOARD
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
# TAB ASSIGN (KHÔNG CRASH)
# ============================================================

def _tab_assign():

    assignments = _cached_assignments()
    all_stats = _cached_submission_stats() or {}

    if not isinstance(all_stats, dict):
        all_stats = {}

    if not assignments:
        st.info("Chưa có đề nào.")
        return

    for a in assignments:

        stats = all_stats.get(a["id"], {
            "count": 0,
            "avg_pct": 0,
            "subs": []
        })

        with st.expander(f"{a['title']} — {stats['count']} nộp"):

            st.metric("Đã nộp", stats["count"])
            st.metric("TB điểm", f"{stats['avg_pct']}%")

            if stats["subs"]:
                for s in stats["subs"]:
                    st.write(
                        f"{s['username']} — "
                        f"{s['score']}/{s['total']} ({s['pct']}%)"
                    )

            if st.button("🗑️ Xóa", key=f"del_{a['id']}"):
                delete_assignment(a["id"])
                _clear_cache()
                st.rerun()


# ============================================================
# TAB STATS
# ============================================================

def _tab_stats():

    users = _cached_users()

    if not users:
        st.info("Chưa có dữ liệu.")
        return

    selected = st.selectbox("Chọn học sinh", users)

    exams = get_user_exams(selected)
    stats = get_user_stats(selected)

    st.write("Thống kê:", stats)

    for e in exams:
        st.write(e)
