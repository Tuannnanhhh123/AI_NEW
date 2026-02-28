# ============================================================
# pages.py — UI chuyên nghiệp: home/select/exam/result/history
# ============================================================
import time
import streamlit as st
import streamlit.components.v1 as components

from config       import GRADE_CONFIG, SUBJECT_OPTIONS, NUM_QUESTIONS
from ai_engine    import generate_exam, grade_exam
from user_manager import save_exam_result, get_user_exams, get_user_stats

# ── CSS riêng cho pages ───────────────────────────────────
_PAGE_CSS = """
<style>
/* ── Hero banner ── */
.hero {
    background: linear-gradient(135deg,#1a73e8 0%,#1557b0 50%,#7c3aed 100%);
    border-radius: 16px; padding: 2rem 2rem 1.5rem;
    color: white; margin-bottom: 1.5rem;
    position: relative; overflow: hidden;
}
.hero::before {
    content:""; position:absolute; top:-40px; right:-40px;
    width:180px; height:180px; border-radius:50%;
    background:rgba(255,255,255,.07);
}
.hero::after {
    content:""; position:absolute; bottom:-30px; right:60px;
    width:100px; height:100px; border-radius:50%;
    background:rgba(255,255,255,.05);
}
.hero-title { font-size:1.8rem; font-weight:800; margin-bottom:.3rem; }
.hero-sub   { font-size:.95rem; opacity:.85; margin-bottom:1.2rem; }
.hero-stats { display:flex; gap:1.5rem; flex-wrap:wrap; }
.hero-stat  {
    background:rgba(255,255,255,.15); border-radius:10px;
    padding:.5rem 1rem; text-align:center; backdrop-filter:blur(4px);
}
.hero-stat-val { font-size:1.3rem; font-weight:800; }
.hero-stat-lbl { font-size:.7rem; opacity:.8; }

/* ── Stat cards ── */
.stat-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1rem; margin-bottom:1.5rem; }
.stat-card {
    background:white; border-radius:12px; padding:1rem 1.2rem;
    border:1px solid #e0e7ff;
    box-shadow:0 2px 8px rgba(26,115,232,.06);
    text-align:center; transition:transform .2s, box-shadow .2s;
}
.stat-card:hover { transform:translateY(-3px); box-shadow:0 6px 20px rgba(26,115,232,.12); }
.stat-card-val { font-size:1.6rem; font-weight:800; color:#1a73e8; }
.stat-card-lbl { font-size:.75rem; color:#888; font-weight:600; margin-top:.2rem; }
.stat-card-sub { font-size:.7rem; color:#bbb; margin-top:.1rem; }

/* ── Subject cards ── */
.subj-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:.75rem; margin-bottom:1.5rem; }
.subj-card {
    background:white; border-radius:12px; padding:1rem;
    border:1px solid #e0e7ff; cursor:pointer;
    transition:all .2s; text-align:center;
    box-shadow:0 1px 4px rgba(0,0,0,.04);
}
.subj-card:hover { border-color:#1a73e8; box-shadow:0 4px 16px rgba(26,115,232,.15); transform:translateY(-2px); }
.subj-card .icon { font-size:1.8rem; margin-bottom:.3rem; }
.subj-card .name { font-size:.82rem; font-weight:700; color:#1a1a2e; }

/* ── Exam card ── */
.exam-header {
    background: linear-gradient(135deg,#1a73e8,#1557b0);
    border-radius:12px; padding:1rem 1.2rem;
    color:white; margin-bottom:1rem;
    display:flex; justify-content:space-between; align-items:center;
}
.exam-title { font-size:1rem; font-weight:700; }
.exam-meta  { font-size:.75rem; opacity:.85; margin-top:.2rem; }

/* ════════════════════════════════════
   PREMIUM TIMER
════════════════════════════════════ */
.timer-outer {
    position: relative;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    padding: .5rem;
}
.timer-svg-wrap {
    position: relative;
    width: 90px; height: 90px;
}
.timer-svg-wrap svg {
    transform: rotate(-90deg);
}
.timer-track { fill: none; stroke-width: 5; }
.timer-progress {
    fill: none; stroke-width: 5;
    stroke-linecap: round;
    transition: stroke-dashoffset .9s linear, stroke .5s ease;
}
.timer-center {
    position: absolute; inset: 0;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    line-height: 1.1;
}
.timer-digits {
    font-size: 1.25rem; font-weight: 800;
    letter-spacing: -.5px;
    font-family: 'Inter', monospace;
}
.timer-label {
    font-size: .55rem; font-weight: 600;
    letter-spacing: .04em; text-transform: uppercase;
    opacity: .65;
}
.t-green .timer-track    { stroke: #d1fae5; }
.t-green .timer-progress { stroke: #10b981; }
.t-green .timer-digits   { color: #065f46; }
.t-green .timer-label    { color: #065f46; }
.t-yellow .timer-track    { stroke: #fef3c7; }
.t-yellow .timer-progress { stroke: #f59e0b; }
.t-yellow .timer-digits   { color: #92400e; }
.t-yellow .timer-label    { color: #92400e; }
.t-red .timer-track    { stroke: #fee2e2; }
.t-red .timer-progress { stroke: #ef4444; }
.t-red .timer-digits   { color: #991b1b; }
.t-red .timer-label    { color: #991b1b; }
.t-red .timer-digits   { animation: digits-shake .5s ease-in-out infinite; }
@keyframes digits-shake {
    0%,100%{ transform:translateX(0) }
    25%    { transform:translateX(-2px) }
    75%    { transform:translateX(2px) }
}
.timer-card {
    border-radius: 14px; padding: .6rem .8rem;
    text-align: center; border: 2px solid;
    transition: all .4s ease;
    min-width: 110px;
}
.timer-card.t-green  { background:#f0fdf9; border-color:#10b981; }
.timer-card.t-yellow { background:#fffbeb; border-color:#f59e0b;
                        box-shadow: 0 0 12px rgba(245,158,11,.2); }
.timer-card.t-red    { background:#fff5f5; border-color:#ef4444;
                        box-shadow: 0 0 18px rgba(239,68,68,.3);
                        animation: card-pulse .8s ease-in-out infinite; }
@keyframes card-pulse {
    0%,100%{ box-shadow:0 0 12px rgba(239,68,68,.25); }
    50%    { box-shadow:0 0 24px rgba(239,68,68,.5); }
}
.timer-toast {
    display: flex; align-items: center; gap: .6rem;
    border-radius: 10px; padding: .6rem 1rem;
    font-size: .82rem; font-weight: 600;
    margin-bottom: .75rem;
    animation: toast-in .3s ease;
}
.timer-toast.warn {
    background: #fffbeb; border: 1px solid #fcd34d;
    border-left: 4px solid #f59e0b; color: #92400e;
}
.timer-toast.danger {
    background: #fff5f5; border: 1px solid #fca5a5;
    border-left: 4px solid #ef4444; color: #991b1b;
    animation: toast-in .3s ease, toast-pulse 1s ease-in-out infinite;
}
@keyframes toast-in    { from{opacity:0;transform:translateY(-8px)} to{opacity:1;transform:none} }
@keyframes toast-pulse { 0%,100%{opacity:1} 50%{opacity:.75} }
.auto-bar-wrap {
    height: 4px; border-radius: 2px;
    background: #fee2e2; margin-top: .4rem; overflow: hidden;
}
.auto-bar-fill {
    height: 100%; border-radius: 2px;
    background: linear-gradient(90deg,#ef4444,#dc2626);
    transition: width .9s linear;
}

/* ── Question card ── */
.q-card {
    background:white; border-radius:12px;
    border:1px solid #e0e7ff; margin-bottom:.75rem;
    overflow:hidden; transition:border-color .2s;
    box-shadow:0 1px 4px rgba(0,0,0,.04);
}
.q-card:hover { border-color:#a5b4fc; }
.q-card.unanswered { border-color:#fca5a5; background:#fff5f5; }
.q-card.answered   { border-left:4px solid #1e8e3e; }
.q-header {
    padding:.75rem 1rem .5rem;
    display:flex; align-items:flex-start; gap:.6rem;
}
.q-num {
    background:#e8f0fe; color:#1a73e8;
    border-radius:6px; padding:.2rem .5rem;
    font-size:.75rem; font-weight:800;
    flex-shrink:0; margin-top:.1rem;
}
.q-num.unanswered { background:#fee2e2; color:#d93025; }
.q-text { font-size:.9rem; font-weight:600; color:#1a1a2e; line-height:1.5; }
.q-body { padding:.25rem 1rem .75rem; }

/* ── Progress exam ── */
.prog-wrap {
    background:white; border-radius:10px;
    padding:.75rem 1rem; margin-bottom:1rem;
    border:1px solid #e0e7ff;
    display:flex; align-items:center; gap:1rem;
}
.prog-bar-bg {
    flex:1; height:8px; background:#e0e7ff;
    border-radius:99px; overflow:hidden;
}
.prog-bar-fill {
    height:100%; border-radius:99px;
    background:linear-gradient(90deg,#1a73e8,#7c3aed);
    transition:width .4s ease;
}
.prog-text { font-size:.8rem; font-weight:700; color:#1a73e8; white-space:nowrap; }

/* ── Result score ring ── */
.result-hero {
    text-align:center; padding:2rem 1rem 1.5rem;
    background:linear-gradient(135deg,#f0f4ff,#faf5ff);
    border-radius:16px; margin-bottom:1.5rem;
    border:1px solid #e0e7ff;
}
.score-ring {
    width:130px; height:130px; border-radius:50%;
    margin:0 auto 1rem;
    display:flex; flex-direction:column;
    align-items:center; justify-content:center;
    font-weight:800; position:relative;
    box-shadow:0 4px 20px rgba(26,115,232,.2);
}
.score-ring-val { font-size:2rem; line-height:1; }
.score-ring-lbl { font-size:.7rem; opacity:.8; }
.score-gold   { background:linear-gradient(135deg,#f59e0b,#d97706); color:white; }
.score-silver { background:linear-gradient(135deg,#1a73e8,#1557b0); color:white; }
.score-bronze { background:linear-gradient(135deg,#6b7280,#4b5563); color:white; }
.result-rank  { font-size:1.3rem; font-weight:800; color:#1a1a2e; margin-bottom:.3rem; }
.result-sub   { font-size:.85rem; color:#888; }

/* ── Result detail card ── */
.res-card {
    border-radius:10px; padding:.75rem 1rem;
    margin-bottom:.5rem; border:1px solid;
    display:flex; align-items:flex-start; gap:.75rem;
}
.res-card.correct { background:#f0fdf4; border-color:#bbf7d0; }
.res-card.wrong   { background:#fff5f5; border-color:#fecaca; }
.res-card.skipped { background:#f9fafb; border-color:#e5e7eb; }
.res-icon { font-size:1.1rem; flex-shrink:0; margin-top:.1rem; }
.res-q    { font-size:.83rem; font-weight:600; color:#1a1a2e; margin-bottom:.3rem; }
.res-ans  { font-size:.78rem; }

/* ── History card ── */
.hist-card {
    background:white; border-radius:12px;
    border:1px solid #e0e7ff; margin-bottom:.75rem;
    overflow:hidden; box-shadow:0 1px 4px rgba(0,0,0,.04);
}
.hist-head {
    padding:.75rem 1rem;
    display:flex; align-items:center; gap:.75rem;
    cursor:pointer;
}
.hist-badge {
    width:44px; height:44px; border-radius:10px;
    display:flex; align-items:center; justify-content:center;
    font-size:1.2rem; flex-shrink:0;
}
.hist-badge.gold   { background:#fef3c7; }
.hist-badge.silver { background:#dbeafe; }
.hist-badge.bronze { background:#f3f4f6; }
.hist-info { flex:1; min-width:0; }
.hist-title { font-size:.88rem; font-weight:700; color:#1a1a2e; }
.hist-meta  { font-size:.72rem; color:#888; margin-top:.1rem; }
.hist-score { text-align:right; flex-shrink:0; }
.hist-pct   { font-size:1.1rem; font-weight:800; }
.hist-pts   { font-size:.7rem; color:#888; }

/* ════════════════════════════════════
   GRADE CARD — xanh đậm hơn
════════════════════════════════════ */
.grade-card {
    background: white;
    border-radius: 12px;
    padding: 1.2rem;
    border: 2px solid #c5d8fc;
    cursor: pointer;
    transition: all .2s;
    text-align: center;
    box-shadow: 0 2px 8px rgba(21,87,176,.08);
}
.grade-card:hover {
    border-color: #1557b0;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(21,87,176,.18);
    background: #eef3fd;
}
.grade-card.active {
    border-color: #0d47a1;
    background: linear-gradient(135deg, #e8f0fe, #dbeafe);
    box-shadow: 0 4px 16px rgba(13,71,161,.2);
}
.grade-emoji { font-size:2rem; margin-bottom:.4rem; }
.grade-name  { font-size:.82rem; font-weight:700; color:#0d47a1; }
.grade-desc  { font-size:.7rem; color:#1557b0; margin-top:.2rem; font-weight:600; }

/* ── Section title ── */
.sec-title {
    font-size:.7rem; font-weight:700; color:#94a3b8;
    letter-spacing:.08em; text-transform:uppercase;
    margin:.75rem 0 .6rem;
}

/* ── Confirm banner ── */
.confirm-banner {
    background:#fff3cd; border:1px solid #f4a300;
    border-left:4px solid #f4a300; border-radius:8px;
    padding:.75rem 1rem; margin-bottom:.75rem;
    font-size:.85rem;
}

/* ════════════════════════════════════
   BUTTONS chọn môn + Tạo đề + Quay lại — xanh đậm
════════════════════════════════════ */

/* Nút primary (active môn, Tạo đề thi) */
div[data-testid="stButton"] > button[kind="primary"] {
    background: linear-gradient(135deg, #1557b0, #0d47a1) !important;
    border: none !important;
    color: white !important;
    font-weight: 700 !important;
    box-shadow: 0 3px 10px rgba(13,71,161,.3) !important;
    transition: all .2s !important;
}
div[data-testid="stButton"] > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #0d47a1, #0a3880) !important;
    box-shadow: 0 5px 16px rgba(13,71,161,.4) !important;
    transform: translateY(-1px) !important;
}

/* Nút secondary (môn chưa chọn, Quay lại) */
div[data-testid="stButton"] > button[kind="secondary"] {
    background: white !important;
    border: 2px solid #1557b0 !important;
    color: #1557b0 !important;
    font-weight: 600 !important;
    transition: all .2s !important;
}
div[data-testid="stButton"] > button[kind="secondary"]:hover {
    background: linear-gradient(135deg, #1557b0, #0d47a1) !important;
    border-color: #0d47a1 !important;
    color: white !important;
    box-shadow: 0 4px 12px rgba(13,71,161,.3) !important;
    transform: translateY(-1px) !important;
}

/* Ô tóm tắt đề thi */
.exam-summary {
    background: linear-gradient(135deg, #eef3fd, #dbeafe);
    border: 1px solid #93c5fd;
    border-left: 4px solid #1557b0;
    border-radius: 10px;
    padding: .75rem 1rem;
    margin: .75rem 0;
    font-size: .85rem;
    color: #1e3a5f;
    font-weight: 500;
}
</style>
"""

# ── Ngưỡng cảnh báo (giây) ───────────────────────────────
_WARN_YELLOW = 300
_WARN_RED    = 120
_WARN_DANGER =  60


def _render_timer(remaining: int, total_dur: int) -> str:
    r    = 36
    circ = 2 * 3.14159265 * r

    return f"""
<div id="timer-root">
  <div class="timer-card t-green" id="tcrd">
    <div class="timer-outer">
      <div class="timer-svg-wrap">
        <svg width="90" height="90" viewBox="0 0 90 90">
          <circle id="ttrack" class="timer-track" cx="45" cy="45" r="{r}" stroke="#d1fae5"/>
          <circle id="tprog"  class="timer-progress" cx="45" cy="45" r="{r}"
                  stroke="#10b981"
                  stroke-dasharray="{circ:.2f}"
                  stroke-dashoffset="0"/>
        </svg>
        <div class="timer-center">
          <span class="timer-digits" id="tdigits" style="color:#065f46">00:00</span>
          <span class="timer-label"  id="tlabel"  style="color:#065f46">còn lại</span>
        </div>
      </div>
    </div>
  </div>
  <div id="ttoast" style="display:none;margin-top:.5rem;
       padding:.55rem .9rem; border-radius:10px; font-size:.8rem;
       font-weight:600; font-family:Inter,sans-serif;"></div>
</div>

<style>
  body {{ margin:0; padding:0; background:transparent; overflow:hidden; }}
  .timer-card {{
    border-radius:14px; padding:.5rem .6rem;
    text-align:center; border:2px solid;
    transition:all .4s ease; display:inline-block;
  }}
  .t-green  {{ background:#f0fdf9; border-color:#10b981; }}
  .t-yellow {{ background:#fffbeb; border-color:#f59e0b;
               box-shadow:0 0 12px rgba(245,158,11,.25); }}
  .t-red    {{ background:#fff5f5; border-color:#ef4444;
               box-shadow:0 0 18px rgba(239,68,68,.35);
               animation:cpulse .8s ease-in-out infinite; }}
  @keyframes cpulse {{
    0%,100%{{box-shadow:0 0 12px rgba(239,68,68,.25)}}
    50%    {{box-shadow:0 0 26px rgba(239,68,68,.55)}}
  }}
  .timer-outer {{ display:flex; align-items:center; justify-content:center; }}
  .timer-svg-wrap {{ position:relative; width:90px; height:90px; }}
  .timer-svg-wrap svg {{ transform:rotate(-90deg); }}
  .timer-track    {{ fill:none; stroke-width:5; }}
  .timer-progress {{ fill:none; stroke-width:5; stroke-linecap:round;
                     transition:stroke-dashoffset .95s linear, stroke .4s ease; }}
  .timer-center {{
    position:absolute; inset:0;
    display:flex; flex-direction:column;
    align-items:center; justify-content:center; line-height:1.1;
  }}
  .timer-digits {{
    font-size:1.25rem; font-weight:800;
    letter-spacing:-.5px; font-family:Inter,monospace;
    transition:color .4s;
  }}
  .t-red .timer-digits {{ animation:dshake .5s ease-in-out infinite; }}
  @keyframes dshake {{
    0%,100%{{transform:translateX(0)}}
    25%    {{transform:translateX(-2px)}}
    75%    {{transform:translateX(2px)}}
  }}
  .timer-label {{
    font-size:.55rem; font-weight:600; letter-spacing:.04em;
    text-transform:uppercase; opacity:.65; font-family:Inter,sans-serif;
  }}
  .auto-bar-wrap {{
    height:4px; border-radius:2px; background:#fee2e2;
    margin-top:.35rem; overflow:hidden;
  }}
  .auto-bar-fill {{
    height:100%; border-radius:2px;
    background:linear-gradient(90deg,#ef4444,#dc2626);
    transition:width .95s linear;
  }}
</style>

<script>
(function(){{
  var REM   = {remaining};
  var TOTAL = {total_dur};
  var CIRC  = {circ:.2f};
  var WARN_Y = {_WARN_YELLOW};
  var WARN_R = {_WARN_RED};
  var WARN_D = {_WARN_DANGER};

  var card   = document.getElementById('tcrd');
  var track  = document.getElementById('ttrack');
  var prog   = document.getElementById('tprog');
  var digits = document.getElementById('tdigits');
  var label  = document.getElementById('tlabel');
  var toast  = document.getElementById('ttoast');

  function findSubmitBtn() {{
    var btns = window.parent.document.querySelectorAll('button[kind="primary"]');
    for (var i = 0; i < btns.length; i++) {{
      if (btns[i].innerText.includes('Nộp bài') ||
          btns[i].innerText.includes('Nộp luôn')) {{
        return btns[i];
      }}
    }}
    return null;
  }}

  function update(rem) {{
    if (!card) return;
    var m = Math.floor(rem / 60);
    var s = rem % 60;
    var mm = (m < 10 ? '0' : '') + m;
    var ss = (s < 10 ? '0' : '') + s;
    digits.textContent = mm + ':' + ss;
    var pct    = TOTAL > 0 ? rem / TOTAL : 0;
    var offset = CIRC * (1 - pct);
    prog.setAttribute('stroke-dashoffset', offset.toFixed(1));
    if (rem <= WARN_R) {{
      card.className   = 'timer-card t-red';
      track.setAttribute('stroke','#fee2e2');
      prog.setAttribute('stroke','#ef4444');
      digits.style.color = '#991b1b';
      label.style.color  = '#991b1b';
    }} else if (rem <= WARN_Y) {{
      card.className   = 'timer-card t-yellow';
      track.setAttribute('stroke','#fef3c7');
      prog.setAttribute('stroke','#f59e0b');
      digits.style.color = '#92400e';
      label.style.color  = '#92400e';
    }} else {{
      card.className   = 'timer-card t-green';
      track.setAttribute('stroke','#d1fae5');
      prog.setAttribute('stroke','#10b981');
      digits.style.color = '#065f46';
      label.style.color  = '#065f46';
    }}
    if (rem <= 0) {{
      toast.style.display = 'flex';
      toast.className = 'timer-toast danger';
      toast.innerHTML = '🏁 <b>Hết giờ!</b> Đang tự động nộp bài...';
    }} else if (rem <= WARN_D) {{
      var barPct = Math.round(rem / WARN_D * 100);
      toast.style.display = 'block';
      toast.className = 'timer-toast danger';
      toast.innerHTML =
        '🚨 Còn <b>' + mm + ':' + ss + '</b> — Bài sẽ tự động nộp khi hết giờ!' +
        '<div class="auto-bar-wrap"><div class="auto-bar-fill" style="width:' +
        barPct + '%"></div></div>';
    }} else if (rem <= WARN_R) {{
      toast.style.display = 'flex';
      toast.className = 'timer-toast danger';
      toast.innerHTML = '⏰ Chỉ còn <b>' + mm + ':' + ss + '</b>! Hãy hoàn thành các câu còn lại.';
    }} else if (rem <= WARN_Y) {{
      toast.style.display = 'flex';
      toast.className = 'timer-toast warn';
      toast.innerHTML = '⚠️ Còn <b>' + m + ' phút</b> — Hãy tăng tốc!';
    }} else {{
      toast.style.display = 'none';
    }}
  }}

  var rem = REM;
  update(rem);
  var iv = setInterval(function() {{
    rem--;
    update(rem);
    if (rem <= 0) {{
      clearInterval(iv);
      setTimeout(function() {{
        var btn = findSubmitBtn();
        if (btn) {{ btn.click(); }}
        else     {{ window.parent.location.reload(); }}
      }}, 1500);
    }}
  }}, 1000);
}})();
</script>
"""


# ─────────────────────────────────────────────
# TRANG CHỦ
# ─────────────────────────────────────────────
def show_home():
    st.markdown(_PAGE_CSS, unsafe_allow_html=True)
    uname  = st.session_state.username or "bạn"
    stats  = get_user_stats(uname)
    exams  = get_user_exams(uname)
    remind = st.session_state.get("remind_assignments", [])

    total_exams = len(exams)
    best_pct    = max((s["best"] for s in stats.values()), default=0) if stats else 0
    avg_pct     = round(sum(s["avg"] for s in stats.values()) / len(stats)) if stats else 0

    st.markdown(f"""
    <div class="hero">
        <div class="hero-title">👋 Xin chào, {uname}!</div>
        <div class="hero-sub">Sẵn sàng ôn luyện hôm nay chưa? Hãy chinh phục bài thi tiếp theo!</div>
        <div class="hero-stats">
            <div class="hero-stat"><div class="hero-stat-val">{total_exams}</div><div class="hero-stat-lbl">Bài đã làm</div></div>
            <div class="hero-stat"><div class="hero-stat-val">{best_pct}%</div><div class="hero-stat-lbl">Điểm cao nhất</div></div>
            <div class="hero-stat"><div class="hero-stat-val">{avg_pct}%</div><div class="hero-stat-lbl">Trung bình</div></div>
            <div class="hero-stat"><div class="hero-stat-val">{NUM_QUESTIONS}</div><div class="hero-stat-lbl">Câu/đề</div></div>
        </div>
    </div>""", unsafe_allow_html=True)

    if remind:
        st.markdown('<div class="sec-title">📢 Đề cần làm từ giáo viên</div>', unsafe_allow_html=True)
        for a in remind:
            dl_str = f" · ⏰ {a['deadline']}" if a.get("deadline") else ""
            c1, c2 = st.columns([5, 1])
            with c1:
                st.markdown(
                    f'<div style="background:#fff9e6;border-left:4px solid #f4a300;'
                    f'padding:.65rem 1rem;border-radius:8px;font-size:.85rem">'
                    f'🟡 <b>{a["title"]}</b> · {a["subject"]} '
                    f'{a["grade"].split("(")[0].strip()}{dl_str}</div>',
                    unsafe_allow_html=True)
            with c2:
                if st.button("Làm ngay", key=f"remind_{a['id']}",
                             use_container_width=True, type="primary"):
                    st.session_state["current_assignment"] = a
                    st.session_state.page = "urgent_exam"; st.rerun()

    if stats:
        st.markdown("""
            <style>
            .sec-title {
                color: #000 !important;
                style="font-size:18px;"
            }
            </style>
            """, unsafe_allow_html=True)
        st.markdown('<div class="sec-title">📊 Kết quả của bạn</div>', unsafe_allow_html=True)
        st.markdown('<div class="stat-grid">', unsafe_allow_html=True)
        for subj, s in stats.items():
            color = "#1e8e3e" if s["avg"]>=80 else ("#f4a300" if s["avg"]>=60 else "#d93025")
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-card-val" style="color:{color}">{s['avg']}%</div>
                <div class="stat-card-lbl">📘 {subj}</div>
                <div class="stat-card-sub">{s['count']} bài · Cao nhất {s['best']}%</div>
            </div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="sec-title">📚 Môn học</div>', unsafe_allow_html=True)
    _SUBJ_ICONS = {"Toán":"🔢","Ngữ Văn":"📖","Tiếng Anh":"🇬🇧",
                   "Vật Lý":"⚡","Hóa Học":"⚗️","Sinh Học":"🧬"}
    cols = st.columns(3)
    for i, subj in enumerate(SUBJECT_OPTIONS):
        with cols[i % 3]:
            st.markdown(
                f'<div class="subj-card">'
                f'<div class="icon">{_SUBJ_ICONS.get(subj,"📚")}</div>'
                f'<div class="name">{subj}</div></div>',
                unsafe_allow_html=True)

    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🚀 Bắt đầu làm bài", use_container_width=True, type="primary"):
            st.session_state.page = "select"; st.rerun()
    with c2:
        if st.button("📋 Xem lịch sử", use_container_width=True):
            st.session_state.page = "history"; st.rerun()


# ─────────────────────────────────────────────
# TRANG CHỌN ĐỀ
# ─────────────────────────────────────────────
def show_select():
    st.markdown(_PAGE_CSS, unsafe_allow_html=True)
    st.markdown("## 📋 Chọn đề thi")

    _SUBJ_ICONS = {"Toán":"🔢","Ngữ Văn":"📖","Tiếng Anh":"🇬🇧",
                   "Vật Lý":"⚡","Hóa Học":"⚗️","Sinh Học":"🧬"}

    st.markdown('<div class="sec-title">📚 Chọn môn học</div>', unsafe_allow_html=True)
    if "sel_subject" not in st.session_state:
        st.session_state["sel_subject"] = SUBJECT_OPTIONS[0]

    subj_cols = st.columns(3)
    for i, subj in enumerate(SUBJECT_OPTIONS):
        with subj_cols[i % 3]:
            active = st.session_state["sel_subject"] == subj
            if st.button(f"{_SUBJ_ICONS.get(subj,'📚')} {subj}",
                         key=f"subj_{subj}", use_container_width=True,
                         type="primary" if active else "secondary"):
                st.session_state["sel_subject"] = subj; st.rerun()

    subject = st.session_state["sel_subject"]
    st.markdown("""
        <style>
        .sec-title {
            
            color: #000 !important;
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown('<div class="sec-title">🏫 Chọn lớp / cấp độ</div>', unsafe_allow_html=True)
    if "sel_grade" not in st.session_state:
        st.session_state["sel_grade"] = list(GRADE_CONFIG.keys())[0]

    avail_grades = [g for g, cfg in GRADE_CONFIG.items() if subject in cfg["subjects"]]
    if st.session_state["sel_grade"] not in avail_grades:
        st.session_state["sel_grade"] = avail_grades[0]

    grade_cols = st.columns(len(avail_grades))
    for i, g in enumerate(avail_grades):
        cfg    = GRADE_CONFIG[g]
        active = st.session_state["sel_grade"] == g
        with grade_cols[i]:
            st.markdown(
                f'<div class="grade-card {"active" if active else ""}">'
                f'<div class="grade-emoji">{cfg["emoji"]}</div>'
                f'<div class="grade-name">{g.split("(")[0].strip()}</div>'
                f'<div class="grade-desc">{cfg["time"]} phút</div></div>',
                unsafe_allow_html=True)
            if st.button("Chọn", key=f"grade_{g}", use_container_width=True,
                         type="primary" if active else "secondary"):
                st.session_state["sel_grade"] = g; st.rerun()

    grade = st.session_state["sel_grade"]
    cfg   = GRADE_CONFIG[grade]

    # ── Chọn số câu hỏi ──────────────────────────────────
    st.markdown('<div class="sec-title">🔢 Số câu hỏi</div>', unsafe_allow_html=True)

    _QUICK_OPTS = [16, 20, 25, 30]
    _MIN_Q = 16
    _MAX_Q = 100
    if "sel_num_q" not in st.session_state or st.session_state["sel_num_q"] < _MIN_Q:
        st.session_state["sel_num_q"] = max(_MIN_Q, _QUICK_OPTS[0])

    qcols = st.columns(len(_QUICK_OPTS))
    for i, n in enumerate(_QUICK_OPTS):
        with qcols[i]:
            active = st.session_state["sel_num_q"] == n
            if st.button(f"{n} câu", key=f"nq_{n}",
                         use_container_width=True,
                         type="primary" if active else "secondary"):
                st.session_state["sel_num_q"] = n
                st.rerun()

    safe_val = max(_MIN_Q, min(_MAX_Q, int(st.session_state["sel_num_q"])))

    custom = st.number_input(
        "Hoặc nhập số câu tuỳ ý:",
        min_value=_MIN_Q, max_value=_MAX_Q,
        value=safe_val,
        step=1, key="nq_custom",
        help=f"Tối thiểu {_MIN_Q} câu, tối đa {_MAX_Q} câu"
    )
    if int(custom) != st.session_state["sel_num_q"]:
        st.session_state["sel_num_q"] = int(custom)

    num_q = st.session_state["sel_num_q"]

    # Ô tóm tắt — dùng class mới
    st.markdown(f"""
    <div class="exam-summary">
        💡 <b>{subject}</b> · {grade} · <b>{num_q} câu</b> ·
        ⏱️ {cfg['time']} phút · {cfg['desc']}
    </div>""", unsafe_allow_html=True)

    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("← Quay lại", use_container_width=True):
            st.session_state.page = "home"; st.rerun()
    with c2:
        if st.button("✨ Tạo đề thi", use_container_width=True, type="primary"):
            num_q = st.session_state.get("sel_num_q", NUM_QUESTIONS)
            with st.spinner(f"🤖 Đang tạo đề {grade.split('(')[0].strip()} — {subject} ({num_q} câu)..."):
                questions, source = generate_exam(subject, grade, num_questions=num_q)

            vsummary = st.session_state.get("verify_summary")
            if vsummary:
                if "⚠️" in vsummary: st.warning(vsummary)
                else:                st.success(vsummary)

            now = time.time()
            st.session_state.update({
                "subject":        subject,
                "grade":          grade,
                "questions":      questions,
                "answers":        {},
                "submitted":      False,
                "score":          0,
                "start_time":     now,
                "exam_start_ts":  now,
                "exam_source":    source,
                "confirm_submit": False,
                "page":           "exam",
            })
            st.rerun()


# ─────────────────────────────────────────────
# TRANG LÀM BÀI
# ─────────────────────────────────────────────
def show_exam():
    st.markdown(_PAGE_CSS, unsafe_allow_html=True)
    qs  = st.session_state.questions
    cfg = GRADE_CONFIG.get(st.session_state.grade, {})
    dur = cfg.get("time", 20) * 60

    elapsed   = time.time() - st.session_state.start_time
    remaining = max(0, dur - int(elapsed))
    mins, secs = divmod(remaining, 60)

    answered   = sum(1 for v in st.session_state.answers.values() if v is not None)
    unanswered = [i for i in range(len(qs))
                  if st.session_state.answers.get(i) is None]
    pct_done   = int(answered / len(qs) * 100) if qs else 0

    if remaining == 0 and not st.session_state.submitted:
        st.markdown("""
        <div class="timer-toast danger" style="font-size:.9rem;padding:.8rem 1.2rem">
            🏁 <b>Hết giờ!</b> Hệ thống đang tự động nộp bài...
        </div>""", unsafe_allow_html=True)
        _submit(); return

    col_title, col_timer = st.columns([3, 1])
    with col_title:
        src       = st.session_state.exam_source
        badge     = '🤖 Groq AI' if src == "ai" else "📚 Local"
        badge_cls = "badge-ai" if src == "ai" else "badge-local"
        st.markdown(
            f'<div class="exam-header">'
            f'<div>'
            f'<div class="exam-title">{cfg.get("emoji","📝")} '
            f'{st.session_state.subject} — {st.session_state.grade.split("(")[0].strip()}</div>'
            f'<div class="exam-meta">'
            f'<span class="source-badge {badge_cls}">{badge}</span>'
            f' &nbsp;{st.session_state.get("verify_summary","")}</div>'
            f'</div></div>',
            unsafe_allow_html=True)
    with col_timer:
        components.html(_render_timer(remaining, dur), height=110, scrolling=False)

    st.markdown(f"""
    <div class="prog-wrap">
        <div class="prog-bar-bg">
            <div class="prog-bar-fill" style="width:{pct_done}%"></div>
        </div>
        <div class="prog-text">{answered}/{len(qs)} câu · {pct_done}%</div>
    </div>""", unsafe_allow_html=True)

    if st.session_state.get("confirm_submit") and unanswered:
        st.markdown(
            f'<div class="confirm-banner">⚠️ Còn <b>{len(unanswered)} câu chưa làm</b>: '
            + ", ".join(f"Câu {i+1}" for i in unanswered)
            + " — Cuộn xuống hoàn thành hoặc nộp luôn.</div>",
            unsafe_allow_html=True)

    for i, q in enumerate(qs):
        is_unanswered = (st.session_state.get("confirm_submit") and i in unanswered)
        is_answered   = st.session_state.answers.get(i) is not None
        card_cls = "unanswered" if is_unanswered else ("answered" if is_answered else "")
        num_cls  = "unanswered" if is_unanswered else ""
        flag     = " 🔴" if is_unanswered else ""

        st.markdown(
            f'<div class="q-card {card_cls}">'
            f'<div class="q-header">'
            f'<span class="q-num {num_cls}">Câu {i+1}</span>'
            f'<span class="q-text">{q["question"]}{flag}</span>'
            f'</div><div class="q-body">', unsafe_allow_html=True)

        cur    = st.session_state.answers.get(i)
        opts   = [None] + q["options"]
        idx    = opts.index(cur) if cur in opts else 0
        choice = st.radio(
            label=f"q_{i}", options=opts, index=idx, key=f"radio_{i}",
            format_func=lambda x: "— Chưa chọn —" if x is None else x,
            label_visibility="collapsed")
        if choice is not None:
            st.session_state.answers[i] = choice

        st.markdown('</div></div>', unsafe_allow_html=True)

    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("← Đổi đề", use_container_width=True):
            st.session_state["confirm_submit"] = False
            st.session_state.page = "select"; st.rerun()
    with c2:
        if answered < len(qs):
            if not st.session_state.get("confirm_submit"):
                if st.button("📤 Nộp bài", use_container_width=True, type="primary"):
                    st.session_state["confirm_submit"] = True; st.rerun()
            else:
                cc1, cc2 = st.columns(2)
                with cc1:
                    if st.button("❌ Làm tiếp", use_container_width=True):
                        st.session_state["confirm_submit"] = False; st.rerun()
                with cc2:
                    if st.button("✔️ Nộp luôn", use_container_width=True, type="primary"):
                        st.session_state["confirm_submit"] = False; _submit()
        else:
            if st.button("📤 Nộp bài", use_container_width=True, type="primary"):
                _submit()


def _submit():
    qs      = st.session_state.questions
    ans     = st.session_state.answers
    score   = grade_exam(qs, ans)
    elapsed = int(time.time() - (st.session_state.exam_start_ts or time.time()))
    save_exam_result(
        username=st.session_state.username, subject=st.session_state.subject,
        grade=st.session_state.grade, score=score, total=len(qs),
        questions=qs, answers=ans, elapsed_seconds=elapsed,
        source=st.session_state.exam_source,
    )
    assignment = st.session_state.get("current_assignment")
    if assignment:
        from assignment_manager import submit_assignment
        submit_assignment(assignment["id"], st.session_state.username, score, len(qs))
        st.session_state["current_assignment"] = None
        st.session_state["remind_assignments"] = []
    st.session_state.update({
        "score": score, "submitted": True,
        "confirm_submit": False, "page": "result",
    })
    st.rerun()


# ─────────────────────────────────────────────
# TRANG KẾT QUẢ
# ─────────────────────────────────────────────
def show_results():
    st.markdown(_PAGE_CSS, unsafe_allow_html=True)
    qs    = st.session_state.questions
    ans   = st.session_state.answers
    score = st.session_state.score
    total = len(qs)
    pct   = round(score / total * 100) if total else 0
    skipped = [i for i in range(total) if ans.get(i) is None]

    if pct == 100:  rank, emo, ring_cls = "Hoàn hảo! 🌟", "🥇", "score-gold"
    elif pct >= 80: rank, emo, ring_cls = "Xuất sắc",      "🥇", "score-gold"
    elif pct >= 60: rank, emo, ring_cls = "Đạt yêu cầu",  "🥈", "score-silver"
    else:           rank, emo, ring_cls = "Cần cố gắng",  "📚", "score-bronze"

    st.markdown(f"""
    <div class="result-hero">
        <div class="score-ring {ring_cls}">
            <div class="score-ring-val">{pct}%</div>
            <div class="score-ring-lbl">{score}/{total}</div>
        </div>
        <div class="result-rank">{emo} {rank}</div>
        <div class="result-sub">
            {st.session_state.subject} · {st.session_state.grade.split("(")[0].strip()}
            · 👤 {st.session_state.username}
        </div>
    </div>""", unsafe_allow_html=True)

    wrong_count   = sum(1 for i, q in enumerate(qs)
                        if ans.get(i) is not None and ans.get(i) != q["answer"])
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("✅ Đúng",    score)
    c2.metric("❌ Sai",     wrong_count)
    c3.metric("⬜ Bỏ qua", len(skipped))
    elapsed = int(time.time() - (st.session_state.exam_start_ts or time.time()))
    c4.metric("⏱️ Thời gian", f"{elapsed//60}p{elapsed%60:02d}s")

    if skipped:
        st.warning(f"⚠️ Bỏ qua {len(skipped)} câu: "
                   + ", ".join(f"Câu {i+1}" for i in skipped))

    st.markdown("---")
    st.markdown("### 📋 Chi tiết từng câu")

    for i, q in enumerate(qs):
        u, c = ans.get(i), q["answer"]
        skp  = u is None
        ok   = (not skp and u == c)
        if ok:    card_cls, icon = "correct", "✅"
        elif skp: card_cls, icon = "skipped", "⬜"
        else:     card_cls, icon = "wrong",   "❌"

        with st.expander(
            f"{icon} Câu {i+1}: {q['question'][:65]}{'...' if len(q['question'])>65 else ''}",
            expanded=not ok):
            st.markdown(f'<div class="res-card {card_cls}">', unsafe_allow_html=True)
            st.markdown(f'<div class="res-q">{q["question"]}</div>', unsafe_allow_html=True)
            if skp:
                st.markdown('<div class="res-ans" style="color:#000">— Chưa trả lời</div>',
                            unsafe_allow_html=True)
            else:
                color = "#1e8e3e" if ok else "#d93025"
                st.markdown(
                    f'<div class="res-ans" style="color:{color};font-weight:600">'
                    f'Bạn chọn: {u}</div>', unsafe_allow_html=True)

            if not ok:
                st.markdown(
                    f'<div style="color:#1e8e3e;font-weight:600">'
                    f'✅ Đáp án đúng: {c}</div>',
                    unsafe_allow_html=True)

            exp_raw = q.get("explanation", "")

            if isinstance(exp_raw, dict):
                exp = "<br>".join(str(v) for v in exp_raw.values())
            else:
                exp = str(exp_raw)
            st.markdown(
                f'''<div style="margin-top:.4rem;font-size:.78rem;background:#f0fdf4;
                    padding:.4rem .6rem;border-radius:6px;color:#000;">
                    💡 {exp}</div>''',
                unsafe_allow_html=True)

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🔄 Làm lại", use_container_width=True):
            st.session_state.update({
                "answers": {}, "submitted": False, "confirm_submit": False,
                "start_time": time.time(), "exam_start_ts": time.time(), "page": "exam"})
            st.rerun()
    with c2:
        if st.button("📋 Lịch sử", use_container_width=True):
            st.session_state.page = "history"; st.rerun()
    with c3:
        if st.button("🏠 Trang chủ", use_container_width=True, type="primary"):
            st.session_state.update({
                "page": "home", "subject": None, "grade": None,
                "questions": [], "answers": {}, "submitted": False,
                "score": 0, "start_time": None, "exam_source": None,
                "confirm_submit": False})
            st.rerun()


# ─────────────────────────────────────────────
# TRANG LỊCH SỬ
# ─────────────────────────────────────────────
def show_history():
    st.markdown(_PAGE_CSS, unsafe_allow_html=True)
    uname = st.session_state.username
    st.markdown("## 📋 Lịch sử bài thi")

    exams = get_user_exams(uname)
    if not exams:
        st.info("Bạn chưa có bài thi nào.")
        if st.button("🚀 Làm bài đầu tiên", type="primary"):
            st.session_state.page = "select"; st.rerun()
        return

    stats = get_user_stats(uname)

    st.markdown('<div class="sec-title">📊 Tổng hợp</div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-grid">', unsafe_allow_html=True)
    for subj, s in stats.items():
        color = "#1e8e3e" if s["avg"]>=80 else ("#f4a300" if s["avg"]>=60 else "#d93025")
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-card-val" style="color:{color}">{s['avg']}%</div>
            <div class="stat-card-lbl">📘 {subj}</div>
            <div class="stat-card-sub">{s['count']} bài · Cao {s['best']}%</div>
        </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    subjects   = ["Tất cả"] + list({e["subject"] for e in exams})
    filter_sub = st.selectbox("🔍 Lọc theo môn", subjects, label_visibility="collapsed")
    shown      = list(reversed(
        exams if filter_sub == "Tất cả"
        else [e for e in exams if e["subject"] == filter_sub]
    ))

    st.markdown(f'<div class="sec-title">{len(shown)} bài thi</div>', unsafe_allow_html=True)

    for e in shown:
        pct  = e["pct"]
        mins = e["time_sec"] // 60
        secs = e["time_sec"] %  60
        if pct >= 80: badge_cls, medal = "gold",   "🥇"
        elif pct>=60: badge_cls, medal = "silver", "🥈"
        else:         badge_cls, medal = "bronze", "📚"

        wrong   = [d for d in e["detail"] if not d["is_right"] and d["user_ans"] != "—"]
        skipped = [d for d in e["detail"] if d["user_ans"] == "—"]

        with st.expander(
            f"{medal} {e['date']} · {e['subject']} "
            f"{e['grade'].split('(')[0].strip()} · {e['score']}/{e['total']} ({pct}%)"):
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("📊 Điểm",  f"{e['score']}/{e['total']}")
            c2.metric("📈 TB",    f"{pct}%")
            c3.metric("⏱️ TG",   f"{mins}p{secs:02d}s")
            c4.metric("🤖 Nguồn","AI" if e.get("source")=="ai" else "Local")

            if skipped:
                st.warning(f"⬜ Bỏ qua {len(skipped)} câu: "
                           + ", ".join(f"Câu {d['no']}" for d in skipped))
            if wrong:
                st.markdown(f"**❌ {len(wrong)} câu sai:**")
                for d in wrong:
                    st.markdown(
                        f"- Câu {d['no']}: _{d['question'][:55]}..._ "
                        f"→ **{d['user_ans']}** | ✅ **{d['correct']}**")
            if not wrong and not skipped:
                st.success("🎉 Hoàn hảo! Đúng tất cả câu.")

    st.markdown("---")
    if st.button("← Về trang chủ", use_container_width=True):
        st.session_state.page = "home"; st.rerun()
