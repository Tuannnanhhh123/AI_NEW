# ============================================================
# ai_engine.py — Random từ ngân hàng + Groq xáo đáp án
# Hash câu GỐC trước khi Groq paraphrase để chống trùng
# ============================================================
import json, re, random, requests
import streamlit as st

from config          import GROQ_API_URL, GROQ_HEADERS, GROQ_MODEL, NUM_QUESTIONS, DIFFICULTY_MAP
from question_bank   import QUESTION_BANK
from history_manager import get_used_hashes, save_exam, filter_new_questions
from teacher_manager import get_approved_for_exam

MAX_RETRIES = 2
_MIN_QUESTIONS = 16   # số câu tối thiểu cho phép


# ── Bước 1: Gom pool ─────────────────────────────────────
def _build_pool(subject: str, grade: str) -> list:
    local = QUESTION_BANK.get(subject, {}).get(grade, [])
    if not local:
        diff = DIFFICULTY_MAP.get(grade, "Khó")
        for g, d in DIFFICULTY_MAP.items():
            if d == diff and g in QUESTION_BANK.get(subject, {}):
                local = QUESTION_BANK[subject][g]
                break

    db_qs       = get_approved_for_exam(subject, grade)
    local_texts = {q["question"] for q in local}
    extra       = [q for q in db_qs if q["question"] not in local_texts]
    return local + extra


# ── Bước 2: Chọn câu, lọc trùng lịch sử ─────────────────
def _pick_questions(subject: str, grade: str, n: int) -> list:
    """
    n : số câu cần lấy (đã được validate >= _MIN_QUESTIONS)
    """
    pool = _build_pool(subject, grade)
    if not pool:
        return []

    used_hashes = get_used_hashes(subject, grade)
    new_pool    = filter_new_questions(pool, used_hashes)

    if len(new_pool) < n:
        # Hết câu mới → reset pool
        st.session_state["reset_pool"] = True
        chosen_pool = pool
    else:
        st.session_state["reset_pool"] = False
        chosen_pool = new_pool

    selected = random.sample(chosen_pool, min(n, len(chosen_pool)))
    random.shuffle(selected)
    return selected


# ── Bước 3: Lưu hash câu GỐC trước khi Groq xáo ─────────
def _save_original_hashes(subject: str, grade: str, questions: list):
    save_exam(subject, grade, questions)


# ── Bước 4: Groq xáo đáp án ──────────────────────────────
def _build_shuffle_prompt(questions: list) -> list:
    q_json = json.dumps(questions, ensure_ascii=False, indent=2)
    system_msg = (
        "Bạn là công cụ xử lý câu hỏi trắc nghiệm. "
        "QUAN TRỌNG: Chỉ trả về JSON array thuần túy, "
        "không có markdown, không có ```json, không có text nào khác."
    )
    user_msg = f"""Cho danh sách câu hỏi trắc nghiệm (JSON array):
{q_json}

NHIỆM VỤ:
1. Xáo ngẫu nhiên thứ tự 4 đáp án trong mỗi câu (options)
2. Cập nhật trường "answer" cho khớp sau khi xáo
3. KHÔNG paraphrase hay thay đổi nội dung câu hỏi — giữ nguyên 100%
4. TUYỆT ĐỐI KHÔNG thay đổi nội dung đáp án đúng hay giải thích
5. Giữ nguyên đúng 4 trường: question, options, answer, explanation

Trả về JSON array đúng cấu trúc gốc:
[{{"question":"...","options":["...","...","...","..."],"answer":"...","explanation":"..."}},...] """
    return [
        {"role": "system", "content": system_msg},
        {"role": "user",   "content": user_msg},
    ]


def _call_groq(messages: list) -> str | None:
    payload = {
        "model":       GROQ_MODEL,
        "messages":    messages,
        "temperature": 0.3,
        "max_tokens":  4096,
        "top_p":       0.9,
    }
    try:
        resp = requests.post(GROQ_API_URL, headers=GROQ_HEADERS,
                             json=payload, timeout=60)
    except requests.exceptions.Timeout:
        st.session_state["ai_error"] = "Timeout khi gọi Groq."
        return None
    except Exception as e:
        st.session_state["ai_error"] = str(e)
        return None

    if resp.status_code in (401, 403):
        st.session_state["ai_error"] = f"API key không hợp lệ (HTTP {resp.status_code})."
        return None
    if resp.status_code == 429:
        st.session_state["ai_error"] = "Rate limit — thử lại sau vài giây."
        return None
    if resp.status_code != 200:
        st.session_state["ai_error"] = f"HTTP {resp.status_code}: {resp.text[:150]}"
        return None

    try:
        return resp.json()["choices"][0]["message"]["content"].strip()
    except Exception:
        st.session_state["ai_error"] = "Không đọc được phản hồi từ Groq."
        return None


def _parse_questions(text: str, original: list) -> list | None:
    m = re.search(r'\[.*\]', text, re.DOTALL)
    if not m: return None
    raw = re.sub(r"```json|```", "", m.group(0)).strip()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return None
    valid = [
        q for q in data
        if isinstance(q, dict)
        and all(k in q for k in ("question","options","answer","explanation"))
        and isinstance(q["options"], list)
        and len(q["options"]) == 4
        and q["answer"] in q["options"]
        and len(q["question"].strip()) > 5
    ]
    return valid if len(valid) == len(original) else None


def _shuffle_with_groq(questions: list) -> tuple[list, str]:
    messages = _build_shuffle_prompt(questions)
    for attempt in range(1, MAX_RETRIES + 1):
        text = _call_groq(messages)
        if text is None: break
        shuffled = _parse_questions(text, questions)
        if shuffled:
            st.session_state["ai_error"] = None
            return shuffled, "ai"
        messages = messages + [
            {"role": "assistant", "content": text},
            {"role": "user", "content":
                "JSON không hợp lệ hoặc thiếu câu. "
                "Trả lại đúng JSON array, 'answer' phải khớp một trong 4 'options'."}
        ]
    st.session_state["ai_error"] = "Groq không phản hồi — xáo đáp án local."
    return _shuffle_local(questions), "local"


def _shuffle_local(questions: list) -> list:
    result = []
    for q in questions:
        opts = q["options"][:]
        random.shuffle(opts)
        result.append({**q, "options": opts, "answer": q["answer"]})
    return result


# ── Entry point ───────────────────────────────────────────
def generate_exam(subject: str, grade: str,
                  num_questions: int | None = None) -> tuple[list, str]:
    """
    num_questions : số câu muốn tạo. Nếu None → dùng NUM_QUESTIONS từ config.
                    Luôn được clamp về [_MIN_QUESTIONS, 100].
    """
    st.session_state["ai_error"]       = None
    st.session_state["verify_summary"] = None
    st.session_state["dup_filtered"]   = 0

    # Xác định số câu — clamp an toàn
    n = int(num_questions) if num_questions is not None else NUM_QUESTIONS
    n = max(_MIN_QUESTIONS, min(100, n))

    questions = _pick_questions(subject, grade, n)
    if not questions:
        st.session_state["ai_error"] = "Ngân hàng câu hỏi trống cho môn/lớp này."
        return [], "local"

    # Lưu hash câu GỐC TRƯỚC khi Groq paraphrase
    _save_original_hashes(subject, grade, questions)

    final, source = _shuffle_with_groq(questions)

    pool      = _build_pool(subject, grade)
    used      = get_used_hashes(subject, grade)
    remaining = len(filter_new_questions(pool, used))

    if st.session_state.get("reset_pool"):
        st.session_state["verify_summary"] = (
            "⚠️ Đã dùng hết câu mới — reset và lấy lại từ đầu."
        )
    else:
        st.session_state["verify_summary"] = (
            f"✅ {len(final)} câu | Pool: {len(pool)} câu "
            f"| Còn ~{remaining} câu chưa dùng"
        )
    return final, source


# ── Chấm điểm ────────────────────────────────────────────
def grade_exam(questions: list, answers: dict) -> int:
    return sum(
        1 for i, q in enumerate(questions)
        if answers.get(i) == q["answer"]
    )