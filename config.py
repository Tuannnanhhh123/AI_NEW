# ============================================================
# config.py — Cấu hình toàn cục, đọc từ .env
# ============================================================
import os
from dotenv import load_dotenv

# Đọc file .env (nếu chạy local)
load_dotenv()

# ── GROQ API ──────────────────────────────────────────────
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
GROQ_MODEL   = "llama-3.3-70b-versatile"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type":  "application/json",
}

if not GROQ_API_KEY:
    import warnings
    warnings.warn("⚠️ GROQ_API_KEY chưa được cấu hình trong file .env!")

# ── ĐỀ THI ────────────────────────────────────────────────
NUM_QUESTIONS   = 10
SUBJECT_OPTIONS = ["Toán", "Ngữ Văn", "Tiếng Anh", "Vật Lý", "Hóa Học", "Sinh Học"]

# ── MÃ GIÁO VIÊN ─────────────────────────────────────────
TEACHER_CODE = os.environ.get("TEACHER_CODE", "GV@2025")

# ── CẤU HÌNH LỚP HỌC ─────────────────────────────────────
GRADE_CONFIG = {
    "Lớp 9 (THCS)":       {"level":"THCS",    "tag":"tag-middle", "emoji":"🎯", "time":20,
                            "desc":"Toán, Văn, Anh cơ bản THCS",
                            "subjects":["Toán","Ngữ Văn","Tiếng Anh"]},
    "Lớp 10 (THPT)":      {"level":"THPT",    "tag":"tag-high",   "emoji":"📊", "time":25,
                            "desc":"Đầy đủ 6 môn, nền tảng THPT",
                            "subjects":["Toán","Ngữ Văn","Tiếng Anh","Vật Lý","Hóa Học","Sinh Học"]},
    "Lớp 11 (THPT)":      {"level":"THPT",    "tag":"tag-high",   "emoji":"📡", "time":25,
                            "desc":"Nâng cao, luyện thi THPT",
                            "subjects":["Toán","Ngữ Văn","Tiếng Anh","Vật Lý","Hóa Học","Sinh Học"]},
    "Lớp 12 (THPT)":      {"level":"THPT",    "tag":"tag-high",   "emoji":"🏆", "time":25,
                            "desc":"Ôn thi THPT Quốc gia",
                            "subjects":["Toán","Ngữ Văn","Tiếng Anh","Vật Lý","Hóa Học","Sinh Học"]},
    "Đại học / Nâng cao": {"level":"Đại học", "tag":"tag-uni",    "emoji":"🎓", "time":30,
                            "desc":"Kiến thức đại học, chuyên sâu",
                            "subjects":["Toán","Tiếng Anh","Vật Lý","Hóa Học","Sinh Học"]},
}

# ── MAPPING ĐỘ KHÓ ───────────────────────────────────────
DIFFICULTY_MAP = {
    "Lớp 9 (THCS)":       "Trung bình",
    "Lớp 10 (THPT)":      "Khó",
    "Lớp 11 (THPT)":      "Khó",
    "Lớp 12 (THPT)":      "Khó",
    "Đại học / Nâng cao": "Khó",
}

# ── FIREBASE CONFIG ───────────────────────────────────────
FIREBASE_CONFIG = {
    "apiKey":            os.environ.get("FB_API_KEY",        ""),
    "authDomain":        os.environ.get("FB_AUTH_DOMAIN",    ""),
    "projectId":         os.environ.get("FB_PROJECT_ID",     ""),
    "storageBucket":     os.environ.get("FB_STORAGE_BUCKET", ""),
    "messagingSenderId": os.environ.get("FB_MESSAGING_ID",   ""),
    "appId":             os.environ.get("FB_APP_ID",         ""),
}