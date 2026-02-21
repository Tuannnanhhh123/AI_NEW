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
  # ==================== TENSES ADVANCED (25 câu) ====================
        {
            "question": "By the time we arrive, the movie _____ for 30 minutes.",
            "options": ["will start", "will be starting", "will have been starting", "will have started"],
            "answer": "will have started",
            "explanation": "Future Perfect: By the time + S + V(hiện tại), S + will have + V3. Diễn tả hành động sẽ hoàn thành trước một thời điểm trong tương lai."
        },
        {
            "question": "She _____ for the company for ten years before she decided to retire.",
            "options": ["works", "worked", "has worked", "had been working"],
            "answer": "had been working",
            "explanation": "Past Perfect Continuous: nhấn mạnh hành động kéo dài liên tục trước một thời điểm trong quá khứ."
        },
        {
            "question": "I _____ three reports this morning and I'm exhausted.",
            "options": ["write", "wrote", "have written", "have been writing"],
            "answer": "have been writing",
            "explanation": "Present Perfect Continuous: nhấn mạnh hành động vừa mới kết thúc và gây ra kết quả hiện tại (exhausted)."
        },
        {
            "question": "When I got to the cinema, the film _____.",
            "options": ["already started", "has already started", "had already started", "was already starting"],
            "answer": "had already started",
            "explanation": "Past Perfect: hành động xảy ra trước một hành động khác trong quá khứ."
        },
        {
            "question": "This time tomorrow, I _____ on a beach in Hawaii.",
            "options": ["lie", "will lie", "will be lying", "will have lain"],
            "answer": "will be lying",
            "explanation": "Future Continuous với 'this time tomorrow': hành động sẽ đang xảy ra tại thời điểm cụ thể trong tương lai."
        },
        {
            "question": "They _____ in Paris for five years when they decided to move to London.",
            "options": ["lived", "have lived", "had lived", "had been living"],
            "answer": "had been living",
            "explanation": "Past Perfect Continuous: hành động kéo dài liên tục trước một thời điểm trong quá khứ."
        },
        {
            "question": "I _____ this book three times already.",
            "options": ["read", "have read", "am reading", "had read"],
            "answer": "have read",
            "explanation": "Present Perfect với 'already': diễn tả kinh nghiệm đã làm nhiều lần."
        },
        {
            "question": "She _____ for two hours when her friend arrived.",
            "options": ["waited", "was waiting", "has waited", "had been waiting"],
            "answer": "had been waiting",
            "explanation": "Past Perfect Continuous: hành động đang kéo dài trước một thời điểm trong quá khứ."
        },
        {
            "question": "By 2030, scientists _____ a cure for many diseases.",
            "options": ["discover", "will discover", "will have discovered", "will be discovering"],
            "answer": "will have discovered",
            "explanation": "Future Perfect với 'by 2030': hành động sẽ hoàn thành trước một thời điểm trong tương lai."
        },
        {
            "question": "He _____ TV when the phone rang.",
            "options": ["watches", "watched", "was watching", "has watched"],
            "answer": "was watching",
            "explanation": "Past Continuous: hành động đang xảy ra thì có hành động khác xen vào."
        },
        {
            "question": "I _____ English since I was six years old.",
            "options": ["learn", "learned", "have been learning", "had been learning"],
            "answer": "have been learning",
            "explanation": "Present Perfect Continuous với 'since': hành động bắt đầu từ quá khứ và vẫn tiếp tục."
        },
        {
            "question": "She said that she _____ the report the following day.",
            "options": ["will finish", "would finish", "finished", "finishes"],
            "answer": "would finish",
            "explanation": "Reported speech: will → would, tomorrow → the following day."
        },
        {
            "question": "They _____ for three hours before they found the solution.",
            "options": ["discussed", "were discussing", "have discussed", "had been discussing"],
            "answer": "had been discussing",
            "explanation": "Past Perfect Continuous: hành động kéo dài trước một thời điểm trong quá khứ."
        },
        {
            "question": "By the end of this month, I _____ here for exactly two years.",
            "options": ["work", "will work", "will have worked", "will have been working"],
            "answer": "will have been working",
            "explanation": "Future Perfect Continuous: hành động sẽ đang kéo dài đến một thời điểm trong tương lai."
        },
        {
            "question": "It's the first time I _____ such a beautiful sunset.",
            "options": ["see", "saw", "have seen", "had seen"],
            "answer": "have seen",
            "explanation": "It's the first time + Present Perfect: diễn tả kinh nghiệm lần đầu."
        },
        {
            "question": "She _____ when I called her last night.",
            "options": ["sleeps", "slept", "was sleeping", "has slept"],
            "answer": "was sleeping",
            "explanation": "Past Continuous: hành động đang xảy ra tại thời điểm cụ thể trong quá khứ."
        },
        {
            "question": "I _____ for the bus for over an hour. Where is it?",
            "options": ["wait", "waited", "have waited", "have been waiting"],
            "answer": "have been waiting",
            "explanation": "Present Perfect Continuous: nhấn mạnh hành động vừa mới xảy ra và kéo dài."
        },
        {
            "question": "Before I moved to the city, I _____ in a small village.",
            "options": ["live", "lived", "have lived", "had lived"],
            "answer": "had lived",
            "explanation": "Past Perfect: hành động xảy ra trước một hành động khác trong quá khứ."
        },
        {
            "question": "This time next year, we _____ our new house.",
            "options": ["build", "will build", "will be building", "will have built"],
            "answer": "will have built",
            "explanation": "Future Perfect: hành động sẽ hoàn thành trước một thời điểm trong tương lai."
        },
        {
            "question": "She _____ tennis every weekend when she was younger.",
            "options": ["plays", "played", "was playing", "used to play"],
            "answer": "used to play",
            "explanation": "Used to + V: thói quen trong quá khứ nhưng không còn nữa."
        },
        {
            "question": "By the time you read this letter, I _____ the country.",
            "options": ["leave", "will leave", "will have left", "am leaving"],
            "answer": "will have left",
            "explanation": "Future Perfect: By the time + hiện tại, S + will have + V3."
        },
        {
            "question": "I _____ my homework when you called me.",
            "options": ["do", "did", "was doing", "have done"],
            "answer": "was doing",
            "explanation": "Past Continuous: hành động đang xảy ra khi có hành động khác xen vào."
        },
        {
            "question": "She _____ abroad before, so she was very excited.",
            "options": ["never travels", "never traveled", "has never traveled", "had never traveled"],
            "answer": "had never traveled",
            "explanation": "Past Perfect: diễn tả kinh nghiệm trước một thời điểm trong quá khứ."
        },
        {
            "question": "I _____ this movie several times, but I still enjoy it.",
            "options": ["watch", "watched", "have watched", "had watched"],
            "answer": "have watched",
            "explanation": "Present Perfect: diễn tả kinh nghiệm đã làm nhiều lần."
        },
        {
            "question": "They _____ dinner when we arrived.",
            "options": ["have", "had", "were having", "have had"],
            "answer": "were having",
            "explanation": "Past Continuous: hành động đang xảy ra khi có hành động khác xen vào."
        },
        
        # ==================== PERFECT MODALS (20 câu) ====================
        {
            "question": "She _____ the meeting. Her car was parked outside.",
            "options": ["must attend", "must have attended", "should attend", "should have attended"],
            "answer": "must have attended",
            "explanation": "Must have + V3: chắc hẳn đã (suy đoán về quá khứ với cơ sở chắc chắn)."
        },
        {
            "question": "You _____ me earlier. I could have helped you.",
            "options": ["should tell", "should have told", "must tell", "must have told"],
            "answer": "should have told",
            "explanation": "Should have + V3: đáng lẽ nên làm (nhưng đã không làm - hối tiếc)."
        },
        {
            "question": "He _____ the exam. He studied very hard.",
            "options": ["may pass", "may have passed", "must pass", "must have passed"],
            "answer": "may have passed",
            "explanation": "May have + V3: có thể đã (suy đoán không chắc chắn về quá khứ)."
        },
        {
            "question": "I _____ my keys. I can't find them anywhere.",
            "options": ["might lose", "might have lost", "must lose", "must have lost"],
            "answer": "might have lost",
            "explanation": "Might have + V3: có thể đã (suy đoán không chắc chắn về quá khứ)."
        },
        {
            "question": "You _____ so much money on that car. It was too expensive.",
            "options": ["shouldn't spend", "shouldn't have spent", "mustn't spend", "mustn't have spent"],
            "answer": "shouldn't have spent",
            "explanation": "Shouldn't have + V3: không nên đã làm (phê bình hành động trong quá khứ)."
        },
        {
            "question": "They _____ the house. The door is locked.",
            "options": ["can't be", "can't have been", "must not be", "must not have been"],
            "answer": "can't have been",
            "explanation": "Can't have + V3: không thể đã (phủ định chắc chắn về quá khứ)."
        },
        {
            "question": "She _____ sick. She didn't come to school yesterday.",
            "options": ["must be", "must have been", "should be", "should have been"],
            "answer": "must have been",
            "explanation": "Must have + V3: chắc hẳn đã (suy đoán chắc chắn về quá khứ)."
        },
        {
            "question": "He _____ harder for the exam. He failed.",
            "options": ["should study", "should have studied", "must study", "must have studied"],
            "answer": "should have studied",
            "explanation": "Should have + V3: đáng lẽ nên (hối tiếc về quá khứ)."
        },
        {
            "question": "I _____ my umbrella at home. It's not in my bag.",
            "options": ["may leave", "may have left", "must leave", "must have left"],
            "answer": "may have left",
            "explanation": "May have + V3: có thể đã (suy đoán không chắc về quá khứ)."
        },
        {
            "question": "You _____ more carefully. You made many mistakes.",
            "options": ["should work", "should have worked", "must work", "must have worked"],
            "answer": "should have worked",
            "explanation": "Should have + V3: đáng lẽ nên (phê bình hành động quá khứ)."
        },
        {
            "question": "She _____ the truth. Everyone knows it now.",
            "options": ["can't tell", "can't have told", "must not tell", "must not have told"],
            "answer": "can't have told",
            "explanation": "Can't have + V3: không thể đã (phủ định chắc chắn về quá khứ)."
        },
        {
            "question": "They _____ before. They seem to know each other very well.",
            "options": ["must meet", "must have met", "should meet", "should have met"],
            "answer": "must have met",
            "explanation": "Must have + V3: chắc hẳn đã (suy đoán chắc chắn về quá khứ)."
        },
        {
            "question": "I _____ my phone at the restaurant. I'll call them.",
            "options": ["might leave", "might have left", "must leave", "must have left"],
            "answer": "might have left",
            "explanation": "Might have + V3: có thể đã (suy đoán không chắc về quá khứ)."
        },
        {
            "question": "You _____ so fast. You could have had an accident.",
            "options": ["shouldn't drive", "shouldn't have driven", "mustn't drive", "mustn't have driven"],
            "answer": "shouldn't have driven",
            "explanation": "Shouldn't have + V3: không nên đã (phê bình hành động quá khứ)."
        },
        {
            "question": "He _____ the message. He replied immediately.",
            "options": ["must receive", "must have received", "should receive", "should have received"],
            "answer": "must have received",
            "explanation": "Must have + V3: chắc hẳn đã (suy đoán chắc chắn về quá khứ)."
        },
        {
            "question": "She _____ about the party. She looked surprised.",
            "options": ["can't know", "can't have known", "must not know", "must not have known"],
            "answer": "can't have known",
            "explanation": "Can't have + V3: không thể đã biết (phủ định chắc chắn về quá khứ)."
        },
        {
            "question": "I _____ the deadline. Now I have to pay a fine.",
            "options": ["should meet", "should have met", "must meet", "must have met"],
            "answer": "should have met",
            "explanation": "Should have + V3: đáng lẽ nên (hối tiếc về quá khứ)."
        },
        {
            "question": "They _____ on vacation. Their house is empty.",
            "options": ["must be", "must have gone", "should go", "should have gone"],
            "answer": "must have gone",
            "explanation": "Must have + V3: chắc hẳn đã (suy đoán chắc chắn về quá khứ)."
        },
        {
            "question": "You _____ your parents about this. They would be worried.",
            "options": ["shouldn't tell", "shouldn't have told", "mustn't tell", "mustn't have told"],
            "answer": "shouldn't have told",
            "explanation": "Shouldn't have + V3: không nên đã (phê bình hành động quá khứ)."
        },
        {
            "question": "He _____ the book already. He's talking about it.",
            "options": ["may read", "may have read", "must read", "must have read"],
            "answer": "must have read",
            "explanation": "Must have + V3: chắc hẳn đã (suy đoán chắc chắn về quá khứ)."
        },
        
        # ==================== SUBJUNCTIVE & WISH (20 câu) ====================
        {
            "question": "I wish I _____ taller.",
            "options": ["am", "was", "were", "have been"],
            "answer": "were",
            "explanation": "Wish + were: ước về hiện tại (điều không có thật ở hiện tại). Luôn dùng 'were' cho mọi ngôi."
        },
        {
            "question": "She wishes she _____ harder when she was young.",
            "options": ["studies", "studied", "has studied", "had studied"],
            "answer": "had studied",
            "explanation": "Wish + had + V3: ước về quá khứ (hối tiếc về điều đã không làm)."
        },
        {
            "question": "It's high time you _____ harder.",
            "options": ["work", "worked", "have worked", "had worked"],
            "answer": "worked",
            "explanation": "It's (high) time + S + V-ed: đã đến lúc phải làm gì (cấu trúc đặc biệt)."
        },
        {
            "question": "I'd rather you _____ smoke in here.",
            "options": ["don't", "didn't", "won't", "haven't"],
            "answer": "didn't",
            "explanation": "Would rather + S + V-ed: muốn ai làm gì (về hiện tại/tương lai)."
        },
        {
            "question": "The doctor suggested that he _____ more exercise.",
            "options": ["take", "takes", "took", "taken"],
            "answer": "take",
            "explanation": "Subjunctive: suggest/recommend/insist + that + S + V (bare infinitive)."
        },
        {
            "question": "I wish it _____ raining. I want to go out.",
            "options": ["stops", "stopped", "would stop", "had stopped"],
            "answer": "would stop",
            "explanation": "Wish + would + V: ước về tương lai hoặc điều khó xảy ra."
        },
        {
            "question": "She acts as though she _____ the owner.",
            "options": ["is", "was", "were", "has been"],
            "answer": "were",
            "explanation": "As if/as though + were: giả định điều không có thật."
        },
        {
            "question": "It's essential that every student _____ a uniform.",
            "options": ["wear", "wears", "wore", "worn"],
            "answer": "wear",
            "explanation": "Subjunctive: It's essential/necessary/important + that + S + V (bare infinitive)."
        },
        {
            "question": "I wish I _____ bought that house. It's worth much more now.",
            "options": ["have", "had", "would", "could"],
            "answer": "had",
            "explanation": "Wish + had + V3: ước về quá khứ (hối tiếc)."
        },
        {
            "question": "If only I _____ speak French!",
            "options": ["can", "could", "will", "would"],
            "answer": "could",
            "explanation": "If only = wish. If only + could: ước có khả năng ở hiện tại."
        },
        {
            "question": "She insisted that he _____ the meeting.",
            "options": ["attend", "attends", "attended", "attending"],
            "answer": "attend",
            "explanation": "Subjunctive: insist + that + S + V (bare infinitive)."
        },
        {
            "question": "I'd rather you _____ told me earlier.",
            "options": ["have", "had", "would", "will"],
            "answer": "had",
            "explanation": "Would rather + S + had + V3: ước về quá khứ."
        },
        {
            "question": "It's time we _____.",
            "options": ["leave", "left", "have left", "had left"],
            "answer": "left",
            "explanation": "It's time + S + V-ed: đã đến lúc phải làm gì."
        },
        {
            "question": "The teacher demanded that the student _____ an apology.",
            "options": ["make", "makes", "made", "making"],
            "answer": "make",
            "explanation": "Subjunctive: demand/require + that + S + V (bare infinitive)."
        },
        {
            "question": "I wish you _____ make so much noise.",
            "options": ["don't", "didn't", "wouldn't", "won't"],
            "answer": "wouldn't",
            "explanation": "Wish + wouldn't: ước ai không làm gì (phàn nàn về thói quen)."
        },
        {
            "question": "If only I _____ to him yesterday!",
            "options": ["talk", "talked", "have talked", "had talked"],
            "answer": "had talked",
            "explanation": "If only + had + V3: ước về quá khứ (hối tiếc)."
        },
        {
            "question": "He speaks to me as if I _____ a child.",
            "options": ["am", "was", "were", "have been"],
            "answer": "were",
            "explanation": "As if + were: giả định điều không có thật ở hiện tại."
        },
        {
            "question": "It's crucial that he _____ on time.",
            "options": ["arrive", "arrives", "arrived", "arriving"],
            "answer": "arrive",
            "explanation": "Subjunctive: It's crucial/vital + that + S + V (bare infinitive)."
        },
        {
            "question": "I wish I _____ more money to buy that car.",
            "options": ["have", "had", "have had", "had had"],
            "answer": "had",
            "explanation": "Wish + had: ước có cái gì ở hiện tại."
        },
        {
            "question": "She recommended that we _____ the museum.",
            "options": ["visit", "visits", "visited", "visiting"],
            "answer": "visit",
            "explanation": "Subjunctive: recommend + that + S + V (bare infinitive)."
        },
        
        # ==================== INVERSION (20 câu) ====================
        {
            "question": "Hardly _____ the door when the phone rang.",
            "options": ["I had opened", "had I opened", "I opened", "did I open"],
            "answer": "had I opened",
            "explanation": "Hardly + had + S + V3: vừa mới... thì. Đảo ngữ với trạng từ phủ định."
        },
        {
            "question": "Never _____ such a beautiful sunset.",
            "options": ["I have seen", "have I seen", "I saw", "did I see"],
            "answer": "have I seen",
            "explanation": "Never + have/has + S + V3: chưa bao giờ. Đảo ngữ với 'never'."
        },
        {
            "question": "No sooner _____ than it started raining.",
            "options": ["we had left", "had we left", "we left", "did we leave"],
            "answer": "had we left",
            "explanation": "No sooner + had + S + V3 + than: vừa mới... thì. Đảo ngữ."
        },
        {
            "question": "Only after finishing the project _____ how difficult it was.",
            "options": ["I realized", "did I realize", "I did realize", "realized I"],
            "answer": "did I realize",
            "explanation": "Only after + phrase/clause + aux + S + V: chỉ sau khi... thì mới. Đảo ngữ."
        },
        {
            "question": "Not only _____ but she also plays the piano.",
            "options": ["she sings", "does she sing", "she does sing", "sings she"],
            "answer": "does she sing",
            "explanation": "Not only + aux + S + V + but also: không chỉ... mà còn. Đảo ngữ."
        },
        {
            "question": "Seldom _____ go to the cinema.",
            "options": ["I", "do I", "I do", "did I"],
            "answer": "do I",
            "explanation": "Seldom + do/does + S + V: hiếm khi. Đảo ngữ với trạng từ tần suất phủ định."
        },
        {
            "question": "Under no circumstances _____ this rule.",
            "options": ["you should break", "should you break", "you break", "break you"],
            "answer": "should you break",
            "explanation": "Under no circumstances + aux + S + V: trong bất kỳ hoàn cảnh nào cũng không. Đảo ngữ."
        },
        {
            "question": "Little _____ that the decision would change his life.",
            "options": ["he knew", "did he know", "he did know", "knew he"],
            "answer": "did he know",
            "explanation": "Little + did + S + V: ít biết rằng. Đảo ngữ với 'little'."
        },
        {
            "question": "Not until yesterday _____ the truth.",
            "options": ["I knew", "did I know", "I did know", "knew I"],
            "answer": "did I know",
            "explanation": "Not until + time/clause + aux + S + V: mãi cho đến khi... thì mới. Đảo ngữ."
        },
        {
            "question": "Rarely _____ seen such a talented musician.",
            "options": ["I have", "have I", "I had", "had I"],
            "answer": "have I",
            "explanation": "Rarely + have/has + S + V3: hiếm khi. Đảo ngữ."
        },
        {
            "question": "Were I in your position, I _____ differently.",
            "options": ["will act", "would act", "act", "acted"],
            "answer": "would act",
            "explanation": "Were + S + to V/adj/noun: nếu... (đảo ngữ câu điều kiện loại 2)."
        },
        {
            "question": "On no account _____ this door unlocked.",
            "options": ["you should leave", "should you leave", "you leave", "leave you"],
            "answer": "should you leave",
            "explanation": "On no account + aux + S + V: trong bất kỳ trường hợp nào cũng không. Đảo ngữ."
        },
        {
            "question": "Only by working hard _____ succeed.",
            "options": ["you can", "can you", "you will", "will you"],
            "answer": "can you",
            "explanation": "Only by + V-ing + aux + S + V: chỉ bằng cách... thì mới. Đảo ngữ."
        },
        {
            "question": "So tired _____ that I went straight to bed.",
            "options": ["I was", "was I", "I am", "am I"],
            "answer": "was I",
            "explanation": "So + adj + be + S + that: quá... đến nỗi. Đảo ngữ nhấn mạnh."
        },
        {
            "question": "Had I known about the party, I _____ there.",
            "options": ["go", "will go", "would go", "would have gone"],
            "answer": "would have gone",
            "explanation": "Had + S + V3: nếu... đã (đảo ngữ câu điều kiện loại 3)."
        },
        {
            "question": "At no time _____ that he was lying.",
            "options": ["I suspected", "did I suspect", "I did suspect", "suspected I"],
            "answer": "did I suspect",
            "explanation": "At no time + aux + S + V: không lúc nào. Đảo ngữ."
        },
        {
            "question": "Should you need any help, _____ me.",
            "options": ["call", "you call", "calling", "to call"],
            "answer": "call",
            "explanation": "Should + S + V: nếu... (đảo ngữ câu điều kiện loại 1). Mệnh đề chính dùng mệnh lệnh."
        },
        {
            "question": "Not a word _____ about the incident.",
            "options": ["he said", "did he say", "he did say", "said he"],
            "answer": "did he say",
            "explanation": "Not a word + aux + S + V: không một lời. Đảo ngữ."
        },
        {
            "question": "Only then _____ what she meant.",
            "options": ["I understood", "did I understand", "I did understand", "understood I"],
            "answer": "did I understand",
            "explanation": "Only then + aux + S + V: chỉ khi đó thì mới. Đảo ngữ."
        },
        {
            "question": "Never before _____ so many people at the beach.",
            "options": ["I had seen", "had I seen", "I saw", "did I see"],
            "answer": "had I seen",
            "explanation": "Never before + had + S + V3: chưa bao giờ trước đây. Đảo ngữ."
        },
        
        # ==================== CLEFT SENTENCES (15 câu) ====================
        {
            "question": "_____ I need is a good night's sleep.",
            "options": ["That", "What", "Which", "Who"],
            "answer": "What",
            "explanation": "Câu chẻ với What: What + S + V + is/was + N. Nhấn mạnh tân ngữ."
        },
        {
            "question": "It _____ Tom who broke the window.",
            "options": ["is", "was", "has been", "will be"],
            "answer": "was",
            "explanation": "Câu chẻ It is/was... that/who: It + be + S/O + that/who + V. Nhấn mạnh chủ ngữ."
        },
        {
            "question": "_____ she told me was completely untrue.",
            "options": ["That", "What", "Which", "Who"],
            "answer": "What",
            "explanation": "What + S + V: cái mà... (câu chẻ nhấn mạnh tân ngữ)."
        },
        {
            "question": "It was in Paris _____ I first met her.",
            "options": ["where", "that", "which", "when"],
            "answer": "that",
            "explanation": "Câu chẻ: It was + địa điểm + that + S + V. Dùng 'that' (không dùng where)."
        },
        {
            "question": "_____ we need to do is finish this project.",
            "options": ["That", "What", "Which", "Who"],
            "answer": "What",
            "explanation": "What + S + need to do + is + V: cái chúng ta cần làm là."
        },
        {
            "question": "It was John _____ gave me this book.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "who",
            "explanation": "Câu chẻ: It is/was + người + who + V. Nhấn mạnh chủ ngữ là người."
        },
        {
            "question": "_____ I want is some peace and quiet.",
            "options": ["That", "What", "Which", "Who"],
            "answer": "What",
            "explanation": "What + S + V + is + N: cái tôi muốn là."
        },
        {
            "question": "It was not until midnight _____ he came home.",
            "options": ["when", "that", "which", "where"],
            "answer": "that",
            "explanation": "Câu chẻ: It was not until... that... (mãi cho đến... thì mới)."
        },
        {
            "question": "_____ surprises me is his attitude.",
            "options": ["That", "What", "Which", "Who"],
            "answer": "What",
            "explanation": "What + V + O + is/was + N: cái làm tôi ngạc nhiên là."
        },
        {
            "question": "It was the blue dress _____ she wore to the party.",
            "options": ["who", "which", "that", "whose"],
            "answer": "that",
            "explanation": "Câu chẻ: It is/was + vật + that + S + V. Nhấn mạnh tân ngữ."
        },
        {
            "question": "_____ matters most is your happiness.",
            "options": ["That", "What", "Which", "Who"],
            "answer": "What",
            "explanation": "What + V + adv + is/was + N: cái quan trọng nhất là."
        },
        {
            "question": "It is you _____ I want to talk to.",
            "options": ["who", "whom", "that", "which"],
            "answer": "that",
            "explanation": "Câu chẻ: It is + người + that/who/whom. Có thể dùng cả 3."
        },
        {
            "question": "_____ I don't understand is why he left.",
            "options": ["That", "What", "Which", "Who"],
            "answer": "What",
            "explanation": "What + S + V + is + mệnh đề: cái tôi không hiểu là."
        },
        {
            "question": "It was his kindness _____ impressed me most.",
            "options": ["who", "which", "that", "whose"],
            "answer": "that",
            "explanation": "Câu chẻ: It was + danh từ + that + V. Nhấn mạnh chủ ngữ."
        },
        {
            "question": "_____ we should focus on is the solution.",
            "options": ["That", "What", "Which", "Who"],
            "answer": "What",
            "explanation": "What + S + should + V + is + N: cái chúng ta nên tập trung là."
        },
        
        # ==================== ADVANCED CONDITIONALS (20 câu) ====================
        {
            "question": "Had I known about the traffic, I _____ earlier.",
            "options": ["leave", "will leave", "would leave", "would have left"],
            "answer": "would have left",
            "explanation": "Đảo ngữ câu điều kiện loại 3: Had + S + V3, S + would have + V3."
        },
        {
            "question": "Were it not for your help, I _____ lost.",
            "options": ["am", "will be", "would be", "would have been"],
            "answer": "would be",
            "explanation": "Đảo ngữ câu điều kiện loại 2: Were it not for = If it were not for (nếu không có)."
        },
        {
            "question": "Should you see him, _____ him my regards.",
            "options": ["give", "giving", "to give", "given"],
            "answer": "give",
            "explanation": "Đảo ngữ câu điều kiện loại 1: Should + S + V, mệnh lệnh thức."
        },
        {
            "question": "If I _____ you, I would accept the offer.",
            "options": ["am", "was", "were", "have been"],
            "answer": "were",
            "explanation": "Câu điều kiện loại 2: If I were you (luôn dùng were)."
        },
        {
            "question": "Provided that you _____ hard, you will succeed.",
            "options": ["work", "worked", "will work", "would work"],
            "answer": "work",
            "explanation": "Provided that = if (với điều kiện là). Câu điều kiện loại 1."
        },
        {
            "question": "But for his help, we _____ the project on time.",
            "options": ["don't finish", "won't finish", "wouldn't finish", "wouldn't have finished"],
            "answer": "wouldn't have finished",
            "explanation": "But for = without (nếu không có). Câu điều kiện loại 3."
        },
        {
            "question": "If only I _____ his phone number!",
            "options": ["know", "knew", "have known", "had known"],
            "answer": "knew",
            "explanation": "If only = wish. Ước về hiện tại: If only + S + V-ed."
        },
        {
            "question": "Suppose you _____ a million dollars, what would you do?",
            "options": ["have", "had", "will have", "would have"],
            "answer": "had",
            "explanation": "Suppose = if (giả sử). Câu điều kiện loại 2: Suppose + S + V-ed."
        },
        {
            "question": "Unless you _____ now, you'll be late.",
            "options": ["leave", "left", "will leave", "would leave"],
            "answer": "leave",
            "explanation": "Unless = if... not. Câu điều kiện loại 1: Unless + S + V(hiện tại)."
        },
        {
            "question": "Had it not been for the rain, we _____ out.",
            "options": ["go", "will go", "would go", "would have gone"],
            "answer": "would have gone",
            "explanation": "Đảo ngữ câu điều kiện loại 3: Had it not been for = If it had not been for."
        },
        {
            "question": "If she _____ harder last year, she would be successful now.",
            "options": ["worked", "works", "had worked", "has worked"],
            "answer": "had worked",
            "explanation": "Mixed conditional: If + S + had + V3 (quá khứ), S + would + V (hiện tại)."
        },
        {
            "question": "As long as you _____ the rules, you can stay.",
            "options": ["follow", "followed", "will follow", "would follow"],
            "answer": "follow",
            "explanation": "As long as = if (miễn là). Câu điều kiện loại 1."
        },
        {
            "question": "If he were here now, he _____ what to do.",
            "options": ["knows", "knew", "would know", "will know"],
            "answer": "would know",
            "explanation": "Câu điều kiện loại 2: If + S + were, S + would + V."
        },
        {
            "question": "In case you _____ her, give her my message.",
            "options": ["see", "saw", "will see", "would see"],
            "answer": "see",
            "explanation": "In case = if (phòng khi). Dùng thì hiện tại."
        },
        {
            "question": "Were I to win the lottery, I _____ a house.",
            "options": ["buy", "will buy", "would buy", "bought"],
            "answer": "would buy",
            "explanation": "Đảo ngữ câu điều kiện loại 2: Were + S + to V, S + would + V."
        },
        {
            "question": "If it _____ rained yesterday, we would have gone out.",
            "options": ["doesn't", "didn't", "hasn't", "hadn't"],
            "answer": "hadn't",
            "explanation": "Câu điều kiện loại 3: If + S + hadn't + V3, S + would have + V3."
        },
        {
            "question": "On condition that you _____ quietly, you can join us.",
            "options": ["work", "worked", "will work", "would work"],
            "answer": "work",
            "explanation": "On condition that = if (với điều kiện là). Câu điều kiện loại 1."
        },
        {
            "question": "If you _____ my advice, you wouldn't be in this situation.",
            "options": ["take", "took", "had taken", "have taken"],
            "answer": "had taken",
            "explanation": "Mixed conditional: If + S + had + V3 (quá khứ), S + would + V (hiện tại)."
        },
        {
            "question": "Assuming that he _____ on time, we can start at 9.",
            "options": ["arrives", "arrived", "will arrive", "would arrive"],
            "answer": "arrives",
            "explanation": "Assuming that = if (giả định rằng). Câu điều kiện loại 1."
        },
        {
            "question": "If you _____ the instructions, you would have succeeded.",
            "options": ["follow", "followed", "had followed", "have followed"],
            "answer": "had followed",
            "explanation": "Câu điều kiện loại 3: If + S + had + V3, S + would have + V3."
        },
        
        # ==================== REDUCED CLAUSES (15 câu) ====================
        {
            "question": "_____ from a distance, the mountain looks beautiful.",
            "options": ["See", "Seeing", "Seen", "To see"],
            "answer": "Seen",
            "explanation": "Rút gọn mệnh đề bị động: (When it is) seen from a distance = Seen from a distance."
        },
        {
            "question": "_____ in the sun, the flowers grew quickly.",
            "options": ["Stand", "Standing", "Stood", "To stand"],
            "answer": "Standing",
            "explanation": "Rút gọn mệnh đề chủ động: (Because they were) standing = Standing."
        },
        {
            "question": "The girl _____ by the window is my sister.",
            "options": ["sit", "sitting", "sat", "to sit"],
            "answer": "sitting",
            "explanation": "Rút gọn mệnh đề quan hệ chủ động: who is sitting = sitting."
        },
        {
            "question": "_____ his homework, he went out to play.",
            "options": ["Finish", "Finishing", "Finished", "Having finished"],
            "answer": "Having finished",
            "explanation": "Having + V3: sau khi hoàn thành hành động (hành động trước xảy ra trước)."
        },
        {
            "question": "The book _____ on the table is mine.",
            "options": ["lie", "lying", "lied", "to lie"],
            "answer": "lying",
            "explanation": "Rút gọn mệnh đề quan hệ chủ động: which is lying = lying."
        },
        {
            "question": "_____ carefully, the product will last longer.",
            "options": ["Use", "Using", "Used", "To use"],
            "answer": "Used",
            "explanation": "Rút gọn mệnh đề bị động: (If it is) used carefully = Used carefully."
        },
        {
            "question": "_____ no one at home, I left a message.",
            "options": ["Find", "Finding", "Found", "To find"],
            "answer": "Finding",
            "explanation": "Rút gọn mệnh đề chủ động: (Because I found) = Finding."
        },
        {
            "question": "The letter _____ yesterday was from my uncle.",
            "options": ["receive", "receiving", "received", "to receive"],
            "answer": "received",
            "explanation": "Rút gọn mệnh đề quan hệ bị động: which was received = received."
        },
        {
            "question": "_____ all his money, he couldn't buy the car.",
            "options": ["Lose", "Losing", "Lost", "Having lost"],
            "answer": "Having lost",
            "explanation": "Having + V3: sau khi mất (hành động xảy ra trước)."
        },
        {
            "question": "The man _____ to you is my boss.",
            "options": ["talk", "talking", "talked", "to talk"],
            "answer": "talking",
            "explanation": "Rút gọn mệnh đề quan hệ chủ động: who is talking = talking."
        },
        {
            "question": "_____ in England, she speaks English fluently.",
            "options": ["Born", "Being born", "Having born", "To be born"],
            "answer": "Born",
            "explanation": "Rút gọn mệnh đề bị động: (Because she was) born = Born."
        },
        {
            "question": "_____ the house, he noticed something strange.",
            "options": ["Enter", "Entering", "Entered", "To enter"],
            "answer": "Entering",
            "explanation": "Rút gọn mệnh đề chủ động: (When he entered) = Entering."
        },
        {
            "question": "The students _____ the test are nervous.",
            "options": ["take", "taking", "took", "to take"],
            "answer": "taking",
            "explanation": "Rút gọn mệnh đề quan hệ chủ động: who are taking = taking."
        },
        {
            "question": "_____ by everyone, she felt very happy.",
            "options": ["Praise", "Praising", "Praised", "To praise"],
            "answer": "Praised",
            "explanation": "Rút gọn mệnh đề bị động: (Because she was) praised = Praised."
        },
        {
            "question": "_____ the movie before, I didn't want to see it again.",
            "options": ["See", "Seeing", "Seen", "Having seen"],
            "answer": "Having seen",
            "explanation": "Having + V3: sau khi xem (hành động xảy ra trước)."
        },
        
        # ==================== VOCABULARY ADVANCED (30 câu) ====================
        {
            "question": "The company has made a significant _____ in technology.",
            "options": ["breakthrough", "breakdown", "outbreak", "cutback"],
            "answer": "breakthrough",
            "explanation": "Breakthrough = đột phá, tiến bộ đáng kể."
        },
        {
            "question": "His speech was very _____ and moved many people.",
            "options": ["eloquent", "elegant", "arrogant", "ignorant"],
            "answer": "eloquent",
            "explanation": "Eloquent = hùng biện, có sức thuyết phục."
        },
        {
            "question": "The government is taking measures to _____ poverty.",
            "options": ["eradicate", "educate", "evaluate", "elaborate"],
            "answer": "eradicate",
            "explanation": "Eradicate = xóa bỏ, loại trừ hoàn toàn."
        },
        {
            "question": "She has an _____ ability to learn languages.",
            "options": ["ordinary", "extraordinary", "contradictory", "satisfactory"],
            "answer": "extraordinary",
            "explanation": "Extraordinary = phi thường, đặc biệt."
        },
        {
            "question": "The evidence was _____, so the case was dismissed.",
            "options": ["conclusive", "inclusive", "inconclusive", "exclusive"],
            "answer": "inconclusive",
            "explanation": "Inconclusive = không quyết định, không thuyết phục."
        },
        {
            "question": "His behavior was _____ to everyone at the party.",
            "options": ["comprehend", "comprehensive", "comprehensible", "incomprehensible"],
            "answer": "incomprehensible",
            "explanation": "Incomprehensible = không thể hiểu được."
        },
        {
            "question": "The report provides a _____ analysis of the situation.",
            "options": ["thorough", "through", "though", "thought"],
            "answer": "thorough",
            "explanation": "Thorough = kỹ lưỡng, toàn diện."
        },
        {
            "question": "The new law will _____ affect small businesses.",
            "options": ["adverse", "adversely", "adversity", "adversarial"],
            "answer": "adversely",
            "explanation": "Adversely = một cách bất lợi, có hại."
        },
        {
            "question": "She made an _____ effort to finish the project on time.",
            "options": ["immense", "immerse", "immune", "immature"],
            "answer": "immense",
            "explanation": "Immense = to lớn, khổng lồ."
        },
        {
            "question": "The discovery has _____ implications for medicine.",
            "options": ["profound", "profane", "profess", "profile"],
            "answer": "profound",
            "explanation": "Profound = sâu sắc, có ý nghĩa lớn."
        },
        {
            "question": "His argument was based on _____ reasoning.",
            "options": ["fallacy", "fallacious", "fallible", "falling"],
            "answer": "fallacious",
            "explanation": "Fallacious = sai lầm, dựa trên ngụy biện."
        },
        {
            "question": "The committee will _____ the proposal next week.",
            "options": ["scrutinize", "scrutiny", "scrutinizing", "scrutinized"],
            "answer": "scrutinize",
            "explanation": "Scrutinize = xem xét kỹ lưỡng."
        },
        {
            "question": "The company's success is _____ to its innovative approach.",
            "options": ["attributed", "contributed", "distributed", "substituted"],
            "answer": "attributed",
            "explanation": "Be attributed to = được quy cho."
        },
        {
            "question": "The situation requires _____ attention.",
            "options": ["immediate", "mediate", "intermediate", "meditate"],
            "answer": "immediate",
            "explanation": "Immediate = ngay lập tức."
        },
        {
            "question": "His _____ for detail is impressive.",
            "options": ["eye", "hand", "ear", "nose"],
            "answer": "eye",
            "explanation": "Eye for detail = sự tỉ mỉ, chú ý đến chi tiết."
        },
        {
            "question": "The results were _____ different from what we expected.",
            "options": ["remarkable", "remarkably", "remark", "remarked"],
            "answer": "remarkably",
            "explanation": "Remarkably = một cách đáng chú ý."
        },
        {
            "question": "The project faces _____ challenges.",
            "options": ["formidable", "forgivable", "favorable", "feasible"],
            "answer": "formidable",
            "explanation": "Formidable = đáng gờm, khó khăn."
        },
        {
            "question": "She showed great _____ in dealing with the crisis.",
            "options": ["compose", "composer", "composure", "composition"],
            "answer": "composure",
            "explanation": "Composure = sự bình tĩnh, tự chủ."
        },
        {
            "question": "The theory lacks _____ evidence.",
            "options": ["empirical", "imperial", "empathetic", "emphatic"],
            "answer": "empirical",
            "explanation": "Empirical = dựa trên thực nghiệm."
        },
        {
            "question": "His _____ attitude made him unpopular.",
            "options": ["arrogant", "elegant", "eloquent", "ignorant"],
            "answer": "arrogant",
            "explanation": "Arrogant = kiêu ngạo, ngạo mạn."
        },
        {
            "question": "The contract contains several _____ clauses.",
            "options": ["ambiguous", "ambitious", "amphibious", "anonymous"],
            "answer": "ambiguous",
            "explanation": "Ambiguous = mơ hồ, không rõ ràng."
        },
        {
            "question": "The company needs to _____ its market position.",
            "options": ["consolidate", "considerate", "considerable", "constellation"],
            "answer": "consolidate",
            "explanation": "Consolidate = củng cố, hợp nhất."
        },
        {
            "question": "His behavior was completely _____.",
            "options": ["rational", "irrational", "rationale", "rationalize"],
            "answer": "irrational",
            "explanation": "Irrational = phi lý, vô lý."
        },
        {
            "question": "The report highlights the _____ of the problem.",
            "options": ["magnitude", "magnify", "magnificent", "magnet"],
            "answer": "magnitude",
            "explanation": "Magnitude = quy mô, tầm quan trọng."
        },
        {
            "question": "She has a _____ understanding of the subject.",
            "options": ["superficial", "superfluous", "superior", "supernatural"],
            "answer": "superficial",
            "explanation": "Superficial = hời hợt, nông cạn."
        },
        {
            "question": "The new policy will _____ existing regulations.",
            "options": ["supersede", "succeed", "proceed", "exceed"],
            "answer": "supersede",
            "explanation": "Supersede = thay thế, thế chỗ."
        },
        {
            "question": "His _____ for perfection is well-known.",
            "options": ["quest", "question", "request", "conquest"],
            "answer": "quest",
            "explanation": "Quest = sự tìm kiếm, khao khát."
        },
        {
            "question": "The situation is _____ and requires immediate action.",
            "options": ["critical", "criticism", "criticize", "critic"],
            "answer": "critical",
            "explanation": "Critical = nghiêm trọng, quan trọng."
        },
        {
            "question": "The company has a _____ reputation in the industry.",
            "options": ["formidable", "favorable", "forgivable", "fashionable"],
            "answer": "formidable",
            "explanation": "Formidable = đáng nể, uy tín lớn."
        },
        {
            "question": "The research provides _____ insights into the problem.",
            "options": ["invaluable", "valuable", "valueless", "valued"],
            "answer": "invaluable",
            "explanation": "Invaluable = vô giá, cực kỳ quý báu."
        },
        
        # ==================== IDIOMS & COLLOCATIONS (20 câu) ====================
        {
            "question": "He finally _____ the courage to ask her out.",
            "options": ["took", "made", "got", "plucked up"],
            "answer": "plucked up",
            "explanation": "Pluck up courage = lấy can đảm."
        },
        {
            "question": "She always _____ a blind eye to his mistakes.",
            "options": ["makes", "turns", "gives", "takes"],
            "answer": "turns",
            "explanation": "Turn a blind eye to = làm ngơ, phớt lờ."
        },
        {
            "question": "The project is _____ schedule.",
            "options": ["behind", "after", "back", "late"],
            "answer": "behind",
            "explanation": "Behind schedule = chậm tiến độ."
        },
        {
            "question": "He's really _____ his depth in this discussion.",
            "options": ["above", "over", "beyond", "out of"],
            "answer": "out of",
            "explanation": "Out of one's depth = vượt quá khả năng."
        },
        {
            "question": "The news came as a bolt from the _____.",
            "options": ["sky", "blue", "heaven", "cloud"],
            "answer": "blue",
            "explanation": "A bolt from the blue = điều bất ngờ."
        },
        {
            "question": "She's always _____ fault with everything.",
            "options": ["making", "finding", "taking", "giving"],
            "answer": "finding",
            "explanation": "Find fault with = chỉ trích, bắt lỗi."
        },
        {
            "question": "He _____ a fortune in the stock market.",
            "options": ["did", "made", "earned", "won"],
            "answer": "made",
            "explanation": "Make a fortune = kiếm được gia tài."
        },
        {
            "question": "The project is now in full _____.",
            "options": ["swing", "speed", "motion", "force"],
            "answer": "swing",
            "explanation": "In full swing = đang diễn ra sôi nổi."
        },
        {
            "question": "He's _____ the same old story again.",
            "options": ["saying", "telling", "speaking", "talking"],
            "answer": "telling",
            "explanation": "Tell a story = kể chuyện."
        },
        {
            "question": "She _____ me off my feet with her performance.",
            "options": ["took", "swept", "knocked", "pulled"],
            "answer": "swept",
            "explanation": "Sweep someone off their feet = làm ai say đắm."
        },
        {
            "question": "The company is on the _____ of bankruptcy.",
            "options": ["edge", "verge", "brink", "border"],
            "answer": "brink",
            "explanation": "On the brink of = trên bờ vực của."
        },
        {
            "question": "He took her criticism with a pinch of _____.",
            "options": ["pepper", "salt", "sugar", "spice"],
            "answer": "salt",
            "explanation": "Take with a pinch of salt = không tin hoàn toàn."
        },
        {
            "question": "She's the _____ of my eye.",
            "options": ["apple", "orange", "banana", "grape"],
            "answer": "apple",
            "explanation": "The apple of one's eye = người được yêu quý nhất."
        },
        {
            "question": "The company is _____ for a fall.",
            "options": ["ready", "heading", "going", "making"],
            "answer": "heading",
            "explanation": "Heading for a fall = sắp thất bại."
        },
        {
            "question": "He _____ his word and helped me.",
            "options": ["made", "took", "kept", "gave"],
            "answer": "kept",
            "explanation": "Keep one's word = giữ lời hứa."
        },
        {
            "question": "The decision rests _____ you.",
            "options": ["on", "with", "by", "to"],
            "answer": "with",
            "explanation": "Rest with = thuộc về (quyết định)."
        },
        {
            "question": "She _____ the world of him.",
            "options": ["makes", "thinks", "does", "says"],
            "answer": "thinks",
            "explanation": "Think the world of = rất trọng vọng."
        },
        {
            "question": "The party went off without a _____.",
            "options": ["problem", "hitch", "trouble", "difficulty"],
            "answer": "hitch",
            "explanation": "Without a hitch = suôn sẻ, không vấn đề."
        },
        {
            "question": "He's _____ in the clouds again.",
            "options": ["flying", "walking", "living", "sitting"],
            "answer": "living",
            "explanation": "Living in the clouds = mơ mộng, không thực tế."
        },
        {
            "question": "She _____ her brains trying to solve the problem.",
            "options": ["picked", "racked", "cracked", "packed"],
            "answer": "racked",
            "explanation": "Rack one's brains = suy nghĩ vắt óc."
        }
]