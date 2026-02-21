# ============================================================
# profile_page.py — Trang thông tin cá nhân học sinh
# ============================================================
import streamlit as st
from config           import GRADE_CONFIG, SUBJECT_OPTIONS
from firebase_manager import update_profile, reset_password, login
from user_manager     import get_user_stats, get_user_exams


def show_profile():
    st.markdown("## 👤 Thông tin cá nhân")
    st.markdown("---")

    uname = st.session_state.username
    uid   = st.session_state.get("uid", "")
    email = st.session_state.get("email", "")
    grade = st.session_state.get("grade", "")
    favs  = st.session_state.get("favorite_subjects", [])

    # ── Avatar + thống kê nhanh ───────────────────────────
    col_av, col_info = st.columns([1, 3])
    with col_av:
        initials = "".join(w[0].upper() for w in uname.split()[:2]) or "HS"
        st.markdown(
            f'<div style="width:80px;height:80px;border-radius:50%;'
            f'background:linear-gradient(135deg,#1a73e8,#0d47a1);'
            f'display:flex;align-items:center;justify-content:center;'
            f'font-size:1.8rem;font-weight:700;color:white;margin:auto">'
            f'{initials}</div>', unsafe_allow_html=True)

    with col_info:
        st.markdown(f"### {uname}")
        st.caption(f"📧 {email}")
        st.caption(f"🏫 {grade}")
        if favs:
            st.caption(f"📚 Môn yêu thích: {', '.join(favs)}")

    st.markdown("---")

    # ── Thống kê học tập ──────────────────────────────────
    stats = get_user_stats(uname)
    exams = get_user_exams(uname)
    if stats:
        st.markdown("### 📊 Thống kê học tập")
        cols = st.columns(min(len(stats), 3))
        for col, (subj, s) in zip(cols, stats.items()):
            col.metric(f"📘 {subj}", f"TB: {s['avg']}%",
                       f"{s['count']} bài | Cao: {s['best']}%")
        st.progress(
            max((s["avg"] for s in stats.values()), default=0) / 100
        )
        st.caption(f"Tổng số bài đã làm: **{len(exams)}**")
    else:
        st.info("Bạn chưa làm bài thi nào. Hãy bắt đầu ngay!")

    st.markdown("---")

    # ── Tab chỉnh sửa ─────────────────────────────────────
    tab1, tab2, tab3 = st.tabs(["✏️ Cập nhật thông tin", "🔒 Đổi mật khẩu", "📚 Môn & Lớp"])

    with tab1:
        st.markdown("### ✏️ Cập nhật tên hiển thị")
        new_name = st.text_input("👤 Tên mới", value=uname, key="pf_name")
        if st.button("💾 Lưu tên", type="primary", use_container_width=True, key="save_name"):
            if not new_name.strip():
                st.error("Tên không được để trống!")
            elif new_name.strip() == uname:
                st.info("Tên không thay đổi.")
            else:
                ok = update_profile(uid, display_name=new_name.strip())
                if ok:
                    st.session_state.username = new_name.strip()
                    st.success("✅ Đã cập nhật tên!")
                    st.rerun()
                else:
                    st.session_state.username = new_name.strip()
                    st.success("✅ Đã cập nhật tên (local)!")

    with tab2:
        st.markdown("### 🔒 Đổi mật khẩu")
        st.info("Chúng tôi sẽ gửi email đặt lại mật khẩu đến địa chỉ của bạn.", icon="📧")
        st.text_input("📧 Email", value=email, disabled=True, key="pf_email")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("📨 Gửi email đặt lại MK", type="primary",
                         use_container_width=True, key="send_reset"):
                if email:
                    ok, msg = reset_password(email)
                    if ok: st.success(msg)
                    else:  st.error(msg)
                else:
                    st.error("Không tìm thấy email tài khoản!")
        with col2:
            if st.button("🚪 Đăng xuất", use_container_width=True, key="pf_logout"):
                _logout()

    with tab3:
        st.markdown("### 🏫 Cập nhật lớp & môn yêu thích")
        new_grade = st.selectbox("🏫 Lớp của bạn",
                                  list(GRADE_CONFIG.keys()),
                                  index=list(GRADE_CONFIG.keys()).index(grade)
                                  if grade in GRADE_CONFIG else 0,
                                  key="pf_grade")
        avail_subs = GRADE_CONFIG[new_grade]["subjects"]
        new_favs   = st.multiselect("📚 Môn yêu thích", avail_subs,
                                     default=[f for f in favs if f in avail_subs],
                                     key="pf_favs")

        if st.button("💾 Lưu thay đổi", type="primary",
                     use_container_width=True, key="save_grade"):
            ok = update_profile(uid, grade=new_grade, favorite_subjects=new_favs)
            st.session_state.grade             = new_grade
            st.session_state.favorite_subjects = new_favs
            st.success("✅ Đã cập nhật!")

    st.markdown("---")
    if st.button("← Về trang chủ", use_container_width=True, key="pf_home"):
        st.session_state.page = "home"; st.rerun()


def _logout():
    from app import _DEFAULTS, _clear_session
    _clear_session()
    for k, v in _DEFAULTS.items():
        st.session_state[k] = v
    st.rerun()