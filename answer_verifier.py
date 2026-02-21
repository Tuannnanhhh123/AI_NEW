# ============================================================
# answer_verifier.py — Tự động verify đáp án AI tạo ra
# Rule-based: kiểm tra tính nhất quán logic của từng câu
# ============================================================
import re, math


# ── Entry point chính ─────────────────────────────────────
def verify_questions(questions: list, subject: str) -> tuple[list, list]:
    """
    Kiểm tra danh sách câu hỏi, trả về:
      - verified : câu hỏi đã qua kiểm tra (hoặc đã sửa)
      - rejected : câu hỏi bị loại (lỗi nghiêm trọng không sửa được)
    """
    verified, rejected = [], []

    for q in questions:
        ok, fixed_q, reason = _check_one(q, subject)
        if ok:
            verified.append(fixed_q)
        else:
            rejected.append({"question": q, "reason": reason})

    return verified, rejected


# ── Kiểm tra từng câu ────────────────────────────────────
def _check_one(q: dict, subject: str) -> tuple[bool, dict, str]:
    """Trả về (passed, question_có_thể_sửa, lý_do_nếu_fail)."""

    # 1. Cấu trúc cơ bản
    for key in ("question", "options", "answer", "explanation"):
        if key not in q:
            return False, q, f"Thiếu trường '{key}'"

    if len(q["options"]) != 4:
        return False, q, f"Cần đúng 4 options, có {len(q['options'])}"

    if not q["question"].strip():
        return False, q, "Câu hỏi rỗng"

    # 2. Đáp án phải nằm trong options
    if q["answer"] not in q["options"]:
        # Thử tìm option gần nhất (whitespace/case khác)
        fixed = _fuzzy_match_answer(q)
        if fixed:
            return True, fixed, ""
        return False, q, f"answer '{q['answer']}' không khớp với bất kỳ option nào"

    # 3. Các option phải khác nhau
    if len(set(q["options"])) != 4:
        return False, q, "Có options bị trùng nhau"

    # 4. Kiểm tra theo môn
    if subject == "Toán":
        ok, reason = _verify_math(q)
        if not ok:
            return False, q, reason

    elif subject == "Tiếng Anh":
        ok, reason = _verify_english(q)
        if not ok:
            return False, q, reason

    elif subject == "Ngữ Văn":
        ok, reason = _verify_nguvan(q)
        if not ok:
            return False, q, reason

    return True, q, ""


# ── Rule: Toán ────────────────────────────────────────────
def _verify_math(q: dict) -> tuple[bool, str]:
    """Kiểm tra tính đúng đắn các phép tính đơn giản."""
    text   = q["question"]
    answer = q["answer"].strip()

    # Kiểm tra phép tính số học đơn giản dạng "A op B = ?"
    m = re.search(r'([\d\.]+)\s*([+\-×x\*÷/])\s*([\d\.]+)\s*=\s*\?', text)
    if m:
        try:
            a, op, b = float(m.group(1)), m.group(2), float(m.group(3))
            ops = {'+': a+b, '-': a-b, '×': a*b, 'x': a*b,
                   '*': a*b, '÷': a/b if b else None, '/': a/b if b else None}
            expected = ops.get(op)
            if expected is not None:
                # So sánh xấp xỉ
                try:
                    ans_val = float(re.sub(r'[^\d\.\-]', '', answer))
                    if not math.isclose(ans_val, expected, rel_tol=1e-6):
                        return False, (
                            f"Phép tính {a}{op}{b} = {expected} "
                            f"nhưng answer là '{answer}'"
                        )
                except ValueError:
                    pass   # answer không phải số thuần → bỏ qua
        except Exception:
            pass

    # Kiểm tra C(n,k) cơ bản
    m = re.search(r'C\((\d+),(\d+)\)', text)
    if m:
        n, k = int(m.group(1)), int(m.group(2))
        if 0 <= k <= n <= 20:
            expected = math.comb(n, k)
            try:
                ans_val = float(re.sub(r'[^\d\.\-]', '', answer))
                if not math.isclose(ans_val, expected, rel_tol=1e-6):
                    return False, f"C({n},{k}) = {expected} nhưng answer là '{answer}'"
            except ValueError:
                pass

    # Kiểm tra lũy thừa đơn giản a^n
    m = re.search(r'(\d+)\s*[\^⁰¹²³⁴⁵⁶⁷⁸⁹]\s*(\d+)', text)
    if not m:
        m = re.search(r'(\d+)\^(\d+)', text)
    if m:
        try:
            base, exp = int(m.group(1)), int(m.group(2))
            if exp <= 10:
                expected = base ** exp
                ans_val  = float(re.sub(r'[^\d\.\-]', '', answer))
                if not math.isclose(ans_val, expected, rel_tol=1e-6):
                    return False, f"{base}^{exp} = {expected} nhưng answer là '{answer}'"
        except Exception:
            pass

    return True, ""


# ── Rule: Tiếng Anh ───────────────────────────────────────
def _verify_english(q: dict) -> tuple[bool, str]:
    """Kiểm tra một số quy tắc cơ bản của Tiếng Anh."""
    answer = q["answer"].strip()
    text   = q["question"]

    # Kiểm tra câu hỏi và options phải bằng tiếng Anh
    viet_chars = re.findall(r'[àáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđ]', text.lower())
    if len(viet_chars) > 5:
        return False, "Câu hỏi Tiếng Anh chứa quá nhiều ký tự tiếng Việt"

    # Options không được rỗng hoặc quá ngắn (< 1 ký tự)
    for opt in q["options"]:
        if len(opt.strip()) == 0:
            return False, f"Option rỗng: '{opt}'"

    # Answer không được là placeholder
    placeholders = ["...", "???", "none", "n/a", ""]
    if answer.lower() in placeholders:
        return False, f"Answer là placeholder: '{answer}'"

    return True, ""


# ── Rule: Ngữ Văn ─────────────────────────────────────────
def _verify_nguvan(q: dict) -> tuple[bool, str]:
    """Kiểm tra một số quy tắc cơ bản của Ngữ Văn."""
    answer = q["answer"].strip()

    # Answer không rỗng
    if not answer:
        return False, "Answer rỗng"

    # Answer không được là placeholder
    if answer in ["...", "???", "Không có", "Tất cả đều sai"]:
        return False, f"Answer là placeholder: '{answer}'"

    # Explanation phải có nội dung thực
    expl = q.get("explanation", "").strip()
    if len(expl) < 10:
        return False, f"Explanation quá ngắn: '{expl}'"

    return True, ""


# ── Fuzzy match answer ────────────────────────────────────
def _fuzzy_match_answer(q: dict) -> dict | None:
    """
    Thử sửa lỗi answer không khớp options do whitespace/case.
    Trả về câu hỏi đã sửa hoặc None nếu không sửa được.
    """
    ans_norm = q["answer"].strip().lower()
    for opt in q["options"]:
        if opt.strip().lower() == ans_norm:
            fixed = dict(q)
            fixed["answer"] = opt   # dùng đúng text của option
            return fixed
    return None


# ── Tóm tắt kết quả verify ───────────────────────────────
def verify_summary(verified: list, rejected: list) -> str:
    total = len(verified) + len(rejected)
    if not rejected:
        return f"✅ {total}/{total} câu hợp lệ"
    reasons = "; ".join(r["reason"] for r in rejected[:3])
    return (
        f"⚠️ {len(verified)}/{total} câu hợp lệ — "
        f"Đã loại {len(rejected)} câu: {reasons}"
    )