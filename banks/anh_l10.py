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
   # ==================== TENSES (30 câu) ====================
        {
            "question": "By the time you arrive, I _____ for two hours.",
            "options": ["will wait", "will be waiting", "will have been waiting", "wait"],
            "answer": "will have been waiting",
            "explanation": "Dùng Future Perfect Continuous với 'by the time' để diễn tả hành động sẽ đang kéo dài đến một thời điểm trong tương lai."
        },
        {
            "question": "She _____ in this company since she graduated from university.",
            "options": ["works", "worked", "has worked", "had worked"],
            "answer": "has worked",
            "explanation": "Dùng Present Perfect với 'since' để diễn tả hành động bắt đầu trong quá khứ và tiếp tục đến hiện tại."
        },
        {
            "question": "While I _____ my homework, my brother was playing video games.",
            "options": ["do", "was doing", "did", "have done"],
            "answer": "was doing",
            "explanation": "Dùng Past Continuous với 'while' để diễn tả hai hành động đang xảy ra song song trong quá khứ."
        },
        {
            "question": "I _____ three cups of coffee this morning.",
            "options": ["drink", "drank", "have drunk", "had drunk"],
            "answer": "have drunk",
            "explanation": "Dùng Present Perfect với 'this morning' (khoảng thời gian chưa kết thúc) để diễn tả hành động đã xảy ra."
        },
        {
            "question": "After he _____ his dinner, he went out for a walk.",
            "options": ["finishes", "finished", "has finished", "had finished"],
            "answer": "had finished",
            "explanation": "Dùng Past Perfect để diễn tả hành động xảy ra trước một hành động khác trong quá khứ."
        },
        {
            "question": "This time next week, we _____ on the beach.",
            "options": ["lie", "will lie", "will be lying", "are lying"],
            "answer": "will be lying",
            "explanation": "Dùng Future Continuous với 'this time next week' để diễn tả hành động sẽ đang xảy ra tại thời điểm cụ thể trong tương lai."
        },
        {
            "question": "I _____ him since we were in high school.",
            "options": ["know", "knew", "have known", "had known"],
            "answer": "have known",
            "explanation": "Dùng Present Perfect với 'since' để diễn tả trạng thái kéo dài từ quá khứ đến hiện tại."
        },
        {
            "question": "When I got home, my mother _____ dinner.",
            "options": ["cooks", "cooked", "was cooking", "has cooked"],
            "answer": "was cooking",
            "explanation": "Dùng Past Continuous để diễn tả hành động đang xảy ra khi có hành động khác xen vào."
        },
        {
            "question": "By 2030, scientists _____ a cure for cancer.",
            "options": ["find", "will find", "will have found", "are finding"],
            "answer": "will have found",
            "explanation": "Dùng Future Perfect với 'by 2030' để diễn tả hành động sẽ hoàn thành trước một thời điểm trong tương lai."
        },
        {
            "question": "She said she _____ to Paris the year before.",
            "options": ["goes", "went", "has gone", "had gone"],
            "answer": "had gone",
            "explanation": "Trong câu tường thuật, Past Simple đổi thành Past Perfect."
        },
        {
            "question": "I _____ my wallet. Can you help me look for it?",
            "options": ["lose", "lost", "have lost", "had lost"],
            "answer": "have lost",
            "explanation": "Dùng Present Perfect để diễn tả hành động vừa xảy ra với kết quả ảnh hưởng đến hiện tại."
        },
        {
            "question": "They _____ married for 25 years by next June.",
            "options": ["are", "will be", "will have been", "have been"],
            "answer": "will have been",
            "explanation": "Dùng Future Perfect với 'by next June' để diễn tả hành động sẽ kéo dài đến một thời điểm trong tương lai."
        },
        {
            "question": "At 8 PM last night, I _____ a movie.",
            "options": ["watch", "watched", "was watching", "have watched"],
            "answer": "was watching",
            "explanation": "Dùng Past Continuous để diễn tả hành động đang xảy ra tại thời điểm cụ thể trong quá khứ."
        },
        {
            "question": "She _____ to the gym three times this week.",
            "options": ["goes", "went", "has gone", "had gone"],
            "answer": "has gone",
            "explanation": "Dùng Present Perfect với 'this week' (khoảng thời gian chưa kết thúc)."
        },
        {
            "question": "Before the teacher arrived, the students _____ already _____ the classroom.",
            "options": ["have/cleaned", "had/cleaned", "were/cleaning", "are/cleaning"],
            "answer": "had/cleaned",
            "explanation": "Dùng Past Perfect để diễn tả hành động đã hoàn thành trước một thời điểm trong quá khứ."
        },
        {
            "question": "The train _____ at 7 AM tomorrow morning.",
            "options": ["leaves", "will leave", "is leaving", "left"],
            "answer": "leaves",
            "explanation": "Dùng Present Simple để diễn tả lịch trình, thời gian biểu cố định."
        },
        {
            "question": "I _____ for you for over an hour. Where have you been?",
            "options": ["wait", "waited", "have been waiting", "had been waiting"],
            "answer": "have been waiting",
            "explanation": "Dùng Present Perfect Continuous để nhấn mạnh hành động vừa mới kết thúc và kéo dài trong một thời gian."
        },
        {
            "question": "When we arrived, the party _____.",
            "options": ["starts", "started", "has started", "had started"],
            "answer": "had started",
            "explanation": "Dùng Past Perfect để diễn tả hành động đã xảy ra trước một hành động khác trong quá khứ."
        },
        {
            "question": "Look! The sun _____.",
            "options": ["rises", "rose", "is rising", "has risen"],
            "answer": "is rising",
            "explanation": "Dùng Present Continuous với 'Look!' để diễn tả hành động đang xảy ra ngay lúc nói."
        },
        {
            "question": "I promise I _____ you tomorrow.",
            "options": ["call", "will call", "am calling", "called"],
            "answer": "will call",
            "explanation": "Dùng Future Simple với 'promise' để diễn tả lời hứa về tương lai."
        },
        {
            "question": "She _____ her project by the deadline next month.",
            "options": ["finishes", "will finish", "will have finished", "is finishing"],
            "answer": "will have finished",
            "explanation": "Dùng Future Perfect với 'by the deadline' để diễn tả hành động sẽ hoàn thành trước thời hạn."
        },
        {
            "question": "We _____ each other since childhood.",
            "options": ["know", "knew", "have known", "had known"],
            "answer": "have known",
            "explanation": "Dùng Present Perfect với 'since childhood' để diễn tả mối quan hệ kéo dài từ quá khứ đến hiện tại."
        },
        {
            "question": "The phone rang while I _____ a shower.",
            "options": ["take", "took", "was taking", "have taken"],
            "answer": "was taking",
            "explanation": "Dùng Past Continuous để diễn tả hành động đang xảy ra khi có hành động khác xen vào."
        },
        {
            "question": "This is the first time I _____ to New York.",
            "options": ["go", "went", "have been", "am going"],
            "answer": "have been",
            "explanation": "Dùng Present Perfect với cấu trúc 'This is the first time + S + have/has + V3'."
        },
        {
            "question": "He _____ his homework before he watched TV last night.",
            "options": ["finishes", "finished", "has finished", "had finished"],
            "answer": "had finished",
            "explanation": "Dùng Past Perfect để diễn tả hành động xảy ra trước một hành động khác trong quá khứ."
        },
        {
            "question": "They _____ in London for five years before they moved to Paris.",
            "options": ["live", "lived", "have lived", "had lived"],
            "answer": "had lived",
            "explanation": "Dùng Past Perfect để diễn tả hành động kéo dài trước một hành động khác trong quá khứ."
        },
        {
            "question": "The concert _____ at 8 PM tonight.",
            "options": ["starts", "will start", "is starting", "started"],
            "answer": "starts",
            "explanation": "Dùng Present Simple để diễn tả sự kiện theo lịch trình cố định."
        },
        {
            "question": "I _____ my keys everywhere, but I can't find them.",
            "options": ["look for", "looked for", "have been looking for", "had looked for"],
            "answer": "have been looking for",
            "explanation": "Dùng Present Perfect Continuous để nhấn mạnh hành động vừa mới xảy ra và kéo dài."
        },
        {
            "question": "When I was young, I _____ play football every weekend.",
            "options": ["use to", "used to", "am used to", "was used to"],
            "answer": "used to",
            "explanation": "Used to + V: diễn tả thói quen trong quá khứ nhưng không còn nữa."
        },
        {
            "question": "By the end of this year, I _____ English for 10 years.",
            "options": ["learn", "will learn", "will have learned", "will have been learning"],
            "answer": "will have been learning",
            "explanation": "Dùng Future Perfect Continuous với 'by the end of this year' để diễn tả hành động sẽ đang kéo dài đến một thời điểm trong tương lai."
        },
        
        # ==================== PASSIVE VOICE (25 câu) ====================
        {
            "question": "The report _____ by the manager yesterday.",
            "options": ["is completed", "was completed", "has been completed", "completes"],
            "answer": "was completed",
            "explanation": "Dùng Past Simple Passive với 'yesterday' để diễn tả hành động đã hoàn thành trong quá khứ."
        },
        {
            "question": "English _____ in many countries around the world.",
            "options": ["speaks", "is spoken", "was spoken", "has spoken"],
            "answer": "is spoken",
            "explanation": "Dùng Present Simple Passive để diễn tả sự thật chung."
        },
        {
            "question": "A new hospital _____ in our town at the moment.",
            "options": ["builds", "is built", "is being built", "has been built"],
            "answer": "is being built",
            "explanation": "Dùng Present Continuous Passive với 'at the moment' để diễn tả hành động đang xảy ra."
        },
        {
            "question": "The thieves _____ by the police last night.",
            "options": ["catch", "caught", "were caught", "have caught"],
            "answer": "were caught",
            "explanation": "Dùng Past Simple Passive với 'last night'."
        },
        {
            "question": "This book _____ into many languages.",
            "options": ["translates", "translated", "has been translated", "was translating"],
            "answer": "has been translated",
            "explanation": "Dùng Present Perfect Passive để diễn tả hành động đã hoàn thành với kết quả còn liên quan đến hiện tại."
        },
        {
            "question": "The meeting _____ when I arrived.",
            "options": ["was cancelling", "was cancelled", "was being cancelled", "has been cancelled"],
            "answer": "was being cancelled",
            "explanation": "Dùng Past Continuous Passive để diễn tả hành động đang xảy ra tại thời điểm cụ thể trong quá khứ."
        },
        {
            "question": "These cars _____ in Germany.",
            "options": ["make", "made", "are made", "have made"],
            "answer": "are made",
            "explanation": "Dùng Present Simple Passive để diễn tả sự thật chung."
        },
        {
            "question": "The house _____ before we moved in.",
            "options": ["paints", "painted", "was painted", "had been painted"],
            "answer": "had been painted",
            "explanation": "Dùng Past Perfect Passive để diễn tả hành động đã hoàn thành trước một thời điểm trong quá khứ."
        },
        {
            "question": "The letter _____ by tomorrow.",
            "options": ["will send", "will be sent", "sends", "is sent"],
            "answer": "will be sent",
            "explanation": "Dùng Future Simple Passive với 'by tomorrow'."
        },
        {
            "question": "My bicycle _____ stolen yesterday.",
            "options": ["is", "was", "has been", "had been"],
            "answer": "was",
            "explanation": "Dùng Past Simple Passive với 'yesterday'."
        },
        {
            "question": "The problem _____ by the experts now.",
            "options": ["discusses", "is discussing", "is being discussed", "has been discussed"],
            "answer": "is being discussed",
            "explanation": "Dùng Present Continuous Passive với 'now'."
        },
        {
            "question": "This building _____ in 1950.",
            "options": ["built", "was built", "has been built", "is built"],
            "answer": "was built",
            "explanation": "Dùng Past Simple Passive với năm cụ thể trong quá khứ."
        },
        {
            "question": "The dishes _____ by my sister every evening.",
            "options": ["wash", "washes", "are washed", "were washed"],
            "answer": "are washed",
            "explanation": "Dùng Present Simple Passive để diễn tả thói quen."
        },
        {
            "question": "Many accidents _____ by careless driving.",
            "options": ["cause", "caused", "are caused", "have caused"],
            "answer": "are caused",
            "explanation": "Dùng Present Simple Passive để diễn tả sự thật chung."
        },
        {
            "question": "The cake _____ by my mother for my birthday.",
            "options": ["bakes", "baked", "was baked", "has baked"],
            "answer": "was baked",
            "explanation": "Dùng Past Simple Passive để diễn tả hành động đã xảy ra trong quá khứ."
        },
        {
            "question": "A new bridge _____ across the river next year.",
            "options": ["builds", "will build", "will be built", "is built"],
            "answer": "will be built",
            "explanation": "Dùng Future Simple Passive với 'next year'."
        },
        {
            "question": "All the homework must _____ before Friday.",
            "options": ["finish", "be finished", "finished", "finishing"],
            "answer": "be finished",
            "explanation": "Sau modal verb (must) dùng 'be + V3' để tạo câu bị động."
        },
        {
            "question": "The window _____ by the storm last night.",
            "options": ["broke", "was broken", "has broken", "is broken"],
            "answer": "was broken",
            "explanation": "Dùng Past Simple Passive với 'last night'."
        },
        {
            "question": "The poem _____ by a famous poet.",
            "options": ["writes", "wrote", "was written", "has written"],
            "answer": "was written",
            "explanation": "Dùng Past Simple Passive để diễn tả hành động đã xảy ra."
        },
        {
            "question": "The patients _____ by the doctor right now.",
            "options": ["examine", "are examining", "are being examined", "have been examined"],
            "answer": "are being examined",
            "explanation": "Dùng Present Continuous Passive với 'right now'."
        },
        {
            "question": "This song _____ all over the world.",
            "options": ["knows", "is known", "was known", "has known"],
            "answer": "is known",
            "explanation": "Dùng Present Simple Passive để diễn tả sự thật chung."
        },
        {
            "question": "The pyramids _____ thousands of years ago.",
            "options": ["built", "were built", "have been built", "are built"],
            "answer": "were built",
            "explanation": "Dùng Past Simple Passive với 'thousands of years ago'."
        },
        {
            "question": "Her new novel will _____ next month.",
            "options": ["publish", "be published", "published", "publishing"],
            "answer": "be published",
            "explanation": "Sau 'will' dùng 'be + V3' để tạo câu bị động."
        },
        {
            "question": "The flowers should _____ every day.",
            "options": ["water", "be watered", "watered", "watering"],
            "answer": "be watered",
            "explanation": "Sau modal verb (should) dùng 'be + V3' để tạo câu bị động."
        },
        {
            "question": "The documents _____ by the secretary before the meeting.",
            "options": ["prepared", "were prepared", "had been prepared", "are prepared"],
            "answer": "had been prepared",
            "explanation": "Dùng Past Perfect Passive để diễn tả hành động đã hoàn thành trước một thời điểm trong quá khứ."
        },
        
        # ==================== CONDITIONAL SENTENCES (25 câu) ====================
        {
            "question": "If I _____ a millionaire, I would travel around the world.",
            "options": ["am", "was", "were", "will be"],
            "answer": "were",
            "explanation": "Câu điều kiện loại 2: If + S + were/V-ed, S + would + V. Dùng 'were' cho tất cả các ngôi."
        },
        {
            "question": "If it rains tomorrow, we _____ at home.",
            "options": ["stay", "will stay", "would stay", "stayed"],
            "answer": "will stay",
            "explanation": "Câu điều kiện loại 1: If + S + V(s/es), S + will + V."
        },
        {
            "question": "If she had studied harder, she _____ the exam.",
            "options": ["would pass", "will pass", "would have passed", "passed"],
            "answer": "would have passed",
            "explanation": "Câu điều kiện loại 3: If + S + had + V3, S + would have + V3."
        },
        {
            "question": "If I _____ his address, I would send him a letter.",
            "options": ["know", "knew", "will know", "have known"],
            "answer": "knew",
            "explanation": "Câu điều kiện loại 2: If + S + V-ed, S + would + V."
        },
        {
            "question": "Unless you hurry, you _____ the bus.",
            "options": ["will miss", "miss", "would miss", "missed"],
            "answer": "will miss",
            "explanation": "Unless = If...not. Unless you hurry = If you don't hurry, you will miss the bus."
        },
        {
            "question": "If he _____ more carefully, he wouldn't have had an accident.",
            "options": ["drove", "drives", "had driven", "would drive"],
            "answer": "had driven",
            "explanation": "Câu điều kiện loại 3: If + S + had + V3, S + would have + V3."
        },
        {
            "question": "If you mix red and blue, you _____ purple.",
            "options": ["get", "will get", "would get", "got"],
            "answer": "get",
            "explanation": "Câu điều kiện loại 0: If + S + V(s/es), S + V(s/es). Diễn tả chân lý."
        },
        {
            "question": "If I see him tomorrow, I _____ him your message.",
            "options": ["give", "will give", "would give", "gave"],
            "answer": "will give",
            "explanation": "Câu điều kiện loại 1: If + S + V(s/es), S + will + V."
        },
        {
            "question": "She would be healthier if she _____ more vegetables.",
            "options": ["eats", "ate", "will eat", "have eaten"],
            "answer": "ate",
            "explanation": "Câu điều kiện loại 2: If + S + V-ed, S + would + V."
        },
        {
            "question": "If they _____ me, I would have attended the party.",
            "options": ["invited", "had invited", "invite", "have invited"],
            "answer": "had invited",
            "explanation": "Câu điều kiện loại 3: If + S + had + V3, S + would have + V3."
        },
        {
            "question": "If we don't protect the environment, our planet _____ in danger.",
            "options": ["is", "will be", "would be", "were"],
            "answer": "will be",
            "explanation": "Câu điều kiện loại 1: If + S + don't/doesn't + V, S + will + V."
        },
        {
            "question": "If you _____ the instructions, you wouldn't have made mistakes.",
            "options": ["followed", "had followed", "follow", "would follow"],
            "answer": "had followed",
            "explanation": "Câu điều kiện loại 3: If + S + had + V3, S + would have + V3."
        },
        {
            "question": "If I were you, I _____ that job offer.",
            "options": ["will accept", "would accept", "accept", "accepted"],
            "answer": "would accept",
            "explanation": "Câu điều kiện loại 2 dùng để khuyên: If I were you, I would + V."
        },
        {
            "question": "You _____ healthier if you exercise regularly.",
            "options": ["are", "will be", "would be", "were"],
            "answer": "will be",
            "explanation": "Câu điều kiện loại 1: If + S + V(s/es), S + will + V (có thể đảo vế)."
        },
        {
            "question": "If she had enough money, she _____ a new car.",
            "options": ["buys", "will buy", "would buy", "bought"],
            "answer": "would buy",
            "explanation": "Câu điều kiện loại 2: If + S + V-ed, S + would + V."
        },
        {
            "question": "If you _____ harder, you will pass the exam.",
            "options": ["study", "studied", "will study", "would study"],
            "answer": "study",
            "explanation": "Câu điều kiện loại 1: If + S + V(s/es), S + will + V."
        },
        {
            "question": "If I had known about the meeting, I _____ attended.",
            "options": ["will have", "would have", "have", "had"],
            "answer": "would have",
            "explanation": "Câu điều kiện loại 3: If + S + had + V3, S + would have + V3."
        },
        {
            "question": "Water _____ if you heat it to 100 degrees Celsius.",
            "options": ["boils", "will boil", "would boil", "boiled"],
            "answer": "boils",
            "explanation": "Câu điều kiện loại 0: If + S + V(s/es), S + V(s/es)."
        },
        {
            "question": "If it _____ tomorrow, we will cancel the picnic.",
            "options": ["rains", "rained", "will rain", "would rain"],
            "answer": "rains",
            "explanation": "Câu điều kiện loại 1: If + S + V(s/es), S + will + V."
        },
        {
            "question": "He would have passed the test if he _____ more.",
            "options": ["studies", "studied", "had studied", "would study"],
            "answer": "had studied",
            "explanation": "Câu điều kiện loại 3: If + S + had + V3, S + would have + V3."
        },
        {
            "question": "If you _____ me earlier, I could have helped you.",
            "options": ["tell", "told", "had told", "would tell"],
            "answer": "had told",
            "explanation": "Câu điều kiện loại 3: If + S + had + V3, S + could have + V3."
        },
        {
            "question": "If she were taller, she _____ a model.",
            "options": ["becomes", "will become", "would become", "became"],
            "answer": "would become",
            "explanation": "Câu điều kiện loại 2: If + S + were, S + would + V."
        },
        {
            "question": "If you don't leave now, you _____ late.",
            "options": ["are", "will be", "would be", "were"],
            "answer": "will be",
            "explanation": "Câu điều kiện loại 1: If + S + don't + V, S + will + V."
        },
        {
            "question": "If I had wings, I _____ fly.",
            "options": ["can", "will", "could", "would"],
            "answer": "could",
            "explanation": "Câu điều kiện loại 2: If + S + V-ed, S + could/would + V."
        },
        {
            "question": "If they had arrived earlier, they _____ the beginning of the show.",
            "options": ["saw", "would see", "would have seen", "will see"],
            "answer": "would have seen",
            "explanation": "Câu điều kiện loại 3: If + S + had + V3, S + would have + V3."
        },
        
        # ==================== RELATIVE CLAUSES (25 câu) ====================
        {
            "question": "The man _____ is talking to my father is a famous doctor.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "who",
            "explanation": "Dùng 'who' thay cho người (the man) làm chủ ngữ."
        },
        {
            "question": "The book _____ I bought yesterday is very interesting.",
            "options": ["who", "which", "whose", "where"],
            "answer": "which",
            "explanation": "Dùng 'which' thay cho vật (the book). Có thể bỏ 'which' vì làm tân ngữ."
        },
        {
            "question": "This is the school _____ I studied when I was young.",
            "options": ["which", "where", "when", "who"],
            "answer": "where",
            "explanation": "Dùng 'where' thay cho địa điểm (at the school)."
        },
        {
            "question": "The woman _____ car was stolen called the police.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "whose",
            "explanation": "Dùng 'whose' để chỉ sở hữu (car của woman)."
        },
        {
            "question": "Do you remember the day _____ we first met?",
            "options": ["which", "where", "when", "who"],
            "answer": "when",
            "explanation": "Dùng 'when' thay cho thời gian (on the day)."
        },
        {
            "question": "The people _____ I met at the party were very friendly.",
            "options": ["who", "whom", "which", "whose"],
            "answer": "whom",
            "explanation": "Dùng 'whom' thay cho người làm tân ngữ. Trong văn nói có thể dùng 'who'."
        },
        {
            "question": "I like movies _____ have happy endings.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "which",
            "explanation": "Dùng 'which' thay cho vật (movies) làm chủ ngữ."
        },
        {
            "question": "The reason _____ he was late is still unknown.",
            "options": ["which", "why", "when", "where"],
            "answer": "why",
            "explanation": "Dùng 'why' thay cho lý do (for the reason)."
        },
        {
            "question": "The students _____ work hard will succeed.",
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
            "question": "The laptop _____ she bought is very expensive.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "which",
            "explanation": "Dùng 'which' thay cho vật (the laptop)."
        },
        {
            "question": "The boy _____ mother is a teacher is my friend.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "whose",
            "explanation": "Dùng 'whose' để chỉ sở hữu (mother của boy)."
        },
        {
            "question": "2020 was the year _____ the pandemic began.",
            "options": ["which", "where", "when", "who"],
            "answer": "when",
            "explanation": "Dùng 'when' thay cho năm/thời gian (in 2020)."
        },
        {
            "question": "The teacher _____ teaches us English is very kind.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "who",
            "explanation": "Dùng 'who' thay cho người (the teacher) làm chủ ngữ."
        },
        {
            "question": "This is the place _____ we spent our honeymoon.",
            "options": ["which", "where", "when", "who"],
            "answer": "where",
            "explanation": "Dùng 'where' thay cho địa điểm (at the place)."
        },
        {
            "question": "The professor _____ I admire most has just retired.",
            "options": ["who", "whom", "which", "whose"],
            "answer": "whom",
            "explanation": "Dùng 'whom' thay cho người làm tân ngữ."
        },
        {
            "question": "The dog _____ bit me belongs to my neighbor.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "which",
            "explanation": "Dùng 'which' thay cho động vật (the dog) làm chủ ngữ."
        },
        {
            "question": "The hotel _____ we stayed was very comfortable.",
            "options": ["which", "where", "when", "who"],
            "answer": "where",
            "explanation": "Dùng 'where' thay cho địa điểm (at the hotel)."
        },
        {
            "question": "The movie _____ we watched last week was boring.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "which",
            "explanation": "Dùng 'which' thay cho vật (the movie)."
        },
        {
            "question": "The girl _____ you were talking about is my sister.",
            "options": ["who", "whom", "which", "whose"],
            "answer": "whom",
            "explanation": "Dùng 'whom' thay cho người làm tân ngữ của giới từ."
        },
        {
            "question": "I'll never forget the moment _____ I first saw her.",
            "options": ["which", "where", "when", "who"],
            "answer": "when",
            "explanation": "Dùng 'when' thay cho thời điểm (at the moment)."
        },
        {
            "question": "The company _____ he works for is very successful.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "which",
            "explanation": "Dùng 'which' thay cho vật (the company)."
        },
        {
            "question": "The house _____ windows are broken is abandoned.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "whose",
            "explanation": "Dùng 'whose' để chỉ sở hữu (windows của house)."
        },
        {
            "question": "That's the man _____ daughter won the competition.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "whose",
            "explanation": "Dùng 'whose' để chỉ sở hữu (daughter của man)."
        },
        {
            "question": "The city _____ I was born has changed a lot.",
            "options": ["which", "where", "when", "who"],
            "answer": "where",
            "explanation": "Dùng 'where' thay cho địa điểm (in the city)."
        },
        
        # ==================== REPORTED SPEECH (20 câu) ====================
        {
            "question": "She said, 'I am tired.' → She said she _____ tired.",
            "options": ["is", "was", "has been", "will be"],
            "answer": "was",
            "explanation": "Trong câu tường thuật, 'am/is' đổi thành 'was'."
        },
        {
            "question": "'I will help you,' he said. → He said he _____ me.",
            "options": ["will help", "would help", "helped", "helps"],
            "answer": "would help",
            "explanation": "Trong câu tường thuật, 'will' đổi thành 'would'."
        },
        {
            "question": "'Where do you live?' she asked. → She asked me where _____.",
            "options": ["do I live", "I lived", "did I live", "I live"],
            "answer": "I lived",
            "explanation": "Câu hỏi tường thuật: asked + wh-word + S + V (lùi thì)."
        },
        {
            "question": "'Don't be late!' she told me. → She told me _____ late.",
            "options": ["don't be", "not to be", "not be", "to not be"],
            "answer": "not to be",
            "explanation": "Câu mệnh lệnh phủ định tường thuật: told + O + not to V."
        },
        {
            "question": "'I have finished my work,' Tom said. → Tom said he _____ his work.",
            "options": ["has finished", "had finished", "finished", "finishes"],
            "answer": "had finished",
            "explanation": "Present Perfect → Past Perfect trong câu tường thuật."
        },
        {
            "question": "'Can you help me?' she asked. → She asked if I _____ help her.",
            "options": ["can", "could", "will", "would"],
            "answer": "could",
            "explanation": "Câu hỏi Yes/No tường thuật: asked if + S + V (lùi thì). 'Can' → 'could'."
        },
        {
            "question": "'I saw him yesterday,' she said. → She said she _____ him the day before.",
            "options": ["sees", "saw", "had seen", "has seen"],
            "answer": "had seen",
            "explanation": "Past Simple → Past Perfect, 'yesterday' → 'the day before'."
        },
        {
            "question": "'Close the door!' the teacher said. → The teacher told us _____ the door.",
            "options": ["close", "to close", "closing", "closed"],
            "answer": "to close",
            "explanation": "Câu mệnh lệnh khẳng định tường thuật: told + O + to V."
        },
        {
            "question": "'I am reading a book,' Mary said. → Mary said she _____ a book.",
            "options": ["is reading", "was reading", "reads", "read"],
            "answer": "was reading",
            "explanation": "Present Continuous → Past Continuous trong câu tường thuật."
        },
        {
            "question": "'What time is it?' he asked. → He asked what time _____.",
            "options": ["is it", "it was", "was it", "it is"],
            "answer": "it was",
            "explanation": "Câu hỏi tường thuật: asked + wh-word + S + V (lùi thì)."
        },
        {
            "question": "'I have never been to Paris,' he said. → He said he _____ to Paris.",
            "options": ["has never been", "had never been", "never was", "was never"],
            "answer": "had never been",
            "explanation": "Present Perfect → Past Perfect trong câu tường thuật."
        },
        {
            "question": "'Please help me,' she said. → She asked me _____ her.",
            "options": ["help", "to help", "helping", "helped"],
            "answer": "to help",
            "explanation": "Câu yêu cầu lịch sự tường thuật: asked + O + to V."
        },
        {
            "question": "'I will be here at 5 PM,' he said. → He said he _____ there at 5 PM.",
            "options": ["will be", "would be", "is", "was"],
            "answer": "would be",
            "explanation": "'Will' → 'would', 'here' → 'there' trong câu tường thuật."
        },
        {
            "question": "'Are you coming to the party?' she asked. → She asked if I _____ to the party.",
            "options": ["am coming", "was coming", "come", "came"],
            "answer": "was coming",
            "explanation": "Câu hỏi Yes/No tường thuật: asked if + S + V (lùi thì)."
        },
        {
            "question": "'I may visit you tomorrow,' he said. → He said he _____ visit me the next day.",
            "options": ["may", "might", "can", "could"],
            "answer": "might",
            "explanation": "'May' → 'might', 'tomorrow' → 'the next day'."
        },
        {
            "question": "'Don't touch that!' he said. → He told me _____ that.",
            "options": ["don't touch", "not to touch", "not touch", "to not touch"],
            "answer": "not to touch",
            "explanation": "Câu mệnh lệnh phủ định tường thuật: told + O + not to V."
        },
        {
            "question": "'I bought a car last week,' John said. → John said he _____ a car the week before.",
            "options": ["bought", "had bought", "buys", "has bought"],
            "answer": "had bought",
            "explanation": "Past Simple → Past Perfect, 'last week' → 'the week before'."
        },
        {
            "question": "'How old are you?' she asked. → She asked me how old _____.",
            "options": ["am I", "I was", "was I", "I am"],
            "answer": "I was",
            "explanation": "Câu hỏi tường thuật: asked + wh-word + S + V (lùi thì)."
        },
        {
            "question": "'I must finish this today,' she said. → She said she _____ finish that that day.",
            "options": ["must", "had to", "has to", "have to"],
            "answer": "had to",
            "explanation": "'Must' → 'had to', 'this' → 'that', 'today' → 'that day'."
        },
        {
            "question": "'Study hard!' the teacher said. → The teacher told us _____ hard.",
            "options": ["study", "to study", "studying", "studied"],
            "answer": "to study",
            "explanation": "Câu mệnh lệnh khẳng định tường thuật: told + O + to V."
        },
        
        # ==================== MODAL VERBS (20 câu) ====================
        {
            "question": "You _____ smoke in the hospital. It's not allowed.",
            "options": ["mustn't", "don't have to", "needn't", "shouldn't"],
            "answer": "mustn't",
            "explanation": "Mustn't = không được phép (cấm đoán)."
        },
        {
            "question": "She _____ speak three languages fluently.",
            "options": ["can", "must", "should", "would"],
            "answer": "can",
            "explanation": "Can = có khả năng làm gì."
        },
        {
            "question": "You _____ come to the party if you don't want to.",
            "options": ["mustn't", "don't have to", "can't", "shouldn't"],
            "answer": "don't have to",
            "explanation": "Don't have to = không cần thiết (không bắt buộc)."
        },
        {
            "question": "You _____ respect your parents and teachers.",
            "options": ["can", "must", "may", "might"],
            "answer": "must",
            "explanation": "Must = phải (bổn phận, quy tắc đạo đức)."
        },
        {
            "question": "She _____ be at home now. I saw her car outside.",
            "options": ["can", "must", "may", "might"],
            "answer": "must",
            "explanation": "Must = chắc hẳn là (suy đoán logic với cơ sở)."
        },
        {
            "question": "_____ I borrow your pen, please?",
            "options": ["Can", "Must", "Should", "Would"],
            "answer": "Can",
            "explanation": "Can I...? = xin phép lịch sự (có thể dùng May I...? trang trọng hơn)."
        },
        {
            "question": "You _____ eat more vegetables. They're good for your health.",
            "options": ["can", "must", "should", "would"],
            "answer": "should",
            "explanation": "Should = nên (lời khuyên)."
        },
        {
            "question": "It _____ rain later. The sky is very cloudy.",
            "options": ["can", "must", "may", "shall"],
            "answer": "may",
            "explanation": "May/Might = có thể (khả năng xảy ra)."
        },
        {
            "question": "I _____ swim when I was five years old.",
            "options": ["can", "could", "may", "might"],
            "answer": "could",
            "explanation": "Could = có khả năng trong quá khứ."
        },
        {
            "question": "You _____ have told me earlier!",
            "options": ["can", "must", "should", "would"],
            "answer": "should",
            "explanation": "Should have + V3 = đáng lẽ nên làm gì (nhưng đã không làm)."
        },
        {
            "question": "Students _____ wear uniforms at school.",
            "options": ["can", "must", "may", "might"],
            "answer": "must",
            "explanation": "Must = phải (quy định bắt buộc)."
        },
        {
            "question": "_____ you help me with this exercise?",
            "options": ["Can", "Must", "Should", "Shall"],
            "answer": "Can",
            "explanation": "Can you...? = nhờ ai làm gì (lịch sự)."
        },
        {
            "question": "He _____ be tired. He has been working all day.",
            "options": ["can", "must", "may", "might"],
            "answer": "must",
            "explanation": "Must = chắc hẳn là (suy đoán với cơ sở chắc chắn)."
        },
        {
            "question": "You _____ drive without a license. It's illegal.",
            "options": ["mustn't", "don't have to", "needn't", "shouldn't"],
            "answer": "mustn't",
            "explanation": "Mustn't = không được phép (cấm theo luật)."
        },
        {
            "question": "I _____ like to have a cup of coffee, please.",
            "options": ["can", "must", "would", "should"],
            "answer": "would",
            "explanation": "Would like = muốn (lịch sự, trang trọng)."
        },
        {
            "question": "You _____ finish your homework before playing games.",
            "options": ["can", "must", "may", "might"],
            "answer": "must",
            "explanation": "Must = phải (bổn phận)."
        },
        {
            "question": "She _____ be in the office. I'm not sure.",
            "options": ["can", "must", "may", "shall"],
            "answer": "may",
            "explanation": "May/Might = có thể (không chắc chắn)."
        },
        {
            "question": "_____ I use your phone to make a call?",
            "options": ["Can", "Must", "Should", "Would"],
            "answer": "Can",
            "explanation": "Can I...? = xin phép lịch sự."
        },
        {
            "question": "You _____ have studied harder for the exam.",
            "options": ["can", "must", "should", "would"],
            "answer": "should",
            "explanation": "Should have + V3 = đáng lẽ nên (hối tiếc việc đã không làm)."
        },
        {
            "question": "We _____ leave now or we'll miss the train.",
            "options": ["can", "must", "may", "might"],
            "answer": "must",
            "explanation": "Must = phải (cần thiết khẩn cấp)."
        },
        
        # ==================== VOCABULARY & WORD FORMATION (25 câu) ====================
        {
            "question": "The internet is a very useful means of _____.",
            "options": ["communication", "communicative", "communicate", "communicator"],
            "answer": "communication",
            "explanation": "Cần danh từ sau 'means of'. Communication = sự giao tiếp."
        },
        {
            "question": "She speaks English _____, so everyone can understand her.",
            "options": ["fluent", "fluently", "fluency", "fluentness"],
            "answer": "fluently",
            "explanation": "Cần trạng từ bổ nghĩa cho động từ 'speaks'. Fluently = trôi chảy."
        },
        {
            "question": "We need to _____ our knowledge of technology.",
            "options": ["improve", "improvement", "improved", "improving"],
            "answer": "improve",
            "explanation": "Sau 'need to' dùng động từ nguyên mẫu. Improve = cải thiện."
        },
        {
            "question": "The _____ of the environment is everyone's responsibility.",
            "options": ["protect", "protection", "protective", "protector"],
            "answer": "protection",
            "explanation": "Cần danh từ làm chủ ngữ. Protection = sự bảo vệ."
        },
        {
            "question": "He is a very _____ person. He always tries his best.",
            "options": ["industry", "industrial", "industrious", "industrially"],
            "answer": "industrious",
            "explanation": "Cần tính từ bổ nghĩa cho danh từ 'person'. Industrious = cần cù, chăm chỉ."
        },
        {
            "question": "The _____ of the internet has changed our lives completely.",
            "options": ["invent", "invention", "inventor", "inventive"],
            "answer": "invention",
            "explanation": "Cần danh từ làm chủ ngữ. Invention = phát minh."
        },
        {
            "question": "She made a _____ to study abroad.",
            "options": ["decide", "decision", "decisive", "decided"],
            "answer": "decision",
            "explanation": "Cần danh từ sau 'made a'. Decision = quyết định."
        },
        {
            "question": "The teacher gave us a _____ explanation.",
            "options": ["clear", "clearly", "clearness", "clarity"],
            "answer": "clear",
            "explanation": "Cần tính từ bổ nghĩa cho danh từ 'explanation'. Clear = rõ ràng."
        },
        {
            "question": "Tourism has _____ rapidly in recent years.",
            "options": ["develop", "developed", "development", "developing"],
            "answer": "developed",
            "explanation": "Cần động từ chia Present Perfect với 'has'. Developed = phát triển."
        },
        {
            "question": "She is very _____ about her future career.",
            "options": ["optimism", "optimist", "optimistic", "optimistically"],
            "answer": "optimistic",
            "explanation": "Cần tính từ sau 'is very'. Optimistic = lạc quan."
        },
        {
            "question": "The _____ between rich and poor is increasing.",
            "options": ["differ", "different", "difference", "differently"],
            "answer": "difference",
            "explanation": "Cần danh từ làm chủ ngữ. Difference = sự khác biệt."
        },
        {
            "question": "He is _____ for his children's education.",
            "options": ["response", "responsible", "responsibility", "responsibly"],
            "answer": "responsible",
            "explanation": "Cần tính từ sau 'is'. Responsible for = chịu trách nhiệm về."
        },
        {
            "question": "The company has made a large _____ in the project.",
            "options": ["invest", "investment", "investor", "invested"],
            "answer": "investment",
            "explanation": "Cần danh từ sau 'a large'. Investment = sự đầu tư."
        },
        {
            "question": "We should _____ natural resources.",
            "options": ["conservation", "conserve", "conservative", "conservatively"],
            "answer": "conserve",
            "explanation": "Sau 'should' dùng động từ nguyên mẫu. Conserve = bảo tồn."
        },
        {
            "question": "The _____ of clean water is a global problem.",
            "options": ["short", "shortage", "shorten", "shortly"],
            "answer": "shortage",
            "explanation": "Cần danh từ làm chủ ngữ. Shortage = sự thiếu hụt."
        },
        {
            "question": "She is _____ of her son's achievements.",
            "options": ["pride", "proud", "proudly", "proudness"],
            "answer": "proud",
            "explanation": "Cần tính từ sau 'is'. Proud of = tự hào về."
        },
        {
            "question": "The _____ of this building took three years.",
            "options": ["construct", "construction", "constructive", "constructor"],
            "answer": "construction",
            "explanation": "Cần danh từ làm chủ ngữ. Construction = sự xây dựng."
        },
        {
            "question": "He spoke _____ about his experience.",
            "options": ["enthusiasm", "enthusiast", "enthusiastic", "enthusiastically"],
            "answer": "enthusiastically",
            "explanation": "Cần trạng từ bổ nghĩa cho động từ 'spoke'. Enthusiastically = một cách nhiệt tình."
        },
        {
            "question": "The _____ of the product depends on its quality.",
            "options": ["succeed", "success", "successful", "successfully"],
            "answer": "success",
            "explanation": "Cần danh từ làm chủ ngữ. Success = sự thành công."
        },
        {
            "question": "We need to find a _____ to this problem.",
            "options": ["solve", "solution", "solvable", "solving"],
            "answer": "solution",
            "explanation": "Cần danh từ sau 'a'. Solution = giải pháp."
        },
        {
            "question": "She is a very _____ student.",
            "options": ["intelligence", "intelligent", "intelligently", "intelligentsia"],
            "answer": "intelligent",
            "explanation": "Cần tính từ bổ nghĩa cho danh từ 'student'. Intelligent = thông minh."
        },
        {
            "question": "The _____ of the program was excellent.",
            "options": ["organize", "organization", "organizational", "organizer"],
            "answer": "organization",
            "explanation": "Cần danh từ làm chủ ngữ. Organization = sự tổ chức."
        },
        {
            "question": "He _____ apologized for his mistake.",
            "options": ["sincere", "sincerely", "sincerity", "sincereness"],
            "answer": "sincerely",
            "explanation": "Cần trạng từ bổ nghĩa cho động từ 'apologized'. Sincerely = một cách chân thành."
        },
        {
            "question": "The _____ system in Vietnam is improving.",
            "options": ["educate", "education", "educational", "educated"],
            "answer": "education",
            "explanation": "Cần danh từ bổ nghĩa cho 'system'. Education = giáo dục."
        },
        {
            "question": "She made a _____ recovery after the surgery.",
            "options": ["miracle", "miraculous", "miraculously", "miracles"],
            "answer": "miraculous",
            "explanation": "Cần tính từ bổ nghĩa cho danh từ 'recovery'. Miraculous = kỳ diệu."
        },
        
        # ==================== PREPOSITIONS (15 câu) ====================
        {
            "question": "She is interested _____ learning foreign languages.",
            "options": ["in", "on", "at", "for"],
            "answer": "in",
            "explanation": "Be interested in + V-ing/N: quan tâm đến."
        },
        {
            "question": "He is good _____ playing the guitar.",
            "options": ["in", "at", "on", "for"],
            "answer": "at",
            "explanation": "Be good at + V-ing/N: giỏi về."
        },
        {
            "question": "We arrived _____ London at midnight.",
            "options": ["in", "on", "at", "to"],
            "answer": "in",
            "explanation": "Arrive in + thành phố lớn, quốc gia."
        },
        {
            "question": "My birthday is _____ June 15th.",
            "options": ["in", "on", "at", "for"],
            "answer": "on",
            "explanation": "On + ngày cụ thể."
        },
        {
            "question": "She has lived here _____ 2010.",
            "options": ["since", "for", "during", "from"],
            "answer": "since",
            "explanation": "Since + mốc thời gian."
        },
        {
            "question": "We have been friends _____ ten years.",
            "options": ["since", "for", "during", "from"],
            "answer": "for",
            "explanation": "For + khoảng thời gian."
        },
        {
            "question": "He is afraid _____ heights.",
            "options": ["of", "at", "in", "for"],
            "answer": "of",
            "explanation": "Be afraid of + N: sợ cái gì."
        },
        {
            "question": "She is responsible _____ organizing the event.",
            "options": ["for", "of", "to", "with"],
            "answer": "for",
            "explanation": "Be responsible for + V-ing/N: chịu trách nhiệm về."
        },
        {
            "question": "The meeting will start _____ 2 PM.",
            "options": ["in", "on", "at", "for"],
            "answer": "at",
            "explanation": "At + giờ cụ thể."
        },
        {
            "question": "She succeeded _____ passing the exam.",
            "options": ["in", "on", "at", "for"],
            "answer": "in",
            "explanation": "Succeed in + V-ing: thành công trong việc gì."
        },
        {
            "question": "They went to school _____ bus.",
            "options": ["by", "on", "in", "with"],
            "answer": "by",
            "explanation": "By + phương tiện (không có 'the')."
        },
        {
            "question": "She is famous _____ her beautiful voice.",
            "options": ["for", "of", "at", "in"],
            "answer": "for",
            "explanation": "Be famous for + N: nổi tiếng về."
        },
        {
            "question": "He apologized _____ his behavior.",
            "options": ["for", "of", "to", "with"],
            "answer": "for",
            "explanation": "Apologize for + N: xin lỗi về."
        },
        {
            "question": "I am looking forward _____ seeing you again.",
            "options": ["to", "for", "at", "in"],
            "answer": "to",
            "explanation": "Look forward to + V-ing: mong chờ."
        },
        {
            "question": "She depends _____ her parents for financial support.",
            "options": ["on", "in", "at", "for"],
            "answer": "on",
            "explanation": "Depend on + N: phụ thuộc vào."
        },
        
        # ==================== PHRASAL VERBS (15 câu) ====================
        {
            "question": "Please _____ your shoes before entering the house.",
            "options": ["take off", "take on", "take up", "take over"],
            "answer": "take off",
            "explanation": "Take off = cởi (giày, quần áo)."
        },
        {
            "question": "I need to _____ some information for my project.",
            "options": ["look up", "look after", "look for", "look into"],
            "answer": "look up",
            "explanation": "Look up = tra cứu (thông tin)."
        },
        {
            "question": "She decided to _____ smoking for her health.",
            "options": ["give up", "give in", "give away", "give back"],
            "answer": "give up",
            "explanation": "Give up = từ bỏ (thói quen)."
        },
        {
            "question": "The plane will _____ at 6 AM.",
            "options": ["take off", "take on", "take up", "take away"],
            "answer": "take off",
            "explanation": "Take off = cất cánh (máy bay)."
        },
        {
            "question": "Could you _____ my dog while I'm on vacation?",
            "options": ["look up", "look after", "look for", "look at"],
            "answer": "look after",
            "explanation": "Look after = chăm sóc."
        },
        {
            "question": "The meeting has been _____ until next Monday.",
            "options": ["put off", "put on", "put up", "put down"],
            "answer": "put off",
            "explanation": "Put off = hoãn lại."
        },
        {
            "question": "I'm _____ my glasses. Have you seen them?",
            "options": ["looking up", "looking after", "looking for", "looking at"],
            "answer": "looking for",
            "explanation": "Look for = tìm kiếm."
        },
        {
            "question": "She _____ well with her colleagues.",
            "options": ["gets on", "gets off", "gets up", "gets over"],
            "answer": "gets on",
            "explanation": "Get on with = có quan hệ tốt với."
        },
        {
            "question": "Please _____ this form before submitting it.",
            "options": ["fill in", "fill up", "fill out", "fill with"],
            "answer": "fill in",
            "explanation": "Fill in = điền vào (mẫu đơn)."
        },
        {
            "question": "He _____ at 6 AM every morning.",
            "options": ["gets up", "gets on", "gets off", "gets over"],
            "answer": "gets up",
            "explanation": "Get up = thức dậy."
        },
        {
            "question": "Can you _____ the music? It's too loud.",
            "options": ["turn up", "turn down", "turn on", "turn off"],
            "answer": "turn down",
            "explanation": "Turn down = giảm (âm lượng)."
        },
        {
            "question": "I _____ an old friend at the supermarket.",
            "options": ["ran into", "ran over", "ran out", "ran away"],
            "answer": "ran into",
            "explanation": "Run into = tình cờ gặp."
        },
        {
            "question": "They had to _____ the concert because of bad weather.",
            "options": ["call off", "call on", "call up", "call for"],
            "answer": "call off",
            "explanation": "Call off = hủy bỏ."
        },
        {
            "question": "She needs to _____ her old clothes.",
            "options": ["throw away", "throw up", "throw out", "throw off"],
            "answer": "throw away",
            "explanation": "Throw away = vứt bỏ."
        },
        {
            "question": "I can't _____ with his bad behavior anymore.",
            "options": ["put up", "put off", "put on", "put down"],
            "answer": "put up",
            "explanation": "Put up with = chịu đựng."
        }
]