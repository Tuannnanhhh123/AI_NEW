# ============================================================
# teacher_manager.py — Quản lý câu hỏi giáo viên qua SQLite
# ============================================================
import sqlite3, json, time
from datetime import datetime

DB_FILE = "teacher_bank.db"


# ── Kết nối SQLite với WAL mode + timeout ─────────────────
def _conn():
    """
    WAL mode cho phép nhiều reader + 1 writer cùng lúc.
    timeout=30 + busy_timeout=10000 để tránh lỗi 'database is locked'.
    """
    con = sqlite3.connect(DB_FILE, timeout=30, check_same_thread=False)
    con.execute("PRAGMA journal_mode=WAL")
    con.execute("PRAGMA synchronous=NORMAL")
    con.execute("PRAGMA busy_timeout=10000")
    return con


def _conn_retry(max_retries: int = 3):
    """Retry kết nối nếu DB bị lock (dùng cho WRITE quan trọng)."""
    for attempt in range(max_retries):
        try:
            return _conn()
        except sqlite3.OperationalError as e:
            if "locked" in str(e) and attempt < max_retries - 1:
                time.sleep(0.5 * (attempt + 1))
                continue
            raise


# ── Khởi tạo DB ──────────────────────────────────────────
def init_db():
    with _conn() as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS questions (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                subject     TEXT    NOT NULL,
                grade       TEXT    NOT NULL,
                question    TEXT    NOT NULL,
                options     TEXT    NOT NULL,
                answer      TEXT    NOT NULL,
                explanation TEXT    NOT NULL,
                approved    INTEGER NOT NULL DEFAULT 0,
                created_by  TEXT    NOT NULL DEFAULT 'teacher',
                created_at  TEXT    NOT NULL
            )
        """)
        con.execute("""
            CREATE TABLE IF NOT EXISTS teacher_exams (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                name       TEXT NOT NULL,
                subject    TEXT NOT NULL,
                grade      TEXT NOT NULL,
                q_ids      TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)


def _row_to_q(row) -> dict:
    return {
        "id":          row[0],
        "subject":     row[1],
        "grade":       row[2],
        "question":    row[3],
        "options":     json.loads(row[4]),
        "answer":      row[5],
        "explanation": row[6],
        "approved":    bool(row[7]),
        "created_by":  row[8],
        "created_at":  row[9],
    }


# ── CRUD câu hỏi ─────────────────────────────────────────
def add_question(subject: str, grade: str, question: str,
                 options: list, answer: str, explanation: str,
                 created_by: str = "teacher") -> int:
    with _conn_retry() as con:
        cur = con.execute(
            """INSERT INTO questions
               (subject, grade, question, options, answer, explanation, approved, created_by, created_at)
               VALUES (?,?,?,?,?,?,0,?,?)""",
            (subject, grade, question, json.dumps(options, ensure_ascii=False),
             answer, explanation, created_by, _now())
        )
        return cur.lastrowid


def update_question(q_id: int, question: str, options: list,
                    answer: str, explanation: str):
    with _conn_retry() as con:
        con.execute(
            """UPDATE questions
               SET question=?, options=?, answer=?, explanation=?, approved=0
               WHERE id=?""",
            (question, json.dumps(options, ensure_ascii=False),
             answer, explanation, q_id)
        )


def delete_question(q_id: int):
    with _conn_retry() as con:
        con.execute("DELETE FROM questions WHERE id=?", (q_id,))


def approve_question(q_id: int, approved: bool = True):
    with _conn_retry() as con:
        con.execute("UPDATE questions SET approved=? WHERE id=?",
                    (1 if approved else 0, q_id))


def approve_all(subject: str, grade: str):
    with _conn_retry() as con:
        con.execute(
            "UPDATE questions SET approved=1 WHERE subject=? AND grade=?",
            (subject, grade)
        )


# ── Truy vấn câu hỏi ─────────────────────────────────────
def get_questions(subject: str = None, grade: str = None,
                  approved_only: bool = False) -> list:
    sql    = "SELECT * FROM questions WHERE 1=1"
    params = []
    if subject:
        sql += " AND subject=?"; params.append(subject)
    if grade:
        sql += " AND grade=?";   params.append(grade)
    if approved_only:
        sql += " AND approved=1"
    sql += " ORDER BY id DESC"
    with _conn() as con:
        rows = con.execute(sql, params).fetchall()
    return [_row_to_q(r) for r in rows]


def get_approved_for_exam(subject: str, grade: str) -> list:
    qs = get_questions(subject, grade, approved_only=True)
    return [{"question": q["question"], "options": q["options"],
             "answer": q["answer"], "explanation": q["explanation"]}
            for q in qs]


def get_stats() -> dict:
    with _conn() as con:
        rows = con.execute(
            """SELECT subject, grade,
                      SUM(CASE WHEN approved=1 THEN 1 ELSE 0 END) as approved,
                      SUM(CASE WHEN approved=0 THEN 1 ELSE 0 END) as pending
               FROM questions GROUP BY subject, grade"""
        ).fetchall()
    return {
        f"{r[0]}|{r[1]}": {"approved": r[2], "pending": r[3]}
        for r in rows
    }


# ── Đề thi riêng của giáo viên ───────────────────────────
def save_teacher_exam(name: str, subject: str, grade: str, q_ids: list) -> int:
    with _conn_retry() as con:
        cur = con.execute(
            "INSERT INTO teacher_exams (name,subject,grade,q_ids,created_at) VALUES (?,?,?,?,?)",
            (name, subject, grade, json.dumps(q_ids), _now())
        )
        return cur.lastrowid


def get_teacher_exams() -> list:
    with _conn() as con:
        rows = con.execute(
            "SELECT id,name,subject,grade,q_ids,created_at FROM teacher_exams ORDER BY id DESC"
        ).fetchall()
    return [{"id":r[0],"name":r[1],"subject":r[2],"grade":r[3],
             "q_ids":json.loads(r[4]),"created_at":r[5]} for r in rows]


def delete_teacher_exam(exam_id: int):
    with _conn_retry() as con:
        con.execute("DELETE FROM teacher_exams WHERE id=?", (exam_id,))


def get_exam_questions(q_ids: list) -> list:
    if not q_ids:
        return []
    placeholders = ",".join("?" * len(q_ids))
    with _conn() as con:
        rows = con.execute(
            f"SELECT * FROM questions WHERE id IN ({placeholders})", q_ids
        ).fetchall()
    return [{"question":r[3],"options":json.loads(r[4]),
             "answer":r[5],"explanation":r[6]} for r in rows]


# ── Helper ────────────────────────────────────────────────
def _now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


init_db()
