# ============================================================
# question_bank.py — Gom tất cả file bank thành QUESTION_BANK
# ============================================================

# ── Toán ─────────────────────────────────────────────────
from banks.toan_l9  import QUESTIONS as _TOAN_L9
from banks.toan_l10 import QUESTIONS as _TOAN_L10
from banks.toan_l11 import QUESTIONS as _TOAN_L11
from banks.toan_l12 import QUESTIONS as _TOAN_L12
from banks.toan_dh  import QUESTIONS as _TOAN_DH

# ── Ngữ Văn ──────────────────────────────────────────────
from banks.van_l9   import QUESTIONS as _VAN_L9
from banks.van_l10  import QUESTIONS as _VAN_L10
from banks.van_l11  import QUESTIONS as _VAN_L11
from banks.van_l12  import QUESTIONS as _VAN_L12
from banks.van_dh   import QUESTIONS as _VAN_DH

# ── Tiếng Anh ─────────────────────────────────────────────
from banks.anh_l9   import QUESTIONS as _ANH_L9
from banks.anh_l10  import QUESTIONS as _ANH_L10
from banks.anh_l11  import QUESTIONS as _ANH_L11
from banks.anh_l12  import QUESTIONS as _ANH_L12
from banks.anh_dh   import QUESTIONS as _ANH_DH

# ── Vật Lý ───────────────────────────────────────────────
from banks.ly_l10   import QUESTIONS as _LY_L10
from banks.ly_l11   import QUESTIONS as _LY_L11
from banks.ly_l12   import QUESTIONS as _LY_L12
from banks.ly_dh    import QUESTIONS as _LY_DH

# ── Hóa Học ──────────────────────────────────────────────
from banks.hoa_l10  import QUESTIONS as _HOA_L10
from banks.hoa_l11  import QUESTIONS as _HOA_L11
from banks.hoa_l12  import QUESTIONS as _HOA_L12
from banks.hoa_dh   import QUESTIONS as _HOA_DH

# ── Sinh Học ──────────────────────────────────────────────
from banks.sinh_l10 import QUESTIONS as _SINH_L10
from banks.sinh_l11 import QUESTIONS as _SINH_L11
from banks.sinh_l12 import QUESTIONS as _SINH_L12
from banks.sinh_dh  import QUESTIONS as _SINH_DH

# ── Gom thành QUESTION_BANK ───────────────────────────────
QUESTION_BANK: dict = {
    "Toán": {
        "Lớp 9 (THCS)":       _TOAN_L9,
        "Lớp 10 (THPT)":      _TOAN_L10,
        "Lớp 11 (THPT)":      _TOAN_L11,
        "Lớp 12 (THPT)":      _TOAN_L12,
        "Đại học / Nâng cao": _TOAN_DH,
    },
    "Ngữ Văn": {
        "Lớp 9 (THCS)":       _VAN_L9,
        "Lớp 10 (THPT)":      _VAN_L10,
        "Lớp 11 (THPT)":      _VAN_L11,
        "Lớp 12 (THPT)":      _VAN_L12,
        "Đại học / Nâng cao": _VAN_DH,
    },
    "Tiếng Anh": {
        "Lớp 9 (THCS)":       _ANH_L9,
        "Lớp 10 (THPT)":      _ANH_L10,
        "Lớp 11 (THPT)":      _ANH_L11,
        "Lớp 12 (THPT)":      _ANH_L12,
        "Đại học / Nâng cao": _ANH_DH,
    },
    "Vật Lý": {
        "Lớp 10 (THPT)":      _LY_L10,
        "Lớp 11 (THPT)":      _LY_L11,
        "Lớp 12 (THPT)":      _LY_L12,
        "Đại học / Nâng cao": _LY_DH,
    },
    "Hóa Học": {
        "Lớp 10 (THPT)":      _HOA_L10,
        "Lớp 11 (THPT)":      _HOA_L11,
        "Lớp 12 (THPT)":      _HOA_L12,
        "Đại học / Nâng cao": _HOA_DH,
    },
    "Sinh Học": {
        "Lớp 10 (THPT)":      _SINH_L10,
        "Lớp 11 (THPT)":      _SINH_L11,
        "Lớp 12 (THPT)":      _SINH_L12,
        "Đại học / Nâng cao": _SINH_DH,
    },
}