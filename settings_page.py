# ============================================================
# settings_page.py — Cài đặt giao diện học sinh
# ============================================================
import streamlit as st

# ── Màu theme có sẵn ─────────────────────────────────────
THEME_COLORS = {
    "🔵 Xanh dương (mặc định)": {"primary": "#1a73e8", "light": "#e8f0fe", "dark": "#0d47a1"},
    "🟢 Xanh lá":               {"primary": "#2e7d32", "light": "#e8f5e9", "dark": "#1b5e20"},
    "🟣 Tím":                   {"primary": "#7b1fa2", "light": "#f3e5f5", "dark": "#4a148c"},
    "🔴 Đỏ":                    {"primary": "#c62828", "light": "#ffebee", "dark": "#b71c1c"},
    "🟠 Cam":                   {"primary": "#e65100", "light": "#fff3e0", "dark": "#bf360c"},
    "🩷 Hồng":                  {"primary": "#ad1457", "light": "#fce4ec", "dark": "#880e4f"},
}

FONT_SIZES = {"Nhỏ": "14px", "Vừa (mặc định)": "16px", "Lớn": "18px", "Rất lớn": "20px"}
LANGUAGES  = {"🇻🇳 Tiếng Việt": "vi", "🇬🇧 English": "en"}

UI_LABELS = {
    "vi": {
        "home":     "🏠 Trang chủ",
        "start":    "🚀 Bắt đầu làm bài",
        "history":  "📋 Lịch sử",
        "profile":  "👤 Hồ sơ",
        "settings": "⚙️ Cài đặt",
        "chatbox":  "💬 Hỏi AI",
        "logout":   "🚪 Đăng xuất",
    },
    "en": {
        "home":     "🏠 Home",
        "start":    "🚀 Start Exam",
        "history":  "📋 History",
        "profile":  "👤 Profile",
        "settings": "⚙️ Settings",
        "chatbox":  "💬 Ask AI",
        "logout":   "🚪 Logout",
    },
}


def get_settings() -> dict:
    """Lấy settings hiện tại (có default) — không còn dark_mode."""
    defaults = {
        "theme_name": "🔵 Xanh dương (mặc định)",
        "font_size":  "Vừa (mặc định)",
        "language":   "🇻🇳 Tiếng Việt",
    }
    saved = st.session_state.get("ui_settings", {})
    # Loại bỏ dark_mode nếu còn sót từ session cũ
    saved.pop("dark_mode", None)
    return {**defaults, **saved}


def get_label(key: str) -> str:
    """Lấy nhãn UI theo ngôn ngữ hiện tại."""
    s    = get_settings()
    lang = LANGUAGES.get(s["language"], "vi")
    return UI_LABELS.get(lang, UI_LABELS["vi"]).get(key, key)


def apply_settings_css():
    """Inject CSS động theo settings — chỉ light mode."""
    s         = get_settings()
    color     = THEME_COLORS.get(s["theme_name"],
                THEME_COLORS["🔵 Xanh dương (mặc định)"])
    font_size = FONT_SIZES.get(s["font_size"], "16px")

    # Luôn là light mode
    bg     = "#ffffff"
    bg2    = "#f8f9fa"
    text   = "#212121"
    text2  = "#555555"
    border = "#e0e0e0"
    q_bg   = "#f0f4ff"

    st.markdown(f"""
<style>
    html, body, [data-testid="stAppViewContainer"] {{
        background-color: {bg} !important;
        color: {text} !important;
        font-size: {font_size} !important;
    }}
    [data-testid="stSidebar"] {{
        background-color: {bg2} !important;
    }}
    .main-title {{ color: {color["primary"]} !important; }}
    .sub-title  {{ color: {text2} !important; }}
    .q-box {{
        background: {q_bg} !important;
        border-left: 4px solid {color["primary"]} !important;
        color: {text} !important;
    }}
    .stButton > button {{ border-radius:8px !important; font-weight:600 !important; }}
    .stButton > button[kind="primary"] {{
        background: {color["primary"]} !important;
        border-color: {color["primary"]} !important;
    }}
    .tag-middle, .tag-high, .tag-uni {{
        background: {color["light"]} !important;
        color: {color["dark"]} !important;
    }}
    .stTextInput input, .stTextArea textarea, .stSelectbox select {{
        background: {bg2} !important;
        color: {text} !important;
        border-color: {border} !important;
    }}
    [data-testid="stMetricValue"] {{ color: {color["primary"]} !important; }}
    .streamlit-expanderHeader     {{ color: {text} !important; }}
    .badge-ai {{
        background: {color["light"]} !important;
        color: {color["primary"]} !important;
    }}
</style>""", unsafe_allow_html=True)


def show_settings():
    st.markdown("## ⚙️ Cài đặt giao diện")
    st.markdown("---")

    s = get_settings()

    # ── Theme color ───────────────────────────────────────
    st.markdown("### 🎨 Màu chủ đạo")
    theme_names = list(THEME_COLORS.keys())
    theme_name  = st.radio(
        "", theme_names,
        index=theme_names.index(s["theme_name"])
              if s["theme_name"] in theme_names else 0,
        horizontal=True, key="cfg_theme",
        label_visibility="collapsed",
    )

    # Preview 3 tông màu
    color = THEME_COLORS[theme_name]
    st.markdown(
        f'<div style="display:flex;gap:.5rem;margin:.5rem 0 1rem">'
        f'<div style="width:40px;height:40px;border-radius:8px;'
        f'background:{color["primary"]};box-shadow:0 2px 6px rgba(0,0,0,.15)"></div>'
        f'<div style="width:40px;height:40px;border-radius:8px;'
        f'background:{color["light"]}; border:1px solid #e0e0e0"></div>'
        f'<div style="width:40px;height:40px;border-radius:8px;'
        f'background:{color["dark"]}; box-shadow:0 2px 6px rgba(0,0,0,.15)"></div>'
        f'<span style="align-self:center;font-size:.8rem;color:#888;margin-left:.3rem">'
        f'Chính · Nhạt · Đậm</span>'
        f'</div>',
        unsafe_allow_html=True)

    # ── Cỡ chữ ───────────────────────────────────────────
    st.markdown("### 🔡 Cỡ chữ")
    font_opts = list(FONT_SIZES.keys())
    font_size = st.select_slider(
        "", options=font_opts,
        value=s["font_size"] if s["font_size"] in font_opts else "Vừa (mặc định)",
        key="cfg_font", label_visibility="collapsed",
    )
    # Preview cỡ chữ
    px = FONT_SIZES[font_size]
    st.markdown(
        f'<p style="font-size:{px};color:#555;margin:.2rem 0 1rem">'
        f'Xem trước: Cỡ chữ {font_size} ({px})</p>',
        unsafe_allow_html=True)

    # ── Ngôn ngữ ─────────────────────────────────────────
    st.markdown("### 🌐 Ngôn ngữ giao diện")
    lang_opts = list(LANGUAGES.keys())
    language  = st.radio(
        "", lang_opts,
        index=lang_opts.index(s["language"])
              if s["language"] in lang_opts else 0,
        horizontal=True, key="cfg_lang",
        label_visibility="collapsed",
    )

    st.markdown("---")

    c1, c2 = st.columns(2)
    with c1:
        if st.button("💾 Lưu cài đặt", type="primary", use_container_width=True):
            st.session_state["ui_settings"] = {
                "theme_name": theme_name,
                "font_size":  font_size,
                "language":   language,
            }
            st.success("✅ Đã lưu cài đặt!")
            st.rerun()
    with c2:
        if st.button("🔄 Khôi phục mặc định", use_container_width=True):
            st.session_state["ui_settings"] = {
                "theme_name": "🔵 Xanh dương (mặc định)",
                "font_size":  "Vừa (mặc định)",
                "language":   "🇻🇳 Tiếng Việt",
            }
            st.success("✅ Đã khôi phục mặc định!")
            st.rerun()

    st.markdown("---")
    if st.button("← Về trang chủ", use_container_width=True):
        st.session_state.page = "home"; st.rerun()