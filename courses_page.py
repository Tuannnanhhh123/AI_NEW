# ============================================================
# courses_page.py — Trang khóa học (học sinh + giáo viên)
# ============================================================
import time
import streamlit as st

from config         import SUBJECT_OPTIONS, GRADE_CONFIG
from course_manager import (
    get_all_courses, get_course, create_course, update_course, delete_course,
    add_chapter, update_chapter, delete_chapter,
    add_lesson, update_lesson, delete_lesson,
    get_progress, mark_lesson_done, issue_certificate,
    calc_progress_pct, count_total_lessons,
    search_youtube, get_youtube_embed,
)

_SUBJ_ICONS = {
    "Toán":"🔢","Ngữ Văn":"📖","Tiếng Anh":"🇬🇧",
    "Vật Lý":"⚡","Hóa Học":"⚗️","Sinh Học":"🧬",
}
_LEVEL_COLOR = {
    "Cơ bản":    ("#e8f5e9","#2e7d32"),
    "Trung bình":("#fff3e0","#e65100"),
    "Nâng cao":  ("#fce4ec","#880e4f"),
}

# ── CSS ──────────────────────────────────────────────────
_CSS = """
<style>
/* Course card */
.course-card {
    background:#fff; border-radius:16px; padding:1.2rem;
    border:1px solid #e0e7ff; margin-bottom:.75rem;
    box-shadow:0 2px 8px rgba(67,56,202,.06);
    transition:transform .2s,box-shadow .2s;
    cursor:pointer;
}
.course-card:hover {
    transform:translateY(-3px);
    box-shadow:0 8px 24px rgba(67,56,202,.13);
    border-color:#a5b4fc;
}
.cc-top   { display:flex; align-items:flex-start; gap:1rem; margin-bottom:.75rem; }
.cc-emoji { font-size:2.5rem; flex-shrink:0; line-height:1; }
.cc-info  { flex:1; min-width:0; }
.cc-title { font-size:.95rem; font-weight:800; color:#1e1b4b; margin-bottom:.2rem; }
.cc-meta  { font-size:.75rem; color:#888; display:flex; gap:.6rem; flex-wrap:wrap; }
.cc-desc  { font-size:.8rem; color:#555; margin-bottom:.75rem; line-height:1.5; }
.cc-tags  { display:flex; gap:.4rem; flex-wrap:wrap; margin-bottom:.6rem; }
.cc-tag   { font-size:.68rem; font-weight:700; padding:.2rem .55rem;
            border-radius:999px; }
.cc-prog  { margin-top:.5rem; }
.prog-bar { height:6px; background:#e0e7ff; border-radius:99px; overflow:hidden; margin:.3rem 0 .2rem; }
.prog-fill{ height:100%; border-radius:99px;
            background:linear-gradient(90deg,#4338ca,#3b82f6); transition:width .4s; }

/* Lesson item */
.lesson-item {
    display:flex; align-items:center; gap:.75rem;
    padding:.65rem .9rem; border-radius:10px;
    border:1px solid #e5e7eb; margin-bottom:.4rem;
    background:#fafbff; transition:all .2s; cursor:pointer;
}
.lesson-item:hover { background:#f0f4ff; border-color:#c7d2fe; }
.lesson-item.done  { background:#f0fdf4; border-color:#bbf7d0; }
.lesson-item.locked{ background:#f9fafb; border-color:#e5e7eb; opacity:.6; cursor:not-allowed; }
.li-icon  { font-size:1.1rem; flex-shrink:0; }
.li-title { flex:1; font-size:.85rem; font-weight:600; color:#1e1b4b; }
.li-meta  { font-size:.72rem; color:#9ca3af; white-space:nowrap; }
.li-badge { font-size:.65rem; font-weight:700; padding:.15rem .45rem;
            border-radius:999px; }

/* Chapter header */
.ch-header {
    display:flex; align-items:center; gap:.6rem;
    padding:.55rem .8rem; background:#f0f4ff;
    border-radius:10px; margin-bottom:.4rem;
    border-left:4px solid #4338ca;
}
.ch-num   { background:#4338ca; color:#fff; font-size:.7rem; font-weight:800;
            padding:.2rem .5rem; border-radius:6px; flex-shrink:0; }
.ch-title { font-size:.88rem; font-weight:700; color:#1e1b4b; flex:1; }
.ch-count { font-size:.72rem; color:#9ca3af; }

/* Video container */
.video-wrap {
    border-radius:14px; overflow:hidden;
    margin-bottom:1rem; background:#000;
    box-shadow:0 4px 20px rgba(0,0,0,.15);
}

/* Quiz */
.quiz-wrap {
    background:linear-gradient(135deg,#f0f4ff,#faf5ff);
    border:1px solid #e0e7ff; border-radius:14px;
    padding:1rem 1.2rem; margin-top:1rem;
}
.quiz-title { font-size:.85rem; font-weight:800; color:#4338ca; margin-bottom:.75rem; }

/* Certificate */
.cert-card {
    background:linear-gradient(135deg,#fffbeb,#fef3c7);
    border:2px solid #f59e0b; border-radius:16px;
    padding:1.5rem; text-align:center;
}
.cert-title { font-size:1.2rem; font-weight:800; color:#92400e; margin-bottom:.3rem; }
.cert-sub   { font-size:.82rem; color:#b45309; }

/* Search result */
.yt-card {
    display:flex; gap:.75rem; align-items:center;
    background:#fff; border:1px solid #e5e7eb; border-radius:12px;
    padding:.65rem; margin-bottom:.5rem;
    transition:border-color .2s;
}
.yt-card:hover { border-color:#c7d2fe; }
.yt-thumb { width:80px; height:54px; border-radius:8px;
            object-fit:cover; flex-shrink:0; background:#e0e7ff; }
.yt-info  { flex:1; min-width:0; }
.yt-title { font-size:.8rem; font-weight:600; color:#1e1b4b;
            display:-webkit-box; -webkit-line-clamp:2;
            -webkit-box-orient:vertical; overflow:hidden; }
.yt-ch    { font-size:.7rem; color:#9ca3af; margin-top:.2rem; }

/* Section title */
.sec-t {
    font-size:.68rem; font-weight:700; color:#94a3b8;
    letter-spacing:.08em; text-transform:uppercase;
    margin:.8rem 0 .5rem;
}
</style>
"""


# ═══════════════════════════════════════════════════════════
# TRANG HỌC SINH
# ═══════════════════════════════════════════════════════════

def show_courses():
    st.markdown(_CSS, unsafe_allow_html=True)
    uid   = st.session_state.get("uid", "")
    uname = st.session_state.get("username", "")

    # ── State nội bộ ──────────────────────────────────────
    if "course_view"   not in st.session_state: st.session_state["course_view"]   = "list"
    if "active_course" not in st.session_state: st.session_state["active_course"] = None
    if "active_lesson" not in st.session_state: st.session_state["active_lesson"] = None
    if "quiz_answers"  not in st.session_state: st.session_state["quiz_answers"]  = {}
    if "quiz_submitted" not in st.session_state: st.session_state["quiz_submitted"] = False

    view = st.session_state["course_view"]

    # ── View: danh sách khóa học ──────────────────────────
    if view == "list":
        _show_course_list(uid)

    # ── View: chi tiết khóa học ───────────────────────────
    elif view == "detail":
        _show_course_detail(uid, uname)

    # ── View: xem bài học ─────────────────────────────────
    elif view == "lesson":
        _show_lesson(uid, uname)


# ── Danh sách khóa học ───────────────────────────────────
def _show_course_list(uid: str):
    st.markdown("## 📚 Khóa học")

    courses = get_all_courses()

    # Bộ lọc
    col_s, col_g, col_search = st.columns([2, 2, 3])
    with col_s:
        subj_opts = ["Tất cả"] + SUBJECT_OPTIONS
        sel_subj  = st.selectbox("📚 Môn", subj_opts, key="cs_subj",
                                  label_visibility="collapsed")
    with col_g:
        grade_opts = ["Tất cả lớp"] + list(GRADE_CONFIG.keys())
        sel_grade  = st.selectbox("🏫 Lớp", grade_opts, key="cs_grade",
                                   label_visibility="collapsed")
    with col_search:
        kw = st.text_input("🔍 Tìm khóa học...", key="cs_kw",
                            label_visibility="collapsed",
                            placeholder="Tìm theo tên, môn học...")

    # Lọc
    filtered = courses
    if sel_subj  != "Tất cả":        filtered = [c for c in filtered if c.get("subject") == sel_subj]
    if sel_grade != "Tất cả lớp":    filtered = [c for c in filtered if c.get("grade")   == sel_grade]
    if kw.strip():
        kw_l = kw.lower()
        filtered = [c for c in filtered
                    if kw_l in c.get("title","").lower()
                    or kw_l in c.get("description","").lower()]

    if not filtered:
        st.info("Chưa có khóa học nào. Hãy chờ giáo viên thêm nội dung!")
        return
    st.markdown("""
    <style>
    .sec-t {
        color: #000 !important;
        font-weight: 600;
        font-size: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown(f'<div class="sec-t" >{len(filtered)} khóa học</div>', unsafe_allow_html=True)

    for c in filtered:
        prog = get_progress(uid, c["id"])
        pct  = calc_progress_pct(c, prog)
        tot  = count_total_lessons(c)
        done = len(prog.get("completed_lessons", []))
        lvl  = c.get("level", "Cơ bản")
        lc   = _LEVEL_COLOR.get(lvl, ("#e8f0fe","##1a73e8"))
        icon = _SUBJ_ICONS.get(c.get("subject",""), "📚")

        st.markdown(f"""
        <div class="course-card">
          <div class="cc-top">
            <div class="cc-emoji">{icon}</div>
            <div class="cc-info">
              <div class="cc-title">{c["title"]}</div>
              <div class="cc-meta">
                <span style="color:#000;!important">👨‍🏫 {c.get("teacher","")}</span>
                <span style="color:#000; !important" >📖 {tot} bài học</span>
                <span style="color:#000; !important">🏫 {c.get("grade","")}</span>
              </div>
            </div>
          </div>
          <div class="cc-desc" style="color:#000;!important">{c.get("description","")}</div>
          <div class="cc-tags">
            <span class="cc-tag" style="background:{lc[0]};color:{lc[1]}">{lvl}</span>
            <span class="cc-tag" style="background:#e8f0fe;color:#1a73e8">{c.get("subject","")}</span>
            {"<span class='cc-tag' style='background:#f0fdf4;color:#166534'>✅ Hoàn thành</span>" if pct==100 else ""}
          </div>
          <div class="cc-prog">
            <div style="font-size:.72rem;color:#000">Tiến độ: {done}/{tot} bài ({pct}%)</div>
            <div class="prog-bar"><div class="prog-fill" style="width:{pct}%"></div></div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("📖 Vào học", key=f"enter_{c['id']}", use_container_width=True,
                     type="primary" if pct < 100 else "secondary"):
            st.session_state["active_course"] = c["id"]
            st.session_state["course_view"]   = "detail"
            st.session_state["active_lesson"] = None
            st.rerun()
        st.markdown("---")


# ── Chi tiết khóa học ────────────────────────────────────
def _show_course_detail(uid: str, uname: str):
    course_id = st.session_state["active_course"]
    course    = get_course(course_id)
    if not course:
        st.error("Không tìm thấy khóa học!")
        st.session_state["course_view"] = "list"; st.rerun(); return

    prog  = get_progress(uid, course_id)
    pct   = calc_progress_pct(course, prog)
    done  = set(prog.get("completed_lessons", []))
    total = count_total_lessons(course)

    # Header
    col_back, col_title = st.columns([1, 6])
    with col_back:
        if st.button("← Quay lại", key="back_list"):
            st.session_state["course_view"] = "list"; st.rerun()
    with col_title:
        st.markdown(f"## {_SUBJ_ICONS.get(course.get('subject',''),'📚')} {course['title']}")

    # Progress tổng
    st.markdown(f"""
    <div style="background:#f0f4ff;border:1px solid #c7d2fe;border-radius:12px;
                padding:.8rem 1.2rem;margin-bottom:1rem">
      <div style="display:flex;justify-content:space-between;margin-bottom:.4rem">
        <span style="font-size:.85rem;font-weight:700;color:#1e1b4b">📊 Tiến độ tổng thể</span>
        <span style="font-size:.85rem;font-weight:800;color:#4338ca">{done.__len__()}/{total} bài · {pct}%</span>
      </div>
      <div class="prog-bar" style="height:10px">
        <div class="prog-fill" style="width:{pct}%"></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Chứng chỉ
    if pct == 100:
        _show_certificate(uid, uname, course, prog)
        st.markdown("---")

    # YouTube search
    with st.expander("🔍 Tìm video YouTube bổ sung", expanded=False):
        q_col, btn_col = st.columns([4, 1])
        with q_col:
            yt_q = st.text_input("", placeholder=f"VD: {course.get('subject','')} lớp 10 bài giảng",
                                  key="yt_search_q", label_visibility="collapsed")
        with btn_col:
            do_search = st.button("🔍 Tìm", key="yt_search_btn", use_container_width=True)
        if do_search and yt_q.strip():
            with st.spinner("Đang tìm..."):
                results = search_youtube(yt_q.strip())
            for r in results:
                if r.get("video_id"):
                    st.markdown(f"""
                    <div class="yt-card">
                      <img class="yt-thumb" src="{r['thumbnail']}" onerror="this.style.display='none'">
                      <div class="yt-info">
                        <div class="yt-title">{r['title']}</div>
                        <div class="yt-ch">📺 {r['channel']}</div>
                      </div>
                    </div>""", unsafe_allow_html=True)
                    if st.button("▶ Xem", key=f"yt_{r['video_id']}", use_container_width=True):
                        st.session_state["yt_preview"] = r["video_id"]
                else:
                    st.markdown(f"[🔗 {r['title']}]({r.get('search_url','')})")

            if "yt_preview" in st.session_state:
                st.markdown(get_youtube_embed(st.session_state["yt_preview"]),
                            unsafe_allow_html=True)

    st.markdown("---")

    # Danh sách chương & bài học
    all_lesson_ids = []
    for ch in course.get("chapters", []):
        for ls in ch.get("lessons", []):
            all_lesson_ids.append(ls["id"])

    for ci, ch in enumerate(course.get("chapters", [])):
        lessons = ch.get("lessons", [])
        ch_done = sum(1 for ls in lessons if ls["id"] in done)
        st.markdown(f"""
        <div class="ch-header">
          <span class="ch-num">Ch.{ci+1}</span>
          <span class="ch-title">{ch['title']}</span>
          <span class="ch-count">{ch_done}/{len(lessons)} bài</span>
        </div>""", unsafe_allow_html=True)

        for li, ls in enumerate(lessons):
            ls_id    = ls["id"]
            is_done  = ls_id in done
            # Unlock logic: bài đầu luôn mở, bài sau cần làm xong bài trước
            prev_idx = all_lesson_ids.index(ls_id) - 1
            is_locked = (prev_idx >= 0 and
                         all_lesson_ids[prev_idx] not in done and
                         ls_id not in done)

            icon  = "✅" if is_done else ("🔒" if is_locked else "▶")
            cls   = "done" if is_done else ("locked" if is_locked else "")
            mins  = ls.get("duration_min", 0)
            quiz  = ls.get("quiz", [])
            st.markdown("""
            <style>
            .li-meta {
                color: #000 !important;
                font-weight: 600;
                font-size: 1rem;
            }
            </style>
            """, unsafe_allow_html=True)
            st.markdown(f"""
            <div class="lesson-item {cls}">
              <span class="li-icon">{icon}</span>
              <span class="li-title">{ls['title']}</span>
              <span class="li-meta">⏱️ {mins} phút</span>
              {"<span class='li-badge' style='background:#e8f0fe;color:#1a73e8'>📝 Quiz</span>" if quiz else ""}
            </div>""", unsafe_allow_html=True)

            if not is_locked:
                if st.button("Vào học" if not is_done else "Xem lại",
                             key=f"ls_{ls_id}", use_container_width=False):
                    st.session_state["active_lesson"]  = ls_id
                    st.session_state["active_ch"]      = ch["id"]
                    st.session_state["course_view"]    = "lesson"
                    st.session_state["quiz_answers"]   = {}
                    st.session_state["quiz_submitted"] = False
                    st.rerun()


# ── Xem bài học ──────────────────────────────────────────
def _show_lesson(uid: str, uname: str):
    course_id = st.session_state["active_course"]
    lesson_id = st.session_state["active_lesson"]
    course    = get_course(course_id)
    if not course:
        st.session_state["course_view"] = "list"; st.rerun(); return

    # Tìm bài học
    lesson = ch_obj = None
    for ch in course.get("chapters", []):
        for ls in ch.get("lessons", []):
            if ls["id"] == lesson_id:
                lesson = ls; ch_obj = ch; break
        if lesson: break

    if not lesson:
        st.error("Không tìm thấy bài học!")
        st.session_state["course_view"] = "detail"; st.rerun(); return

    prog = get_progress(uid, course_id)
    done = set(prog.get("completed_lessons", []))

    # Navigation
    col_b, col_t = st.columns([1, 6])
    with col_b:
        if st.button("← Quay lại", key="back_detail"):
            st.session_state["course_view"] = "detail"; st.rerun()
    with col_t:
        st.markdown(f"### 📖 {lesson['title']}")
    st.caption(f"📂 {ch_obj['title']} · ⏱️ {lesson.get('duration_min',0)} phút · 📚 {course['title']}")
    st.markdown("---")

    # Video
    vid_url  = lesson.get("video_url", "")
    vid_type = lesson.get("video_type", "youtube")

    if vid_url:
        st.markdown('<div class="sec-t">🎬 Video bài giảng</div>', unsafe_allow_html=True)
        if vid_type == "youtube":
            # Trích video ID từ URL đầy đủ hoặc ID ngắn
            vid_id = vid_url
            if "youtube.com/watch" in vid_url:
                import urllib.parse as up
                vid_id = up.parse_qs(up.urlparse(vid_url).query).get("v", [vid_url])[0]
            elif "youtu.be/" in vid_url:
                vid_id = vid_url.split("youtu.be/")[-1].split("?")[0]
            st.markdown(
                f'<div class="video-wrap">{get_youtube_embed(vid_id)}</div>',
                unsafe_allow_html=True)
        else:
            st.video(vid_url)

    # Nội dung text
    content = lesson.get("content", "")
    if content:
        st.markdown('<div class="sec-t">📝 Nội dung bài học</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div style="background:#fafbff;border:1px solid #e0e7ff;border-radius:12px;'
            f'padding:1rem 1.2rem;font-size:.9rem;line-height:1.7;color:#1e1b4b">'
            f'{content}</div>',
            unsafe_allow_html=True)

    # Quiz
    quiz = lesson.get("quiz", [])
    already_done = lesson_id in done

    if quiz and not already_done:
        st.markdown('<div class="quiz-wrap">', unsafe_allow_html=True)
        st.markdown('<div class="quiz-title">📝 Quiz nhanh — Kiểm tra hiểu bài</div>',
                    unsafe_allow_html=True)

        qa = st.session_state.get("quiz_answers", {})
        submitted = st.session_state.get("quiz_submitted", False)

        for qi, qitem in enumerate(quiz):
            opts = qitem["options"]
            cur  = qa.get(qi)
            if submitted:
                correct = qitem["answer"]
                color   = "#1e8e3e" if cur == correct else "#d93025"
                st.markdown(
                    f'<p style="font-size:.85rem;font-weight:600;color:#1e1b4b">'
                    f'Q{qi+1}. {qitem["question"]}</p>',
                    unsafe_allow_html=True)
                for opt in opts:
                    mark = "✅" if opt == correct else ("❌" if opt == cur else "○")
                    st.markdown(
                        f'<p style="font-size:.82rem;margin-left:.8rem;'
                        f'color:{"#1e8e3e" if opt==correct else "#d93025" if opt==cur else "#555"}">'
                        f'{mark} {opt}</p>', unsafe_allow_html=True)
            else:
                choice = st.radio(
                    f"Q{qi+1}. {qitem['question']}", opts,
                    key=f"quiz_{lesson_id}_{qi}", index=None,
                    label_visibility="visible")
                if choice:
                    st.session_state["quiz_answers"][qi] = choice

        if not submitted:
            if st.button("✅ Nộp quiz", type="primary", use_container_width=True,
                         key="submit_quiz"):
                st.session_state["quiz_submitted"] = True
                score = sum(1 for qi, q in enumerate(quiz)
                            if qa.get(qi) == q["answer"])
                pct_q = int(score / len(quiz) * 100)
                if pct_q >= 60:
                    mark_lesson_done(uid, course_id, lesson_id, quiz_score=score)
                    st.success(f"🎉 Xuất sắc! {score}/{len(quiz)} câu đúng ({pct_q}%) — Bài đã được lưu!")
                else:
                    st.warning(f"😅 {score}/{len(quiz)} câu đúng ({pct_q}%) — Cần ≥60% để hoàn thành. Xem lại nhé!")
                st.rerun()
        else:
            score = sum(1 for qi, q in enumerate(quiz)
                        if qa.get(qi) == q["answer"])
            pct_q = int(score / len(quiz) * 100)
            if pct_q >= 60:
                st.success(f"✅ {score}/{len(quiz)} đúng ({pct_q}%) — Đã hoàn thành!")
            else:
                st.error(f"❌ {score}/{len(quiz)} đúng ({pct_q}%) — Chưa đạt. Ôn lại bài rồi thử lại!")
                if st.button("🔄 Làm lại quiz", key="retry_quiz"):
                    st.session_state["quiz_answers"]   = {}
                    st.session_state["quiz_submitted"] = False
                    st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

    # Hoàn thành bài (không có quiz hoặc đã làm)
    if not quiz and not already_done:
        st.markdown("---")
        if st.button("✅ Đánh dấu đã học xong", type="primary",
                     use_container_width=True, key="mark_done"):
            mark_lesson_done(uid, course_id, lesson_id)
            st.success("🎉 Đã lưu bài học! Tiếp tục bài tiếp theo nhé.")
            st.session_state["course_view"] = "detail"; st.rerun()

    if already_done:
        st.success("✅ Bạn đã hoàn thành bài học này!")
        if st.button("→ Tiếp tục", key="next_lesson", use_container_width=True):
            st.session_state["course_view"] = "detail"; st.rerun()


# ── Chứng chỉ ────────────────────────────────────────────
def _show_certificate(uid: str, uname: str, course: dict, prog: dict):
    issue_certificate(uid, course["id"])
    completed_time = prog.get("completed_at")
    date_str = time.strftime("%d/%m/%Y", time.localtime(completed_time)) \
               if completed_time else time.strftime("%d/%m/%Y")
    st.markdown(f"""
    <div class="cert-card">
      <div style="font-size:3rem">🏆</div>
      <div class="cert-title">Chứng chỉ hoàn thành khóa học</div>
      <div style="font-size:1.1rem;font-weight:800;color:#1e1b4b;margin:.5rem 0">
        {course['title']}
      </div>
      <div class="cert-sub">
        Cấp cho: <b>{uname}</b> · Hoàn thành ngày {date_str}
      </div>
      <div style="margin-top:.75rem;font-size:.78rem;color:#b45309">
        🎓 Được cấp bởi AI Exam Generator · Giáo viên: {course.get("teacher","")}
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.balloons()


# ═══════════════════════════════════════════════════════════
# TRANG GIÁO VIÊN
# ═══════════════════════════════════════════════════════════

def show_teacher_courses():
    st.markdown(_CSS, unsafe_allow_html=True)
    st.markdown("## 📚 Quản lý khóa học")

    if "tc_view"      not in st.session_state: st.session_state["tc_view"]      = "list"
    if "tc_course_id" not in st.session_state: st.session_state["tc_course_id"] = None

    v = st.session_state["tc_view"]

    if v == "list":
        _teacher_list()
    elif v == "edit":
        _teacher_edit()


def _teacher_list():
    courses = get_all_courses()
    teacher = st.session_state.get("username", "")

    # Tạo khóa học mới
    with st.expander("➕ Tạo khóa học mới", expanded=False):
        c1, c2 = st.columns(2)
        with c1:
            t_title = st.text_input("Tên khóa học *", key="tc_title")
            t_subj  = st.selectbox("Môn học *", SUBJECT_OPTIONS, key="tc_subj")
            t_level = st.selectbox("Cấp độ", ["Cơ bản","Trung bình","Nâng cao"], key="tc_level")
        with c2:
            t_grade = st.selectbox("Lớp *", list(GRADE_CONFIG.keys()), key="tc_grade")
            t_desc  = st.text_area("Mô tả", key="tc_desc", height=100)

        if st.button("✅ Tạo khóa học", type="primary", use_container_width=True, key="tc_create"):
            if not t_title.strip():
                st.error("Vui lòng nhập tên khóa học!")
            else:
                cid = create_course({
                    "title":       t_title.strip(),
                    "subject":     t_subj,
                    "grade":       t_grade,
                    "description": t_desc.strip(),
                    "teacher":     teacher,
                    "level":       t_level,
                    "thumbnail":   _SUBJ_ICONS.get(t_subj, "📚"),
                })
                st.success(f"✅ Đã tạo khóa học!")
                st.rerun()

    st.markdown("---")
    my_courses = [c for c in courses if c.get("teacher") == teacher] or courses

    if not my_courses:
        st.info("Chưa có khóa học nào. Hãy tạo khóa học đầu tiên!")
        return

    for c in my_courses:
        tot = count_total_lessons(c)
        col1, col2, col3 = st.columns([5, 1, 1])
        with col1:
            icon = _SUBJ_ICONS.get(c.get("subject",""),"📚")
            st.markdown(
                f'<div style="padding:.4rem 0">'
                f'<b>{icon} {c["title"]}</b>'
                f'<span style="font-size:.75rem;color:#888;margin-left:.5rem">'
                f'{c.get("subject","")} · {c.get("grade","")} · {tot} bài</span>'
                f'</div>', unsafe_allow_html=True)
        with col2:
            if st.button("✏️ Sửa", key=f"tc_edit_{c['id']}", use_container_width=True):
                st.session_state["tc_course_id"] = c["id"]
                st.session_state["tc_view"]      = "edit"
                st.rerun()
        with col3:
            if st.button("🗑️ Xóa", key=f"tc_del_{c['id']}", use_container_width=True):
                delete_course(c["id"]); st.rerun()
        st.divider()


def _teacher_edit():
    cid    = st.session_state["tc_course_id"]
    course = get_course(cid)
    if not course:
        st.error("Không tìm thấy khóa học!")
        st.session_state["tc_view"] = "list"; st.rerun(); return

    col_b, col_t = st.columns([1, 5])
    with col_b:
        if st.button("← Quay lại", key="tc_back"):
            st.session_state["tc_view"] = "list"; st.rerun()
    with col_t:
        st.markdown(f"### ✏️ {course['title']}")

    # Thêm chương
    st.markdown('<div class="sec-t">📂 Chương học</div>', unsafe_allow_html=True)
    with st.expander("➕ Thêm chương mới"):
        ch_title = st.text_input("Tên chương", key="new_ch_title")
        if st.button("✅ Thêm chương", key="add_ch"):
            if ch_title.strip():
                add_chapter(cid, ch_title.strip())
                st.success("Đã thêm chương!")
                st.rerun()

    # Danh sách chương
    for ci, ch in enumerate(course.get("chapters", [])):
        with st.expander(f"📂 Ch.{ci+1}: {ch['title']} ({len(ch.get('lessons',[]))} bài)",
                         expanded=False):
            # Sửa/xóa chương
            cc1, cc2, cc3 = st.columns([4, 1, 1])
            with cc1:
                new_ch_t = st.text_input("Tên chương", value=ch["title"],
                                          key=f"cht_{ch['id']}", label_visibility="collapsed")
            with cc2:
                if st.button("💾", key=f"savech_{ch['id']}", help="Lưu"):
                    update_chapter(cid, ch["id"], new_ch_t); st.rerun()
            with cc3:
                if st.button("🗑️", key=f"delch_{ch['id']}", help="Xóa chương"):
                    delete_chapter(cid, ch["id"]); st.rerun()

            st.markdown("**Bài học:**")

            # Danh sách bài học hiện có
            for ls in ch.get("lessons", []):
                lc1, lc2 = st.columns([5, 1])
                with lc1:
                    st.markdown(
                        f'<div style="font-size:.83rem;padding:.3rem 0">'
                        f'▶ {ls["title"]} · ⏱️{ls.get("duration_min",0)}p'
                        f'{"· 📝Quiz" if ls.get("quiz") else ""}</div>',
                        unsafe_allow_html=True)
                with lc2:
                    if st.button("🗑️", key=f"dells_{ls['id']}"):
                        delete_lesson(cid, ch["id"], ls["id"]); st.rerun()

            # Thêm bài học mới
            st.markdown("---")
            st.markdown("**➕ Thêm bài học:**")
            ls_title = st.text_input("Tiêu đề bài *", key=f"lst_{ch['id']}")
            ls_content = st.text_area("Nội dung", key=f"lsc_{ch['id']}", height=80)
            lv1, lv2   = st.columns(2)
            with lv1:
                ls_video   = st.text_input("Link YouTube / ID video",
                                            key=f"lsv_{ch['id']}",
                                            placeholder="VD: dQw4w9WgXcQ")
                ls_vtype   = st.selectbox("Loại video",
                                           ["youtube","upload"],
                                           key=f"lsvt_{ch['id']}")
            with lv2:
                ls_dur = st.number_input("Thời lượng (phút)",
                                          min_value=1, max_value=180,
                                          value=15, key=f"lsd_{ch['id']}")

            # Quiz đơn giản
            with st.expander("📝 Thêm câu quiz (tuỳ chọn)"):
                qqs = st.text_input("Câu hỏi quiz", key=f"qq_{ch['id']}")
                qa1 = st.text_input("Đáp án A",     key=f"qa1_{ch['id']}")
                qa2 = st.text_input("Đáp án B",     key=f"qa2_{ch['id']}")
                qa3 = st.text_input("Đáp án C",     key=f"qa3_{ch['id']}")
                qa4 = st.text_input("Đáp án D",     key=f"qa4_{ch['id']}")
                qans = st.selectbox("Đáp án đúng",
                                     ["A","B","C","D"],
                                     key=f"qans_{ch['id']}")
                ans_map = {"A": qa1,"B": qa2,"C": qa3,"D": qa4}

            if st.button("✅ Thêm bài học", key=f"addls_{ch['id']}",
                         type="primary", use_container_width=True):
                if not ls_title.strip():
                    st.error("Vui lòng nhập tiêu đề bài học!")
                else:
                    quiz_list = []
                    if qqs.strip() and all([qa1,qa2,qa3,qa4]):
                        quiz_list = [{
                            "question": qqs.strip(),
                            "options":  [qa1, qa2, qa3, qa4],
                            "answer":   ans_map[qans],
                        }]
                    add_lesson(cid, ch["id"], {
                        "title":        ls_title.strip(),
                        "content":      ls_content.strip(),
                        "video_url":    ls_video.strip(),
                        "video_type":   ls_vtype,
                        "duration_min": int(ls_dur),
                        "quiz":         quiz_list,
                    })
                    st.success("✅ Đã thêm bài học!")
                    st.rerun()
