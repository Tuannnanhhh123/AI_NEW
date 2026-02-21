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
 # ==================== ARTICLES (15 câu) ====================
        {
            "question": "_____ disabled need more support from society.",
            "options": ["A", "An", "The", "No article"],
            "answer": "The",
            "explanation": "The + adj = chỉ một nhóm người (the disabled = người khuyết tật)."
        },
        {
            "question": "She plays _____ piano beautifully.",
            "options": ["a", "an", "the", "no article"],
            "answer": "the",
            "explanation": "The + musical instrument: chơi nhạc cụ."
        },
        {
            "question": "_____ honesty is the best policy.",
            "options": ["A", "An", "The", "No article"],
            "answer": "No article",
            "explanation": "Không dùng mạo từ trước danh từ trừu tượng mang nghĩa chung."
        },
        {
            "question": "He is _____ European working in Vietnam.",
            "options": ["a", "an", "the", "no article"],
            "answer": "a",
            "explanation": "Dùng 'a' trước âm /j/ (European phát âm /ˌjʊərəˈpiːən/)."
        },
        {
            "question": "_____ rich should help _____ poor.",
            "options": ["The/the", "A/the", "The/a", "No article/no article"],
            "answer": "The/the",
            "explanation": "The + adj = chỉ nhóm người: the rich (người giàu), the poor (người nghèo)."
        },
        {
            "question": "She goes to _____ church every Sunday.",
            "options": ["a", "an", "the", "no article"],
            "answer": "no article",
            "explanation": "Go to church (đi nhà thờ để cầu nguyện) - không dùng mạo từ."
        },
        {
            "question": "_____ United States is a developed country.",
            "options": ["A", "An", "The", "No article"],
            "answer": "The",
            "explanation": "Dùng 'the' trước tên quốc gia có States, Kingdom, Republic."
        },
        {
            "question": "He had _____ breakfast before going to work.",
            "options": ["a", "an", "the", "no article"],
            "answer": "no article",
            "explanation": "Không dùng mạo từ trước bữa ăn khi nói chung."
        },
        {
            "question": "Mount Everest is _____ highest mountain in the world.",
            "options": ["a", "an", "the", "no article"],
            "answer": "the",
            "explanation": "Dùng 'the' trước so sánh nhất."
        },
        {
            "question": "She is _____ honest person.",
            "options": ["a", "an", "the", "no article"],
            "answer": "an",
            "explanation": "Dùng 'an' trước nguyên âm /ɒ/ (honest phát âm /ˈɒnɪst/ - h câm)."
        },
        {
            "question": "_____ life is full of surprises.",
            "options": ["A", "An", "The", "No article"],
            "answer": "No article",
            "explanation": "Không dùng mạo từ trước danh từ trừu tượng mang nghĩa chung."
        },
        {
            "question": "He is in _____ hospital after the accident.",
            "options": ["a", "an", "the", "no article"],
            "answer": "the",
            "explanation": "In the hospital = đang nằm viện (như bệnh nhân hoặc khách)."
        },
        {
            "question": "She plays _____ tennis twice a week.",
            "options": ["a", "an", "the", "no article"],
            "answer": "no article",
            "explanation": "Không dùng mạo từ trước môn thể thao."
        },
        {
            "question": "_____ Pacific Ocean is the largest ocean.",
            "options": ["A", "An", "The", "No article"],
            "answer": "The",
            "explanation": "Dùng 'the' trước tên đại dương, biển, sông."
        },
        {
            "question": "He goes to _____ school by bus.",
            "options": ["a", "an", "the", "no article"],
            "answer": "no article",
            "explanation": "Go to school (đi học) - không dùng mạo từ."
        },
        
        # ==================== CONJUNCTIONS & LINKING WORDS (20 câu) ====================
        {
            "question": "_____ it was raining heavily, we decided to go out.",
            "options": ["Despite", "In spite of", "Although", "Because"],
            "answer": "Although",
            "explanation": "Although + clause: mặc dù (+ mệnh đề)."
        },
        {
            "question": "He studied hard; _____, he failed the exam.",
            "options": ["therefore", "however", "moreover", "furthermore"],
            "answer": "however",
            "explanation": "However = tuy nhiên (chỉ sự đối lập)."
        },
        {
            "question": "_____ the bad weather, the match continued.",
            "options": ["Although", "Despite", "Because", "Because of"],
            "answer": "Despite",
            "explanation": "Despite + N/V-ing: mặc dù (+ danh từ/cụm danh từ)."
        },
        {
            "question": "She is intelligent; _____, she is hardworking.",
            "options": ["however", "moreover", "therefore", "otherwise"],
            "answer": "moreover",
            "explanation": "Moreover = hơn nữa (bổ sung thông tin)."
        },
        {
            "question": "_____ being tired, she continued working.",
            "options": ["Although", "Despite", "In spite", "Because"],
            "answer": "Despite",
            "explanation": "Despite + V-ing: mặc dù."
        },
        {
            "question": "He didn't study; _____, he failed.",
            "options": ["however", "moreover", "therefore", "furthermore"],
            "answer": "therefore",
            "explanation": "Therefore = do đó, vì vậy (chỉ kết quả)."
        },
        {
            "question": "_____ the fact that he was sick, he went to work.",
            "options": ["Although", "Despite", "Because", "Because of"],
            "answer": "Despite",
            "explanation": "Despite the fact that = mặc dù thực tế là."
        },
        {
            "question": "She speaks English fluently; _____, she can speak French.",
            "options": ["however", "in addition", "therefore", "otherwise"],
            "answer": "in addition",
            "explanation": "In addition = thêm vào đó (bổ sung)."
        },
        {
            "question": "_____ he is young, he is very responsible.",
            "options": ["Despite", "In spite of", "Although", "Because"],
            "answer": "Although",
            "explanation": "Although + clause: mặc dù."
        },
        {
            "question": "Study hard, _____ you will fail.",
            "options": ["and", "or", "but", "so"],
            "answer": "or",
            "explanation": "Or = nếu không thì (chỉ hậu quả tiêu cực)."
        },
        {
            "question": "_____ his hard work, he didn't get promoted.",
            "options": ["Although", "Despite", "Because", "Because of"],
            "answer": "Despite",
            "explanation": "Despite + N: mặc dù."
        },
        {
            "question": "She is beautiful; _____, she is kind.",
            "options": ["however", "besides", "therefore", "otherwise"],
            "answer": "besides",
            "explanation": "Besides = hơn nữa, ngoài ra."
        },
        {
            "question": "_____ it rained, we stayed at home.",
            "options": ["Because", "Because of", "Although", "Despite"],
            "answer": "Because",
            "explanation": "Because + clause: bởi vì."
        },
        {
            "question": "He is rich; _____, he is not happy.",
            "options": ["therefore", "however", "moreover", "furthermore"],
            "answer": "however",
            "explanation": "However = tuy nhiên."
        },
        {
            "question": "_____ the rain, the match was cancelled.",
            "options": ["Because", "Because of", "Although", "Despite"],
            "answer": "Because of",
            "explanation": "Because of + N: bởi vì."
        },
        {
            "question": "She worked hard; _____, she succeeded.",
            "options": ["however", "consequently", "moreover", "otherwise"],
            "answer": "consequently",
            "explanation": "Consequently = kết quả là."
        },
        {
            "question": "_____ having little money, they are happy.",
            "options": ["Although", "Despite", "Because", "Because of"],
            "answer": "Despite",
            "explanation": "Despite + V-ing: mặc dù."
        },
        {
            "question": "He is lazy; _____, he is intelligent.",
            "options": ["therefore", "nevertheless", "moreover", "furthermore"],
            "answer": "nevertheless",
            "explanation": "Nevertheless = tuy nhiên, dù vậy."
        },
        {
            "question": "_____ her illness, she attended the meeting.",
            "options": ["Although", "Despite", "Because", "Because of"],
            "answer": "Despite",
            "explanation": "Despite + N: mặc dù."
        },
        {
            "question": "Study hard; _____, you won't pass.",
            "options": ["and", "or", "but", "otherwise"],
            "answer": "otherwise",
            "explanation": "Otherwise = nếu không thì."
        },
        
        # ==================== WORD FORMATION (25 câu) ====================
        {
            "question": "The company has shown great _____ in developing new products.",
            "options": ["innovate", "innovation", "innovative", "innovatively"],
            "answer": "innovation",
            "explanation": "Cần danh từ sau 'great'. Innovation = sự đổi mới."
        },
        {
            "question": "She spoke _____ about her achievements.",
            "options": ["pride", "proud", "proudly", "proudness"],
            "answer": "proudly",
            "explanation": "Cần trạng từ bổ nghĩa cho động từ 'spoke'. Proudly = một cách tự hào."
        },
        {
            "question": "The _____ of the project was delayed due to bad weather.",
            "options": ["complete", "completion", "completely", "completeness"],
            "answer": "completion",
            "explanation": "Cần danh từ làm chủ ngữ. Completion = sự hoàn thành."
        },
        {
            "question": "His _____ to detail is remarkable.",
            "options": ["attend", "attention", "attentive", "attentively"],
            "answer": "attention",
            "explanation": "Cần danh từ sau tính từ sở hữu 'his'. Attention = sự chú ý."
        },
        {
            "question": "The movie was _____ boring.",
            "options": ["disappoint", "disappointment", "disappointing", "disappointingly"],
            "answer": "disappointingly",
            "explanation": "Cần trạng từ bổ nghĩa cho tính từ 'boring'. Disappointingly = một cách thất vọng."
        },
        {
            "question": "We need to find a _____ solution to this problem.",
            "options": ["sustain", "sustainable", "sustainability", "sustainably"],
            "answer": "sustainable",
            "explanation": "Cần tính từ bổ nghĩa cho danh từ 'solution'. Sustainable = bền vững."
        },
        {
            "question": "The _____ between the two countries has improved.",
            "options": ["relate", "relation", "relationship", "relative"],
            "answer": "relationship",
            "explanation": "Cần danh từ làm chủ ngữ. Relationship = mối quan hệ."
        },
        {
            "question": "She is _____ known for her charitable work.",
            "options": ["wide", "width", "widely", "widen"],
            "answer": "widely",
            "explanation": "Cần trạng từ bổ nghĩa cho 'known'. Widely = rộng rãi."
        },
        {
            "question": "The _____ of the environment is everyone's responsibility.",
            "options": ["protect", "protection", "protective", "protector"],
            "answer": "protection",
            "explanation": "Cần danh từ làm chủ ngữ. Protection = sự bảo vệ."
        },
        {
            "question": "He made an _____ decision without thinking.",
            "options": ["impulse", "impulsive", "impulsively", "impulsiveness"],
            "answer": "impulsive",
            "explanation": "Cần tính từ bổ nghĩa cho danh từ 'decision'. Impulsive = bốc đồng."
        },
        {
            "question": "The _____ of technology has changed our lives.",
            "options": ["advance", "advancement", "advanced", "advancing"],
            "answer": "advancement",
            "explanation": "Cần danh từ làm chủ ngữ. Advancement = sự tiến bộ."
        },
        {
            "question": "She is _____ committed to her work.",
            "options": ["total", "totally", "totality", "totalize"],
            "answer": "totally",
            "explanation": "Cần trạng từ bổ nghĩa cho 'committed'. Totally = hoàn toàn."
        },
        {
            "question": "The _____ of the new system was successful.",
            "options": ["implement", "implementation", "implemented", "implementing"],
            "answer": "implementation",
            "explanation": "Cần danh từ làm chủ ngữ. Implementation = sự thực hiện."
        },
        {
            "question": "He is _____ qualified for this position.",
            "options": ["high", "height", "highly", "heighten"],
            "answer": "highly",
            "explanation": "Cần trạng từ bổ nghĩa cho 'qualified'. Highly = rất, cao."
        },
        {
            "question": "The _____ of the product exceeded expectations.",
            "options": ["perform", "performance", "performer", "performing"],
            "answer": "performance",
            "explanation": "Cần danh từ làm chủ ngữ. Performance = hiệu suất, sự thực hiện."
        },
        {
            "question": "She is _____ aware of the risks.",
            "options": ["full", "fully", "fulfill", "fullness"],
            "answer": "fully",
            "explanation": "Cần trạng từ bổ nghĩa cho 'aware'. Fully = hoàn toàn."
        },
        {
            "question": "The _____ of clean energy is essential.",
            "options": ["develop", "development", "developed", "developing"],
            "answer": "development",
            "explanation": "Cần danh từ làm chủ ngữ. Development = sự phát triển."
        },
        {
            "question": "He speaks _____ about his experience.",
            "options": ["passion", "passionate", "passionately", "passionateness"],
            "answer": "passionately",
            "explanation": "Cần trạng từ bổ nghĩa cho động từ 'speaks'. Passionately = một cách nhiệt huyết."
        },
        {
            "question": "The _____ of the disease is unknown.",
            "options": ["origin", "original", "originally", "originate"],
            "answer": "origin",
            "explanation": "Cần danh từ làm chủ ngữ. Origin = nguồn gốc."
        },
        {
            "question": "She is _____ talented in music.",
            "options": ["exception", "exceptional", "exceptionally", "except"],
            "answer": "exceptionally",
            "explanation": "Cần trạng từ bổ nghĩa cho 'talented'. Exceptionally = đặc biệt."
        },
        {
            "question": "The _____ between theory and practice is important.",
            "options": ["connect", "connection", "connected", "connecting"],
            "answer": "connection",
            "explanation": "Cần danh từ làm chủ ngữ. Connection = sự kết nối."
        },
        {
            "question": "He worked _____ to finish the project.",
            "options": ["tire", "tired", "tireless", "tirelessly"],
            "answer": "tirelessly",
            "explanation": "Cần trạng từ bổ nghĩa cho động từ 'worked'. Tirelessly = không mệt mỏi."
        },
        {
            "question": "The _____ of the program was impressive.",
            "options": ["execute", "execution", "executive", "executing"],
            "answer": "execution",
            "explanation": "Cần danh từ làm chủ ngữ. Execution = sự thực thi."
        },
        {
            "question": "She is _____ satisfied with the results.",
            "options": ["thorough", "thoroughly", "thoroughness", "through"],
            "answer": "thoroughly",
            "explanation": "Cần trạng từ bổ nghĩa cho 'satisfied'. Thoroughly = hoàn toàn."
        },
        {
            "question": "The _____ of resources is crucial.",
            "options": ["allocate", "allocation", "allocated", "allocating"],
            "answer": "allocation",
            "explanation": "Cần danh từ làm chủ ngữ. Allocation = sự phân bổ."
        },
        
        # ==================== PHRASAL VERBS ADVANCED (25 câu) ====================
        {
            "question": "The meeting was _____ until next week.",
            "options": ["put off", "put on", "put up", "put down"],
            "answer": "put off",
            "explanation": "Put off = hoãn lại."
        },
        {
            "question": "She _____ with a brilliant idea.",
            "options": ["came up", "came down", "came in", "came out"],
            "answer": "came up",
            "explanation": "Come up with = nêu ra, nghĩ ra (ý tưởng)."
        },
        {
            "question": "The company had to _____ several employees.",
            "options": ["lay off", "lay on", "lay up", "lay down"],
            "answer": "lay off",
            "explanation": "Lay off = sa thải (nhân viên)."
        },
        {
            "question": "I can't _____ his bad behavior anymore.",
            "options": ["put up with", "put off with", "put on with", "put down with"],
            "answer": "put up with",
            "explanation": "Put up with = chịu đựng."
        },
        {
            "question": "The plane _____ on time despite bad weather.",
            "options": ["took off", "took on", "took up", "took over"],
            "answer": "took off",
            "explanation": "Take off = cất cánh."
        },
        {
            "question": "She _____ her father in appearance.",
            "options": ["takes after", "takes on", "takes up", "takes over"],
            "answer": "takes after",
            "explanation": "Take after = giống (về ngoại hình/tính cách)."
        },
        {
            "question": "The fire _____ by the strong wind.",
            "options": ["broke out", "broke up", "broke down", "broke in"],
            "answer": "broke out",
            "explanation": "Break out = bùng phát (lửa, chiến tranh, dịch bệnh)."
        },
        {
            "question": "I need to _____ this matter before making a decision.",
            "options": ["look into", "look after", "look for", "look up"],
            "answer": "look into",
            "explanation": "Look into = điều tra, xem xét kỹ."
        },
        {
            "question": "The relationship _____ after many arguments.",
            "options": ["broke up", "broke out", "broke down", "broke in"],
            "answer": "broke up",
            "explanation": "Break up = tan vỡ (mối quan hệ)."
        },
        {
            "question": "He _____ a new hobby during the lockdown.",
            "options": ["took up", "took off", "took on", "took over"],
            "answer": "took up",
            "explanation": "Take up = bắt đầu (sở thích mới)."
        },
        {
            "question": "The car _____ on the highway.",
            "options": ["broke down", "broke up", "broke out", "broke in"],
            "answer": "broke down",
            "explanation": "Break down = hỏng (máy móc)."
        },
        {
            "question": "She _____ the job offer without hesitation.",
            "options": ["turned down", "turned up", "turned on", "turned off"],
            "answer": "turned down",
            "explanation": "Turn down = từ chối."
        },
        {
            "question": "The company is _____ a new project.",
            "options": ["carrying out", "carrying on", "carrying away", "carrying off"],
            "answer": "carrying out",
            "explanation": "Carry out = thực hiện (dự án, kế hoạch)."
        },
        {
            "question": "He _____ his business to his son.",
            "options": ["handed over", "handed in", "handed out", "handed down"],
            "answer": "handed over",
            "explanation": "Hand over = chuyển giao."
        },
        {
            "question": "The issue was _____ at the meeting.",
            "options": ["brought up", "brought in", "brought out", "brought down"],
            "answer": "brought up",
            "explanation": "Bring up = nêu ra (vấn đề để thảo luận)."
        },
        {
            "question": "She _____ an excuse for being late.",
            "options": ["made up", "made out", "made off", "made for"],
            "answer": "made up",
            "explanation": "Make up = bịa ra, dựng lên."
        },
        {
            "question": "The contract will _____ next month.",
            "options": ["run out", "run over", "run into", "run away"],
            "answer": "run out",
            "explanation": "Run out = hết hạn."
        },
        {
            "question": "He _____ his mistakes and apologized.",
            "options": ["owned up to", "owned in to", "owned out to", "owned down to"],
            "answer": "owned up to",
            "explanation": "Own up to = thành thật thừa nhận."
        },
        {
            "question": "The company decided to _____ with the merger.",
            "options": ["go ahead", "go on", "go over", "go through"],
            "answer": "go ahead",
            "explanation": "Go ahead with = tiếp tục thực hiện."
        },
        {
            "question": "She _____ the opportunity to study abroad.",
            "options": ["passed up", "passed on", "passed out", "passed by"],
            "answer": "passed up",
            "explanation": "Pass up = bỏ lỡ (cơ hội)."
        },
        {
            "question": "The story was _____ from generation to generation.",
            "options": ["handed down", "handed over", "handed in", "handed out"],
            "answer": "handed down",
            "explanation": "Hand down = truyền lại (qua các thế hệ)."
        },
        {
            "question": "He _____ a lot of criticism for his decision.",
            "options": ["came in for", "came up with", "came down with", "came out with"],
            "answer": "came in for",
            "explanation": "Come in for = nhận phải (sự phê bình)."
        },
        {
            "question": "The negotiations _____ after several days.",
            "options": ["broke down", "broke up", "broke out", "broke in"],
            "answer": "broke down",
            "explanation": "Break down = thất bại, đổ vỡ (đàm phán)."
        },
        {
            "question": "She _____ her shopping list before going to the supermarket.",
            "options": ["drew up", "drew in", "drew out", "drew on"],
            "answer": "drew up",
            "explanation": "Draw up = lập ra, soạn thảo (danh sách, kế hoạch)."
        },
        {
            "question": "The company is trying to _____ its image.",
            "options": ["build up", "build on", "build in", "build out"],
            "answer": "build up",
            "explanation": "Build up = xây dựng, tạo dựng (hình ảnh, uy tín)."
        },
        
        # ==================== EMPHASIS & FOCUS (15 câu) ====================
        {
            "question": "It _____ in 1945 that World War II ended.",
            "options": ["is", "was", "has been", "had been"],
            "answer": "was",
            "explanation": "Câu chẻ nhấn mạnh thời gian: It was in 1945 that..."
        },
        {
            "question": "_____ I admire most about her is her determination.",
            "options": ["That", "What", "Which", "Who"],
            "answer": "What",
            "explanation": "What = cái mà (câu chẻ với What để nhấn mạnh)."
        },
        {
            "question": "It was Mary _____ told me the news.",
            "options": ["who", "which", "whose", "whom"],
            "answer": "who",
            "explanation": "Câu chẻ nhấn mạnh chủ ngữ: It was Mary who..."
        },
        {
            "question": "_____ we need is more time.",
            "options": ["That", "What", "Which", "Who"],
            "answer": "What",
            "explanation": "What + S + V + is...: cái chúng ta cần là."
        },
        {
            "question": "It is on Sunday _____ we usually visit our grandparents.",
            "options": ["when", "that", "which", "where"],
            "answer": "that",
            "explanation": "Câu chẻ nhấn mạnh thời gian: It is on Sunday that... (dùng that, không dùng when)."
        },
        {
            "question": "_____ surprised me was his reaction.",
            "options": ["That", "What", "Which", "Who"],
            "answer": "What",
            "explanation": "What + V + O: cái làm tôi ngạc nhiên là."
        },
        {
            "question": "It was in Paris _____ they first met.",
            "options": ["where", "that", "which", "when"],
            "answer": "that",
            "explanation": "Câu chẻ nhấn mạnh địa điểm: It was in Paris that... (dùng that)."
        },
        {
            "question": "_____ matters most is your health.",
            "options": ["That", "What", "Which", "Who"],
            "answer": "What",
            "explanation": "What + V + adv: cái quan trọng nhất là."
        },
        {
            "question": "It was not until midnight _____ he returned home.",
            "options": ["when", "that", "which", "where"],
            "answer": "that",
            "explanation": "It was not until... that...: mãi cho đến... thì mới."
        },
        {
            "question": "_____ I can't understand is why he left.",
            "options": ["That", "What", "Which", "Who"],
            "answer": "What",
            "explanation": "What + S + can't V: cái tôi không thể hiểu là."
        },
        {
            "question": "It was the blue dress _____ she bought.",
            "options": ["who", "which", "that", "whose"],
            "answer": "that",
            "explanation": "Câu chẻ nhấn mạnh tân ngữ: It was... that..."
        },
        {
            "question": "_____ she said made everyone angry.",
            "options": ["That", "What", "Which", "Who"],
            "answer": "What",
            "explanation": "What + S + V: cái mà cô ấy nói."
        },
        {
            "question": "It is you _____ should apologize.",
            "options": ["who", "which", "that", "whose"],
            "answer": "who",
            "explanation": "Câu chẻ nhấn mạnh chủ ngữ người: It is you who... (có thể dùng that)."
        },
        {
            "question": "_____ I want to know is the truth.",
            "options": ["That", "What", "Which", "Who"],
            "answer": "What",
            "explanation": "What + S + V + is...: cái tôi muốn biết là."
        },
        {
            "question": "It was his kindness _____ impressed me.",
            "options": ["who", "which", "that", "whose"],
            "answer": "that",
            "explanation": "Câu chẻ nhấn mạnh chủ ngữ vật: It was... that..."
        },
        
        # ==================== READING COMPREHENSION SKILLS (20 câu) ====================
        {
            "question": "The word 'plethora' in the passage is closest in meaning to _____.",
            "options": ["shortage", "abundance", "lack", "scarcity"],
            "answer": "abundance",
            "explanation": "Plethora = sự dồi dào, phong phú = abundance."
        },
        {
            "question": "The author's attitude towards the subject can be described as _____.",
            "options": ["neutral", "critical", "supportive", "indifferent"],
            "answer": "supportive",
            "explanation": "Thái độ của tác giả được thể hiện qua các từ ngữ tích cực trong bài."
        },
        {
            "question": "Which of the following is NOT mentioned in the passage?",
            "options": ["Economic factors", "Social issues", "Political aspects", "Religious beliefs"],
            "answer": "Religious beliefs",
            "explanation": "Đọc kỹ để tìm thông tin không được đề cập."
        },
        {
            "question": "The word 'it' in line 5 refers to _____.",
            "options": ["the problem", "the solution", "the government", "the policy"],
            "answer": "the problem",
            "explanation": "Đại từ 'it' thay thế cho danh từ gần nhất phù hợp về ngữ cảnh."
        },
        {
            "question": "According to the passage, the main cause of the problem is _____.",
            "options": ["lack of funding", "poor management", "inadequate training", "insufficient resources"],
            "answer": "poor management",
            "explanation": "Nguyên nhân chính được nêu rõ trong đoạn văn."
        },
        {
            "question": "The word 'mitigate' in the text is closest in meaning to _____.",
            "options": ["worsen", "reduce", "eliminate", "increase"],
            "answer": "reduce",
            "explanation": "Mitigate = giảm nhẹ, làm dịu đi = reduce."
        },
        {
            "question": "What can be inferred from the passage?",
            "options": [
                "The situation will improve soon",
                "More research is needed",
                "The problem is unsolvable",
                "Current methods are sufficient"
            ],
            "answer": "More research is needed",
            "explanation": "Suy luận dựa trên thông tin gián tiếp trong bài."
        },
        {
            "question": "The tone of the passage is _____.",
            "options": ["humorous", "serious", "sarcastic", "lighthearted"],
            "answer": "serious",
            "explanation": "Giọng văn nghiêm túc thể hiện qua cách dùng từ và nội dung."
        },
        {
            "question": "Which of the following best summarizes the passage?",
            "options": [
                "A detailed analysis of the issue",
                "A personal opinion on the matter",
                "A historical account",
                "A comparison of different views"
            ],
            "answer": "A detailed analysis of the issue",
            "explanation": "Tóm tắt phải bao quát ý chính của toàn bài."
        },
        {
            "question": "The word 'paramount' in the passage means _____.",
            "options": ["minor", "significant", "supreme", "irrelevant"],
            "answer": "supreme",
            "explanation": "Paramount = tối quan trọng = supreme."
        },
        {
            "question": "The author mentions the example to _____.",
            "options": [
                "support the main argument",
                "contradict the previous statement",
                "introduce a new topic",
                "confuse the reader"
            ],
            "answer": "support the main argument",
            "explanation": "Ví dụ thường được dùng để minh họa cho luận điểm chính."
        },
        {
            "question": "The phrase 'in the long run' in the text means _____.",
            "options": ["immediately", "eventually", "temporarily", "never"],
            "answer": "eventually",
            "explanation": "In the long run = về lâu dài, cuối cùng = eventually."
        },
        {
            "question": "What is the main purpose of the passage?",
            "options": [
                "To entertain readers",
                "To inform about a topic",
                "To persuade the audience",
                "To criticize a policy"
            ],
            "answer": "To inform about a topic",
            "explanation": "Mục đích chính là cung cấp thông tin."
        },
        {
            "question": "The word 'contemporary' is closest in meaning to _____.",
            "options": ["ancient", "modern", "traditional", "historical"],
            "answer": "modern",
            "explanation": "Contemporary = đương đại, hiện đại = modern."
        },
        {
            "question": "Which statement would the author most likely agree with?",
            "options": [
                "The problem is exaggerated",
                "Immediate action is necessary",
                "The situation is hopeless",
                "Current approaches are effective"
            ],
            "answer": "Immediate action is necessary",
            "explanation": "Quan điểm của tác giả được thể hiện qua các luận điểm trong bài."
        },
        {
            "question": "The word 'detrimental' in the passage means _____.",
            "options": ["beneficial", "harmful", "neutral", "positive"],
            "answer": "harmful",
            "explanation": "Detrimental = có hại = harmful."
        },
        {
            "question": "According to the passage, which is true about the topic?",
            "options": [
                "It has been widely discussed",
                "It is a new phenomenon",
                "It only affects certain groups",
                "It is not important"
            ],
            "answer": "It has been widely discussed",
            "explanation": "Thông tin cụ thể được nêu trong bài."
        },
        {
            "question": "The word 'ubiquitous' in the text means _____.",
            "options": ["rare", "everywhere", "specific", "limited"],
            "answer": "everywhere",
            "explanation": "Ubiquitous = có mặt khắp nơi = everywhere."
        },
        {
            "question": "The passage suggests that _____.",
            "options": [
                "The problem will resolve itself",
                "Collective effort is required",
                "Individual action is sufficient",
                "No solution exists"
            ],
            "answer": "Collective effort is required",
            "explanation": "Gợi ý được thể hiện qua ngữ cảnh của đoạn văn."
        },
        {
            "question": "The word 'advocate' in the passage is closest in meaning to _____.",
            "options": ["oppose", "support", "ignore", "criticize"],
            "answer": "support",
            "explanation": "Advocate = ủng hộ, tán thành = support."
        },
        
        # ==================== SENTENCE TRANSFORMATION (20 câu) ====================
        {
            "question": "'I didn't break the vase,' said Tom. → Tom _____ the vase.",
            "options": ["denied breaking", "denied to break", "denied break", "denied broke"],
            "answer": "denied breaking",
            "explanation": "Deny + V-ing: phủ nhận làm gì."
        },
        {
            "question": "She started learning English 5 years ago. → She _____ English for 5 years.",
            "options": ["learns", "learned", "has learned", "had learned"],
            "answer": "has learned",
            "explanation": "Started... ago → Present Perfect: has/have + V3 + for..."
        },
        {
            "question": "They don't allow smoking here. → Smoking _____ here.",
            "options": ["doesn't allow", "isn't allowed", "hasn't allowed", "wasn't allowed"],
            "answer": "isn't allowed",
            "explanation": "Chuyển sang câu bị động: is not allowed."
        },
        {
            "question": "'Why don't we go to the cinema?' he said. → He suggested _____ to the cinema.",
            "options": ["go", "to go", "going", "went"],
            "answer": "going",
            "explanation": "Suggest + V-ing: gợi ý làm gì."
        },
        {
            "question": "It's two months since I last saw him. → I haven't seen him _____ two months.",
            "options": ["since", "for", "during", "in"],
            "answer": "for",
            "explanation": "Haven't + V3 + for + khoảng thời gian."
        },
        {
            "question": "I'm sorry I didn't attend the meeting. → I regret _____ the meeting.",
            "options": ["not attending", "not to attend", "to not attend", "don't attend"],
            "answer": "not attending",
            "explanation": "Regret + (not) V-ing: hối tiếc đã (không) làm gì."
        },
        {
            "question": "People believe that he is innocent. → He _____ innocent.",
            "options": ["believes to be", "is believed to be", "believed to be", "is believing to be"],
            "answer": "is believed to be",
            "explanation": "Câu bị động với believe: is believed to be."
        },
        {
            "question": "She is too young to get married. → She is not _____ to get married.",
            "options": ["young enough", "old enough", "enough old", "enough young"],
            "answer": "old enough",
            "explanation": "Too young to = not old enough to."
        },
        {
            "question": "'Don't forget to lock the door,' she said. → She reminded me _____ the door.",
            "options": ["lock", "to lock", "locking", "locked"],
            "answer": "to lock",
            "explanation": "Remind + to V: nhắc nhở làm gì."
        },
        {
            "question": "As soon as she arrived, the meeting started. → No sooner _____ than the meeting started.",
            "options": ["she had arrived", "had she arrived", "she arrived", "did she arrive"],
            "answer": "had she arrived",
            "explanation": "No sooner + had + S + V3 + than: vừa mới... thì (đảo ngữ)."
        },
        {
            "question": "Without your help, I couldn't have succeeded. → If it _____ your help, I couldn't have succeeded.",
            "options": ["wasn't for", "weren't for", "hadn't been for", "hasn't been for"],
            "answer": "hadn't been for",
            "explanation": "Without = If it hadn't been for (câu điều kiện loại 3)."
        },
        {
            "question": "'Let's have a picnic,' Mary said. → Mary suggested _____ a picnic.",
            "options": ["have", "to have", "having", "had"],
            "answer": "having",
            "explanation": "Suggest + V-ing: gợi ý làm gì."
        },
        {
            "question": "He said, 'I will finish it tomorrow.' → He said he _____ it the next day.",
            "options": ["will finish", "would finish", "finished", "finishes"],
            "answer": "would finish",
            "explanation": "Reported speech: will → would, tomorrow → the next day."
        },
        {
            "question": "I would rather stay at home than go out. → I prefer _____ at home to going out.",
            "options": ["stay", "staying", "to stay", "stayed"],
            "answer": "staying",
            "explanation": "Prefer + V-ing + to + V-ing."
        },
        {
            "question": "'I'm sorry I'm late,' she said. → She apologized _____ late.",
            "options": ["to be", "for being", "being", "to being"],
            "answer": "for being",
            "explanation": "Apologize for + V-ing: xin lỗi về việc gì."
        },
        {
            "question": "The last time I saw her was in 2020. → I _____ her since 2020.",
            "options": ["don't see", "didn't see", "haven't seen", "hadn't seen"],
            "answer": "haven't seen",
            "explanation": "The last time... was → haven't + V3 + since."
        },
        {
            "question": "He is said to be very rich. → People say that _____.",
            "options": ["he is very rich", "he was very rich", "he has been very rich", "he will be very rich"],
            "answer": "he is very rich",
            "explanation": "Is said to be → People say that + hiện tại."
        },
        {
            "question": "Despite being tired, she continued working. → Although _____, she continued working.",
            "options": ["she tired", "she was tired", "she is tired", "she be tired"],
            "answer": "she was tired",
            "explanation": "Despite + V-ing = Although + S + V."
        },
        {
            "question": "'I didn't take your book,' he said to me. → He denied _____ my book.",
            "options": ["take", "to take", "taking", "took"],
            "answer": "taking",
            "explanation": "Deny + V-ing: phủ nhận làm gì."
        },
        {
            "question": "She wishes she had studied harder. → She regrets _____ harder.",
            "options": ["not study", "not to study", "not studying", "not studied"],
            "answer": "not studying",
            "explanation": "Wish + had + V3 = Regret + (not) V-ing."
        },
        
        # ==================== IDIOMS & EXPRESSIONS ADVANCED (25 câu) ====================
        {
            "question": "She really pulled out all the _____ for the party.",
            "options": ["stops", "steps", "strings", "stakes"],
            "answer": "stops",
            "explanation": "Pull out all the stops = làm hết sức, không tiếc công sức."
        },
        {
            "question": "He's been burning the midnight _____ preparing for exams.",
            "options": ["lamp", "oil", "candle", "light"],
            "answer": "oil",
            "explanation": "Burn the midnight oil = thức khuya làm việc/học."
        },
        {
            "question": "The project is now in full _____.",
            "options": ["swing", "speed", "motion", "force"],
            "answer": "swing",
            "explanation": "In full swing = đang diễn ra sôi nổi."
        },
        {
            "question": "She took his criticism with a grain of _____.",
            "options": ["pepper", "salt", "sugar", "spice"],
            "answer": "salt",
            "explanation": "Take with a grain of salt = không tin hoàn toàn."
        },
        {
            "question": "He's walking on _____ around his boss.",
            "options": ["ice", "eggs", "eggshells", "glass"],
            "answer": "eggshells",
            "explanation": "Walk on eggshells = hành động rất cẩn thận (sợ làm ai đó khó chịu)."
        },
        {
            "question": "The new policy was a blessing in _____.",
            "options": ["disguise", "surprise", "disguised", "surprised"],
            "answer": "disguise",
            "explanation": "A blessing in disguise = điều tốt đằng sau vẻ ngoài xấu."
        },
        {
            "question": "She hit the nail on the _____ with her analysis.",
            "options": ["head", "hand", "finger", "thumb"],
            "answer": "head",
            "explanation": "Hit the nail on the head = nói đúng trọng tâm."
        },
        {
            "question": "The news spread like _____.",
            "options": ["water", "wind", "wildfire", "lightning"],
            "answer": "wildfire",
            "explanation": "Spread like wildfire = lan truyền rất nhanh."
        },
        {
            "question": "He's always beating around the _____.",
            "options": ["tree", "bush", "plant", "garden"],
            "answer": "bush",
            "explanation": "Beat around the bush = nói vòng vo tam quốc."
        },
        {
            "question": "She kept her cards close to her _____.",
            "options": ["heart", "chest", "body", "hand"],
            "answer": "chest",
            "explanation": "Keep cards close to chest = giữ bí mật."
        },
        {
            "question": "The situation is now beyond our _____.",
            "options": ["control", "reach", "grasp", "power"],
            "answer": "control",
            "explanation": "Beyond control = ngoài tầm kiểm soát."
        },
        {
            "question": "She's the black _____ of the family.",
            "options": ["sheep", "horse", "cat", "dog"],
            "answer": "sheep",
            "explanation": "Black sheep = người bị coi thường trong gia đình."
        },
        {
            "question": "He let the cat out of the _____.",
            "options": ["box", "bag", "basket", "house"],
            "answer": "bag",
            "explanation": "Let the cat out of the bag = để lộ bí mật."
        },
        {
            "question": "She's got a chip on her _____.",
            "options": ["head", "shoulder", "back", "arm"],
            "answer": "shoulder",
            "explanation": "Have a chip on one's shoulder = hay cáu gắt, dễ bị xúc phạm."
        },
        {
            "question": "The ball is in your _____ now.",
            "options": ["hand", "court", "field", "ground"],
            "answer": "court",
            "explanation": "The ball is in your court = đến lượt bạn quyết định/hành động."
        },
        {
            "question": "He's got his head in the _____.",
            "options": ["sky", "clouds", "stars", "moon"],
            "answer": "clouds",
            "explanation": "Head in the clouds = mơ mộng, không thực tế."
        },
        {
            "question": "She really went the extra _____.",
            "options": ["mile", "step", "way", "distance"],
            "answer": "mile",
            "explanation": "Go the extra mile = nỗ lực thêm, làm nhiều hơn mong đợi."
        },
        {
            "question": "The project got off to a flying _____.",
            "options": ["start", "begin", "launch", "opening"],
            "answer": "start",
            "explanation": "Get off to a flying start = bắt đầu thuận lợi."
        },
        {
            "question": "He's sitting on the _____.",
            "options": ["wall", "fence", "gate", "door"],
            "answer": "fence",
            "explanation": "Sit on the fence = do dự, không quyết định."
        },
        {
            "question": "She's at the end of her _____.",
            "options": ["rope", "string", "line", "thread"],
            "answer": "rope",
            "explanation": "At the end of one's rope = kiệt sức, không còn kiên nhẫn."
        },
        {
            "question": "The deal fell _____.",
            "options": ["through", "down", "off", "out"],
            "answer": "through",
            "explanation": "Fall through = thất bại, không thành công (kế hoạch, thỏa thuận)."
        },
        {
            "question": "He's got too many irons in the _____.",
            "options": ["fire", "flame", "heat", "burn"],
            "answer": "fire",
            "explanation": "Too many irons in the fire = làm quá nhiều việc cùng lúc."
        },
        {
            "question": "She's keeping up _____.",
            "options": ["faces", "fronts", "shows", "appearances"],
            "answer": "appearances",
            "explanation": "Keep up appearances = giữ thể diện."
        },
        {
            "question": "The company is on its last _____.",
            "options": ["legs", "feet", "hands", "arms"],
            "answer": "legs",
            "explanation": "On one's last legs = sắp sụp đổ, kiệt sức."
        },
        {
            "question": "He really stuck his neck _____.",
            "options": ["in", "out", "up", "down"],
            "answer": "out",
            "explanation": "Stick one's neck out = mạo hiểm, liều lĩnh."
        }
]