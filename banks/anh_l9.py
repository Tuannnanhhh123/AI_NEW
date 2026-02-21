# ============================================================
# banks/toan_l9.py — Ngân hàng Toán Lớp 9
# Thêm câu hỏi vào list QUESTIONS bên dưới
# Cấu trúc mỗi câu:
# {
#   "question": "Nội dung câu hỏi?",
#   "options": ["A", "B", "C", "D"],   ← đúng 4 lựa chọn
#   "answer": "B",                      ← phải khớp 1 trong 4 options
#   "explanation": "Giải thích..."
# }
# ============================================================

QUESTIONS = [
    
   {
            "question": "I _____ English for five years.",
            "options": ["learn", "am learning", "have learned", "learned"],
            "answer": "have learned",
            "explanation": "Dùng Present Perfect với 'for + khoảng thời gian' để diễn tả hành động bắt đầu trong quá khứ và kéo dài đến hiện tại."
        },
        {
            "question": "She _____ to the market when I met her yesterday.",
            "options": ["goes", "was going", "went", "has gone"],
            "answer": "was going",
            "explanation": "Dùng Past Continuous để diễn tả hành động đang xảy ra tại một thời điểm cụ thể trong quá khứ."
        },
        {
            "question": "By the time you arrive, we _____ dinner.",
            "options": ["finish", "will finish", "will have finished", "finished"],
            "answer": "will have finished",
            "explanation": "Dùng Future Perfect với 'by the time' để diễn tả hành động sẽ hoàn thành trước một thời điểm trong tương lai."
        },
        {
            "question": "He _____ his homework before he went out to play.",
            "options": ["finishes", "finished", "has finished", "had finished"],
            "answer": "had finished",
            "explanation": "Dùng Past Perfect để diễn tả hành động xảy ra trước một hành động khác trong quá khứ."
        },
        {
            "question": "They _____ in this city since 2010.",
            "options": ["live", "lived", "have lived", "are living"],
            "answer": "have lived",
            "explanation": "Dùng Present Perfect với 'since + mốc thời gian' để diễn tả hành động bắt đầu từ quá khứ và tiếp tục đến hiện tại."
        },
        {
            "question": "What _____ you _____ at 8 PM last night?",
            "options": ["do/do", "did/do", "were/doing", "have/done"],
            "answer": "were/doing",
            "explanation": "Dùng Past Continuous để hỏi về hành động đang xảy ra tại thời điểm cụ thể trong quá khứ."
        },
        {
            "question": "I _____ him since we graduated from high school.",
            "options": ["don't see", "didn't see", "haven't seen", "won't see"],
            "answer": "haven't seen",
            "explanation": "Dùng Present Perfect với 'since' để diễn tả hành động chưa xảy ra từ quá khứ đến hiện tại."
        },
        {
            "question": "While she _____ TV, the phone rang.",
            "options": ["watches", "was watching", "watched", "has watched"],
            "answer": "was watching",
            "explanation": "Dùng Past Continuous trong mệnh đề 'while' để diễn tả hành động đang xảy ra thì có hành động khác xen vào."
        },
        {
            "question": "Tomorrow at 3 PM, I _____ a meeting with my teacher.",
            "options": ["have", "will have", "will be having", "am having"],
            "answer": "will be having",
            "explanation": "Dùng Future Continuous để diễn tả hành động sẽ đang xảy ra tại một thời điểm cụ thể trong tương lai."
        },
        {
            "question": "She _____ three books this month.",
            "options": ["reads", "read", "has read", "had read"],
            "answer": "has read",
            "explanation": "Dùng Present Perfect với 'this month' để diễn tả hành động xảy ra trong khoảng thời gian còn liên quan đến hiện tại."
        },
        {
            "question": "Before I went to bed, I _____ all the lights.",
            "options": ["turn off", "turned off", "have turned off", "had turned off"],
            "answer": "had turned off",
            "explanation": "Dùng Past Perfect để diễn tả hành động xảy ra trước một hành động khác trong quá khứ."
        },
        {
            "question": "My mother _____ in the kitchen when I got home.",
            "options": ["cooks", "cooked", "was cooking", "has cooked"],
            "answer": "was cooking",
            "explanation": "Dùng Past Continuous để diễn tả hành động đang xảy ra khi có hành động khác xen vào."
        },
        {
            "question": "I _____ my keys. I can't find them anywhere.",
            "options": ["lose", "lost", "have lost", "had lost"],
            "answer": "have lost",
            "explanation": "Dùng Present Perfect để diễn tả hành động xảy ra trong quá khứ nhưng kết quả còn ảnh hưởng đến hiện tại."
        },
        {
            "question": "They _____ married for 20 years by next month.",
            "options": ["are", "will be", "will have been", "have been"],
            "answer": "will have been",
            "explanation": "Dùng Future Perfect với 'by next month' để diễn tả hành động sẽ kéo dài đến một thời điểm trong tương lai."
        },
        {
            "question": "We _____ to school by bus every day.",
            "options": ["go", "goes", "are going", "went"],
            "answer": "go",
            "explanation": "Dùng Present Simple để diễn tả thói quen, hành động lặp đi lặp lại."
        },
        {
            "question": "She _____ her friends when I saw her.",
            "options": ["meets", "met", "was meeting", "has met"],
            "answer": "was meeting",
            "explanation": "Dùng Past Continuous để diễn tả hành động đang xảy ra tại thời điểm cụ thể trong quá khứ."
        },
        {
            "question": "I _____ to Paris twice.",
            "options": ["go", "went", "have been", "had been"],
            "answer": "have been",
            "explanation": "Dùng Present Perfect để diễn tả kinh nghiệm đã từng làm gì đó bao nhiêu lần."
        },
        {
            "question": "The train _____ at 6 PM tomorrow.",
            "options": ["leaves", "will leave", "is leaving", "left"],
            "answer": "leaves",
            "explanation": "Dùng Present Simple để diễn tả lịch trình, thời gian biểu cố định."
        },
        {
            "question": "When I arrived, they _____ already _____ lunch.",
            "options": ["have/eaten", "had/eaten", "were/eating", "are/eating"],
            "answer": "had/eaten",
            "explanation": "Dùng Past Perfect để diễn tả hành động đã hoàn thành trước một thời điểm trong quá khứ."
        },
        {
            "question": "Look! The children _____ in the garden.",
            "options": ["play", "plays", "are playing", "played"],
            "answer": "are playing",
            "explanation": "Dùng Present Continuous với 'Look!' để diễn tả hành động đang xảy ra ngay lúc nói."
        },
        {
            "question": "He said he _____ me the next day.",
            "options": ["will call", "would call", "calls", "called"],
            "answer": "would call",
            "explanation": "Trong câu tường thuật, 'will' đổi thành 'would'."
        },
        {
            "question": "I _____ my report by tomorrow evening.",
            "options": ["finish", "will finish", "will have finished", "am finishing"],
            "answer": "will have finished",
            "explanation": "Dùng Future Perfect với 'by tomorrow evening' để diễn tả hành động sẽ hoàn thành trước một thời điểm trong tương lai."
        },
        {
            "question": "This is the first time I _____ such a beautiful place.",
            "options": ["visit", "visited", "have visited", "am visiting"],
            "answer": "have visited",
            "explanation": "Dùng Present Perfect với cấu trúc 'This is the first time + S + have/has + V3'."
        },
        {
            "question": "She _____ always _____ her room on Sundays.",
            "options": ["is/cleaning", "has/cleaned", "-/cleans", "was/cleaning"],
            "answer": "-/cleans",
            "explanation": "Dùng Present Simple với 'always' để diễn tả thói quen."
        },
        {
            "question": "After he _____ his homework, he went to bed.",
            "options": ["finishes", "finished", "has finished", "had finished"],
            "answer": "had finished",
            "explanation": "Dùng Past Perfect trong mệnh đề 'After' khi hai hành động xảy ra liên tiếp trong quá khứ."
        },
        {
            "question": "The sun _____ in the east.",
            "options": ["rise", "rises", "is rising", "rose"],
            "answer": "rises",
            "explanation": "Dùng Present Simple để diễn tả sự thật hiển nhiên, chân lý."
        },
        {
            "question": "I _____ my friend tomorrow afternoon.",
            "options": ["meet", "will meet", "am meeting", "met"],
            "answer": "am meeting",
            "explanation": "Dùng Present Continuous để diễn tả kế hoạch, lịch hẹn đã sắp xếp trong tương lai gần."
        },
        {
            "question": "She _____ for that company for 10 years before she retired.",
            "options": ["works", "worked", "has worked", "had worked"],
            "answer": "had worked",
            "explanation": "Dùng Past Perfect để diễn tả hành động xảy ra và kéo dài trước một thời điểm trong quá khứ."
        },
        {
            "question": "They _____ a new house next month.",
            "options": ["buy", "will buy", "are buying", "bought"],
            "answer": "are buying",
            "explanation": "Dùng Present Continuous để diễn tả kế hoạch đã quyết định trong tương lai gần."
        },
        {
            "question": "How long _____ you _____ English?",
            "options": ["do/learn", "did/learn", "have/learned", "are/learning"],
            "answer": "have/learned",
            "explanation": "Dùng Present Perfect với 'How long' để hỏi về thời gian một hành động đã kéo dài."
        },
        
        # ==================== PASSIVE VOICE (25 câu) ====================
        {
            "question": "The letter _____ yesterday.",
            "options": ["was sent", "is sent", "has been sent", "sent"],
            "answer": "was sent",
            "explanation": "Dùng Past Simple Passive với dấu hiệu 'yesterday' (thời gian cụ thể trong quá khứ)."
        },
        {
            "question": "English _____ all over the world.",
            "options": ["speaks", "is spoken", "was spoken", "has spoken"],
            "answer": "is spoken",
            "explanation": "Dùng Present Simple Passive để diễn tả sự thật hiện tại."
        },
        {
            "question": "A new bridge _____ in our city at the moment.",
            "options": ["is built", "is being built", "was built", "has been built"],
            "answer": "is being built",
            "explanation": "Dùng Present Continuous Passive với 'at the moment' để diễn tả hành động đang xảy ra."
        },
        {
            "question": "The room _____ when I arrived.",
            "options": ["cleans", "was cleaning", "was being cleaned", "is cleaned"],
            "answer": "was being cleaned",
            "explanation": "Dùng Past Continuous Passive để diễn tả hành động đang xảy ra tại một thời điểm trong quá khứ."
        },
        {
            "question": "This book _____ by millions of people.",
            "options": ["reads", "is read", "has been read", "was read"],
            "answer": "has been read",
            "explanation": "Dùng Present Perfect Passive để diễn tả hành động đã hoàn thành với kết quả còn liên quan đến hiện tại."
        },
        {
            "question": "The house _____ before we moved in.",
            "options": ["painted", "was painted", "has been painted", "had been painted"],
            "answer": "had been painted",
            "explanation": "Dùng Past Perfect Passive để diễn tả hành động xảy ra trước một hành động khác trong quá khứ."
        },
        {
            "question": "These cars _____ in Japan.",
            "options": ["make", "are made", "made", "have made"],
            "answer": "are made",
            "explanation": "Dùng Present Simple Passive để diễn tả sự thật chung."
        },
        {
            "question": "The problem _____ by the teacher now.",
            "options": ["explains", "is explaining", "is being explained", "was explained"],
            "answer": "is being explained",
            "explanation": "Dùng Present Continuous Passive với 'now' để diễn tả hành động đang xảy ra."
        },
        {
            "question": "The project _____ by next Friday.",
            "options": ["will finish", "will be finished", "finishes", "is finished"],
            "answer": "will be finished",
            "explanation": "Dùng Future Simple Passive với 'by next Friday' để diễn tả hành động sẽ hoàn thành."
        },
        {
            "question": "My wallet _____ stolen.",
            "options": ["has", "has been", "was", "is"],
            "answer": "has been",
            "explanation": "Dùng Present Perfect Passive để diễn tả hành động xảy ra trong quá khứ nhưng kết quả còn ảnh hưởng đến hiện tại."
        },
        {
            "question": "The cake _____ by my mother yesterday.",
            "options": ["bakes", "baked", "was baked", "is baked"],
            "answer": "was baked",
            "explanation": "Dùng Past Simple Passive với 'yesterday'."
        },
        {
            "question": "A new hospital _____ in this area next year.",
            "options": ["builds", "will build", "will be built", "is built"],
            "answer": "will be built",
            "explanation": "Dùng Future Simple Passive với 'next year'."
        },
        {
            "question": "The dishes _____ after every meal.",
            "options": ["wash", "washes", "are washed", "were washed"],
            "answer": "are washed",
            "explanation": "Dùng Present Simple Passive để diễn tả thói quen."
        },
        {
            "question": "The window _____ by the children.",
            "options": ["broke", "was broken", "is broken", "has broken"],
            "answer": "was broken",
            "explanation": "Dùng Past Simple Passive để diễn tả hành động đã xảy ra trong quá khứ."
        },
        {
            "question": "Many houses _____ by the storm last night.",
            "options": ["destroy", "destroyed", "were destroyed", "are destroyed"],
            "answer": "were destroyed",
            "explanation": "Dùng Past Simple Passive với 'last night'."
        },
        {
            "question": "The report must _____ by tomorrow.",
            "options": ["finish", "be finished", "finished", "finishing"],
            "answer": "be finished",
            "explanation": "Sau modal verb (must) dùng 'be + V3' để tạo câu bị động."
        },
        {
            "question": "Her new novel will _____ next month.",
            "options": ["publish", "be published", "published", "publishing"],
            "answer": "be published",
            "explanation": "Sau 'will' dùng 'be + V3' để tạo câu bị động."
        },
        {
            "question": "The exam papers _____ by the teacher right now.",
            "options": ["are marking", "are being marked", "mark", "marked"],
            "answer": "are being marked",
            "explanation": "Dùng Present Continuous Passive với 'right now'."
        },
        {
            "question": "All the homework _____ before I went to bed.",
            "options": ["was done", "has been done", "had been done", "is done"],
            "answer": "had been done",
            "explanation": "Dùng Past Perfect Passive để diễn tả hành động đã hoàn thành trước một thời điểm trong quá khứ."
        },
        {
            "question": "The thief _____ by the police yesterday.",
            "options": ["catches", "caught", "was caught", "is caught"],
            "answer": "was caught",
            "explanation": "Dùng Past Simple Passive với 'yesterday'."
        },
        {
            "question": "This building _____ in 1990.",
            "options": ["built", "was built", "has been built", "is built"],
            "answer": "was built",
            "explanation": "Dùng Past Simple Passive với năm cụ thể trong quá khứ."
        },
        {
            "question": "The streets _____ every morning.",
            "options": ["clean", "cleans", "are cleaned", "were cleaned"],
            "answer": "are cleaned",
            "explanation": "Dùng Present Simple Passive để diễn tả thói quen."
        },
        {
            "question": "The packages _____ to the customers tomorrow.",
            "options": ["will send", "will be sent", "send", "are sent"],
            "answer": "will be sent",
            "explanation": "Dùng Future Simple Passive với 'tomorrow'."
        },
        {
            "question": "The concert _____ because of bad weather.",
            "options": ["cancelled", "was cancelled", "has cancelled", "is cancelling"],
            "answer": "was cancelled",
            "explanation": "Dùng Past Simple Passive để diễn tả hành động đã xảy ra."
        },
        {
            "question": "These toys _____ from recycled materials.",
            "options": ["make", "made", "are made", "were made"],
            "answer": "are made",
            "explanation": "Dùng Present Simple Passive để diễn tả sự thật chung."
        },
        
        # ==================== CONDITIONAL SENTENCES (20 câu) ====================
        {
            "question": "If I _____ you, I would study harder.",
            "options": ["am", "was", "were", "will be"],
            "answer": "were",
            "explanation": "Câu điều kiện loại 2: If + S + were/V-ed, S + would + V. Dùng 'were' cho tất cả các ngôi."
        },
        {
            "question": "If it rains tomorrow, we _____ at home.",
            "options": ["stay", "will stay", "would stay", "stayed"],
            "answer": "will stay",
            "explanation": "Câu điều kiện loại 1: If + S + V(s/es), S + will + V. Diễn tả điều có thể xảy ra trong tương lai."
        },
        {
            "question": "If she had studied harder, she _____ the exam.",
            "options": ["would pass", "will pass", "would have passed", "passed"],
            "answer": "would have passed",
            "explanation": "Câu điều kiện loại 3: If + S + had + V3, S + would have + V3. Diễn tả điều không có thật trong quá khứ."
        },
        {
            "question": "If I _____ a lot of money, I would travel around the world.",
            "options": ["have", "had", "will have", "have had"],
            "answer": "had",
            "explanation": "Câu điều kiện loại 2: If + S + V-ed/were, S + would + V. Diễn tả điều không có thật ở hiện tại."
        },
        {
            "question": "Unless you work hard, you _____ pass the test.",
            "options": ["will", "won't", "would", "wouldn't"],
            "answer": "won't",
            "explanation": "Unless = If...not. Unless you work hard = If you don't work hard, you won't pass."
        },
        {
            "question": "If he _____ earlier, he wouldn't have missed the train.",
            "options": ["left", "leaves", "had left", "would leave"],
            "answer": "had left",
            "explanation": "Câu điều kiện loại 3: If + S + had + V3, S + would have + V3."
        },
        {
            "question": "If you heat ice, it _____.",
            "options": ["melts", "will melt", "would melt", "melted"],
            "answer": "melts",
            "explanation": "Câu điều kiện loại 0: If + S + V(s/es), S + V(s/es). Diễn tả chân lý, sự thật hiển nhiên."
        },
        {
            "question": "If I see him, I _____ him your message.",
            "options": ["give", "will give", "would give", "gave"],
            "answer": "will give",
            "explanation": "Câu điều kiện loại 1: If + S + V(s/es), S + will + V."
        },
        {
            "question": "She would buy a new car if she _____ enough money.",
            "options": ["has", "had", "will have", "have"],
            "answer": "had",
            "explanation": "Câu điều kiện loại 2: If + S + V-ed, S + would + V."
        },
        {
            "question": "If they _____ invited me, I would have gone to the party.",
            "options": ["invited", "had invited", "invite", "have invited"],
            "answer": "had invited",
            "explanation": "Câu điều kiện loại 3: If + S + had + V3, S + would have + V3."
        },
        {
            "question": "If we don't hurry, we _____ late for school.",
            "options": ["are", "will be", "would be", "were"],
            "answer": "will be",
            "explanation": "Câu điều kiện loại 1: If + S + don't/doesn't + V, S + will + V."
        },
        {
            "question": "If you _____ the instructions carefully, you wouldn't have made mistakes.",
            "options": ["read", "had read", "have read", "would read"],
            "answer": "had read",
            "explanation": "Câu điều kiện loại 3: If + S + had + V3, S + would have + V3."
        },
        {
            "question": "If I were you, I _____ accept that offer.",
            "options": ["will", "would", "can", "could"],
            "answer": "would",
            "explanation": "Câu điều kiện loại 2 dùng để khuyên: If I were you, I would + V."
        },
        {
            "question": "Water _____ at 100 degrees Celsius if you boil it.",
            "options": ["boils", "will boil", "would boil", "boiled"],
            "answer": "boils",
            "explanation": "Câu điều kiện loại 0: If + S + V(s/es), S + V(s/es). Diễn tả sự thật khoa học."
        },
        {
            "question": "If she practiced more, she _____ play the piano better.",
            "options": ["will", "would", "can", "should"],
            "answer": "would",
            "explanation": "Câu điều kiện loại 2: If + S + V-ed, S + would + V."
        },
        {
            "question": "If you _____ me, I will help you.",
            "options": ["ask", "asked", "will ask", "would ask"],
            "answer": "ask",
            "explanation": "Câu điều kiện loại 1: If + S + V(s/es), S + will + V."
        },
        {
            "question": "If I had known you were coming, I _____ a cake.",
            "options": ["bake", "baked", "would bake", "would have baked"],
            "answer": "would have baked",
            "explanation": "Câu điều kiện loại 3: If + S + had + V3, S + would have + V3."
        },
        {
            "question": "If it _____ sunny tomorrow, we will go to the beach.",
            "options": ["is", "will be", "was", "were"],
            "answer": "is",
            "explanation": "Câu điều kiện loại 1: If + S + is/am/are, S + will + V."
        },
        {
            "question": "He would have passed the exam if he _____ more carefully.",
            "options": ["studied", "had studied", "studies", "would study"],
            "answer": "had studied",
            "explanation": "Câu điều kiện loại 3: If + S + had + V3, S + would have + V3."
        },
        {
            "question": "If you don't leave now, you _____ the bus.",
            "options": ["miss", "will miss", "would miss", "missed"],
            "answer": "will miss",
            "explanation": "Câu điều kiện loại 1: If + S + don't/doesn't + V, S + will + V."
        },
        
        # ==================== RELATIVE CLAUSES (20 câu) ====================
        {
            "question": "The book _____ I bought yesterday is very interesting.",
            "options": ["who", "which", "whose", "where"],
            "answer": "which",
            "explanation": "Dùng 'which' thay cho vật (the book). 'Which' có thể làm chủ ngữ hoặc tân ngữ."
        },
        {
            "question": "The man _____ is standing over there is my teacher.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "who",
            "explanation": "Dùng 'who' thay cho người (the man) làm chủ ngữ trong mệnh đề quan hệ."
        },
        {
            "question": "This is the house _____ I was born.",
            "options": ["which", "where", "when", "who"],
            "answer": "where",
            "explanation": "Dùng 'where' thay cho địa điểm (in the house). Where = in/at/on which."
        },
        {
            "question": "The girl _____ mother is a doctor is my classmate.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "whose",
            "explanation": "Dùng 'whose' để chỉ sở hữu (của ai). Whose + danh từ."
        },
        {
            "question": "Do you remember the day _____ we first met?",
            "options": ["which", "where", "when", "who"],
            "answer": "when",
            "explanation": "Dùng 'when' thay cho thời gian (on the day). When = on/at/in which."
        },
        {
            "question": "The woman _____ you met yesterday is my aunt.",
            "options": ["who", "whom", "which", "whose"],
            "answer": "whom",
            "explanation": "Dùng 'whom' thay cho người làm tân ngữ. Có thể dùng 'who' trong văn nói thông thường."
        },
        {
            "question": "I like books _____ have happy endings.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "which",
            "explanation": "Dùng 'which' thay cho vật (books) làm chủ ngữ."
        },
        {
            "question": "The reason _____ he was late is still unknown.",
            "options": ["which", "why", "when", "where"],
            "answer": "why",
            "explanation": "Dùng 'why' thay cho lý do (for the reason). Why = for which."
        },
        {
            "question": "The students _____ study hard will pass the exam.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "who",
            "explanation": "Dùng 'who' thay cho người (the students) làm chủ ngữ."
        },
        {
            "question": "Is that the restaurant _____ you had dinner last night?",
            "options": ["which", "where", "when", "who"],
            "answer": "where",
            "explanation": "Dùng 'where' thay cho địa điểm (at the restaurant)."
        },
        {
            "question": "The car _____ he bought is very expensive.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "which",
            "explanation": "Dùng 'which' thay cho vật (the car). Có thể bỏ 'which' vì làm tân ngữ."
        },
        {
            "question": "The boy _____ bicycle was stolen is very sad.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "whose",
            "explanation": "Dùng 'whose' để chỉ sở hữu (bicycle của boy)."
        },
        {
            "question": "2020 was the year _____ the pandemic started.",
            "options": ["which", "where", "when", "who"],
            "answer": "when",
            "explanation": "Dùng 'when' thay cho năm/thời gian (in 2020)."
        },
        {
            "question": "The people _____ live next door are very friendly.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "who",
            "explanation": "Dùng 'who' thay cho người (the people) làm chủ ngữ."
        },
        {
            "question": "This is the place _____ we spent our vacation.",
            "options": ["which", "where", "when", "who"],
            "answer": "where",
            "explanation": "Dùng 'where' thay cho địa điểm (at the place)."
        },
        {
            "question": "The teacher _____ I respect most is Mrs. Smith.",
            "options": ["who", "whom", "which", "whose"],
            "answer": "whom",
            "explanation": "Dùng 'whom' thay cho người làm tân ngữ. Trong văn nói có thể dùng 'who'."
        },
        {
            "question": "The dog _____ barks all night belongs to my neighbor.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "which",
            "explanation": "Dùng 'which' thay cho động vật (the dog) làm chủ ngữ. Có thể dùng 'that'."
        },
        {
            "question": "The hotel _____ we stayed was very comfortable.",
            "options": ["which", "where", "when", "who"],
            "answer": "where",
            "explanation": "Dùng 'where' thay cho địa điểm (at the hotel)."
        },
        {
            "question": "The movie _____ we watched last night was boring.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "which",
            "explanation": "Dùng 'which' thay cho vật (the movie). Có thể bỏ vì làm tân ngữ."
        },
        {
            "question": "The girl _____ I told you about is coming to visit.",
            "options": ["who", "whom", "which", "whose"],
            "answer": "whom",
            "explanation": "Dùng 'whom' thay cho người làm tân ngữ của giới từ. Có thể dùng 'who' trong văn nói."
        },
        
        # ==================== REPORTED SPEECH (20 câu) ====================
        {
            "question": "She said, 'I am tired.' → She said she _____ tired.",
            "options": ["is", "was", "has been", "will be"],
            "answer": "was",
            "explanation": "Trong câu tường thuật, 'am/is' đổi thành 'was'."
        },
        {
            "question": "He said, 'I will call you tomorrow.' → He said he _____ me the next day.",
            "options": ["will call", "would call", "called", "calls"],
            "answer": "would call",
            "explanation": "Trong câu tường thuật, 'will' đổi thành 'would', 'tomorrow' đổi thành 'the next day'."
        },
        {
            "question": "'Where do you live?' he asked me. → He asked me where _____.",
            "options": ["do I live", "I lived", "did I live", "I live"],
            "answer": "I lived",
            "explanation": "Câu hỏi tường thuật: asked + wh-word + S + V (lùi thì). 'Do you live' → 'I lived'."
        },
        {
            "question": "'Don't be late!' she told me. → She told me _____ late.",
            "options": ["don't be", "not to be", "not be", "to not be"],
            "answer": "not to be",
            "explanation": "Câu mệnh lệnh phủ định tường thuật: told + O + not to V."
        },
        {
            "question": "She said, 'I have finished my homework.' → She said she _____ her homework.",
            "options": ["has finished", "had finished", "finished", "finishes"],
            "answer": "had finished",
            "explanation": "Trong câu tường thuật, Present Perfect đổi thành Past Perfect."
        },
        {
            "question": "'Can you help me?' he asked. → He asked if I _____ help him.",
            "options": ["can", "could", "will", "would"],
            "answer": "could",
            "explanation": "Câu hỏi Yes/No tường thuật: asked if + S + V (lùi thì). 'Can' → 'could'."
        },
        {
            "question": "'I saw him yesterday,' she said. → She said she _____ him the day before.",
            "options": ["sees", "saw", "had seen", "has seen"],
            "answer": "had seen",
            "explanation": "Trong câu tường thuật, Past Simple đổi thành Past Perfect, 'yesterday' → 'the day before'."
        },
        {
            "question": "'Close the door!' the teacher said. → The teacher told us _____ the door.",
            "options": ["close", "to close", "closing", "closed"],
            "answer": "to close",
            "explanation": "Câu mệnh lệnh khẳng định tường thuật: told + O + to V."
        },
        {
            "question": "'I am reading a book,' Tom said. → Tom said he _____ a book.",
            "options": ["is reading", "was reading", "reads", "read"],
            "answer": "was reading",
            "explanation": "Trong câu tường thuật, Present Continuous đổi thành Past Continuous."
        },
        {
            "question": "'What time is it?' she asked. → She asked what time _____.",
            "options": ["is it", "it was", "was it", "it is"],
            "answer": "it was",
            "explanation": "Câu hỏi tường thuật: asked + wh-word + S + V (lùi thì). 'Is' → 'was'."
        },
        {
            "question": "'I have never been to Paris,' he said. → He said he _____ to Paris.",
            "options": ["has never been", "had never been", "never was", "was never"],
            "answer": "had never been",
            "explanation": "Present Perfect → Past Perfect trong câu tường thuật."
        },
        {
            "question": "'Please sit down,' she said to me. → She asked me _____ down.",
            "options": ["sit", "to sit", "sitting", "sat"],
            "answer": "to sit",
            "explanation": "Câu yêu cầu lịch sự tường thuật: asked + O + to V."
        },
        {
            "question": "'I will be there at 5 PM,' he said. → He said he _____ there at 5 PM.",
            "options": ["will be", "would be", "is", "was"],
            "answer": "would be",
            "explanation": "'Will' đổi thành 'would' trong câu tường thuật."
        },
        {
            "question": "'Are you coming to the party?' she asked. → She asked if I _____ to the party.",
            "options": ["am coming", "was coming", "come", "came"],
            "answer": "was coming",
            "explanation": "Câu hỏi Yes/No tường thuật: asked if + S + V (lùi thì)."
        },
        {
            "question": "'I may go there,' she said. → She said she _____ go there.",
            "options": ["may", "might", "can", "could"],
            "answer": "might",
            "explanation": "'May' đổi thành 'might' trong câu tường thuật."
        },
        {
            "question": "'Don't touch that!' he said. → He told me _____ that.",
            "options": ["don't touch", "not to touch", "not touch", "to not touch"],
            "answer": "not to touch",
            "explanation": "Câu mệnh lệnh phủ định tường thuật: told + O + not to V."
        },
        {
            "question": "'I bought a new car last week,' John said. → John said he _____ a new car the week before.",
            "options": ["bought", "had bought", "buys", "has bought"],
            "answer": "had bought",
            "explanation": "Past Simple → Past Perfect, 'last week' → 'the week before'."
        },
        {
            "question": "'How old are you?' she asked me. → She asked me how old _____.",
            "options": ["am I", "I was", "was I", "I am"],
            "answer": "I was",
            "explanation": "Câu hỏi tường thuật: asked + wh-word + S + V (lùi thì)."
        },
        {
            "question": "'I must finish this today,' she said. → She said she _____ finish that that day.",
            "options": ["must", "had to", "has to", "have to"],
            "answer": "had to",
            "explanation": "'Must' có thể đổi thành 'had to' trong câu tường thuật."
        },
        {
            "question": "'Study hard!' the teacher said to us. → The teacher told us _____ hard.",
            "options": ["study", "to study", "studying", "studied"],
            "answer": "to study",
            "explanation": "Câu mệnh lệnh khẳng định tường thuật: told + O + to V."
        },
        
        # ==================== COMPARATIVES & SUPERLATIVES (20 câu) ====================
        {
            "question": "My brother is _____ than me.",
            "options": ["tall", "taller", "tallest", "more tall"],
            "answer": "taller",
            "explanation": "So sánh hơn của tính từ ngắn: adj + -er + than."
        },
        {
            "question": "This is the _____ book I have ever read.",
            "options": ["interesting", "more interesting", "most interesting", "interestinger"],
            "answer": "most interesting",
            "explanation": "So sánh nhất của tính từ dài: the most + adj."
        },
        {
            "question": "She runs _____ than her sister.",
            "options": ["fast", "faster", "fastest", "more fast"],
            "answer": "faster",
            "explanation": "So sánh hơn của trạng từ ngắn: adv + -er + than."
        },
        {
            "question": "Gold is _____ than silver.",
            "options": ["expensive", "more expensive", "most expensive", "expensiver"],
            "answer": "more expensive",
            "explanation": "So sánh hơn của tính từ dài: more + adj + than."
        },
        {
            "question": "He is the _____ student in the class.",
            "options": ["good", "better", "best", "well"],
            "answer": "best",
            "explanation": "So sánh nhất của 'good' là 'the best'."
        },
        {
            "question": "The weather today is _____ than yesterday.",
            "options": ["bad", "worse", "worst", "more bad"],
            "answer": "worse",
            "explanation": "So sánh hơn của 'bad' là 'worse'."
        },
        {
            "question": "This exercise is _____ than that one.",
            "options": ["easy", "easier", "easiest", "more easy"],
            "answer": "easier",
            "explanation": "So sánh hơn của tính từ ngắn: adj + -er + than."
        },
        {
            "question": "Mount Everest is the _____ mountain in the world.",
            "options": ["high", "higher", "highest", "most high"],
            "answer": "highest",
            "explanation": "So sánh nhất của tính từ ngắn: the + adj + -est."
        },
        {
            "question": "She speaks English _____ than I do.",
            "options": ["fluent", "more fluently", "most fluently", "fluently"],
            "answer": "more fluently",
            "explanation": "So sánh hơn của trạng từ dài: more + adv + than."
        },
        {
            "question": "This is the _____ day of my life.",
            "options": ["happy", "happier", "happiest", "more happy"],
            "answer": "happiest",
            "explanation": "So sánh nhất của tính từ ngắn: the + adj + -est."
        },
        {
            "question": "The Nile is _____ river in the world.",
            "options": ["long", "longer", "longest", "the longest"],
            "answer": "the longest",
            "explanation": "So sánh nhất: the + adj + -est. Cần có 'the'."
        },
        {
            "question": "My car is _____ expensive than yours.",
            "options": ["little", "less", "least", "more less"],
            "answer": "less",
            "explanation": "So sánh kém: less + adj + than."
        },
        {
            "question": "This movie is _____ boring than the last one.",
            "options": ["much", "many", "more", "most"],
            "answer": "more",
            "explanation": "So sánh hơn của tính từ dài: more + adj + than."
        },
        {
            "question": "She is the _____ beautiful girl in the school.",
            "options": ["more", "most", "much", "many"],
            "answer": "most",
            "explanation": "So sánh nhất của tính từ dài: the most + adj."
        },
        {
            "question": "Today is _____ cold as yesterday.",
            "options": ["as", "so", "more", "most"],
            "answer": "as",
            "explanation": "So sánh bằng: as + adj + as."
        },
        {
            "question": "He works _____ than his colleagues.",
            "options": ["hard", "harder", "hardest", "more hard"],
            "answer": "harder",
            "explanation": "So sánh hơn của trạng từ ngắn: adv + -er + than."
        },
        {
            "question": "This is _____ difficult question on the test.",
            "options": ["more", "most", "the more", "the most"],
            "answer": "the most",
            "explanation": "So sánh nhất: the most + adj."
        },
        {
            "question": "My house is not as _____ as yours.",
            "options": ["big", "bigger", "biggest", "more big"],
            "answer": "big",
            "explanation": "So sánh bằng: not as + adj + as (dùng dạng nguyên mẫu)."
        },
        {
            "question": "The _____ you practice, the better you become.",
            "options": ["more", "most", "much", "many"],
            "answer": "more",
            "explanation": "Cấu trúc so sánh kép: The + comparative..., the + comparative..."
        },
        {
            "question": "She sings _____ beautifully than anyone else.",
            "options": ["more", "most", "much", "many"],
            "answer": "more",
            "explanation": "So sánh hơn của trạng từ dài: more + adv + than."
        },
        
        # ==================== PREPOSITIONS (20 câu) ====================
        {
            "question": "I am interested _____ learning English.",
            "options": ["in", "on", "at", "for"],
            "answer": "in",
            "explanation": "Be interested in + V-ing: quan tâm đến việc gì."
        },
        {
            "question": "She is good _____ Mathematics.",
            "options": ["in", "at", "on", "for"],
            "answer": "at",
            "explanation": "Be good at + N/V-ing: giỏi về môn gì."
        },
        {
            "question": "The book is _____ the table.",
            "options": ["in", "on", "at", "for"],
            "answer": "on",
            "explanation": "On + bề mặt phẳng (bàn, tường...)."
        },
        {
            "question": "We arrived _____ the station at 6 PM.",
            "options": ["in", "on", "at", "to"],
            "answer": "at",
            "explanation": "Arrive at + địa điểm nhỏ (ga, trường...). Arrive in + thành phố, quốc gia."
        },
        {
            "question": "My birthday is _____ May.",
            "options": ["in", "on", "at", "for"],
            "answer": "in",
            "explanation": "In + tháng, năm, mùa."
        },
        {
            "question": "I will meet you _____ Monday.",
            "options": ["in", "on", "at", "for"],
            "answer": "on",
            "explanation": "On + thứ, ngày cụ thể."
        },
        {
            "question": "She is afraid _____ snakes.",
            "options": ["of", "at", "in", "for"],
            "answer": "of",
            "explanation": "Be afraid of + N/V-ing: sợ cái gì."
        },
        {
            "question": "We have lived here _____ 10 years.",
            "options": ["since", "for", "during", "from"],
            "answer": "for",
            "explanation": "For + khoảng thời gian (10 years, 3 months...)."
        },
        {
            "question": "They have been friends _____ childhood.",
            "options": ["since", "for", "during", "from"],
            "answer": "since",
            "explanation": "Since + mốc thời gian (2010, childhood...)."
        },
        {
            "question": "The cat is hiding _____ the bed.",
            "options": ["under", "on", "at", "in"],
            "answer": "under",
            "explanation": "Under = dưới, phía dưới."
        },
        {
            "question": "I am waiting _____ the bus.",
            "options": ["for", "to", "at", "on"],
            "answer": "for",
            "explanation": "Wait for + N: đợi ai/cái gì."
        },
        {
            "question": "She is famous _____ her singing.",
            "options": ["for", "of", "at", "in"],
            "answer": "for",
            "explanation": "Be famous for + N: nổi tiếng về cái gì."
        },
        {
            "question": "The meeting will start _____ 9 o'clock.",
            "options": ["in", "on", "at", "for"],
            "answer": "at",
            "explanation": "At + giờ cụ thể."
        },
        {
            "question": "He apologized _____ being late.",
            "options": ["for", "of", "to", "with"],
            "answer": "for",
            "explanation": "Apologize for + V-ing: xin lỗi về việc gì."
        },
        {
            "question": "The picture is hanging _____ the wall.",
            "options": ["in", "on", "at", "for"],
            "answer": "on",
            "explanation": "On the wall = trên tường (bề mặt)."
        },
        {
            "question": "They went to Paris _____ plane.",
            "options": ["by", "on", "in", "with"],
            "answer": "by",
            "explanation": "By + phương tiện (không có 'the'): by plane, by car..."
        },
        {
            "question": "I am proud _____ my son.",
            "options": ["of", "at", "in", "for"],
            "answer": "of",
            "explanation": "Be proud of + N: tự hào về ai/cái gì."
        },
        {
            "question": "She succeeded _____ passing the exam.",
            "options": ["in", "on", "at", "for"],
            "answer": "in",
            "explanation": "Succeed in + V-ing: thành công trong việc gì."
        },
        {
            "question": "The store is _____ the corner of the street.",
            "options": ["in", "on", "at", "for"],
            "answer": "at",
            "explanation": "At the corner = ở góc phố."
        },
        {
            "question": "He depends _____ his parents for money.",
            "options": ["on", "in", "at", "for"],
            "answer": "on",
            "explanation": "Depend on + N: phụ thuộc vào ai/cái gì."
        },
        
        # ==================== VOCABULARY (25 câu) ====================
        {
            "question": "The internet is a very useful means of _____.",
            "options": ["communication", "communicative", "communicate", "communicator"],
            "answer": "communication",
            "explanation": "Cần danh từ sau 'means of'. Communication = sự giao tiếp."
        },
        {
            "question": "English is _____ spoken all over the world.",
            "options": ["wide", "width", "widely", "widen"],
            "answer": "widely",
            "explanation": "Cần trạng từ bổ nghĩa cho động từ 'spoken'. Widely = rộng rãi."
        },
        {
            "question": "We should _____ the environment from pollution.",
            "options": ["protect", "protection", "protective", "protector"],
            "answer": "protect",
            "explanation": "Sau 'should' dùng động từ nguyên mẫu. Protect = bảo vệ."
        },
        {
            "question": "The _____ of the air makes it difficult to breathe.",
            "options": ["pollute", "pollution", "polluted", "polluting"],
            "answer": "pollution",
            "explanation": "Cần danh từ làm chủ ngữ. Pollution = sự ô nhiễm."
        },
        {
            "question": "She speaks English _____, so everyone can understand her.",
            "options": ["clear", "clearly", "clearness", "clarity"],
            "answer": "clearly",
            "explanation": "Cần trạng từ bổ nghĩa cho động từ 'speaks'. Clearly = rõ ràng."
        },
        {
            "question": "The weather was _____, so we stayed at home.",
            "options": ["terribly", "terrible", "terror", "terrify"],
            "answer": "terrible",
            "explanation": "Cần tính từ sau động từ 'was'. Terrible = tồi tệ."
        },
        {
            "question": "He is a very _____ person. He always helps others.",
            "options": ["help", "helpful", "helpless", "helpfully"],
            "answer": "helpful",
            "explanation": "Cần tính từ bổ nghĩa cho danh từ 'person'. Helpful = hay giúp đỡ."
        },
        {
            "question": "The _____ of this machine is very simple.",
            "options": ["operate", "operation", "operator", "operating"],
            "answer": "operation",
            "explanation": "Cần danh từ làm chủ ngữ. Operation = sự vận hành."
        },
        {
            "question": "We need to _____ our knowledge of technology.",
            "options": ["improve", "improvement", "improved", "improving"],
            "answer": "improve",
            "explanation": "Sau 'need to' dùng động từ nguyên mẫu. Improve = cải thiện."
        },
        {
            "question": "The teacher gave us a _____ explanation.",
            "options": ["satisfy", "satisfactory", "satisfaction", "satisfied"],
            "answer": "satisfactory",
            "explanation": "Cần tính từ bổ nghĩa cho danh từ 'explanation'. Satisfactory = thỏa đáng."
        },
        {
            "question": "Tourism has _____ rapidly in recent years.",
            "options": ["develop", "developed", "development", "developing"],
            "answer": "developed",
            "explanation": "Cần động từ chia Present Perfect với 'has'. Developed = phát triển."
        },
        {
            "question": "She is very _____ about her exam results.",
            "options": ["worry", "worried", "worrying", "worriedly"],
            "answer": "worried",
            "explanation": "Cần tính từ diễn tả cảm xúc. Worried = lo lắng."
        },
        {
            "question": "The _____ of the internet has changed our lives.",
            "options": ["invent", "invention", "inventor", "inventive"],
            "answer": "invention",
            "explanation": "Cần danh từ làm chủ ngữ. Invention = phát minh."
        },
        {
            "question": "We should save _____ resources for the future.",
            "options": ["nature", "natural", "naturally", "naturalist"],
            "answer": "natural",
            "explanation": "Cần tính từ bổ nghĩa cho danh từ 'resources'. Natural = tự nhiên."
        },
        {
            "question": "The movie was very _____. I fell asleep.",
            "options": ["bore", "bored", "boring", "boringly"],
            "answer": "boring",
            "explanation": "Cần tính từ diễn tả đặc tính của vật. Boring = buồn chán."
        },
        {
            "question": "He made a _____ to visit his grandparents.",
            "options": ["decide", "decision", "decisive", "decided"],
            "answer": "decision",
            "explanation": "Cần danh từ sau 'made a'. Decision = quyết định."
        },
        {
            "question": "The _____ between the two cultures is very interesting.",
            "options": ["differ", "different", "difference", "differently"],
            "answer": "difference",
            "explanation": "Cần danh từ làm chủ ngữ. Difference = sự khác biệt."
        },
        {
            "question": "She is _____ for her children's education.",
            "options": ["response", "responsible", "responsibility", "responsibly"],
            "answer": "responsible",
            "explanation": "Cần tính từ sau 'is'. Responsible for = chịu trách nhiệm về."
        },
        {
            "question": "The teacher's _____ helped me understand the lesson.",
            "options": ["explain", "explanation", "explained", "explaining"],
            "answer": "explanation",
            "explanation": "Cần danh từ làm chủ ngữ. Explanation = lời giải thích."
        },
        {
            "question": "We should _____ reduce plastic waste.",
            "options": ["serious", "seriously", "seriousness", "series"],
            "answer": "seriously",
            "explanation": "Cần trạng từ bổ nghĩa cho động từ 'reduce'. Seriously = một cách nghiêm túc."
        },
        {
            "question": "The company has made a large _____ in the project.",
            "options": ["invest", "investment", "investor", "invested"],
            "answer": "investment",
            "explanation": "Cần danh từ sau 'a large'. Investment = sự đầu tư."
        },
        {
            "question": "He is _____ about his future career.",
            "options": ["optimism", "optimist", "optimistic", "optimistically"],
            "answer": "optimistic",
            "explanation": "Cần tính từ sau 'is'. Optimistic = lạc quan."
        },
        {
            "question": "The _____ of clean water is a serious problem.",
            "options": ["short", "shortage", "shorten", "shortly"],
            "answer": "shortage",
            "explanation": "Cần danh từ làm chủ ngữ. Shortage = sự thiếu hụt."
        },
        {
            "question": "They _____ discussed the matter at the meeting.",
            "options": ["care", "careful", "carefully", "carefulness"],
            "answer": "carefully",
            "explanation": "Cần trạng từ bổ nghĩa cho động từ 'discussed'. Carefully = một cách cẩn thận."
        },
        {
            "question": "The _____ of this building took two years.",
            "options": ["construct", "construction", "constructive", "constructor"],
            "answer": "construction",
            "explanation": "Cần danh từ làm chủ ngữ. Construction = sự xây dựng."
        },
        
        # ==================== GERUNDS & INFINITIVES (15 câu) ====================
        {
            "question": "She enjoys _____ books in her free time.",
            "options": ["read", "to read", "reading", "reads"],
            "answer": "reading",
            "explanation": "Enjoy + V-ing: thích làm gì."
        },
        {
            "question": "I want _____ a doctor when I grow up.",
            "options": ["become", "to become", "becoming", "becomes"],
            "answer": "to become",
            "explanation": "Want + to V: muốn làm gì."
        },
        {
            "question": "They decided _____ to the beach on Sunday.",
            "options": ["go", "to go", "going", "goes"],
            "answer": "to go",
            "explanation": "Decide + to V: quyết định làm gì."
        },
        {
            "question": "He avoids _____ fast food.",
            "options": ["eat", "to eat", "eating", "eats"],
            "answer": "eating",
            "explanation": "Avoid + V-ing: tránh làm gì."
        },
        {
            "question": "Would you mind _____ the window?",
            "options": ["open", "to open", "opening", "opens"],
            "answer": "opening",
            "explanation": "Mind + V-ing: phiền làm gì."
        },
        {
            "question": "I hope _____ you again soon.",
            "options": ["see", "to see", "seeing", "sees"],
            "answer": "to see",
            "explanation": "Hope + to V: hy vọng làm gì."
        },
        {
            "question": "She suggested _____ to the movies.",
            "options": ["go", "to go", "going", "goes"],
            "answer": "going",
            "explanation": "Suggest + V-ing: gợi ý làm gì."
        },
        {
            "question": "I can't help _____ when I watch comedy shows.",
            "options": ["laugh", "to laugh", "laughing", "laughs"],
            "answer": "laughing",
            "explanation": "Can't help + V-ing: không thể không làm gì."
        },
        {
            "question": "They promised _____ on time.",
            "options": ["arrive", "to arrive", "arriving", "arrives"],
            "answer": "to arrive",
            "explanation": "Promise + to V: hứa làm gì."
        },
        {
            "question": "She is good at _____ English.",
            "options": ["speak", "to speak", "speaking", "speaks"],
            "answer": "speaking",
            "explanation": "Giới từ (at) + V-ing."
        },
        {
            "question": "He needs _____ more exercise.",
            "options": ["do", "to do", "doing", "does"],
            "answer": "to do",
            "explanation": "Need + to V: cần làm gì."
        },
        {
            "question": "I look forward to _____ from you.",
            "options": ["hear", "hearing", "heard", "hears"],
            "answer": "hearing",
            "explanation": "Look forward to + V-ing: mong chờ làm gì."
        },
        {
            "question": "She finished _____ her homework at 9 PM.",
            "options": ["do", "to do", "doing", "does"],
            "answer": "doing",
            "explanation": "Finish + V-ing: hoàn thành việc gì."
        },
        {
            "question": "I would like _____ a cup of coffee.",
            "options": ["have", "to have", "having", "has"],
            "answer": "to have",
            "explanation": "Would like + to V: muốn làm gì (lịch sự)."
        },
        {
            "question": "He kept _____ during the lesson.",
            "options": ["talk", "to talk", "talking", "talks"],
            "answer": "talking",
            "explanation": "Keep + V-ing: tiếp tục làm gì."
        },
        
        # ==================== PHRASAL VERBS (15 câu) ====================
        {
            "question": "Can you _____ the television? I want to watch the news.",
            "options": ["turn on", "turn off", "turn up", "turn down"],
            "answer": "turn on",
            "explanation": "Turn on = bật (thiết bị điện)."
        },
        {
            "question": "I need to _____ this word in the dictionary.",
            "options": ["look up", "look after", "look for", "look forward to"],
            "answer": "look up",
            "explanation": "Look up = tra cứu (từ điển)."
        },
        {
            "question": "She _____ her coat before going outside.",
            "options": ["put on", "put off", "put up", "put down"],
            "answer": "put on",
            "explanation": "Put on = mặc (quần áo)."
        },
        {
            "question": "The plane will _____ at 6 AM tomorrow.",
            "options": ["take off", "take on", "take up", "take over"],
            "answer": "take off",
            "explanation": "Take off = cất cánh (máy bay)."
        },
        {
            "question": "Could you _____ after my cat while I'm away?",
            "options": ["look up", "look after", "look for", "look at"],
            "answer": "look after",
            "explanation": "Look after = chăm sóc."
        },
        {
            "question": "He decided to _____ smoking for his health.",
            "options": ["give up", "give in", "give away", "give back"],
            "answer": "give up",
            "explanation": "Give up = từ bỏ (thói quen xấu)."
        },
        {
            "question": "The meeting has been _____ until next week.",
            "options": ["put off", "put on", "put up", "put down"],
            "answer": "put off",
            "explanation": "Put off = hoãn lại."
        },
        {
            "question": "I'm _____ my keys. Have you seen them?",
            "options": ["looking up", "looking after", "looking for", "looking at"],
            "answer": "looking for",
            "explanation": "Look for = tìm kiếm."
        },
        {
            "question": "She _____ well with her colleagues.",
            "options": ["gets on", "gets off", "gets up", "gets over"],
            "answer": "gets on",
            "explanation": "Get on with = hòa hợp, có quan hệ tốt với."
        },
        {
            "question": "Please _____ the form and send it back to us.",
            "options": ["fill in", "fill up", "fill out", "fill with"],
            "answer": "fill in",
            "explanation": "Fill in = điền vào (mẫu đơn). Fill out cũng đúng (Anh-Mỹ)."
        },
        {
            "question": "He _____ at 7 AM every day.",
            "options": ["gets up", "gets on", "gets off", "gets over"],
            "answer": "gets up",
            "explanation": "Get up = thức dậy."
        },
        {
            "question": "Can you _____ the volume? It's too loud.",
            "options": ["turn up", "turn down", "turn on", "turn off"],
            "answer": "turn down",
            "explanation": "Turn down = giảm âm lượng."
        },
        {
            "question": "I _____ an old friend at the supermarket yesterday.",
            "options": ["ran into", "ran over", "ran out", "ran away"],
            "answer": "ran into",
            "explanation": "Run into = tình cờ gặp."
        },
        {
            "question": "They _____ their trip to Paris because of the weather.",
            "options": ["called off", "called on", "called up", "called for"],
            "answer": "called off",
            "explanation": "Call off = hủy bỏ."
        },
        {
            "question": "She needs to _____ her old clothes.",
            "options": ["throw away", "throw up", "throw out", "throw off"],
            "answer": "throw away",
            "explanation": "Throw away = vứt bỏ. Throw out cũng đúng."
        },
        
        # ==================== CONJUNCTIONS (10 câu) ====================
        {
            "question": "I was tired, _____ I went to bed early.",
            "options": ["but", "so", "because", "although"],
            "answer": "so",
            "explanation": "So = vì vậy, chỉ kết quả."
        },
        {
            "question": "_____ it was raining, we went out.",
            "options": ["Because", "Although", "So", "But"],
            "answer": "Although",
            "explanation": "Although = mặc dù, chỉ sự tương phản."
        },
        {
            "question": "He studied hard _____ he wanted to pass the exam.",
            "options": ["so", "but", "because", "although"],
            "answer": "because",
            "explanation": "Because = bởi vì, chỉ nguyên nhân."
        },
        {
            "question": "She is beautiful _____ kind.",
            "options": ["but", "and", "or", "so"],
            "answer": "and",
            "explanation": "And = và, nối hai tính từ cùng loại."
        },
        {
            "question": "Would you like tea _____ coffee?",
            "options": ["but", "and", "or", "so"],
            "answer": "or",
            "explanation": "Or = hoặc, dùng trong câu hỏi lựa chọn."
        },
        {
            "question": "I like swimming, _____ my sister doesn't.",
            "options": ["and", "but", "so", "because"],
            "answer": "but",
            "explanation": "But = nhưng, chỉ sự đối lập."
        },
        {
            "question": "It was late, _____ we decided to leave.",
            "options": ["but", "so", "because", "although"],
            "answer": "so",
            "explanation": "So = vì vậy, chỉ kết quả."
        },
        {
            "question": "_____ he is rich, he is not happy.",
            "options": ["Because", "Although", "So", "And"],
            "answer": "Although",
            "explanation": "Although = mặc dù."
        },
        {
            "question": "Study hard, _____ you will fail the exam.",
            "options": ["and", "or", "but", "so"],
            "answer": "or",
            "explanation": "Or = nếu không thì, diễn tả hậu quả tiêu cực."
        },
        {
            "question": "She can speak English _____ French.",
            "options": ["but", "and", "or", "so"],
            "answer": "and",
            "explanation": "And = và, nối hai ngôn ngữ."
        }
]