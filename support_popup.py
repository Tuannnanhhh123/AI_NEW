# ============================================================
# support_popup.py — Popup tư vấn hỗ trợ (FAB góc dưới phải)
# Gọi render_support_popup() ở cuối bất kỳ trang nào
# ============================================================
import streamlit as st
import streamlit.components.v1 as components

# ── Cấu hình liên hệ — chỉnh tại đây ─────────────────────
CONTACT_INFO = {
    "email":    "support@aiexamgen.vn",
    "phone":    "1800 1234",
    "zalo":     "0901 234 567",
    "facebook": "https://facebook.com/aiexamgen",
    "hours":    "T2–T6: 8:00–17:00",
}

# ── FAQ ───────────────────────────────────────────────────
FAQ_LIST = [
    {
        "q": "Làm sao để tạo đề thi?",
        "a": "Vào <b>Bắt đầu làm bài</b> → chọn môn học → chọn lớp → nhấn <b>Tạo đề thi</b>."
    },
    {
        "q": "Tôi có thể chọn số câu hỏi không?",
        "a": "Có! Trong trang Chọn đề, bạn có thể chọn nhanh 16/20/25/30 câu hoặc nhập tuỳ ý từ 16–100 câu."
    },
    {
        "q": "Đề thi có bị lặp câu không?",
        "a": "Hệ thống tự động lọc câu đã dùng. Khi hết câu mới, pool sẽ được reset để tái sử dụng."
    },
    {
        "q": "Bài thi tự nộp khi nào?",
        "a": "Bài sẽ tự động nộp khi hết thời gian. Bạn cũng có thể nộp sớm bất cứ lúc nào."
    },
    {
        "q": "Giáo viên giao bài như thế nào?",
        "a": "Giáo viên đăng nhập vào Dashboard → tạo bài tập và giao cho học sinh theo tên."
    },
    {
        "q": "Tôi quên mật khẩu thì làm sao?",
        "a": "Ở màn hình đăng nhập, chọn tab <b>Quên mật khẩu</b> → nhập email → nhận link đặt lại."
    },
]

# ── AI FAQ quick-answer (không cần API) ───────────────────
_AI_KB = {
    "tạo đề":       "Vào <b>Bắt đầu làm bài</b> → chọn môn & lớp → nhấn <b>Tạo đề thi</b>.",
    "số câu":       "Chọn nhanh 16/20/25/30 câu hoặc nhập tuỳ ý (16–100) trong trang Chọn đề.",
    "mật khẩu":     "Tab <b>Quên mật khẩu</b> ở màn đăng nhập → nhập email → nhận link.",
    "lịch sử":      "Vào menu <b>Lịch sử</b> để xem tất cả bài thi đã làm.",
    "điểm":         "Điểm hiển thị ngay sau khi nộp bài và được lưu vào Lịch sử.",
    "giáo viên":    "Giáo viên đăng nhập bằng <b>Mã giáo viên</b> riêng ở màn hình đăng nhập.",
    "chatbot":      "Vào menu <b>Hỏi AI</b> để chat với trợ lý AI về bài học.",
    "hết giờ":      "Bài tự động nộp khi hết giờ. Có cảnh báo trước 5 phút, 2 phút và 1 phút.",
    "đăng ký":      "Tab <b>Đăng ký</b> ở màn đăng nhập → nhập thông tin → chọn lớp & môn yêu thích.",
    "xin chào":     "Xin chào! 👋 Tôi có thể giúp gì cho bạn?",
    "hi":           "Xin chào! 👋 Bạn cần hỗ trợ gì?",
    "hello":        "Hello! 👋 How can I help you?",
}

def _ai_reply(msg: str) -> str:
    msg_l = msg.lower()
    for kw, ans in _AI_KB.items():
        if kw in msg_l:
            return ans
    return ("Tôi chưa có câu trả lời chính xác cho câu hỏi này. "
            "Vui lòng gửi form bên tab <b>Gửi yêu cầu</b> hoặc liên hệ "
            f"email <b>{CONTACT_INFO['email']}</b> để được hỗ trợ nhanh nhất! 😊")


def render_support_popup():
    """
    Gọi hàm này ở CUỐI hàm show_* của bất kỳ trang nào.
    Popup hoàn toàn chạy bằng HTML/CSS/JS — không rerun Python.
    """

    # ── Chuẩn bị dữ liệu FAQ cho JS ──────────────────────
    faq_js = "[" + ",".join(
        f'{{q:{repr(f["q"])},a:{repr(f["a"])}}}'
        for f in FAQ_LIST
    ) + "]"

    # ── Chuẩn bị KB cho AI ────────────────────────────────
    kb_js = "{" + ",".join(
        f'{repr(k)}:{repr(v)}'
        for k, v in _AI_KB.items()
    ) + "}"

    html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
* {{ box-sizing:border-box; margin:0; padding:0; font-family:'Inter',sans-serif; }}

/* ── FAB button ── */
#fab {{
  position:fixed; bottom:1.6rem; right:1.6rem;
  width:56px; height:56px; border-radius:50%;
  background:linear-gradient(135deg,#4338ca,#3b82f6);
  border:none; cursor:pointer; z-index:9999;
  display:flex; align-items:center; justify-content:center;
  box-shadow:0 4px 20px rgba(67,56,202,.45);
  transition:transform .2s, box-shadow .2s;
  animation:fab-in .4s cubic-bezier(.36,.07,.19,.97) both;
}}
#fab:hover {{
  transform:scale(1.1);
  box-shadow:0 6px 28px rgba(67,56,202,.55);
}}
@keyframes fab-in {{
  0%  {{transform:scale(0) rotate(-30deg);opacity:0}}
  100%{{transform:scale(1) rotate(0);opacity:1}}
}}
#fab svg {{ transition:transform .3s; }}
#fab.open svg {{ transform:rotate(45deg); }}

/* Tooltip */
#fab-tip {{
  position:fixed; bottom:1.9rem; right:4.8rem;
  background:#1e1b4b; color:#fff;
  padding:.3rem .75rem; border-radius:8px;
  font-size:.75rem; font-weight:600; white-space:nowrap;
  pointer-events:none; opacity:0;
  transition:opacity .2s;
  z-index:9998;
}}
#fab-tip::after {{
  content:''; position:absolute;
  top:50%; right:-6px; transform:translateY(-50%);
  border:6px solid transparent;
  border-left-color:#1e1b4b;
}}
#fab:hover + #fab-tip {{ opacity:1; }}

/* ── Popup panel ── */
#popup {{
  position:fixed; bottom:5.2rem; right:1.6rem;
  width:360px; max-height:560px;
  background:#fff; border-radius:20px;
  box-shadow:0 8px 40px rgba(0,0,0,.18),
             0 0 0 1px rgba(67,56,202,.08);
  z-index:9998; display:none; flex-direction:column;
  overflow:hidden;
  animation:pop-in .3s cubic-bezier(.4,0,.2,1);
}}
#popup.show {{ display:flex; }}
@keyframes pop-in {{
  0%  {{transform:scale(.85) translateY(20px);opacity:0}}
  100%{{transform:scale(1) translateY(0);opacity:1}}
}}

/* Header */
.pp-header {{
  background:linear-gradient(135deg,#4338ca,#3b82f6);
  padding:1rem 1.1rem .8rem;
  display:flex; align-items:center; gap:.7rem;
  flex-shrink:0;
}}
.pp-avatar {{
  width:38px; height:38px; border-radius:50%;
  background:rgba(255,255,255,.2);
  display:flex; align-items:center; justify-content:center;
  font-size:1.3rem; flex-shrink:0;
}}
.pp-hinfo {{ flex:1; }}
.pp-hname  {{ color:#fff; font-weight:700; font-size:.9rem; }}
.pp-hstatus{{ color:rgba(255,255,255,.75); font-size:.72rem; display:flex; align-items:center; gap:.3rem; }}
.online-dot {{ width:6px; height:6px; border-radius:50%; background:#4ade80;
               box-shadow:0 0 6px #4ade80; animation:blink 1.5s infinite; }}
@keyframes blink{{0%,100%{{opacity:1}}50%{{opacity:.3}}}}
.pp-close {{
  background:rgba(255,255,255,.15); border:none; cursor:pointer;
  width:28px; height:28px; border-radius:50%;
  display:flex; align-items:center; justify-content:center;
  color:#fff; font-size:1rem; transition:background .2s;
}}
.pp-close:hover {{ background:rgba(255,255,255,.3); }}

/* Tabs */
.pp-tabs {{
  display:flex; background:#f8f9ff;
  border-bottom:1px solid #e8eaf6; flex-shrink:0;
}}
.pp-tab {{
  flex:1; border:none; background:transparent;
  padding:.6rem .3rem; font-size:.72rem; font-weight:600;
  color:#6b7280; cursor:pointer; border-bottom:2px solid transparent;
  transition:all .2s; display:flex; flex-direction:column;
  align-items:center; gap:.15rem;
}}
.pp-tab .ti {{ font-size:1rem; }}
.pp-tab.active {{ color:#4338ca; border-bottom-color:#4338ca; background:#fff; }}
.pp-tab:hover:not(.active) {{ color:#4338ca; background:#f0f4ff; }}

/* Panels */
.pp-body {{ flex:1; overflow-y:auto; min-height:0; }}
.pp-panel {{ display:none; padding:1rem; }}
.pp-panel.active {{ display:block; }}

/* ── Chat panel ── */
.chat-msgs {{
  height:200px; overflow-y:auto; margin-bottom:.75rem;
  display:flex; flex-direction:column; gap:.5rem;
  padding:.2rem 0;
}}
.msg {{ max-width:82%; padding:.5rem .75rem; border-radius:12px; font-size:.82rem; line-height:1.45; }}
.msg.bot {{ background:#f0f4ff; color:#1e1b4b; border-radius:12px 12px 12px 4px; align-self:flex-start; }}
.msg.user{{ background:linear-gradient(135deg,#4338ca,#3b82f6); color:#fff;
            border-radius:12px 12px 4px 12px; align-self:flex-end; }}
.chat-input-row {{ display:flex; gap:.5rem; }}
.chat-inp {{
  flex:1; border:1.5px solid #e5e7eb; border-radius:10px;
  padding:.5rem .75rem; font-size:.83rem; outline:none;
  transition:border-color .2s;
}}
.chat-inp:focus {{ border-color:#4338ca; }}
.chat-send {{
  background:linear-gradient(135deg,#4338ca,#3b82f6);
  border:none; border-radius:10px; cursor:pointer;
  width:36px; height:36px; display:flex;
  align-items:center; justify-content:center;
  color:#fff; font-size:1rem; transition:transform .15s;
  flex-shrink:0;
}}
.chat-send:hover {{ transform:scale(1.08); }}

/* ── Form panel ── */
.form-group {{ margin-bottom:.7rem; }}
.form-lbl {{ font-size:.75rem; font-weight:600; color:#374151; margin-bottom:.3rem; display:block; }}
.form-inp, .form-sel, .form-ta {{
  width:100%; border:1.5px solid #e5e7eb; border-radius:9px;
  padding:.5rem .75rem; font-size:.83rem; outline:none;
  font-family:'Inter',sans-serif;
  transition:border-color .2s, box-shadow .2s;
  color:#111827;
}}
.form-inp:focus, .form-sel:focus, .form-ta:focus {{
  border-color:#4338ca;
  box-shadow:0 0 0 3px rgba(67,56,202,.1);
}}
.form-ta {{ resize:vertical; min-height:80px; }}
.form-btn {{
  width:100%; background:linear-gradient(135deg,#4338ca,#3b82f6);
  color:#fff; border:none; border-radius:10px; padding:.65rem;
  font-size:.88rem; font-weight:700; cursor:pointer;
  transition:transform .15s, box-shadow .15s;
}}
.form-btn:hover {{ transform:translateY(-1px); box-shadow:0 4px 14px rgba(67,56,202,.4); }}
.form-success {{
  background:#f0fdf4; border:1px solid #bbf7d0;
  border-radius:10px; padding:.75rem; text-align:center;
  color:#166534; font-size:.85rem; font-weight:600;
  display:none;
}}

/* ── Contact panel ── */
.contact-item {{
  display:flex; align-items:center; gap:.75rem;
  padding:.6rem .5rem; border-radius:10px;
  transition:background .2s; cursor:default;
}}
.contact-item:hover {{ background:#f0f4ff; }}
.ct-icon {{
  width:36px; height:36px; border-radius:10px;
  display:flex; align-items:center; justify-content:center;
  font-size:1.1rem; flex-shrink:0;
}}
.ct-label {{ font-size:.72rem; color:#9ca3af; font-weight:500; }}
.ct-val   {{ font-size:.85rem; color:#1e1b4b; font-weight:600; }}
.hours-box {{
  background:linear-gradient(135deg,#f0f4ff,#faf5ff);
  border:1px solid #e0e7ff; border-radius:12px;
  padding:.65rem .9rem; margin-top:.5rem;
  display:flex; align-items:center; gap:.6rem;
  font-size:.8rem; color:#4338ca; font-weight:600;
}}

/* ── FAQ panel ── */
.faq-item {{
  border:1px solid #e5e7eb; border-radius:11px;
  margin-bottom:.5rem; overflow:hidden;
  transition:border-color .2s;
}}
.faq-item:hover {{ border-color:#c7d2fe; }}
.faq-q {{
  padding:.65rem .85rem; font-size:.82rem; font-weight:600;
  color:#1e1b4b; cursor:pointer;
  display:flex; align-items:center; justify-content:space-between;
  gap:.5rem; background:#fafbff;
  transition:background .2s;
}}
.faq-q:hover {{ background:#f0f4ff; }}
.faq-arr {{ font-size:.7rem; color:#6b7280; transition:transform .25s; flex-shrink:0; }}
.faq-a {{
  display:none; padding:.6rem .85rem .75rem;
  font-size:.8rem; color:#555; line-height:1.55;
  border-top:1px solid #f0f0f0; background:#fff;
}}

/* Scrollbar */
.pp-body::-webkit-scrollbar,
.chat-msgs::-webkit-scrollbar {{ width:4px; }}
.pp-body::-webkit-scrollbar-track,
.chat-msgs::-webkit-scrollbar-track {{ background:transparent; }}
.pp-body::-webkit-scrollbar-thumb,
.chat-msgs::-webkit-scrollbar-thumb {{ background:#c7d2fe; border-radius:2px; }}

body {{ background:transparent; overflow:hidden; }}
</style>
</head>
<body>

<!-- FAB -->
<button id="fab" onclick="togglePopup()" aria-label="Hỗ trợ">
  <svg id="fab-icon" width="24" height="24" fill="none" stroke="white"
       stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
  </svg>
</button>
<div id="fab-tip">Hỗ trợ &amp; Tư vấn</div>

<!-- Popup -->
<div id="popup">
  <!-- Header -->
  <div class="pp-header">
    <div class="pp-avatar">🎓</div>
    <div class="pp-hinfo">
      <div class="pp-hname">Hỗ trợ AI Exam Generator</div>
      <div class="pp-hstatus">
        <span class="online-dot"></span> Đang trực tuyến
      </div>
    </div>
    <button class="pp-close" onclick="togglePopup()">✕</button>
  </div>

  <!-- Tabs -->
  <div class="pp-tabs">
    <button class="pp-tab active" onclick="switchTab('chat')" id="tab-chat">
      <span class="ti">💬</span>Chat AI
    </button>
    <button class="pp-tab" onclick="switchTab('form')" id="tab-form">
      <span class="ti">📝</span>Gửi yêu cầu
    </button>
    <button class="pp-tab" onclick="switchTab('contact')" id="tab-contact">
      <span class="ti">📞</span>Liên hệ
    </button>
    <button class="pp-tab" onclick="switchTab('faq')" id="tab-faq">
      <span class="ti">❓</span>FAQ
    </button>
  </div>

  <!-- Body -->
  <div class="pp-body">

    <!-- ── Tab Chat ── -->
    <div class="pp-panel active" id="panel-chat">
      <div class="chat-msgs" id="chat-msgs"></div>
      <div class="chat-input-row">
        <input class="chat-inp" id="chat-inp" placeholder="Nhập câu hỏi..."
               onkeydown="if(event.key==='Enter')sendMsg()">
        <button class="chat-send" onclick="sendMsg()">➤</button>
      </div>
    </div>

    <!-- ── Tab Form ── -->
    <div class="pp-panel" id="panel-form">
      <div class="form-group">
        <label class="form-lbl">👤 Họ và tên</label>
        <input class="form-inp" id="f-name" placeholder="Nguyễn Văn A">
      </div>
      <div class="form-group">
        <label class="form-lbl">📧 Email</label>
        <input class="form-inp" id="f-email" placeholder="email@example.com" type="email">
      </div>
      <div class="form-group">
        <label class="form-lbl">📋 Loại yêu cầu</label>
        <select class="form-sel" id="f-type">
          <option value="">-- Chọn loại --</option>
          <option>🐛 Báo lỗi kỹ thuật</option>
          <option>💡 Góp ý tính năng</option>
          <option>❓ Câu hỏi về sản phẩm</option>
          <option>👨‍🏫 Hỗ trợ giáo viên</option>
          <option>🎓 Hỗ trợ học sinh</option>
          <option>💳 Vấn đề tài khoản</option>
        </select>
      </div>
      <div class="form-group">
        <label class="form-lbl">✍️ Nội dung</label>
        <textarea class="form-ta" id="f-msg" placeholder="Mô tả chi tiết vấn đề bạn gặp phải..."></textarea>
      </div>
      <button class="form-btn" onclick="submitForm()">📤 Gửi yêu cầu</button>
      <div class="form-success" id="form-ok">
        ✅ Đã gửi thành công! Chúng tôi sẽ phản hồi trong vòng 24 giờ.
      </div>
    </div>

    <!-- ── Tab Contact ── -->
    <div class="pp-panel" id="panel-contact">
      <div class="contact-item">
        <div class="ct-icon" style="background:#e8f0fe">📧</div>
        <div><div class="ct-label">Email hỗ trợ</div>
             <div class="ct-val">{CONTACT_INFO["email"]}</div></div>
      </div>
      <div class="contact-item">
        <div class="ct-icon" style="background:#e8f5e9">📞</div>
        <div><div class="ct-label">Hotline (miễn phí)</div>
             <div class="ct-val">{CONTACT_INFO["phone"]}</div></div>
      </div>
      <div class="contact-item">
        <div class="ct-icon" style="background:#e3f2fd">💬</div>
        <div><div class="ct-label">Zalo</div>
             <div class="ct-val">{CONTACT_INFO["zalo"]}</div></div>
      </div>
      <div class="contact-item">
        <div class="ct-icon" style="background:#e8eaf6">👥</div>
        <div><div class="ct-label">Facebook</div>
             <div class="ct-val">AI Exam Generator</div></div>
      </div>
      <div class="hours-box">
        🕐 Giờ làm việc: {CONTACT_INFO["hours"]}
      </div>
    </div>

    <!-- ── Tab FAQ ── -->
    <div class="pp-panel" id="panel-faq">
      <div id="faq-list"></div>
    </div>

  </div><!-- /pp-body -->
</div><!-- /popup -->

<script>
var KB   = {kb_js};
var FAQS = {faq_js};
var chatOpen = false;

/* ── Khởi tạo chat với lời chào ── */
window.addEventListener('load', function() {{
  addMsg('bot', 'Xin chào! 👋 Tôi là trợ lý hỗ trợ của <b>AI Exam Generator</b>.<br>Tôi có thể giúp gì cho bạn hôm nay?');
  buildFAQ();
}});

/* ── Toggle popup ── */
function togglePopup() {{
  var p = document.getElementById('popup');
  var f = document.getElementById('fab');
  chatOpen = !chatOpen;
  if (chatOpen) {{
    p.classList.add('show');
    f.classList.add('open');
    document.getElementById('chat-inp').focus();
  }} else {{
    p.classList.remove('show');
    f.classList.remove('open');
  }}
}}

/* ── Switch tab ── */
function switchTab(name) {{
  ['chat','form','contact','faq'].forEach(function(t) {{
    document.getElementById('tab-'+t).classList.remove('active');
    document.getElementById('panel-'+t).classList.remove('active');
  }});
  document.getElementById('tab-'+name).classList.add('active');
  document.getElementById('panel-'+name).classList.add('active');
}}

/* ── Chat ── */
function addMsg(role, html) {{
  var box = document.getElementById('chat-msgs');
  var d   = document.createElement('div');
  d.className = 'msg ' + role;
  d.innerHTML = html;
  box.appendChild(d);
  box.scrollTop = box.scrollHeight;
}}

function aiReply(msg) {{
  var ml = msg.toLowerCase();
  for (var kw in KB) {{
    if (ml.indexOf(kw) !== -1) return KB[kw];
  }}
  return 'Tôi chưa có câu trả lời chính xác cho câu hỏi này. Vui lòng gửi form bên tab <b>Gửi yêu cầu</b> hoặc liên hệ email <b>{CONTACT_INFO["email"]}</b> để được hỗ trợ! 😊';
}}

function sendMsg() {{
  var inp = document.getElementById('chat-inp');
  var txt = inp.value.trim();
  if (!txt) return;
  addMsg('user', txt);
  inp.value = '';
  var reply = aiReply(txt);
  setTimeout(function() {{ addMsg('bot', reply); }}, 420);
}}

/* ── Form submit ── */
function submitForm() {{
  var name  = document.getElementById('f-name').value.trim();
  var email = document.getElementById('f-email').value.trim();
  var type  = document.getElementById('f-type').value;
  var msg   = document.getElementById('f-msg').value.trim();
  if (!name || !email || !type || !msg) {{
    alert('Vui lòng điền đầy đủ thông tin!'); return;
  }}
  /* Giả lập gửi thành công — thay bằng API thật nếu cần */
  document.getElementById('form-ok').style.display = 'block';
  document.getElementById('f-name').value  = '';
  document.getElementById('f-email').value = '';
  document.getElementById('f-type').value  = '';
  document.getElementById('f-msg').value   = '';
  setTimeout(function() {{
    document.getElementById('form-ok').style.display = 'none';
  }}, 4000);
}}

/* ── Build FAQ ── */
function buildFAQ() {{
  var container = document.getElementById('faq-list');
  FAQS.forEach(function(item, i) {{
    var div = document.createElement('div');
    div.className = 'faq-item';
    div.innerHTML =
      '<div class="faq-q" onclick="toggleFAQ(' + i + ')" id="fq-' + i + '">' +
        item.q +
        '<span class="faq-arr" id="fa-' + i + '">▼</span>' +
      '</div>' +
      '<div class="faq-a" id="fa-ans-' + i + '">' + item.a + '</div>';
    container.appendChild(div);
  }});
}}

function toggleFAQ(i) {{
  var ans = document.getElementById('fa-ans-' + i);
  var arr = document.getElementById('fa-' + i);
  var open = ans.style.display === 'block';
  ans.style.display = open ? 'none' : 'block';
  arr.style.transform = open ? 'rotate(0)' : 'rotate(180deg)';
}}
</script>
</body>
</html>
"""
    components.html(html, height=660, scrolling=False)