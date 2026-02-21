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
            "question": "The committee has decided to _____ the proposal until further information is available.",
            "options": ["postpone", "cancel", "reject", "approve"],
            "answer": "postpone",
            "explanation": "Postpone (hoãn lại) phù hợp nhất với ngữ cảnh 'until further information is available'."
        },
        {
            "question": "Which sentence uses the subjunctive mood correctly?",
            "options": [
                "I suggest that he goes to the doctor immediately.",
                "I suggest that he go to the doctor immediately.",
                "I suggest that he will go to the doctor immediately.",
                "I suggest that he is going to the doctor immediately."
            ],
            "answer": "I suggest that he go to the doctor immediately.",
            "explanation": "Sau động từ 'suggest', ta dùng subjunctive mood: suggest + that + S + V(bare infinitive)."
        },
        {
            "question": "_____ the heavy rain, the outdoor concert was not cancelled.",
            "options": ["Although", "Despite", "Because of", "Due to"],
            "answer": "Despite",
            "explanation": "Despite + noun phrase (the heavy rain). Although + clause."
        },
        {
            "question": "By the time the report is published next month, the team _____ on it for over a year.",
            "options": [
                "will work",
                "will be working",
                "will have been working",
                "has been working"
            ],
            "answer": "will have been working",
            "explanation": "By the time + tương lai → dùng Future Perfect Continuous."
        },
        {
            "question": "Which sentence demonstrates proper parallel structure?",
            "options": [
                "She enjoys reading, writing, and to paint.",
                "She enjoys reading, writing, and painting.",
                "She enjoys to read, writing, and painting.",
                "She enjoys reading, to write, and painting."
            ],
            "answer": "She enjoys reading, writing, and painting.",
            "explanation": "Parallel structure yêu cầu các thành phần liệt kê có cấu trúc giống nhau."
        },
        {
            "question": "_____ thoroughly researched, the thesis still contained several factual errors.",
            "options": ["Despite being", "Although it was", "In spite of", "Even though"],
            "answer": "Despite being",
            "explanation": "Sau chỗ trống là V-ed (researched), cần cấu trúc Despite/In spite of + being + V-ed."
        },
        {
            "question": "Hardly _____ the presentation when the fire alarm went off.",
            "options": [
                "had she begun",
                "she had begun",
                "she has begun",
                "has she begun"
            ],
            "answer": "had she begun",
            "explanation": "Hardly + had + S + V3 (đảo ngữ với Hardly)."
        },
        {
            "question": "The manager requested that all employees _____ the new safety procedures.",
            "options": ["follow", "follows", "followed", "will follow"],
            "answer": "follow",
            "explanation": "Request + that + S + V(bare infinitive) - dùng subjunctive mood."
        },
        {
            "question": "Not only _____ the deadline, but she also exceeded expectations.",
            "options": [
                "did she meet",
                "she met",
                "she did meet",
                "met she"
            ],
            "answer": "did she meet",
            "explanation": "Not only + auxiliary + S + V (đảo ngữ)."
        },
        {
            "question": "Were I in your position, I _____ a different approach.",
            "options": [
                "would take",
                "will take",
                "would have taken",
                "take"
            ],
            "answer": "would take",
            "explanation": "Were I = If I were (đảo ngữ câu điều kiện loại 2)."
        },
        {
            "question": "The contract stipulates that payment _____ within 30 days of invoice.",
            "options": ["be made", "is made", "will be made", "should make"],
            "answer": "be made",
            "explanation": "Stipulate + that + S + be + V3 (subjunctive mood)."
        },
        {
            "question": "She would rather _____ at home than go to the party.",
            "options": ["stay", "stays", "staying", "to stay"],
            "answer": "stay",
            "explanation": "Would rather + V(bare infinitive)."
        },
        {
            "question": "No sooner _____ the office than it started raining.",
            "options": [
                "had I left",
                "I had left",
                "did I leave",
                "I have left"
            ],
            "answer": "had I left",
            "explanation": "No sooner + had + S + V3 (đảo ngữ)."
        },
        {
            "question": "It is imperative that he _____ on time for the meeting.",
            "options": ["arrive", "arrives", "arrived", "will arrive"],
            "answer": "arrive",
            "explanation": "It is imperative that + S + V(bare infinitive) - subjunctive mood."
        },
        {
            "question": "The document needs _____ before submission.",
            "options": ["revising", "to revise", "revised", "revise"],
            "answer": "revising",
            "explanation": "Need + V-ing (passive meaning) = need to be revised."
        },
        {
            "question": "_____ more carefully, she would have noticed the mistake.",
            "options": [
                "Had she read",
                "If she read",
                "Should she read",
                "Were she to read"
            ],
            "answer": "Had she read",
            "explanation": "Had + S + V3 (đảo ngữ câu điều kiện loại 3)."
        },
        {
            "question": "The professor insisted that the student _____ the experiment again.",
            "options": ["conduct", "conducts", "conducted", "will conduct"],
            "answer": "conduct",
            "explanation": "Insist + that + S + V(bare infinitive) - subjunctive mood."
        },
        {
            "question": "Under no circumstances _____ this information to unauthorized personnel.",
            "options": [
                "should you disclose",
                "you should disclose",
                "you disclose",
                "disclose you"
            ],
            "answer": "should you disclose",
            "explanation": "Under no circumstances + auxiliary + S + V (đảo ngữ)."
        },
        {
            "question": "I wish I _____ more attention during the lecture.",
            "options": [
                "had paid",
                "paid",
                "have paid",
                "pay"
            ],
            "answer": "had paid",
            "explanation": "Wish + S + had + V3 (ước về quá khứ)."
        },
        {
            "question": "Seldom _____ such dedication in a student.",
            "options": [
                "have I seen",
                "I have seen",
                "do I see",
                "I see"
            ],
            "answer": "have I seen",
            "explanation": "Seldom + auxiliary + S + V (đảo ngữ với trạng từ phủ định)."
        },
        {
            "question": "The company's policy requires that all visitors _____ identification.",
            "options": ["show", "shows", "showed", "will show"],
            "answer": "show",
            "explanation": "Require + that + S + V(bare infinitive) - subjunctive mood."
        },
        {
            "question": "_____ the circumstances, we decided to proceed with the project.",
            "options": ["Given", "Giving", "Give", "To give"],
            "answer": "Given",
            "explanation": "Given = xét về, xét cho - dạng participle làm liên từ."
        },
        {
            "question": "Neither the students nor the teacher _____ aware of the schedule change.",
            "options": ["was", "were", "are", "is"],
            "answer": "was",
            "explanation": "Neither...nor: động từ chia theo chủ ngữ gần nhất (the teacher - số ít)."
        },
        {
            "question": "She acts as if she _____ the owner of the company.",
            "options": ["were", "was", "is", "has been"],
            "answer": "were",
            "explanation": "As if + S + were (subjunctive mood cho tình huống không có thật)."
        },
        {
            "question": "It's high time we _____ action on climate change.",
            "options": ["took", "take", "have taken", "will take"],
            "answer": "took",
            "explanation": "It's high time + S + V(past) - cấu trúc đặc biệt."
        },
        {
            "question": "The results were _____ what we had anticipated.",
            "options": ["far better than", "far better as", "much better from", "very better than"],
            "answer": "far better than",
            "explanation": "Far/much + comparative + than (nhấn mạnh so sánh)."
        },
        {
            "question": "_____ he had prepared thoroughly, he still felt nervous.",
            "options": ["Although", "Despite", "However", "In spite"],
            "answer": "Although",
            "explanation": "Although + clause. Despite/In spite + noun/V-ing."
        },
        {
            "question": "The data _____ analyzed before any conclusions can be drawn.",
            "options": ["must be", "must", "must have", "must have been"],
            "answer": "must be",
            "explanation": "Modal + be + V3 (passive voice)."
        },
        {
            "question": "Little _____ that this decision would change his life.",
            "options": [
                "did he know",
                "he knew",
                "he did know",
                "knew he"
            ],
            "answer": "did he know",
            "explanation": "Little + auxiliary + S + V (đảo ngữ với Little)."
        },
        {
            "question": "The conference _____ next month has been postponed indefinitely.",
            "options": [
                "scheduled for",
                "scheduling for",
                "which scheduled for",
                "that scheduling for"
            ],
            "answer": "scheduled for",
            "explanation": "Reduced relative clause: which is scheduled for → scheduled for."
        },
        {
            "question": "_____ to the meeting, I would have voiced my concerns.",
            "options": [
                "Had I been invited",
                "If I invited",
                "Were I invited",
                "Should I be invited"
            ],
            "answer": "Had I been invited",
            "explanation": "Had + S + been + V3 (đảo ngữ câu điều kiện loại 3 với passive)."
        },
        {
            "question": "Not until the deadline passed _____ realize the importance of time management.",
            "options": [
                "did he",
                "he did",
                "he does",
                "does he"
            ],
            "answer": "did he",
            "explanation": "Not until + phrase/clause + auxiliary + S + V (đảo ngữ)."
        },
        {
            "question": "The teacher recommended that each student _____ a dictionary.",
            "options": ["bring", "brings", "brought", "will bring"],
            "answer": "bring",
            "explanation": "Recommend + that + S + V(bare infinitive) - subjunctive mood."
        },
        {
            "question": "_____ the budget constraints, the project was completed successfully.",
            "options": ["Despite", "Although", "However", "Because"],
            "answer": "Despite",
            "explanation": "Despite + noun phrase. Although + clause."
        },
        {
            "question": "I'd rather you _____ smoke in the office.",
            "options": ["didn't", "don't", "won't", "haven't"],
            "answer": "didn't",
            "explanation": "Would rather + S + V(past) - diễn tả mong muốn về hiện tại."
        },
        {
            "question": "Only after finishing the report _____ how challenging it was.",
            "options": [
                "did she realize",
                "she realized",
                "she did realize",
                "realized she"
            ],
            "answer": "did she realize",
            "explanation": "Only after + phrase + auxiliary + S + V (đảo ngữ)."
        },
        {
            "question": "The medication should _____ with food.",
            "options": ["be taken", "take", "taken", "taking"],
            "answer": "be taken",
            "explanation": "Should + be + V3 (passive voice)."
        },
        {
            "question": "_____ studying harder, he might have passed the exam.",
            "options": ["By", "With", "Through", "For"],
            "answer": "By",
            "explanation": "By + V-ing = bằng cách."
        },
        {
            "question": "The proposal _____ by the board next week.",
            "options": [
                "will be reviewed",
                "will review",
                "reviews",
                "is reviewing"
            ],
            "answer": "will be reviewed",
            "explanation": "Will + be + V3 (future passive)."
        },
        {
            "question": "So complex _____ that few people understood it.",
            "options": [
                "was the theory",
                "the theory was",
                "is the theory",
                "the theory is"
            ],
            "answer": "was the theory",
            "explanation": "So + adjective + be + S (đảo ngữ nhấn mạnh)."
        },
        
        # ==================== VOCABULARY - ACADEMIC (30 câu) ====================
        {
            "question": "The researcher's findings were _____ with previous studies in the field.",
            "options": ["consistent", "resistant", "persistent", "insistent"],
            "answer": "consistent",
            "explanation": "Consistent with = phù hợp với, nhất quán với."
        },
        {
            "question": "The professor's lecture was so _____ that several students fell asleep.",
            "options": ["tedious", "tenacious", "meticulous", "vivacious"],
            "answer": "tedious",
            "explanation": "Tedious = buồn tẻ, nhàm chán."
        },
        {
            "question": "The company's new policy aims to _____ employee satisfaction and productivity.",
            "options": ["enhance", "hinder", "diminish", "restrict"],
            "answer": "enhance",
            "explanation": "Enhance = nâng cao, cải thiện."
        },
        {
            "question": "The data collected from the experiment proved to be _____ for drawing meaningful conclusions.",
            "options": ["insufficient", "affluent", "efficient", "proficient"],
            "answer": "insufficient",
            "explanation": "Insufficient = không đủ, thiếu."
        },
        {
            "question": "The author's argument lacks _____ evidence to support the main claim.",
            "options": ["empirical", "imperial", "emphatic", "empathetic"],
            "answer": "empirical",
            "explanation": "Empirical evidence = bằng chứng thực nghiệm."
        },
        {
            "question": "The government's decision to implement the policy was met with _____ from various interest groups.",
            "options": ["resistance", "assistance", "persistence", "insistence"],
            "answer": "resistance",
            "explanation": "Resistance = sự phản kháng, chống đối."
        },
        {
            "question": "The scientist's theory was considered _____ because it challenged established beliefs.",
            "options": ["conventional", "traditional", "radical", "typical"],
            "answer": "radical",
            "explanation": "Radical = cực đoan, triệt để, mang tính cách mạng."
        },
        {
            "question": "The study's findings have _____ implications for public health policy.",
            "options": ["significant", "insignificant", "magnificent", "malignant"],
            "answer": "significant",
            "explanation": "Significant implications = ý nghĩa/tác động quan trọng."
        },
        {
            "question": "The novel explores themes of identity and _____ in contemporary society.",
            "options": ["alienate", "alien", "alienation", "alienated"],
            "answer": "alienation",
            "explanation": "Alienation (sự xa lánh, cô lập) là danh từ phù hợp."
        },
        {
            "question": "The committee decided to _____ the outdated regulations.",
            "options": ["abolish", "polish", "establish", "publish"],
            "answer": "abolish",
            "explanation": "Abolish = bãi bỏ, hủy bỏ."
        },
        {
            "question": "The research methodology was _____ and followed international standards.",
            "options": ["rigorous", "vigorous", "frivolous", "conspicuous"],
            "answer": "rigorous",
            "explanation": "Rigorous = nghiêm ngặt, chặt chẽ."
        },
        {
            "question": "The author's writing style is known for its _____ and clarity.",
            "options": ["ambiguity", "brevity", "complexity", "obscurity"],
            "answer": "brevity",
            "explanation": "Brevity = sự ngắn gọn, súc tích."
        },
        {
            "question": "The economic downturn had a _____ effect on small businesses.",
            "options": ["detrimental", "beneficial", "neutral", "favorable"],
            "answer": "detrimental",
            "explanation": "Detrimental = có hại, bất lợi."
        },
        {
            "question": "The scholar's work contributed significantly to the _____ of knowledge in the field.",
            "options": ["advancement", "retirement", "treatment", "adjustment"],
            "answer": "advancement",
            "explanation": "Advancement of knowledge = sự phát triển kiến thức."
        },
        {
            "question": "The patient showed remarkable _____ after receiving treatment.",
            "options": ["deterioration", "improvement", "complication", "inflammation"],
            "answer": "improvement",
            "explanation": "Improvement = sự cải thiện, tiến bộ."
        },
        {
            "question": "The debate centered on the _____ of implementing new environmental regulations.",
            "options": ["feasibility", "possibility", "probability", "capability"],
            "answer": "feasibility",
            "explanation": "Feasibility = tính khả thi."
        },
        {
            "question": "The artist's work is characterized by its _____ and innovative approach.",
            "options": ["originality", "triviality", "banality", "mortality"],
            "answer": "originality",
            "explanation": "Originality = tính độc đáo, sáng tạo."
        },
        {
            "question": "The company demonstrated its _____ to environmental sustainability.",
            "options": ["commitment", "retirement", "treatment", "adjustment"],
            "answer": "commitment",
            "explanation": "Commitment to = sự cam kết với."
        },
        {
            "question": "The findings of the study _____ earlier research on the topic.",
            "options": ["corroborate", "corporate", "collaborate", "commemorate"],
            "answer": "corroborate",
            "explanation": "Corroborate = xác nhận, củng cố."
        },
        {
            "question": "The philosopher's ideas had a _____ influence on modern thought.",
            "options": ["profound", "superficial", "trivial", "marginal"],
            "answer": "profound",
            "explanation": "Profound = sâu sắc, có ý nghĩa lớn."
        },
        {
            "question": "The technology sector is known for its rapid _____ and innovation.",
            "options": ["evolution", "revolution", "resolution", "dissolution"],
            "answer": "evolution",
            "explanation": "Evolution = sự tiến hóa, phát triển."
        },
        {
            "question": "The report provides a _____ analysis of the current economic situation.",
            "options": ["comprehensive", "apprehensive", "defensive", "offensive"],
            "answer": "comprehensive",
            "explanation": "Comprehensive = toàn diện, bao quát."
        },
        {
            "question": "The researcher's approach was highly _____ and based on systematic observation.",
            "options": ["analytical", "analogical", "anarchical", "apolitical"],
            "answer": "analytical",
            "explanation": "Analytical = mang tính phân tích."
        },
        {
            "question": "The new policy aims to _____ discrimination in the workplace.",
            "options": ["eliminate", "illuminate", "nominate", "dominate"],
            "answer": "eliminate",
            "explanation": "Eliminate = loại bỏ, xóa bỏ."
        },
        {
            "question": "The study revealed a _____ between smoking and lung disease.",
            "options": ["correlation", "corporation", "coronation", "cooperation"],
            "answer": "correlation",
            "explanation": "Correlation = mối tương quan."
        },
        {
            "question": "The author's perspective on the issue is quite _____.",
            "options": ["controversial", "conversational", "conventional", "provisional"],
            "answer": "controversial",
            "explanation": "Controversial = gây tranh cãi."
        },
        {
            "question": "The experiment was conducted under _____ laboratory conditions.",
            "options": ["controlled", "controlling", "controllable", "uncontrolled"],
            "answer": "controlled",
            "explanation": "Controlled conditions = điều kiện được kiểm soát."
        },
        {
            "question": "The company's success can be _____ to its innovative marketing strategy.",
            "options": ["attributed", "contributed", "distributed", "substituted"],
            "answer": "attributed",
            "explanation": "Be attributed to = được quy cho."
        },
        {
            "question": "The research team maintained _____ throughout the experiment.",
            "options": ["objectivity", "subjectivity", "creativity", "sensitivity"],
            "answer": "objectivity",
            "explanation": "Objectivity = tính khách quan."
        },
        {
            "question": "The theory remains _____ despite years of research.",
            "options": ["speculative", "spectative", "spectacular", "perspective"],
            "answer": "speculative",
            "explanation": "Speculative = mang tính suy đoán."
        },
        
        # ==================== READING COMPREHENSION (25 câu) ====================
        {
            "question": "In academic writing, which transition word best indicates contrast?",
            "options": ["Furthermore", "Consequently", "Nevertheless", "Similarly"],
            "answer": "Nevertheless",
            "explanation": "Nevertheless = tuy nhiên, chỉ sự tương phản."
        },
        {
            "question": "The term 'correlation' in research indicates that two variables _____.",
            "options": [
                "have a cause-and-effect relationship",
                "are completely unrelated",
                "show a relationship but not necessarily causation",
                "always occur simultaneously"
            ],
            "answer": "show a relationship but not necessarily causation",
            "explanation": "Correlation ≠ Causation. Tương quan không chứng minh nhân quả."
        },
        {
            "question": "A 'hypothesis' in scientific research is best described as _____.",
            "options": [
                "a proven fact",
                "a testable prediction",
                "a final conclusion",
                "an unquestionable theory"
            ],
            "answer": "a testable prediction",
            "explanation": "Hypothesis = giả thuyết, là dự đoán có thể kiểm chứng."
        },
        {
            "question": "When an author uses 'anecdotal evidence', they are using _____.",
            "options": [
                "statistical data from large samples",
                "personal stories or individual cases",
                "peer-reviewed scientific studies",
                "mathematical proofs"
            ],
            "answer": "personal stories or individual cases",
            "explanation": "Anecdotal evidence = bằng chứng giai thoại, dựa trên trải nghiệm cá nhân."
        },
        {
            "question": "The phrase 'to refute an argument' means to _____.",
            "options": [
                "support the argument with additional evidence",
                "prove the argument is false or incorrect",
                "ignore the argument completely",
                "rephrase the argument more clearly"
            ],
            "answer": "prove the argument is false or incorrect",
            "explanation": "Refute = bác bỏ, phản bác lập luận."
        },
        {
            "question": "A 'peer-reviewed' article means it has been _____.",
            "options": [
                "read by many people",
                "evaluated by experts in the field",
                "published in a popular magazine",
                "written by multiple authors"
            ],
            "answer": "evaluated by experts in the field",
            "explanation": "Peer-reviewed = được đánh giá bởi các chuyên gia cùng lĩnh vực."
        },
        {
            "question": "In research, a 'control group' is used to _____.",
            "options": [
                "regulate the behavior of participants",
                "provide a baseline for comparison",
                "ensure all participants are similar",
                "control the research budget"
            ],
            "answer": "provide a baseline for comparison",
            "explanation": "Control group = nhóm đối chứng, cung cấp cơ sở để so sánh."
        },
        {
            "question": "The term 'abstract' in an academic paper refers to _____.",
            "options": [
                "complex and difficult ideas",
                "a brief summary of the research",
                "the theoretical framework",
                "artistic or creative writing"
            ],
            "answer": "a brief summary of the research",
            "explanation": "Abstract = phần tóm tắt ngắn gọn của nghiên cứu."
        },
        {
            "question": "When a study has 'external validity', it means _____.",
            "options": [
                "the results are statistically significant",
                "the findings can be generalized to other contexts",
                "the research was conducted ethically",
                "the data was collected properly"
            ],
            "answer": "the findings can be generalized to other contexts",
            "explanation": "External validity = tính giá trị bên ngoài, khả năng tổng quát hóa."
        },
        {
            "question": "A 'sample size' in research refers to _____.",
            "options": [
                "the physical size of the research materials",
                "the number of participants or observations",
                "the duration of the study",
                "the amount of data collected"
            ],
            "answer": "the number of participants or observations",
            "explanation": "Sample size = cỡ mẫu, số lượng người tham gia hoặc quan sát."
        },
        {
            "question": "The 'methodology' section of a paper describes _____.",
            "options": [
                "the results of the study",
                "how the research was conducted",
                "the literature review",
                "the author's conclusions"
            ],
            "answer": "how the research was conducted",
            "explanation": "Methodology = phương pháp luận, mô tả cách thực hiện nghiên cứu."
        },
        {
            "question": "In academic writing, 'objectivity' means _____.",
            "options": [
                "writing about objects",
                "presenting information without personal bias",
                "setting clear objectives",
                "objecting to other viewpoints"
            ],
            "answer": "presenting information without personal bias",
            "explanation": "Objectivity = tính khách quan, trình bày không thiên vị."
        },
        {
            "question": "A 'longitudinal study' is characterized by _____.",
            "options": [
                "studying very long subjects",
                "research conducted over an extended period",
                "examining geographical length",
                "using lengthy questionnaires"
            ],
            "answer": "research conducted over an extended period",
            "explanation": "Longitudinal study = nghiên cứu dọc, theo dõi trong thời gian dài."
        },
        {
            "question": "The term 'variable' in research refers to _____.",
            "options": [
                "something that changes or can be changed",
                "inconsistent data",
                "unreliable results",
                "varying opinions"
            ],
            "answer": "something that changes or can be changed",
            "explanation": "Variable = biến số, yếu tố có thể thay đổi hoặc được thay đổi."
        },
        {
            "question": "When research findings are 'statistically significant', it means _____.",
            "options": [
                "the results are very important",
                "the results are unlikely to have occurred by chance",
                "many statistics were used",
                "the numbers are large"
            ],
            "answer": "the results are unlikely to have occurred by chance",
            "explanation": "Statistical significance = ý nghĩa thống kê, kết quả không phải do ngẫu nhiên."
        },
        {
            "question": "A 'qualitative' research approach focuses on _____.",
            "options": [
                "numerical data and statistics",
                "quality control in experiments",
                "non-numerical data like experiences and meanings",
                "the quantity of participants"
            ],
            "answer": "non-numerical data like experiences and meanings",
            "explanation": "Qualitative = định tính, tập trung vào dữ liệu phi số liệu."
        },
        {
            "question": "The 'literature review' section serves to _____.",
            "options": [
                "review literary works like novels",
                "summarize existing research on the topic",
                "list all books the author has read",
                "critique other researchers personally"
            ],
            "answer": "summarize existing research on the topic",
            "explanation": "Literature review = tổng quan tài liệu, tóm tắt nghiên cứu hiện có."
        },
        {
            "question": "When a researcher uses 'triangulation', they are _____.",
            "options": [
                "studying triangles",
                "using multiple methods to study the same phenomenon",
                "working with three researchers",
                "dividing participants into three groups"
            ],
            "answer": "using multiple methods to study the same phenomenon",
            "explanation": "Triangulation = tam giác hóa, dùng nhiều phương pháp để tăng độ tin cậy."
        },
        {
            "question": "An 'operational definition' in research _____.",
            "options": [
                "defines how to operate equipment",
                "specifies how a concept will be measured",
                "explains operational procedures",
                "defines business operations"
            ],
            "answer": "specifies how a concept will be measured",
            "explanation": "Operational definition = định nghĩa thao tác, cách đo lường khái niệm."
        },
        {
            "question": "The term 'bias' in research refers to _____.",
            "options": [
                "personal opinions in everyday conversation",
                "systematic error that skews results in a particular direction",
                "random variation in data",
                "the conclusion of a study"
            ],
            "answer": "systematic error that skews results in a particular direction",
            "explanation": "Bias = sai lệch có hệ thống làm kết quả nghiêng về một hướng."
        },
        {
            "question": "A 'pilot study' is conducted to _____.",
            "options": [
                "study airplane pilots",
                "test research procedures on a small scale",
                "guide other studies",
                "train research assistants"
            ],
            "answer": "test research procedures on a small scale",
            "explanation": "Pilot study = nghiên cứu thí điểm, thử nghiệm quy trình trước khi nghiên cứu chính."
        },
        {
            "question": "When results are 'replicable', it means _____.",
            "options": [
                "they can be copied easily",
                "other researchers can obtain similar results",
                "they involve replication of DNA",
                "they are repeated in the same study"
            ],
            "answer": "other researchers can obtain similar results",
            "explanation": "Replicable = có thể tái lập, nhà nghiên cứu khác có thể thu được kết quả tương tự."
        },
        {
            "question": "The 'dependent variable' in an experiment is _____.",
            "options": [
                "the variable that is manipulated",
                "the variable that is measured",
                "the variable that depends on funding",
                "any variable in the study"
            ],
            "answer": "the variable that is measured",
            "explanation": "Dependent variable = biến phụ thuộc, biến được đo lường."
        },
        {
            "question": "A 'cross-sectional study' examines _____.",
            "options": [
                "data from different sections of society",
                "data collected at one point in time",
                "cross-cultural differences",
                "intersecting variables"
            ],
            "answer": "data collected at one point in time",
            "explanation": "Cross-sectional study = nghiên cứu cắt ngang, thu thập dữ liệu tại một thời điểm."
        },
        {
            "question": "What does it mean to evaluate sources for 'credibility'?",
            "options": [
                "Check if the source agrees with your opinion",
                "Assess the author's expertise, evidence quality, and potential bias",
                "Count the number of references cited",
                "Determine if the source is easy to read"
            ],
            "answer": "Assess the author's expertise, evidence quality, and potential bias",
            "explanation": "Credibility = độ tin cậy, đánh giá qua chuyên môn, chất lượng bằng chứng và thiên vị."
        },
        
        # ==================== ACADEMIC WRITING (20 câu) ====================
        {
            "question": "Which sentence is most appropriate for formal academic writing?",
            "options": [
                "The results are pretty interesting and stuff.",
                "The results demonstrate a significant correlation.",
                "The results are kinda cool, you know?",
                "We think the results are awesome."
            ],
            "answer": "The results demonstrate a significant correlation.",
            "explanation": "Văn phong học thuật cần chính xác, khách quan, tránh ngôn ngữ thông tục."
        },
        {
            "question": "In academic writing, the passive voice is preferred when _____.",
            "options": [
                "you want to make writing more interesting",
                "the action is more important than the doer",
                "you want to sound more intelligent",
                "you need to fill more pages"
            ],
            "answer": "the action is more important than the doer",
            "explanation": "Passive voice nhấn mạnh hành động và kết quả."
        },
        {
            "question": "What is the primary purpose of a literature review in academic research?",
            "options": [
                "To summarize every book you've read",
                "To critique other researchers personally",
                "To contextualize your research within existing scholarship",
                "To make your paper longer"
            ],
            "answer": "To contextualize your research within existing scholarship",
            "explanation": "Literature review đặt nghiên cứu trong bối cảnh các công trình đã có."
        },
        {
            "question": "Which citation format is commonly used in humanities disciplines?",
            "options": ["APA", "MLA", "IEEE", "Chicago (Author-Date)"],
            "answer": "MLA",
            "explanation": "MLA được dùng phổ biến trong văn học, ngôn ngữ học và nhân văn."
        },
        {
            "question": "Plagiarism includes _____.",
            "options": [
                "only copying entire paragraphs word-for-word",
                "using ideas without citation, even if paraphrased",
                "citing sources in your bibliography",
                "writing in your own words"
            ],
            "answer": "using ideas without citation, even if paraphrased",
            "explanation": "Plagiarism bao gồm cả việc sử dụng ý tưởng không trích dẫn."
        },
        {
            "question": "In academic writing, you should avoid _____.",
            "options": [
                "using evidence to support claims",
                "personal pronouns like 'I think'",
                "citing credible sources",
                "logical organization"
            ],
            "answer": "personal pronouns like 'I think'",
            "explanation": "Văn phong học thuật thường tránh đại từ nhân xưng để duy trì tính khách quan."
        },
        {
            "question": "A thesis statement should _____.",
            "options": [
                "be vague and open to interpretation",
                "present the main argument of the paper",
                "ask a question",
                "include all supporting details"
            ],
            "answer": "present the main argument of the paper",
            "explanation": "Thesis statement = câu luận điểm, trình bày lập luận chính."
        },
        {
            "question": "Which is the correct way to introduce a quote in academic writing?",
            "options": [
                "Someone said, 'quote here.'",
                "According to Smith (2020), 'quote here' (p. 45).",
                "Here's a quote: 'quote here.'",
                "'Quote here.'"
            ],
            "answer": "According to Smith (2020), 'quote here' (p. 45).",
            "explanation": "Trích dẫn cần giới thiệu rõ nguồn, tác giả, năm và trang."
        },
        {
            "question": "The conclusion of an academic paper should _____.",
            "options": [
                "introduce new information not discussed before",
                "summarize main points and restate the thesis",
                "apologize for any weaknesses",
                "be as long as the introduction"
            ],
            "answer": "summarize main points and restate the thesis",
            "explanation": "Kết luận tóm tắt điểm chính và nhắc lại luận điểm."
        },
        {
            "question": "When paraphrasing, you must _____.",
            "options": [
                "use the exact same words as the original",
                "change a few words but keep the same structure",
                "rewrite the idea in your own words and cite the source",
                "not cite the source if you change the words"
            ],
            "answer": "rewrite the idea in your own words and cite the source",
            "explanation": "Paraphrase = diễn giải lại bằng từ ngữ của bạn + trích dẫn nguồn."
        },
        {
            "question": "A topic sentence in a paragraph should _____.",
            "options": [
                "appear at the end of the paragraph",
                "state the main idea of the paragraph",
                "include all supporting details",
                "be the longest sentence"
            ],
            "answer": "state the main idea of the paragraph",
            "explanation": "Topic sentence = câu chủ đề, nêu ý chính của đoạn."
        },
        {
            "question": "In APA style, in-text citations typically include _____.",
            "options": [
                "Author's name and year",
                "Full title of the work",
                "Publisher information",
                "URL of the source"
            ],
            "answer": "Author's name and year",
            "explanation": "APA in-text citation: (Author, Year)."
        },
        {
            "question": "Which transition word indicates addition of information?",
            "options": ["However", "Moreover", "Although", "Conversely"],
            "answer": "Moreover",
            "explanation": "Moreover = hơn nữa, thêm vào đó - chỉ sự bổ sung."
        },
        {
            "question": "The abstract of a research paper is typically _____.",
            "options": [
                "5-10 pages long",
                "150-250 words",
                "the same as the introduction",
                "written in bullet points"
            ],
            "answer": "150-250 words",
            "explanation": "Abstract thường dài 150-250 từ, tóm tắt ngắn gọn."
        },
        {
            "question": "When should you use direct quotes in academic writing?",
            "options": [
                "As often as possible",
                "When the original wording is particularly powerful or precise",
                "Never",
                "Only in the introduction"
            ],
            "answer": "When the original wording is particularly powerful or precise",
            "explanation": "Trích dẫn trực tiếp khi từ ngữ gốc đặc biệt mạnh mẽ hoặc chính xác."
        },
        {
            "question": "A counterargument in an essay serves to _____.",
            "options": [
                "confuse the reader",
                "acknowledge and refute opposing viewpoints",
                "fill space",
                "show you don't have a strong opinion"
            ],
            "answer": "acknowledge and refute opposing viewpoints",
            "explanation": "Counterargument = lập luận phản biện, thừa nhận và bác bỏ quan điểm đối lập."
        },
        {
            "question": "Which is NOT a characteristic of academic writing?",
            "options": [
                "Formal tone",
                "Evidence-based arguments",
                "Emotional appeals",
                "Logical organization"
            ],
            "answer": "Emotional appeals",
            "explanation": "Văn học thuật dựa trên lý lẽ và bằng chứng, không dựa vào cảm xúc."
        },
        {
            "question": "The purpose of peer review is to _____.",
            "options": [
                "reject as many papers as possible",
                "ensure quality and validity of research",
                "make researchers feel bad",
                "delay publication"
            ],
            "answer": "ensure quality and validity of research",
            "explanation": "Peer review đảm bảo chất lượng và độ tin cậy của nghiên cứu."
        },
        {
            "question": "When writing an argumentative essay, you should _____.",
            "options": [
                "only present your own viewpoint",
                "insult opposing viewpoints",
                "present multiple perspectives and defend your position",
                "avoid using any evidence"
            ],
            "answer": "present multiple perspectives and defend your position",
            "explanation": "Argumentative essay trình bày nhiều góc nhìn và bảo vệ lập trường của bạn."
        },
        {
            "question": "The references or bibliography section should _____.",
            "options": [
                "include all books you've ever read",
                "list only sources cited in the paper",
                "be organized randomly",
                "omit publication dates"
            ],
            "answer": "list only sources cited in the paper",
            "explanation": "References chỉ liệt kê các nguồn được trích dẫn trong bài."
        },
        
        # ==================== CRITICAL THINKING (20 câu) ====================
        {
            "question": "An 'ad hominem' fallacy occurs when someone _____.",
            "options": [
                "attacks the person instead of the argument",
                "uses statistical evidence incorrectly",
                "appeals to tradition",
                "makes a false analogy"
            ],
            "answer": "attacks the person instead of the argument",
            "explanation": "Ad hominem = tấn công cá nhân thay vì bác bỏ lập luận."
        },
        {
            "question": "A 'straw man' argument involves _____.",
            "options": [
                "misrepresenting someone's argument to make it easier to attack",
                "using expert testimony as evidence",
                "appealing to emotions rather than logic",
                "making circular reasoning"
            ],
            "answer": "misrepresenting someone's argument to make it easier to attack",
            "explanation": "Straw man = bóp méo lập luận để dễ tấn công hơn."
        },
        {
            "question": "Which of the following represents deductive reasoning?",
            "options": [
                "Every swan I've seen is white, so all swans are white",
                "All mammals are warm-blooded. Whales are mammals. Therefore, whales are warm-blooded",
                "The sun rose yesterday, so it will rise tomorrow",
                "Most students study hard, so John probably studies hard"
            ],
            "answer": "All mammals are warm-blooded. Whales are mammals. Therefore, whales are warm-blooded",
            "explanation": "Deductive reasoning đi từ quy luật chung đến trường hợp cụ thể."
        },
        {
            "question": "Inductive reasoning involves _____.",
            "options": [
                "drawing general conclusions from specific observations",
                "starting with a general principle and applying it to specific cases",
                "using emotional appeals",
                "circular logic"
            ],
            "answer": "drawing general conclusions from specific observations",
            "explanation": "Inductive reasoning = suy luận quy nạp, từ cụ thể đến tổng quát."
        },
        {
            "question": "A 'false dilemma' fallacy presents _____.",
            "options": [
                "only two options when more exist",
                "a true either/or choice",
                "multiple valid alternatives",
                "statistical evidence"
            ],
            "answer": "only two options when more exist",
            "explanation": "False dilemma = lưỡng khó giả, chỉ đưa ra 2 lựa chọn khi có nhiều hơn."
        },
        {
            "question": "The 'slippery slope' fallacy assumes that _____.",
            "options": [
                "one action will inevitably lead to extreme consequences",
                "slopes are always dangerous",
                "change happens gradually",
                "evidence supports the conclusion"
            ],
            "answer": "one action will inevitably lead to extreme consequences",
            "explanation": "Slippery slope = dốc trơn, cho rằng một hành động sẽ dẫn đến hậu quả cực đoan."
        },
        {
            "question": "'Begging the question' occurs when _____.",
            "options": [
                "someone asks too many questions",
                "the conclusion is assumed in the premise",
                "evidence is requested",
                "a valid question is raised"
            ],
            "answer": "the conclusion is assumed in the premise",
            "explanation": "Begging the question = lập luận vòng, kết luận được giả định trong tiền đề."
        },
        {
            "question": "An 'appeal to authority' is fallacious when _____.",
            "options": [
                "citing any expert",
                "the authority is not relevant to the topic",
                "using peer-reviewed sources",
                "referencing credible research"
            ],
            "answer": "the authority is not relevant to the topic",
            "explanation": "Appeal to authority = viện dẫn uy quyền, sai khi uy quyền không liên quan đến chủ đề."
        },
        {
            "question": "Critical thinking involves _____.",
            "options": [
                "criticizing everything",
                "analyzing and evaluating information objectively",
                "accepting all information at face value",
                "ignoring evidence"
            ],
            "answer": "analyzing and evaluating information objectively",
            "explanation": "Critical thinking = tư duy phản biện, phân tích và đánh giá khách quan."
        },
        {
            "question": "A 'hasty generalization' is made when _____.",
            "options": [
                "conclusions are drawn from insufficient evidence",
                "generalizations are made quickly",
                "broad conclusions are supported by extensive data",
                "general statements are avoided"
            ],
            "answer": "conclusions are drawn from insufficient evidence",
            "explanation": "Hasty generalization = khái quát vội vàng từ bằng chứng không đủ."
        },
        {
            "question": "The 'bandwagon fallacy' suggests that something is true because _____.",
            "options": [
                "everyone believes it",
                "it has been proven scientifically",
                "experts support it",
                "evidence confirms it"
            ],
            "answer": "everyone believes it",
            "explanation": "Bandwagon fallacy = đi theo số đông, cho rằng đúng vì mọi người tin."
        },
        {
            "question": "When evaluating an argument, you should first identify _____.",
            "options": [
                "the author's name",
                "the main claim and supporting evidence",
                "grammatical errors",
                "the publication date"
            ],
            "answer": "the main claim and supporting evidence",
            "explanation": "Đánh giá lập luận bắt đầu với xác định luận điểm chính và bằng chứng."
        },
        {
            "question": "A 'red herring' in an argument _____.",
            "options": [
                "introduces irrelevant information to distract",
                "uses fish as an example",
                "highlights important points",
                "provides relevant evidence"
            ],
            "answer": "introduces irrelevant information to distract",
            "explanation": "Red herring = thông tin không liên quan để đánh lạc hướng."
        },
        {
            "question": "The 'appeal to emotion' fallacy relies on _____.",
            "options": [
                "manipulating feelings rather than using logic",
                "showing empathy",
                "emotional intelligence",
                "passionate delivery"
            ],
            "answer": "manipulating feelings rather than using logic",
            "explanation": "Appeal to emotion = lợi dụng cảm xúc thay vì lý lẽ."
        },
        {
            "question": "A strong argument is characterized by _____.",
            "options": [
                "loud delivery",
                "valid reasoning and credible evidence",
                "length and complexity",
                "emotional appeals"
            ],
            "answer": "valid reasoning and credible evidence",
            "explanation": "Lập luận mạnh có lý lẽ hợp lệ và bằng chứng đáng tin cậy."
        },
        {
            "question": "'Confirmation bias' refers to _____.",
            "options": [
                "seeking information that confirms existing beliefs",
                "confirming all information is accurate",
                "bias in favor of confirmatory research",
                "statistical confirmation"
            ],
            "answer": "seeking information that confirms existing beliefs",
            "explanation": "Confirmation bias = thiên kiến xác nhận, tìm kiếm thông tin ủng hộ niềm tin sẵn có."
        },
        {
            "question": "The 'post hoc' fallacy assumes that _____.",
            "options": [
                "because one event followed another, the first caused the second",
                "events after a deadline don't count",
                "historical events are irrelevant",
                "causation requires correlation"
            ],
            "answer": "because one event followed another, the first caused the second",
            "explanation": "Post hoc fallacy = sau đây do đây, cho rằng sự kiện sau do sự kiện trước gây ra."
        },
        {
            "question": "To think critically, you should _____.",
            "options": [
                "accept information from authority figures without question",
                "question assumptions and evaluate evidence",
                "reject all new ideas",
                "rely only on personal experience"
            ],
            "answer": "question assumptions and evaluate evidence",
            "explanation": "Tư duy phản biện đòi hỏi đặt câu hỏi về giả định và đánh giá bằng chứng."
        },
        {
            "question": "A 'tu quoque' fallacy _____.",
            "options": [
                "dismisses criticism by pointing out the critic's hypocrisy",
                "uses Latin to sound intelligent",
                "presents valid counterarguments",
                "acknowledges mistakes"
            ],
            "answer": "dismisses criticism by pointing out the critic's hypocrisy",
            "explanation": "Tu quoque = cậu cũng thế, bác bỏ chỉ trích bằng cách chỉ ra sự đạo đức giả."
        },
        {
            "question": "Logical fallacies weaken arguments because they _____.",
            "options": [
                "use formal logic",
                "contain errors in reasoning",
                "are too complex",
                "require background knowledge"
            ],
            "answer": "contain errors in reasoning",
            "explanation": "Logical fallacies = ngụy biện logic, chứa lỗi suy luận làm yếu lập luận."
        },
        
        # ==================== COLLOCATIONS & IDIOMS (15 câu) ====================
        {
            "question": "The company decided to _____ a blind eye to the employee's minor violations.",
            "options": ["turn", "make", "give", "take"],
            "answer": "turn",
            "explanation": "Turn a blind eye to = làm ngơ, bỏ qua."
        },
        {
            "question": "After months of negotiation, both parties finally reached a _____.",
            "options": ["consensus", "census", "consent", "conscience"],
            "answer": "consensus",
            "explanation": "Reach a consensus = đạt được sự đồng thuận."
        },
        {
            "question": "The research _____ light on the previously misunderstood phenomenon.",
            "options": ["threw", "shed", "cast", "gave"],
            "answer": "shed",
            "explanation": "Shed light on = làm sáng tỏ, làm rõ vấn đề."
        },
        {
            "question": "The deadline is fast _____, so we need to finish the project soon.",
            "options": ["approaching", "reaching", "coming", "arriving"],
            "answer": "approaching",
            "explanation": "Fast approaching = đang đến gần nhanh chóng."
        },
        {
            "question": "The politician's speech failed to _____ with the audience.",
            "options": ["resonate", "resonant", "resonance", "resounding"],
            "answer": "resonate",
            "explanation": "Resonate with = tạo được tiếng vang, gây được sự đồng cảm."
        },
        {
            "question": "The new evidence _____ doubt on the validity of the theory.",
            "options": ["cast", "threw", "made", "gave"],
            "answer": "cast",
            "explanation": "Cast doubt on = gây nghi ngờ về."
        },
        {
            "question": "She made a _____ effort to complete the project on time.",
            "options": ["conscious", "conscience", "conscientious", "consciousness"],
            "answer": "conscientious",
            "explanation": "Conscientious effort = nỗ lực tận tâm, chu đáo."
        },
        {
            "question": "The committee will _____ a decision at the next meeting.",
            "options": ["make", "do", "take", "have"],
            "answer": "make",
            "explanation": "Make a decision = đưa ra quyết định."
        },
        {
            "question": "The proposal was met with strong _____ from environmental groups.",
            "options": ["opposition", "opposite", "opposing", "opponent"],
            "answer": "opposition",
            "explanation": "Meet with opposition = gặp phải sự phản đối."
        },
        {
            "question": "The company needs to _____ into account the environmental impact.",
            "options": ["take", "make", "give", "bring"],
            "answer": "take",
            "explanation": "Take into account = xem xét, tính đến."
        },
        {
            "question": "The study _____ the way for further research in the field.",
            "options": ["paved", "made", "built", "created"],
            "answer": "paved",
            "explanation": "Pave the way for = mở đường cho."
        },
        {
            "question": "The theory has gained _____ acceptance in the scientific community.",
            "options": ["widespread", "wildspread", "wide-spread", "wild-spread"],
            "answer": "widespread",
            "explanation": "Widespread acceptance = sự chấp nhận rộng rãi."
        },
        {
            "question": "The evidence _____ heavily in favor of the defendant.",
            "options": ["weighs", "weights", "measures", "counts"],
            "answer": "weighs",
            "explanation": "Weigh in favor of = nghiêng về phía."
        },
        {
            "question": "The researchers drew _____ from multiple sources of data.",
            "options": ["conclusions", "conclusions from", "the conclusions", "concluding"],
            "answer": "conclusions",
            "explanation": "Draw conclusions = rút ra kết luận."
        },
        {
            "question": "The findings have far-_____ implications for public policy.",
            "options": ["reaching", "ranging", "spreading", "stretching"],
            "answer": "reaching",
            "explanation": "Far-reaching implications = ý nghĩa/tác động sâu rộng."
        }
]