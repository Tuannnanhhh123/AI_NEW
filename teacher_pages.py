# ============================================================
# teacher_pages.py — Giao diện dashboard giáo viên
# Tối ưu: cache bank file, cache DB queries, batch stats
# ============================================================
import os, ast, json, sqlite3
import streamlit as st
from config          import SUBJECT_OPTIONS, GRADE_CONFIG
from teacher_manager import (save_teacher_exam, get_teacher_exams,
                              delete_teacher_exam, get_exam_questions,
                              get_stats)
from assignment_manager import (create_assignment, deactivate_assignment,
                                delete_assignment, toggle_required,
                                get_all_assignments, get_submission_stats)
from user_manager import get_user_exams, get_user_stats, get_all_users

_MON_MAP = {
    "Toán":"toan","Ngữ Văn":"van","Tiếng Anh":"anh",
    "Vật Lý":"ly","Hóa Học":"hoa","Sinh Học":"sinh",
}
_LOP_MAP = {
    "Lớp 9 (THCS)":"l9","Lớp 10 (THPT)":"l10",
    "Lớp 11 (THPT)":"l11","Lớp 12 (THPT)":"l12",
    "Đại học / Nâng cao":"dh",
}

def _bank_path(subject: str, grade: str) -> str | None:
    mon = _MON_MAP.get(subject)
    lop = _LOP_MAP.get(grade)
    if not mon or not lop:
        return None
    return f"banks/{mon}_{lop}.py"


# ── Cache đọc bank file (TTL 60s) ────────────────────────
@st.cache_data(ttl=60, show_spinner=False)
def _read_bank(fpath: str) -> list:
    if not os.path.exists(fpath):
        return []
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for t in node.targets:
                    if isinstance(t, ast.Name) and t.id == "QUESTIONS":
                        return ast.literal_eval(node.value)
    except Exception:
        pass
    return []


def _write_bank(fpath: str, questions: list) -> tuple[bool, str]:
    try:
        os.makedirs(os.path.dirname(fpath), exist_ok=True)
        lines = ["QUESTIONS = [\n"]
        for q in questions:
            lines.append("    {\n")
            lines.append(f'        "question": {json.dumps(q["question"], ensure_ascii=False)},\n')
            lines.append(f'        "options": {json.dumps(q["options"], ensure_ascii=False)},\n')
            lines.append(f'        "answer": {json.dumps(q["answer"], ensure_ascii=False)},\n')
            lines.append(f'        "explanation": {json.dumps(q["explanation"], ensure_ascii=False)}\n')
            lines.append("    },\n")
        lines.append("]\n")
        with open(fpath, "w", encoding="utf-8") as f:
            f.writelines(lines)
        # Xóa cache sau khi ghi để lần sau đọc lại
        _read_bank.clear()
        return True, ""
    except Exception as e:
        return False, str(e)


def _append_to_bank(subject: str, grade: str, new_q: dict) -> tuple[bool, str]:
    fpath = _bank_path(subject, grade)
    if not fpath:
        return False, f"Không tìm thấy file bank cho {subject} / {grade}"
    questions = _read_bank(fpath)
    existing  = {q["question"].strip().lower() for q in questions}
    if new_q["question"].strip().lower() in existing:
        return False, "Câu hỏi này đã tồn tại trong ngân hàng!"
    questions.append(new_q)
    ok, err = _write_bank(fpath, questions)
    if ok:
        return True, f"✅ Đã lưu vào `{fpath}` — tổng {len(questions)} câu"
    return False, f"Lỗi ghi file: {err}"


# ── Cache query DB (TTL 30s) ──────────────────────────────
@st.cache_data(ttl=30, show_spinner=False)
def _cached_all_assignments() -> list:
    return get_all_assignments()

@st.cache_data(ttl=30, show_spinner=False)
def _cached_teacher_exams() -> list:
    return get_teacher_exams()

@st.cache_data(ttl=30, show_spinner=False)
def _cached_all_users() -> list:
    return get_all_users()

@st.cache_data(ttl=30, show_spinner=False)
def _cached_submission_stats(a_id: int) -> dict:
    return get_submission_stats(a_id)

@st.cache_data(ttl=30, show_spinner=False)
def _cached_user_exams(uname: str) -> list:
    return get_user_exams(uname)

@st.cache_data(ttl=30, show_spinner=False)
def _cached_user_stats(uname: str) -> dict:
    return get_user_stats(uname)

def _clear_caches():
    """Gọi sau mỗi thao tác ghi để invalidate cache."""
    _cached_all_assignments.clear()
    _cached_teacher_exams.clear()
    _cached_submission_stats.clear()
    _cached_all_users.clear()
    _cached_user_exams.clear()
    _cached_user_stats.clear()


# ── Entry point ───────────────────────────────────────────
def show_teacher_dashboard():
    st.markdown('<div class="main-title">👩‍🏫 Dashboard Giáo viên</div>',
                unsafe_allow_html=True)
    st.markdown(f'<div class="sub-title">Xin chào, {st.session_state.username}!</div>',
                unsafe_allow_html=True)
    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "➕ Thêm câu hỏi",
        "📝 Quản lý ngân hàng",
        "📋 Đề thi riêng",
        "📢 Giao đề",
        "📊 Thống kê HS",
    ])
    with tab1: _tab_add()
    with tab2: _tab_manage()
    with tab3: _tab_custom_exam()
    with tab4: _tab_assign()
    with tab5: _tab_stats()


# ── Tab 1: Thêm câu hỏi ──────────────────────────────────
def _tab_add():
    st.markdown("### ➕ Thêm câu hỏi vào ngân hàng")
    c1, c2 = st.columns(2)
    with c1: subject = st.selectbox("📚 Môn học", SUBJECT_OPTIONS, key="add_sub")
    with c2:
        avail_grades = [g for g, cfg in GRADE_CONFIG.items() if subject in cfg["subjects"]]
        grade = st.selectbox("🏫 Lớp", avail_grades, key="add_grade")

    fpath = _bank_path(subject, grade)
    count = len(_read_bank(fpath)) if fpath else 0
    st.caption(f"📦 `{fpath}` — hiện có **{count} câu**")
    st.markdown("---")

    question = st.text_area("❓ Nội dung câu hỏi", height=100, key="add_q",
                             placeholder="Nhập câu hỏi tại đây...")
    st.markdown("**4 đáp án:**")
    c1, c2 = st.columns(2)
    with c1:
        opt_a = st.text_input("A", key="opt_a", placeholder="Đáp án A")
        opt_b = st.text_input("B", key="opt_b", placeholder="Đáp án B")
    with c2:
        opt_c = st.text_input("C", key="opt_c", placeholder="Đáp án C")
        opt_d = st.text_input("D", key="opt_d", placeholder="Đáp án D")

    options    = [opt_a, opt_b, opt_c, opt_d]
    valid_opts = [o for o in options if o.strip()]
    answer      = st.selectbox("✅ Đáp án đúng", valid_opts if valid_opts else ["—"], key="add_ans")
    explanation = st.text_area("💡 Giải thích", height=80, key="add_exp",
                                placeholder="Giải thích tại sao đáp án đúng...")

    if st.button("💾 Lưu vào ngân hàng", type="primary", use_container_width=True):
        errs = []
        if not question.strip():    errs.append("Chưa nhập câu hỏi")
        if len(valid_opts) != 4:    errs.append("Cần đúng 4 đáp án không rỗng")
        if len(set(options)) != 4:  errs.append("4 đáp án phải khác nhau")
        if answer not in options:   errs.append("Đáp án đúng phải là một trong 4 options")
        if not explanation.strip(): errs.append("Chưa nhập giải thích")
        if errs:
            for e in errs: st.error(e)
        else:
            new_q = {
                "question":    question.strip(),
                "options":     [o.strip() for o in options],
                "answer":      answer.strip(),
                "explanation": explanation.strip(),
            }
            ok, msg = _append_to_bank(subject, grade, new_q)
            if ok:
                st.success(msg)
                st.balloons()
                st.rerun()
            else:
                st.error(f"❌ {msg}")


# ── Tab 2: Quản lý ngân hàng ─────────────────────────────
def _tab_manage():
    st.markdown("### 📝 Quản lý ngân hàng câu hỏi")
    c1, c2 = st.columns(2)
    with c1: subject = st.selectbox("📚 Môn", SUBJECT_OPTIONS, key="mgr_sub")
    with c2:
        avail_grades = [g for g, cfg in GRADE_CONFIG.items() if subject in cfg["subjects"]]
        grade = st.selectbox("🏫 Lớp", avail_grades, key="mgr_grade")

    fpath     = _bank_path(subject, grade)
    questions = _read_bank(fpath) if fpath else []

    if not questions:
        st.info(f"File `{fpath}` chưa có câu hỏi nào."); return

    st.markdown(f"**{len(questions)} câu** trong `{fpath}`:")
    st.markdown("---")

    for i, q in enumerate(questions):
        with st.expander(f"**{i+1}.** {q['question'][:70]}{'...' if len(q['question'])>70 else ''}"):
            new_q   = st.text_area("Câu hỏi", q["question"], key=f"eq_{i}")
            c1, c2  = st.columns(2)
            new_opts = []
            for j, opt in enumerate(q["options"]):
                col = c1 if j < 2 else c2
                new_opts.append(col.text_input(f"Đáp án {['A','B','C','D'][j]}", opt, key=f"eo_{i}_{j}"))
            new_ans = st.selectbox("Đáp án đúng", new_opts,
                                    index=new_opts.index(q["answer"]) if q["answer"] in new_opts else 0,
                                    key=f"ea_{i}")
            new_exp = st.text_area("Giải thích", q["explanation"], key=f"ee_{i}")

            ca, cb = st.columns(2)
            with ca:
                if st.button("💾 Lưu thay đổi", key=f"save_{i}", use_container_width=True):
                    questions[i] = {
                        "question":    new_q.strip(),
                        "options":     [o.strip() for o in new_opts],
                        "answer":      new_ans.strip(),
                        "explanation": new_exp.strip(),
                    }
                    ok, err = _write_bank(fpath, questions)
                    if ok: st.success("✅ Đã lưu!"); st.rerun()
                    else:  st.error(f"❌ {err}")
            with cb:
                if st.button("🗑️ Xóa câu này", key=f"del_{i}", use_container_width=True):
                    questions.pop(i)
                    ok, err = _write_bank(fpath, questions)
                    if ok: st.success("Đã xóa!"); st.rerun()
                    else:  st.error(f"❌ {err}")


# ── Tab 3: Đề thi riêng ───────────────────────────────────
def _tab_custom_exam():
    st.markdown("### 📋 Tạo đề thi riêng")

    with st.expander("➕ Tạo đề thi mới", expanded=True):
        exam_name = st.text_input("Tên đề thi", placeholder="VD: Đề kiểm tra 15 phút Toán 12")
        c1, c2 = st.columns(2)
        with c1: ex_sub = st.selectbox("Môn", SUBJECT_OPTIONS, key="ex_sub")
        with c2:
            avail  = [g for g, cfg in GRADE_CONFIG.items() if ex_sub in cfg["subjects"]]
            ex_grade = st.selectbox("Lớp", avail, key="ex_grade")

        fpath   = _bank_path(ex_sub, ex_grade)
        qs_pool = _read_bank(fpath) if fpath else []

        if not qs_pool:
            st.warning(f"File `{fpath}` chưa có câu hỏi nào.")
        else:
            st.markdown(f"**Chọn câu hỏi** (pool: {len(qs_pool)} câu):")
            selected_qs = []
            for i, q in enumerate(qs_pool):
                if st.checkbox(f"{q['question'][:80]}{'...' if len(q['question'])>80 else ''}",
                               key=f"sel_{i}"):
                    selected_qs.append(q)
            st.caption(f"Đã chọn: {len(selected_qs)} câu")

            if st.button("💾 Lưu đề thi", type="primary", use_container_width=True):
                if not exam_name.strip():
                    st.error("Chưa nhập tên đề thi!")
                elif not selected_qs:
                    st.error("Chưa chọn câu hỏi nào!")
                else:
                    from teacher_manager import add_question, approve_question
                    ids = []
                    for q in selected_qs:
                        qid = add_question(ex_sub, ex_grade, q["question"], q["options"],
                                           q["answer"], q["explanation"],
                                           created_by=st.session_state.username)
                        approve_question(qid, True)
                        ids.append(qid)
                    save_teacher_exam(exam_name.strip(), ex_sub, ex_grade, ids)
                    _clear_caches()
                    st.success("✅ Đã lưu đề thi!"); st.rerun()

    st.markdown("---")
    st.markdown("### 📚 Danh sách đề đã tạo")
    # Dùng cache thay vì gọi DB trực tiếp
    exams = _cached_teacher_exams()
    if not exams:
        st.info("Chưa có đề thi nào."); return

    for ex in exams:
        with st.expander(
            f"📋 {ex['name']} | {ex['subject']} / "
            f"{ex['grade'].split('(')[0].strip()} | {len(ex['q_ids'])} câu"
        ):
            st.caption(f"Tạo lúc: {ex['created_at']}")
            qs = get_exam_questions(ex["q_ids"])
            for i, q in enumerate(qs):
                st.markdown(f"**{i+1}.** {q['question']}")
                for j, opt in enumerate(q["options"]):
                    mark = "✅" if opt == q["answer"] else "　"
                    st.markdown(f"&nbsp;&nbsp;{mark} {['A','B','C','D'][j]}. {opt}")
            if st.button("🗑️ Xóa đề này", key=f"delex_{ex['id']}", use_container_width=True):
                delete_teacher_exam(ex["id"])
                _clear_caches()
                st.warning("Đã xóa!"); st.rerun()


# ── Tab 4: Giao đề ────────────────────────────────────────
def _tab_assign():
    st.markdown("### 📢 Giao đề cho học sinh")

    with st.expander("➕ Giao đề mới", expanded=True):
        title = st.text_input("📌 Tiêu đề", placeholder="VD: Kiểm tra 15p Toán 12 — Tuần 3")
        c1, c2 = st.columns(2)
        with c1: a_sub = st.selectbox("📚 Môn", SUBJECT_OPTIONS, key="as_sub")
        with c2:
            avail   = [g for g, cfg in GRADE_CONFIG.items() if a_sub in cfg["subjects"]]
            a_grade = st.selectbox("🏫 Lớp", avail, key="as_grade")

        # Dùng cache
        exams     = _cached_teacher_exams()
        exam_opts = {"🎲 Random từ ngân hàng": None}
        exam_opts.update({f"📋 {e['name']}": e["id"] for e in exams
                          if e["subject"] == a_sub and e["grade"] == a_grade})
        exam_choice = st.selectbox("📄 Đề thi", list(exam_opts.keys()), key="as_exam")
        exam_id     = exam_opts[exam_choice]

        c1, c2 = st.columns(2)
        with c1:
            use_dl = st.checkbox("⏰ Đặt deadline", key="as_use_dl")
            if use_dl:
                dl_date  = st.date_input("Ngày", key="as_date")
                dl_time  = st.time_input("Giờ",  key="as_time")
                deadline = f"{dl_date} {dl_time.strftime('%H:%M')}"
            else:
                deadline = None
        with c2:
            is_required = st.radio("⚠️ Mức độ",
                                    ["🔴 Bắt buộc", "🟡 Nhắc nhở"],
                                    key="as_req") == "🔴 Bắt buộc"

        if st.button("📢 Giao đề ngay", type="primary", use_container_width=True):
            if not title.strip():
                st.error("Chưa nhập tiêu đề!")
            else:
                create_assignment(title=title.strip(), subject=a_sub, grade=a_grade,
                                  exam_id=exam_id, deadline=deadline,
                                  is_required=is_required,
                                  created_by=st.session_state.username)
                _clear_caches()
                st.success(f"✅ Đã giao đề **{title}**!"); st.rerun()

    st.markdown("---")
    st.markdown("### 📋 Đề đã giao")

    # Dùng cache — không gọi DB mỗi lần render
    all_assigns = _cached_all_assignments()
    if not all_assigns:
        st.info("Chưa có đề nào được giao."); return

    for a in all_assigns:
        # Dùng cache stats theo assignment_id
        stats    = _cached_submission_stats(a["id"])
        req_icon = "🔴" if a["is_required"] else "🟡"
        status   = "✅ Active" if a["is_active"] else "⛔ Ẩn"
        dl_str   = f"⏰ {a['deadline']}" if a["deadline"] else "Không hạn"

        with st.expander(
            f"{req_icon} {a['title']} | {a['subject']} "
            f"{a['grade'].split('(')[0].strip()} | {dl_str} | {status} | 👥 {stats['count']} nộp"
        ):
            c1, c2, c3 = st.columns(3)
            c1.metric("👥 Đã nộp",  stats["count"])
            c2.metric("📈 TB điểm", f"{stats['avg_pct']}%")
            c3.metric("⚠️ Mức độ",  "Bắt buộc" if a["is_required"] else "Nhắc nhở")

            if stats["subs"]:
                st.markdown("**Kết quả:**")
                for s in stats["subs"]:
                    color = "#1e8e3e" if s["pct"]>=80 else ("#f4a300" if s["pct"]>=60 else "#d93025")
                    st.markdown(
                        f"- 👤 **{s['username']}** — "
                        f"<span style='color:{color};font-weight:700'>"
                        f"{s['score']}/{s['total']} ({s['pct']}%)</span> lúc {s['submitted_at']}",
                        unsafe_allow_html=True)

            st.markdown("---")
            ca, cb, cc = st.columns(3)
            with ca:
                lbl = "🟡 Nhắc nhở" if a["is_required"] else "🔴 Bắt buộc"
                if st.button(lbl, key=f"tog_{a['id']}", use_container_width=True):
                    toggle_required(a["id"], not a["is_required"])
                    _clear_caches(); st.rerun()
            with cb:
                lbl2 = "⛔ Ẩn" if a["is_active"] else "✅ Kích hoạt"
                if st.button(lbl2, key=f"act_{a['id']}", use_container_width=True):
                    if a["is_active"]:
                        deactivate_assignment(a["id"])
                    else:
                        with sqlite3.connect("teacher_bank.db") as con:
                            con.execute("UPDATE assignments SET is_active=1 WHERE id=?", (a["id"],))
                    _clear_caches(); st.rerun()
            with cc:
                if st.button("🗑️ Xóa", key=f"delA_{a['id']}", use_container_width=True):
                    delete_assignment(a["id"])
                    _clear_caches()
                    st.success("Đã xóa!"); st.rerun()


# ── Tab 5: Thống kê học sinh ──────────────────────────────
def _tab_stats():
    st.markdown("### 📊 Thống kê kết quả học sinh")

    st.markdown("**📦 Ngân hàng câu hỏi (banks/*.py):**")
    bank_cols = st.columns(3)
    idx = 0
    for subject in SUBJECT_OPTIONS:
        for grade in GRADE_CONFIG:
            fpath = _bank_path(subject, grade)
            if fpath and os.path.exists(fpath):
                count = len(_read_bank(fpath))
                if count > 0:
                    bank_cols[idx % 3].metric(
                        f"{subject} / {grade.split('(')[0].strip()}",
                        f"{count} câu", fpath)
                    idx += 1

    st.markdown("---")

    # Dùng cache
    users = _cached_all_users()
    if not users:
        st.info("Chưa có học sinh nào làm bài."); return

    st.markdown("**👨‍🎓 Kết quả học sinh:**")
    c1, c2 = st.columns(2)
    with c1: filter_sub  = st.selectbox("Lọc môn", ["Tất cả"] + SUBJECT_OPTIONS, key="st_sub")
    with c2: filter_user = st.selectbox("Lọc HS",  ["Tất cả"] + users,            key="st_usr")

    target_users = [filter_user] if filter_user != "Tất cả" else users

    for uname in target_users:
        # Dùng cache thay vì gọi Firestore mỗi lần
        exams = _cached_user_exams(uname)
        if filter_sub != "Tất cả":
            exams = [e for e in exams if e["subject"] == filter_sub]
        if not exams:
            continue

        stats = _cached_user_stats(uname)
        with st.expander(f"👤 {uname} — {len(exams)} bài thi"):
            stat_cols = st.columns(min(len(stats), 3))
            for col, (subj, s) in zip(stat_cols, stats.items()):
                if filter_sub == "Tất cả" or subj == filter_sub:
                    col.metric(f"📘 {subj}", f"TB: {s['avg']}%",
                               f"{s['count']} lần | Cao: {s['best']}%")
            st.markdown("**Chi tiết:**")
            for e in reversed(exams):
                if filter_sub != "Tất cả" and e["subject"] != filter_sub:
                    continue
                pct   = e["pct"]
                color = "#1e8e3e" if pct>=80 else ("#f4a300" if pct>=60 else "#d93025")
                st.markdown(
                    f"- {e['date']} | **{e['subject']}** "
                    f"{e['grade'].split('(')[0].strip()} | "
                    f"<span style='color:{color};font-weight:700'>"
                    f"{e['score']}/{e['total']} ({pct}%)</span>",
                    unsafe_allow_html=True)
