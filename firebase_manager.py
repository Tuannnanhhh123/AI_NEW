# ============================================================
# firebase_manager.py — Firebase Auth REST + Firestore REST
# KHÔNG dùng firebase-admin SDK → không cần service account
# ============================================================
import json
import requests
import os
import streamlit as st

_FIREBASE_OK = False
_db          = None

from config import FIREBASE_CONFIG
_API_KEY    = FIREBASE_CONFIG["apiKey"]
_PROJECT_ID = FIREBASE_CONFIG["projectId"]

_FIRESTORE_BASE = (
    f"https://firestore.googleapis.com/v1/"
    f"projects/{_PROJECT_ID}/databases/(default)/documents"
)


# ── Firebase Auth REST ────────────────────────────────────
def _auth_url(endpoint: str) -> str:
    return f"https://identitytoolkit.googleapis.com/v1/accounts:{endpoint}?key={_API_KEY}"


def _auth_post(endpoint: str, payload: dict) -> tuple:
    try:
        r    = requests.post(_auth_url(endpoint), json=payload, timeout=10)
        data = r.json()
        if "error" in data:
            msg = data["error"].get("message", "Lỗi không xác định")
            return {}, _translate_error(msg)
        return data, ""
    except Exception as e:
        return {}, f"Lỗi kết nối: {e}"


def _translate_error(msg: str) -> str:
    MAP = {
        "EMAIL_EXISTS":                "Email đã được đăng ký!",
        "INVALID_EMAIL":               "Email không hợp lệ!",
        "WEAK_PASSWORD":               "Mật khẩu quá yếu (tối thiểu 6 ký tự)!",
        "EMAIL_NOT_FOUND":             "Email chưa đăng ký!",
        "INVALID_PASSWORD":            "Mật khẩu không đúng!",
        "INVALID_LOGIN_CREDENTIALS":   "Email hoặc mật khẩu không đúng!",
        "USER_DISABLED":               "Tài khoản đã bị vô hiệu hóa!",
        "TOO_MANY_ATTEMPTS_TRY_LATER": "Quá nhiều lần thử, vui lòng thử lại sau!",
    }
    for k, v in MAP.items():
        if k in msg:
            return v
    return msg


# ── Firestore REST helpers ────────────────────────────────
def _fs_get(path: str, id_token: str = "") -> dict | None:
    """
    Đọc 1 document.
    path = 'collection/doc_id'
    """
    token = id_token or st.session_state.get("_id_token", "")
    url   = f"{_FIRESTORE_BASE}/{path}"
    try:
        r = requests.get(
            url,
            headers={"Authorization": f"Bearer {token}"},
            timeout=8,
        )
        if r.status_code == 200:
            return _fs_parse(r.json())
        if r.status_code == 404:
            return None
    except Exception as e:
        print(f"[Firestore GET] {e}")
    return None


def _fs_set(collection: str, doc_id: str, data: dict, id_token: str):
    """
    Ghi / merge document.
    Nhận RIÊNG collection và doc_id để tránh nhầm lẫn path.
    """
    url  = f"{_FIRESTORE_BASE}/{collection}/{doc_id}"
    body = {"fields": _fs_encode(data)}
    try:
        requests.patch(
            url,
            headers={
                "Authorization": f"Bearer {id_token}",
                "Content-Type":  "application/json",
            },
            json=body,
            timeout=8,
        )
    except Exception as e:
        print(f"[Firestore SET] {e}")


def _fs_encode(data: dict) -> dict:
    """dict Python → Firestore field format."""
    fields = {}
    for k, v in data.items():
        if isinstance(v, str):
            fields[k] = {"stringValue": v}
        elif isinstance(v, bool):
            fields[k] = {"booleanValue": v}
        elif isinstance(v, int):
            fields[k] = {"integerValue": str(v)}
        elif isinstance(v, float):
            fields[k] = {"doubleValue": v}
        elif isinstance(v, list):
            fields[k] = {"arrayValue": {"values": [
                {"stringValue": i} if isinstance(i, str)
                else {"integerValue": str(i)}
                for i in v
            ]}}
        elif v is None:
            fields[k] = {"nullValue": None}
        else:
            fields[k] = {"stringValue": str(v)}
    return fields


def _fs_parse(doc: dict) -> dict:
    """Firestore document → dict Python."""
    result = {}
    for k, v in doc.get("fields", {}).items():
        if "stringValue"   in v: result[k] = v["stringValue"]
        elif "booleanValue" in v: result[k] = v["booleanValue"]
        elif "integerValue" in v: result[k] = int(v["integerValue"])
        elif "doubleValue"  in v: result[k] = v["doubleValue"]
        elif "nullValue"    in v: result[k] = None
        elif "arrayValue"   in v:
            vals = v["arrayValue"].get("values", [])
            result[k] = [list(i.values())[0] if i else None for i in vals]
    return result


# ── Đăng ký ──────────────────────────────────────────────
def register(email: str, password: str, display_name: str,
             grade: str, favorite_subjects: list) -> tuple:
    data, err = _auth_post("signUp", {
        "email":             email,
        "password":          password,
        "returnSecureToken": True,
    })
    if err:
        return False, err

    uid      = data.get("localId", "")
    id_token = data.get("idToken", "")

    if uid and id_token:
        # ── Gọi đúng: collection="users", doc_id=uid ──
        _fs_set("users", uid, {
            "uid":               uid,
            "email":             email,
            "display_name":      display_name,
            "grade":             grade,
            "favorite_subjects": favorite_subjects,
            "role":              "student",
        }, id_token)

    return True, "Đăng ký thành công!"


# ── Đăng nhập ─────────────────────────────────────────────
def login(email: str, password: str) -> tuple:
    data, err = _auth_post("signInWithPassword", {
        "email":             email,
        "password":          password,
        "returnSecureToken": True,
    })
    if err:
        return False, err, {}

    uid      = data.get("localId", "")
    id_token = data.get("idToken", "")

    user_info = {
        "uid":               uid,
        "email":             email,
        "display_name":      data.get("displayName", email.split("@")[0]),
        "grade":             "",
        "favorite_subjects": [],
        "role":              "student",
        "_id_token":         id_token,
    }

    if uid and id_token:
        profile = _fs_get(f"users/{uid}", id_token)
        if profile:
            user_info.update({
                "display_name":      profile.get("display_name",      user_info["display_name"]),
                "grade":             profile.get("grade",             ""),
                "favorite_subjects": profile.get("favorite_subjects", []),
                "role":              profile.get("role",              "student"),
            })

    return True, "Đăng nhập thành công!", user_info


# ── Đặt lại mật khẩu ─────────────────────────────────────
def reset_password(email: str) -> tuple:
    _, err = _auth_post("sendOobCode", {
        "requestType": "PASSWORD_RESET",
        "email":       email,
    })
    if err:
        return False, err
    return True, f"Đã gửi email đặt lại mật khẩu đến {email}!"


# ── Cập nhật profile ──────────────────────────────────────
def update_profile(uid: str, display_name: str = None,
                   grade: str = None,
                   favorite_subjects: list = None) -> bool:
    id_token = st.session_state.get("_id_token", "")
    if not uid or not id_token:
        return False

    update = {}
    if display_name      is not None: update["display_name"]      = display_name
    if grade             is not None: update["grade"]             = grade
    if favorite_subjects is not None: update["favorite_subjects"] = favorite_subjects

    if update:
        _fs_set("users", uid, update, id_token)
    return True


def is_firebase_ok() -> bool:
    return bool(_API_KEY)
