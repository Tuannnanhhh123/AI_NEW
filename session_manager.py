# ============================================================
# session_manager.py
# Giữ session qua F5 bằng localStorage (JS) + query_params
# Flow:
#   Login  → lưu uid/role/token vào localStorage + query_params
#   F5     → JS đọc localStorage → ghi vào query_params → Python đọc
#   Logout → xóa localStorage + query_params + session_state
# ============================================================
import streamlit as st
import streamlit.components.v1 as components

DEFAULTS = {
    "page":               "login",
    "username":           None,
    "uid":                None,
    "email":              None,
    "role":               None,
    "grade":              None,
    "favorite_subjects":  [],
    "subject":            None,
    "questions":          [],
    "answers":            {},
    "submitted":          False,
    "score":              0,
    "start_time":         None,
    "exam_source":        None,
    "ai_error":           None,
    "verify_summary":     None,
    "dup_filtered":       0,
    "exam_start_ts":      None,
    "current_assignment": None,
    "remind_assignments": [],
    "teacher_tab":        "dashboard",
    "_id_token":          "",
    "_session_restored":  False,
}


# ── 1. Khởi tạo session state ─────────────────────────────
def init_session():
    for k, v in DEFAULTS.items():
        if k not in st.session_state:
            st.session_state[k] = v


# ── 2. Inject JS để đồng bộ localStorage → query_params ──
def inject_session_js():
    """
    Gọi 1 lần duy nhất ở đầu app.py (trước khi render bất kỳ thứ gì).
    JS sẽ:
      - Đọc localStorage['exam_session']
      - Nếu có → ghi vào URL query params → reload 1 lần để Python đọc
    Sau đó Python gọi restore_session() để đọc query_params vào session_state.
    """
    components.html("""
<script>
(function() {
    try {
        var raw = localStorage.getItem('exam_session');
        if (!raw) return;
        var s = JSON.parse(raw);
        if (!s.uid || !s.role) return;

        // Kiểm tra URL hiện tại đã có uid chưa
        var params = new URLSearchParams(window.parent.location.search);
        if (params.get('uid') === s.uid) return; // Đã có rồi, không reload

        // Ghi vào query params rồi reload để Python đọc
        params.set('uid',   s.uid);
        params.set('role',  s.role);
        if (s.role === 'teacher') params.set('uname', s.uname || '');
        if (s.token) params.set('token', s.token);
        if (s.email) params.set('email', s.email);

        window.parent.history.replaceState(null, '',
            window.parent.location.pathname + '?' + params.toString());
        window.parent.location.reload();
    } catch(e) {}
})();
</script>
""", height=0, scrolling=False)


# ── 3. Lưu session vào localStorage (gọi sau khi login) ──
def save_session_to_storage():
    """
    Gọi ngay sau khi set session_state thành công (sau login).
    Lưu vào cả localStorage lẫn query_params.
    """
    uid      = st.session_state.get("uid", "")
    role     = st.session_state.get("role", "")
    token    = st.session_state.get("_id_token", "")
    email    = st.session_state.get("email", "")
    username = st.session_state.get("username", "")

    if not uid or not role:
        return

    # Cập nhật query_params
    params = {"uid": uid, "role": role}
    if role == "teacher":
        params["uname"] = username
    if token:
        params["token"] = token
    if email:
        params["email"] = email
    st.query_params.update(params)

    # Lưu vào localStorage qua JS
    import json
    payload = json.dumps({
        "uid":   uid,
        "role":  role,
        "token": token,
        "email": email,
        "uname": username,
    })
    components.html(f"""
<script>
try {{
    localStorage.setItem('exam_session', {json.dumps(payload)});
}} catch(e) {{}}
</script>
""", height=0, scrolling=False)


# ── 4. Khôi phục session từ query_params ─────────────────
def restore_session():
    """
    Gọi ở đầu app.py sau inject_session_js().
    Đọc query_params (đã được JS điền) → set session_state.
    """
    if st.session_state.get("_session_restored"):
        return  # Chỉ restore 1 lần mỗi Python session
    if st.session_state.get("uid"):
        st.session_state["_session_restored"] = True
        return  # Đã login rồi

    uid   = st.query_params.get("uid",   "")
    role  = st.query_params.get("role",  "")
    token = st.query_params.get("token", "")
    email = st.query_params.get("email", "")
    uname = st.query_params.get("uname", "")

    if not uid or not role:
        return

    st.session_state["_session_restored"] = True

    if role == "teacher":
        st.session_state.update({
            "uid":      uid,
            "username": uname or "Giáo viên",
            "role":     "teacher",
            "page":     "teacher",
        })
        return

    # Student → lấy profile từ Firestore REST
    user_info = {
        "uid":               uid,
        "email":             email,
        "username":          email.split("@")[0] if email else "Học sinh",
        "role":              "student",
        "grade":             "",
        "favorite_subjects": [],
        "_id_token":         token,
        "page":              "home",
    }

    if uid and token:
        try:
            from firebase_manager import _fs_get
            profile = _fs_get(f"users/{uid}", token)
            if profile:
                user_info.update({
                    "username":          profile.get("display_name", user_info["username"]),
                    "grade":             profile.get("grade", ""),
                    "favorite_subjects": profile.get("favorite_subjects", []),
                    "role":              profile.get("role", "student"),
                })
        except Exception as e:
            print(f"[restore_session] Firestore lỗi: {e}")

    st.session_state.update(user_info)


# ── 5. Xóa session (logout) ───────────────────────────────
def clear_session():
    """Xóa localStorage + query_params + reset session_state."""
    # Xóa localStorage
    components.html("""
<script>
try { localStorage.removeItem('exam_session'); } catch(e) {}
// Xóa query params trên URL
window.parent.history.replaceState(null, '', window.parent.location.pathname);
</script>
""", height=0, scrolling=False)

    # Xóa query_params
    try:
        st.query_params.clear()
    except Exception:
        pass

    # Reset session_state
    for k, v in DEFAULTS.items():
        st.session_state[k] = v


# ── 6. Hàm tiện ích ──────────────────────────────────────
def is_logged_in() -> bool:
    return bool(st.session_state.get("uid"))


def do_logout():
    clear_session()
    st.rerun()