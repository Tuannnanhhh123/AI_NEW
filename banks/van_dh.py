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
        "question": "Trong bài thơ 'Tây Tiến', hình ảnh 'Mai Châu mùa em thơm nếp xôi' gợi lên cảm xúc gì?",
        "options": ["Sự ấm áp, nồng hậu của tình quân dân và hương vị quê hương", "Sự mệt mỏi sau quãng đường hành quân", "Nỗi nhớ về gia đình ở thủ đô", "Vẻ đẹp hùng vĩ của núi rừng Tây Bắc"],
        "answer": "Sự ấm áp, nồng hậu của tình quân dân và hương vị quê hương",
        "explanation": "Chữ 'mùa em' là cách kết hợp từ sáng tạo, gợi sự trẻ trung, tình tứ và dư vị ngọt ngào của vùng đất lạ."
    },
    {
        "question": "Tính chất 'điệp khúc' trong bài thơ 'Sóng' của Xuân Quỳnh được tạo nên bởi yếu tố nào?",
        "options": ["Nhịp thơ 5 chữ và hình ảnh sóng vỗ liên hồi", "Sử dụng nhiều từ Hán Việt", "Sử dụng các câu hỏi tu từ", "Việc lặp lại tên bài thơ nhiều lần"],
        "answer": "Nhịp thơ 5 chữ và hình ảnh sóng vỗ liên hồi",
        "explanation": "Nhịp thơ mô phỏng nhịp của sóng biển, cũng là nhịp đập thổn thức của trái tim người phụ nữ khi yêu."
    },
    {
        "question": "Trong truyện 'Vợ nhặt', tại sao nhân vật người đàn bà hàng xóm lại nói: 'Ôi chao! Giời đất này còn rước cái nợ đời về'?",
        "options": ["Sự xót xa cho hoàn cảnh của Tràng giữa lúc đói khát", "Sự ghen tị với gia đình Tràng", "Sự khinh bỉ người vợ nhặt", "Sự vui mừng cho hạnh phúc của Tràng"],
        "answer": "Sự xót xa cho hoàn cảnh của Tràng giữa lúc đói khát",
        "explanation": "Câu nói thể hiện cái nhìn thực tế đầy đau đớn về việc nuôi thân còn khó, nói gì đến nuôi thêm người."
    },
    {
        "question": "Hình ảnh 'con đường' và 'dòng sông' trong văn học kháng chiến thường mang ý nghĩa gì?",
        "options": ["Sự kết nối giữa tiền tuyến - hậu phương và mạch nguồn lịch sử dân tộc", "Sự ngăn cách địa lý", "Cảnh đẹp thiên nhiên thuần túy", "Sự khó khăn của giao thông vận tải"],
        "answer": "Sự kết nối giữa tiền tuyến - hậu phương và mạch nguồn lịch sử dân tộc",
        "explanation": "Đó là những huyết mạch của đất nước, nơi ghi dấu những bước chân hành quân và những chiến công."
    },
    {
        "question": "Nghệ thuật xây dựng nhân vật cụ Mết trong 'Rừng xà nu' có điểm gì tương đồng với các anh hùng sử thi?",
        "options": ["Lời nói đanh thép, ngoại hình quật cường, đại diện cho ý chí cộng đồng", "Sự lãng mạn, đa tình", "Sự bí ẩn, khó hiểu", "Sự giàu có về tài sản"],
        "answer": "Lời nói đanh thép, ngoại hình quật cường, đại diện cho ý chí cộng đồng",
        "explanation": "Cụ Mết là 'cây xà nu đại thụ', là gạch nối giữa truyền thống quật khởi và hiện tại chiến đấu."
    },
    {
        "question": "Trong 'Ai đã đặt tên cho dòng sông?', chi tiết sông Hương 'không bao giờ từ bỏ kinh thành' thể hiện điều gì?",
        "options": ["Lòng chung thủy của dòng sông đối với Huế", "Dòng chảy của sông bị bao quanh bởi núi", "Sự quy hoạch của thành phố", "Sự sợ hãi khi phải ra biển lớn"],
        "answer": "Lòng chung thủy của dòng sông đối với Huế",
        "explanation": "Hoàng Phủ Ngọc Tường nhân hóa dòng sông như một người tình chung thủy, luôn hướng về người mình yêu."
    },
    {
        "question": "Thao tác lập luận 'So sánh' trong văn nghị luận nhằm mục đích gì?",
        "options": ["Làm sáng tỏ đối tượng qua việc chỉ ra nét tương đồng hoặc khác biệt", "Phủ định ý kiến của người khác", "Đưa ra lời khuyên cho người đọc", "Kể lại một câu chuyện thú vị"],
        "answer": "Làm sáng tỏ đối tượng qua việc chỉ ra nét tương đồng hoặc khác biệt",
        "explanation": "So sánh giúp đối tượng được nhìn nhận một cách khách quan và sâu sắc hơn."
    },
    {
        "question": "Hình ảnh 'ngọn lửa' trong bài thơ 'Bếp lửa' của Bằng Việt mang ý nghĩa ẩn dụ cho:",
        "options": ["Sức sống, tình yêu thương và niềm tin mà bà truyền cho cháu", "Sự ấm áp của mùa đông", "Sự tàn phá của chiến tranh", "Cảnh nấu nướng vất vả"],
        "answer": "Sức sống, tình yêu thương và niềm tin mà bà truyền cho cháu",
        "explanation": "Từ bếp lửa cụ thể, tác giả nâng lên thành ngọn lửa của lòng biết ơn và lý tưởng sống."
    },
    {
        "question": "Trong 'Vợ chồng A Phủ', chi tiết Mị 'thấy phơi phới trở lại' trong đêm tình mùa xuân là do tác động của:",
        "options": ["Hơi rượu, tiếng sáo và không khí ngày tết", "Sự quan tâm của A Sử", "Sự giàu có của nhà thống lý", "Lời hứa của cha Mị"],
        "answer": "Hơi rượu, tiếng sáo và không khí ngày tết",
        "explanation": "Các yếu tố ngoại cảnh đã đánh thức sức sống tiềm tàng bên trong tâm hồn người phụ nữ trẻ."
    },
    {
        "question": "Hàm ý của câu nói 'Đàn bà ở thuyền chúng tôi cần phải có người đàn ông để chèo chống khi phong ba' là gì?",
        "options": ["Khẳng định vai trò trụ cột của người đàn ông trong gia đình lao động", "Sự yếu đuối của phụ nữ vùng biển", "Lời than vãn về số phận", "Sự biện hộ cho hành động đánh vợ của người chồng"],
        "answer": "Khẳng định vai trò trụ cột của người đàn ông trong gia đình lao động",
        "explanation": "Người đàn bà hàng chài nhìn thấu quy luật sinh tồn khắc nghiệt của nghề biển."
    },
    {
        "question": "Trong bài thơ 'Việt Bắc', khổ thơ về 'bức tranh tứ bình' miêu tả điều gì?",
        "options": ["Vẻ đẹp hài hòa giữa thiên nhiên và con người qua bốn mùa", "Bốn trận đánh lớn ở chiến khu", "Bốn vị lãnh đạo cách mạng", "Bốn loại cây đặc trưng của miền núi"],
        "answer": "Vẻ đẹp hài hòa giữa thiên nhiên và con người qua bốn mùa",
        "explanation": "Sự đan xen giữa cảnh và người tạo nên một không gian Việt Bắc trữ tình và đậm đà bản sắc."
    },
    {
        "question": "Lý luận văn học khẳng định: 'Văn học là nhân học' có nghĩa là:",
        "options": ["Văn học tập trung vào nghiên cứu và ngợi ca con người", "Văn học chỉ viết về những người tốt", "Văn học là môn học về chữ viết", "Văn học là công cụ để dạy tiếng mẹ đẻ"],
        "answer": "Văn học tập trung vào nghiên cứu và ngợi ca con người",
        "explanation": "Mục đích cuối cùng của văn chương là hướng con người tới cái Chân - Thiện - Mỹ."
    },
    {
        "question": "Chi tiết 'bát nước ngô' và 'tiếng sáo' trong đêm tình mùa xuân biểu tượng cho:",
        "options": ["Sự đối lập giữa hiện thực nghèo khổ và khát vọng tinh thần", "Sự giàu sang của nhà thống lý Pá Tra", "Lễ vật cúng tế của người Mông", "Sự no ấm của bản làng"],
        "answer": "Sự đối lập giữa hiện thực nghèo khổ và khát vọng tinh thần",
        "explanation": "Mị sống trong cảnh nô lệ (bát nước ngô) nhưng lòng vẫn hướng về tự do (tiếng sáo)."
    },
    {
        "question": "Tại sao Nguyễn Đình Thi gọi Việt Nam là 'Đất nước của những người chưa bao giờ khuất'?",
        "options": ["Vì truyền thống bất khuất, kiên cường chống ngoại xâm của dân tộc", "Vì người Việt Nam không bao giờ ngủ", "Vì dân số Việt Nam rất đông", "Vì Việt Nam có nhiều đồi núi"],
        "answer": "Vì truyền thống bất khuất, kiên cường chống ngoại xâm của dân tộc",
        "explanation": "Câu thơ khẳng định tư thế hiên ngang và sức sống mãnh liệt của dân tộc qua hàng ngàn năm lịch sử."
    },
    {
        "question": "Điểm nhìn trần thuật trong truyện ngắn 'Chiếc thuyền ngoài xa' của Nguyễn Minh Châu là:",
        "options": ["Nhân vật Phùng - một nghệ sĩ nhiếp ảnh", "Người kể chuyện ngôi thứ ba khách quan", "Nhân vật chánh án Đẩu", "Người đàn bà hàng chài"],
        "answer": "Nhân vật Phùng - một nghệ sĩ nhiếp ảnh",
        "explanation": "Sử dụng điểm nhìn của một nghệ sĩ giúp câu chuyện mang tính trải nghiệm và tự vấn sâu sắc."
    },
    {
        "question": "Hình ảnh 'hồn Trương Ba' và 'xác hàng thịt' đại diện cho mâu thuẫn nào?",
        "options": ["Mâu thuẫn giữa lý tưởng đạo đức và nhu cầu bản năng", "Mâu thuẫn giữa người giàu và người nghèo", "Mâu thuẫn giữa sự sống và cái chết", "Mâu thuẫn giữa tiên giới và trần gian"],
        "answer": "Mâu thuẫn giữa lý tưởng đạo đức và nhu cầu bản năng",
        "explanation": "Trương Ba đại diện cho cái cao thượng, xác hàng thịt đại diện cho những ham muốn tầm thường."
    },
    {
        "question": "Chi tiết Tnú 'không cảm thấy đau ở mười đầu ngón tay' khi bị đốt bằng nhựa xà nu gợi lên:",
        "options": ["Sự căm thù đã nén chặt làm lu mờ nỗi đau thể xác", "Tnú bị mất cảm giác", "Nhựa xà nu không nóng", "Tnú là người có siêu năng lực"],
        "answer": "Sự căm thù đã nén chặt làm lu mờ nỗi đau thể xác",
        "explanation": "Lửa căm thù cháy mạnh hơn cả lửa nhựa xà nu, thúc đẩy ý chí quật khởi của nhân vật."
    },
    {
        "question": "Trong văn bản 'Tuyên ngôn Độc lập', Hồ Chí Minh khẳng định điều gì về chế độ thực dân Pháp?",
        "options": ["Đó là chế độ bóc lột, tàn bạo, đi ngược lại nhân đạo và chính nghĩa", "Đó là chế độ mang lại ánh sáng văn minh", "Đó là đối tác tiềm năng của Việt Nam", "Đó là một chế độ tiến bộ bị hiểu lầm"],
        "answer": "Đó là chế độ bóc lột, tàn bạo, đi ngược lại nhân đạo và chính nghĩa",
        "explanation": "Bác dùng các dẫn chứng thép về kinh tế, chính trị để bác bỏ chiêu bài 'khai hóa' của Pháp."
    },
    {
        "question": "Câu thơ 'Rải rác biên cương mồ viễn xứ' trong Tây Tiến gợi lên không khí:",
        "options": ["Bi tráng, trang trọng và đầy kiêu hãnh", "Tang thương, bi lụy", "Vui vẻ, nhộn nhịp", "Lạnh lẽo, hoang tàn"],
        "answer": "Bi tráng, trang trọng và đầy kiêu hãnh",
        "explanation": "Sử dụng từ Hán Việt giúp cái chết của người lính không còn thê lương mà trở nên bất tử."
    },
    {
        "question": "Biện pháp tu từ 'Nhân hóa' dòng sông Hương chảy qua thành phố Huế có tác dụng:",
        "options": ["Làm cho dòng sông có tâm hồn, có tình cảm và sự gắn bó sâu sắc với vùng đất", "Làm cho sông rộng hơn", "Làm cho nước sông xanh hơn", "Để giới thiệu các loài cá"],
        "answer": "Làm cho dòng sông có tâm hồn, có tình cảm và sự gắn bó sâu sắc với vùng đất",
        "explanation": "Sông Hương không chỉ là dòng nước mà là linh hồn, là nhân chứng lịch sử của cố đô."
    },
    {
        "question": "Trong 'Vợ nhặt', bát 'cháo cám' ở bữa cơm ngày đói mang ý nghĩa gì?",
        "options": ["Nỗi đau xót của hiện thực và tình nghĩa ấm áp của gia đình", "Sự giàu có đột ngột của gia đình Tràng", "Sự lãng phí thức ăn", "Một đặc sản của vùng nông thôn"],
        "answer": "Nỗi đau xót của hiện thực và tình nghĩa ấm áp của gia đình",
        "explanation": "Bát cháo 'đắng chát, nghẹn bứ' nhưng bà cụ Tứ gọi là 'chè kho' để nhen nhóm hy vọng sống."
    },
    {
        "question": "Sự 'thức tỉnh' của nhân vật nghệ sĩ Phùng ở cuối truyện 'Chiếc thuyền ngoài xa' là gì?",
        "options": ["Nhận ra mối quan hệ phức tạp giữa nghệ thuật và đời sống", "Nhận ra mình chụp ảnh chưa đẹp", "Nhận ra người đàn bà hàng chài rất giàu", "Nhận ra mình cần đổi nghề"],
        "answer": "Nhận ra mối quan hệ phức tạp giữa nghệ thuật và đời sống",
        "explanation": "Phùng hiểu rằng không thể dùng cái nhìn nghệ thuật thuần túy để phán xét cuộc đời đầy nghịch lý."
    },
    {
        "question": "Câu thơ 'Đất là nơi anh đến trường / Nước là nơi em tắm' trong bài Đất Nước (Nguyễn Khoa Điềm) thể hiện:",
        "options": ["Đất nước hiện hữu trong những sinh hoạt bình thường nhất của mỗi cá nhân", "Kiến thức về vệ sinh cá nhân", "Sở thích đi học của trẻ em", "Vẻ đẹp của thiên nhiên"],
        "answer": "Đất nước hiện hữu trong những sinh hoạt bình thường nhất của mỗi cá nhân",
        "explanation": "Tác giả định nghĩa Đất Nước bằng những kỷ niệm cá nhân gắn bó, không xa vời."
    },
    {
        "question": "Tại sao bài thơ 'Tây Tiến' lại sử dụng nhiều từ láy tượng hình như: khúc khuỷu, thăm thẳm, cồn mây...?",
        "options": ["Để nhấn mạnh sự hiểm trở và hùng vĩ của núi rừng", "Để làm cho bài thơ dễ thuộc", "Để thể hiện sự vui vẻ của người lính", "Để miêu tả cảnh sinh hoạt ở bản làng"],
        "answer": "Để nhấn mạnh sự hiểm trở và hùng vĩ của núi rừng",
        "explanation": "Các từ láy tạo hiệu ứng thị giác mạnh mẽ, giúp người đọc hình dung sự gian khổ của quân đi."
    },
    {
        "question": "Thông điệp của vở kịch 'Hồn Trương Ba, da hàng thịt' hướng tới việc:",
        "options": ["Phê phán lối sống giả dối và khát vọng sống hoàn thiện mình", "Khuyến khích việc mượn xác để sống", "Ca ngợi quyền năng của tiên giới", "Phê phán nghề hàng thịt"],
        "answer": "Phê phán lối sống giả dối và khát vọng sống hoàn thiện mình",
        "explanation": "Con người cần sự thống nhất giữa tâm hồn và thể xác để có được hạnh phúc thực sự."
    },
    # (Tiếp tục thêm 25 câu nữa để đủ 50 câu cho danh sách này)
    {
        "question": "Đặc trưng của bút pháp lãng mạn trong 'Tây Tiến' là:",
        "options": ["Cái nhìn bay bổng, tôn vinh vẻ đẹp lý tưởng và bi tráng", "Miêu tả thực tế trần trụi của chiến tranh", "Sự châm biếm sâu cay đối với kẻ thù", "Sự tập trung vào những chi tiết đời thường vụn vặt"],
        "answer": "Cái nhìn bay bổng, tôn vinh vẻ đẹp lý tưởng và bi tráng",
        "explanation": "Bút pháp lãng mạn giúp tác giả vượt lên trên cái khắc nghiệt của thực tại để ngợi ca anh hùng."
    },
    {
        "question": "Hình ảnh 'con sóng' trong thơ Xuân Quỳnh có đặc tính nào dưới đây?",
        "options": ["Luôn vận động và không bao giờ đứng yên như nỗi nhớ trong tình yêu", "Sự tĩnh lặng của mặt nước hồ", "Sự hung dữ tiêu diệt thuyền bè", "Sự khô cằn của đại dương"],
        "answer": "Luôn vận động và không bao giờ đứng yên như nỗi nhớ trong tình yêu",
        "explanation": "Sóng không ngủ được cũng như em không ngủ được vì nhớ anh."
    },
    {
        "question": "Trong 'Vợ chồng A Phủ', hành động Mị xắn mỡ bỏ vào đĩa đèn cho sáng gợi lên điều gì?",
        "options": ["Ý thức muốn thay đổi không gian sống và thắp sáng hy vọng", "Sự lãng phí tài sản của chủ", "Mị muốn nấu ăn đêm", "Thói quen làm việc của Mị"],
        "answer": "Ý thức muốn thay đổi không gian sống và thắp sáng hy vọng",
        "explanation": "Đèn sáng là biểu tượng cho sự thức tỉnh của ý thức về cuộc sống hiện tại."
    },
    {
        "question": "Nét độc đáo trong ngôn ngữ tùy bút của Nguyễn Tuân là:",
        "options": ["Giàu vốn từ vựng, độc đáo và đầy bất ngờ", "Đơn giản, dễ hiểu đối với mọi lứa tuổi", "Nghèo nàn, lặp lại", "Chỉ sử dụng tiếng lóng"],
        "answer": "Giàu vốn từ vựng, độc đáo và đầy bất ngờ",
        "explanation": "Ông luôn tìm những từ ngữ đắt giá nhất để miêu tả đối tượng (như 'thanh bảo kiếm', 'hút nước')."
    },
    {
        "question": "Tại sao người đàn bà hàng chài từ chối ly hôn dù bị chồng đánh đập dã man?",
        "options": ["Vì hạnh phúc của các con và vì lòng thấu hiểu cho nỗi khổ của chồng", "Vì bà không biết đi đâu", "Vì bà sợ bị dân làng chê cười", "Vì bà vẫn còn yêu chồng tha thiết"],
        "answer": "Vì hạnh phúc của các con và vì lòng thấu hiểu cho nỗi khổ của chồng",
        "explanation": "Bà hy sinh bản thân để duy trì gia đình, đồng thời hiểu chồng mình cũng là nạn nhân của cái đói nghèo."
    },
    {
        "question": "Câu thơ 'Thanh thản trong tiếng đàn / Lor-ca bơi sang ngang' gợi ý nghĩa gì?",
        "options": ["Sự bất tử của người nghệ sĩ và giá trị của cái đẹp", "Lor-ca đang thi bơi", "Cái chết vô ích của nghệ sĩ", "Sự thất bại của nghệ thuật"],
        "answer": "Sự bất tử của người nghệ sĩ và giá trị của cái đẹp",
        "explanation": "Cái chết về thể xác là bắt đầu cho sự sống vĩnh cửu của những bản nhạc Lor-ca để lại."
    },
    {
        "question": "Trong văn bản 'Phong cách Hồ Chí Minh', nét nổi bật trong lối sống của Bác là gì?",
        "options": ["Sự giản dị kết hợp với tinh hoa văn hóa nhân loại", "Sự xa hoa, lộng lẫy", "Sự tách biệt với thế giới bên ngoài", "Sự bắt chước hoàn toàn văn hóa phương Tây"],
        "answer": "Sự giản dị kết hợp với tinh hoa văn hóa nhân loại",
        "explanation": "Bác tiếp thu văn hóa thế giới một cách chọn lọc trên nền tảng truyền thống dân tộc."
    },
    {
        "question": "Thành phần 'biệt lập' trong câu văn thường dùng để làm gì?",
        "options": ["Thể hiện thái độ của người nói hoặc giải thích thông tin bổ sung", "Thay thế cho chủ ngữ chính", "Làm cho câu dài hơn", "Để kết thúc câu"],
        "answer": "Thể hiện thái độ của người nói hoặc giải thích thông tin bổ sung",
        "explanation": "Nó không tham gia vào cấu trúc ngữ pháp chính nhưng rất quan trọng để biểu đạt cảm xúc."
    },
    {
        "question": "Phông nền của bài thơ 'Việt Bắc' là sự kiện lịch sử nào?",
        "options": ["Chiến thắng Điện Biên Phủ và hiệp định Giơ-ne-vơ (1954)", "Cách mạng tháng Tám (1945)", "Khởi nghĩa Nam Kỳ", "Chiến thắng mùa xuân năm 1975"],
        "answer": "Chiến thắng Điện Biên Phủ và hiệp định Giơ-ne-vơ (1954)",
        "explanation": "Bài thơ là lời chào biệt sau 15 năm gắn bó giữa cán bộ kháng chiến và nhân dân Việt Bắc."
    },
    {
        "question": "Biện pháp 'Ẩn dụ' trong câu 'Quân xanh màu lá dữ oai hùm' miêu tả đặc điểm nào của lính Tây Tiến?",
        "options": ["Sự ốm yếu do bệnh tật nhưng tinh thần vẫn dũng mãnh", "Người lính mặc áo màu xanh", "Lính Tây Tiến rất sợ hổ", "Sự hòa nhập vào thiên nhiên"],
        "answer": "Sự ốm yếu do bệnh tật nhưng tinh thần vẫn dũng mãnh",
        "explanation": "Xanh màu lá là do sốt rét rừng, nhưng 'dữ oai hùm' khẳng định khí thế hiên ngang."
    },
    {
        "question": "Mục đích của việc sử dụng 'dẫn chứng thực tế' trong bài nghị luận xã hội là:",
        "options": ["Tăng sức thuyết phục và làm cho bài viết có chiều sâu thực tiễn", "Để bài viết dài hơn", "Để chứng tỏ mình đi nhiều nơi", "Để thay thế cho lý lẽ"],
        "answer": "Tăng sức thuyết phục và làm cho bài viết có chiều sâu thực tiễn",
        "explanation": "Lý lẽ suông sẽ khô khan, dẫn chứng giúp vấn đề trở nên sống động và rõ ràng."
    },
    {
        "question": "Trong truyện 'Rừng xà nu', hình ảnh cụ Mết kể chuyện cho dân làng nghe vào đêm mưa gợi không gian:",
        "options": ["Thiêng liêng, huyền ảo mang âm hưởng sử thi", "U buồn, chán nản", "Sợ hãi trước kẻ thù", "Vui vẻ của một buổi tiệc"],
        "answer": "Thiêng liêng, huyền ảo mang âm hưởng sử thi",
        "explanation": "Lối kể chuyện cổ truyền giữ lửa cho niềm tin và lòng tự hào dân tộc."
    },
    {
        "question": "Tại sao Nguyễn Tuân lại miêu tả dòng sông Đà như một 'áng tóc trữ tình'?",
        "options": ["Để làm nổi bật vẻ đẹp mềm mại, thơ mộng của dòng sông khi nhìn từ trên cao", "Vì sông Đà có nhiều tóc", "Để miêu tả sự nguy hiểm của dòng nước", "Vì nước sông có màu đen"],
        "answer": "Để làm nổi bật vẻ đẹp mềm mại, thơ mộng của dòng sông khi nhìn từ trên cao",
        "explanation": "Sự đối lập hoàn toàn với tính cách hung bạo ở thượng nguồn, tạo nên vẻ đẹp toàn diện cho con sông."
    },
    {
        "question": "Giá trị nhân đạo trong tác phẩm 'Vợ nhặt' thể hiện ở điểm nào?",
        "options": ["Phát hiện khát vọng sống và tình thương của con người trong hoàn cảnh khốn cùng", "Sự thương hại của tác giả dành cho nhân vật", "Lên án sự lười biếng của người dân", "Khuyên con người không nên lấy vợ khi nghèo"],
        "answer": "Phát hiện khát vọng sống và tình thương của con người trong hoàn cảnh khốn cùng",
        "explanation": "Kim Lân không chỉ thấy cái đói mà còn thấy được ánh sáng của tình người rạng rỡ."
    },
    {
        "question": "Thông điệp từ nhân vật Việt trong 'Những đứa con trong gia đình' là:",
        "options": ["Sự tiếp nối truyền thống đánh giặc hào hùng của gia đình và dân tộc", "Tình cảm anh em hay cãi nhau", "Sự nhút nhát của trẻ con miền Tây", "Sở thích đi bộ đội để được vui chơi"],
        "answer": "Sự tiếp nối truyền thống đánh giặc hào hùng của gia đình và dân tộc",
        "explanation": "Cuốn sổ gia đình là nhân chứng cho dòng chảy căm thù và chiến đấu qua các thế hệ."
    },
    {
        "question": "Thơ Tố Hữu thường sử dụng cặp đại từ 'Mình - Ta' của ca dao dân ca nhằm:",
        "options": ["Tạo sự gần gũi, thân thiết và mang đậm tính dân tộc", "Để bài thơ nghe giống bài hát", "Vì ông không biết dùng đại từ khác", "Để thể hiện sự xa cách"],
        "answer": "Tạo sự gần gũi, thân thiết và mang đậm tính dân tộc",
        "explanation": "Xoay quanh tình cảm cách mạng nhưng lại mang âm hưởng tình yêu đôi lứa, dễ đi vào lòng người."
    },
    {
        "question": "Đoạn thơ 'Đất Nước là nơi ta hò hẹn / Đất Nước là nơi em đánh rơi chiếc khăn trong nỗi nhớ thầm' thể hiện:",
        "options": ["Đất Nước gắn liền với tình yêu lứa đôi và những kỷ niệm riêng tư", "Đất Nước rất rộng lớn", "Nhân vật em rất hay quên đồ", "Sự khó khăn của việc yêu xa"],
        "answer": "Đất Nước gắn liền với tình yêu lứa đôi và những kỷ niệm riêng tư",
        "explanation": "Định nghĩa đất nước không bằng vĩ tuyến mà bằng không gian của tình yêu."
    },
    {
        "question": "Chi tiết 'đàn bò' và 'tiếng đàn' trong bài 'Đàn ghi ta của Lor-ca' gợi lên không gian văn hóa của quốc gia nào?",
        "options": ["Tây Ban Nha", "Việt Nam", "Pháp", "Mỹ"],
        "answer": "Tây Ban Nha",
        "explanation": "Hình ảnh đặc trưng của quê hương Lor-ca với các trận đấu bò tót và tiếng ghi ta huyền thoại."
    },
    {
        "question": "Trong nghị luận văn học, việc liên hệ so sánh với các tác giả khác có tác dụng:",
        "options": ["Làm nổi bật nét riêng của tác giả đang phân tích và mở rộng kiến thức", "Làm bài viết bị loãng ý", "Chứng tỏ mình đọc nhiều sách", "Để tránh phải viết về tác phẩm chính"],
        "answer": "Làm nổi bật nét riêng của tác giả đang phân tích và mở rộng kiến thức",
        "explanation": "So sánh giúp định vị phong cách nghệ thuật độc đáo của mỗi nhà văn."
    },
    {
        "question": "Hình ảnh 'con thuyền' trong 'Chiếc thuyền ngoài xa' mang ý nghĩa biểu tượng gì ở cuối tác phẩm?",
        "options": ["Biểu tượng cho gia đình hàng chài lênh đênh giữa sóng gió cuộc đời", "Một phương tiện giao thông lỗi thời", "Sự thành công của nghệ thuật nhiếp ảnh", "Vẻ đẹp vĩnh cửu của biển cả"],
        "answer": "Biểu tượng cho gia đình hàng chài lênh đênh giữa sóng gió cuộc đời",
        "explanation": "Con thuyền hiện ra mờ ảo trong sương nhưng thực tế bên trong là những phận đời đầy đau khổ."
    },
    {
        "question": "Tại sao Mị lại nói 'Nếu có nắm lá ngón trong tay lúc này, Mị sẽ ăn cho chết ngay chứ không buồn nhớ lại nữa'?",
        "options": ["Sự thức tỉnh về nỗi đau thân phận khiến Mị không chịu nổi thực tại", "Mị thích ăn lá ngón", "Mị muốn hù dọa A Sử", "Mị quá mệt mỏi vì công việc"],
        "answer": "Sự thức tỉnh về nỗi đau thân phận khiến Mị không chịu nổi thực tại",
        "explanation": "Chỉ khi muốn sống đúng nghĩa, con người mới cảm thấy cái chết là sự giải thoát khỏi kiếp nô lệ."
    },
    {
        "question": "Hình ảnh 'dòng sông' trong thơ Việt Nam thời kỳ 1945-1975 thường gắn liền với cảm hứng:",
        "options": ["Đất nước hóa thân và lịch sử chống ngoại xâm", "Sự lãng mạn, cô độc", "Sự tàn phá của thiên tai", "Nỗi buồn chia ly"],
        "answer": "Đất nước hóa thân và lịch sử chống ngoại xâm",
        "explanation": "Sông Hồng, sông Đà, sông Lô... đều trở thành những nhân chứng hùng hồn cho sức mạnh dân tộc."
    },
    {
        "question": "Đặc trưng của thơ Nguyễn Khoa Điềm là gì?",
        "options": ["Sự kết hợp giữa cảm xúc nồng nàn và suy tư sâu sắc của người trí thức", "Sự hồn nhiên, trong sáng", "Sự gai góc, hận thù", "Sự trào phúng, mỉa mai"],
        "answer": "Sự kết hợp giữa cảm xúc nồng nàn và suy tư sâu sắc của người trí thức",
        "explanation": "Thơ ông giàu chất suy tưởng, triết lý nhưng vẫn rất thiết tha, gần gũi."
    },
    {
        "question": "Trong văn bản đọc hiểu, câu hỏi 'Anh/chị hiểu như thế nào về nhận định sau' yêu cầu thí sinh làm gì?",
        "options": ["Giải thích nghĩa của nhận định và nêu quan điểm cá nhân", "Chép lại nhận định đó", "Phê phán người viết nhận định", "Tìm lỗi chính tả trong nhận định"],
        "answer": "Giải thích nghĩa của nhận định và nêu quan điểm cá nhân",
        "explanation": "Thí sinh cần phân tích các từ khóa và rút ra thông điệp mà nhận định muốn truyền tải."
    },
    {
        "question": "Ý nghĩa cái chết của Lor-ca trong bài thơ của Thanh Thảo là gì?",
        "options": ["Sự hy sinh vì tự do và sự bất diệt của nghệ thuật đích thực", "Một tai nạn đáng tiếc", "Sự chấm dứt của một trào lưu văn học", "Lời cảnh báo cho các nghệ sĩ khác"],
        "answer": "Sự hy sinh vì tự do và sự bất diệt của nghệ thuật đích thực",
        "explanation": "Tiếng đàn vẫn vang lên 'li-la li-la' dù người nghệ sĩ đã nằm xuống."
    }
,
    {
        "question": "Văn bản 'Tuyên ngôn Độc lập' của Hồ Chí Minh được viết theo phong cách ngôn ngữ nào?",
        "options": ["Chính luận", "Báo chí", "Hành chính", "Nghệ thuật"],
        "answer": "Chính luận",
        "explanation": "Sử dụng lý lẽ, bằng chứng thép để khẳng định quyền độc lập dân tộc trước toàn thế giới."
    },
    {
        "question": "Trong 'Tuyên ngôn Độc lập', Bác Hồ trích dẫn bản Tuyên ngôn của Mỹ và Pháp nhằm mục đích gì?",
        "options": ["Dùng lý lẽ của đối phương để bác bỏ luận điệu của chúng", "Để khoe kiến thức sâu rộng", "Để nhờ vả sự giúp đỡ của hai nước này", "Để ca ngợi chủ nghĩa đế quốc"],
        "answer": "Dùng lý lẽ của đối phương để bác bỏ luận điệu của chúng",
        "explanation": "Đây là nghệ thuật 'gậy ông đập lưng ông', tạo tính khách quan và uy lực cho bản tuyên ngôn."
    },
    {
        "question": "Hình ảnh 'Đất nước mình người con gái kiêu sa' trong thơ Nguyễn Đình Thi gợi lên vẻ đẹp gì?",
        "options": ["Vẻ đẹp kiêu hãnh, lãng mạn giữa đau thương", "Sự yếu đuối của phụ nữ", "Vẻ đẹp của một mỹ nhân cụ thể", "Sự giàu sang của đất nước"],
        "answer": "Vẻ đẹp kiêu hãnh, lãng mạn giữa đau thương",
        "explanation": "Khắc họa hình tượng đất nước hóa thân vào những vẻ đẹp tâm hồn cao khiết ngay trong khói lửa."
    },
    {
        "question": "Ý nghĩa biểu tượng của hình ảnh 'con tàu' trong bài thơ 'Tiếng hát con tàu' là:",
        "options": ["Khát vọng lên đường, tìm về với nhân dân và ngọn nguồn cảm hứng", "Phương tiện vận tải hiện đại", "Sự di cư của dân cư", "Biểu tượng của ngành đường sắt"],
        "answer": "Khát vọng lên đường, tìm về với nhân dân và ngọn nguồn cảm hứng",
        "explanation": "Con tàu là tâm hồn nhà thơ đang khao khát thoát khỏi cái tôi chật hẹp để hòa nhập cuộc sống chung."
    },
    {
        "question": "Trong bài thơ 'Việt Bắc', những kỷ niệm về 'bát cơm chấm muối, mối thù nặng vai' thể hiện điều gì?",
        "options": ["Cuộc sống gian khổ nhưng giàu nghĩa tình cách mạng", "Sự nghèo đói của vùng cao", "Lòng căm thù giặc sâu sắc", "Sự thiếu thốn của quân đội"],
        "answer": "Cuộc sống gian khổ nhưng giàu nghĩa tình cách mạng",
        "explanation": "Sự đồng cam cộng khổ đã tạo nên sợi dây liên kết bền chặt giữa quân và dân."
    },
    {
        "question": "Dòng sông Hương ở thượng nguồn trong 'Ai đã đặt tên cho dòng sông?' được ví như:",
        "options": ["Một bản trường ca của rừng già", "Một người con gái dịu dàng", "Một áng tóc trữ tình", "Một người mẹ hiền"],
        "answer": "Một bản trường ca của rừng già",
        "explanation": "Sông Hương ở đây mang vẻ đẹp mãnh liệt, hoang dại và đầy cá tính trước khi về đồng bằng."
    },
    {
        "question": "Nghệ thuật xây dựng tình huống trong 'Vợ nhặt' được đánh giá là:",
        "options": ["Tình huống độc đáo, oái oăm (vừa mừng vừa lo)", "Tình huống trào phúng", "Tình huống tâm lý phức tạp", "Tình huống hành động kịch tính"],
        "answer": "Tình huống độc đáo, oái oăm (vừa mừng vừa lo)",
        "explanation": "Việc lấy vợ là chuyện vui nhưng lại diễn ra giữa lúc đói khát, người chết như ngả rạ."
    },
    {
        "question": "Trong 'Vợ chồng A Phủ', âm thanh tiếng sáo có ý nghĩa gì đối với Mị?",
        "options": ["Là sợi dây nối Mị với quá khứ và khát vọng sống", "Là âm thanh gây phiền nhiễu", "Là tín hiệu của thống lý Pá Tra", "Là điệu nhạc buồn về thân phận"],
        "answer": "Là sợi dây nối Mị với quá khứ và khát vọng sống",
        "explanation": "Tiếng sáo đánh thức phần hồn đang bị tê liệt, khiến Mị muốn đi chơi, muốn làm người."
    },
    {
        "question": "Sông Đà hung bạo được Nguyễn Tuân miêu tả qua những chi tiết nào?",
        "options": ["Thác đá, hút nước và thạch trận", "Cây cối hai bên bờ", "Màu nước theo mùa", "Đàn cá bơi lội"],
        "answer": "Thác đá, hút nước và thạch trận",
        "explanation": "Tác giả sử dụng thuật ngữ quân sự và thể thao để tô đậm vẻ dữ dằn của dòng sông."
    },
    {
        "question": "Nhân vật ông lái đò trong cuộc chiến với sông Đà thể hiện vẻ đẹp gì?",
        "options": ["Vẻ đẹp của trí dũng và tay lái hoa mỹ", "Vẻ đẹp của sự may mắn", "Vẻ đẹp của sức mạnh cơ bắp thuần túy", "Vẻ đẹp của sự nhút nhát"],
        "answer": "Vẻ đẹp của trí dũng và tay lái hoa mỹ",
        "explanation": "Ông nắm chắc 'binh pháp của thần sông thần đá', điều khiển con thuyền như một nghệ sĩ."
    },
    {
        "question": "Trong bài thơ 'Đất Nước' của Nguyễn Khoa Điềm, Đất Nước được hình thành từ đâu?",
        "options": ["Từ những cái gần gũi như câu chuyện cổ tích, miếng trầu, cái kèo cái cột", "Từ những cuộc chiến tranh vĩ đại", "Từ những vị thần", "Từ sự ban phát của thiên nhiên"],
        "answer": "Từ những cái gần gũi như câu chuyện cổ tích, miếng trầu, cái kèo cái cột",
        "explanation": "Đất Nước không ở đâu xa mà kết tinh trong cuộc sống bình dị hàng ngày của nhân dân."
    },
    {
        "question": "Phong cách nghệ thuật của Hoàng Phủ Ngọc Tường là gì?",
        "options": ["Sự kết hợp nhuần nhuyễn giữa chất trí tuệ và chất trữ tình", "Sự gai góc, góc cạnh", "Sự giản dị, mộc mạc", "Sự phóng túng, ngông ngạo"],
        "answer": "Sự kết hợp nhuần nhuyễn giữa chất trí tuệ và chất trữ tình",
        "explanation": "Văn ông giàu kiến thức văn hóa, lịch sử nhưng lại rất lãng mạn và bay bổng."
    },
    {
        "question": "Thông điệp về nghệ thuật trong 'Chiếc thuyền ngoài xa' là gì?",
        "options": ["Nghệ thuật phải gắn liền với cuộc đời, người nghệ sĩ không được nhìn hời hợt", "Nghệ thuật chỉ cần cái đẹp là đủ", "Nghệ sĩ phải đi thật xa mới có tác phẩm hay", "Nghệ thuật không nên quan tâm đến cái xấu"],
        "answer": "Nghệ thuật phải gắn liền với cuộc đời, người nghệ sĩ không được nhìn hời hợt",
        "explanation": "Phải có cái nhìn đa diện, sâu sắc mới thấu hiểu được bản chất của cuộc sống."
    },
    {
        "question": "Sự thay đổi của Tràng sau khi 'nhặt' được vợ thể hiện qua chi tiết nào?",
        "options": ["Thấy mình nên người, có bổn phận lo cho gia đình", "Trở nên cáu gắt hơn", "Chỉ biết lo sợ cái đói", "Không có thay đổi gì"],
        "answer": "Thấy mình nên người, có bổn phận lo cho gia đình",
        "explanation": "Hạnh phúc gia đình đã khơi dậy ý thức trách nhiệm và sự trưởng thành trong anh."
    },
    {
        "question": "Trong 'Hồn Trương Ba, da hàng thịt', nguyên nhân khiến Trương Ba đau khổ là:",
        "options": ["Sự lệch lạc giữa linh hồn thanh cao và thể xác phàm tục", "Vì bị gia đình ruồng bỏ", "Vì không được đánh cờ", "Vì xác hàng thịt quá xấu"],
        "answer": "Sự lệch lạc giữa linh hồn thanh cao và thể xác phàm tục",
        "explanation": "Đây là bi kịch về sự tha hóa khi con người không được sống đúng với bản chất của mình."
    },
    {
        "question": "Lối thơ của Xuân Quỳnh trong bài 'Sóng' mang đặc điểm gì?",
        "options": ["Vừa nồng nàn táo bạo, vừa giàu đức hy sinh và lo âu", "Mạnh mẽ và đầy triết lý", "Hồn nhiên, vô tư lự", "Bí ẩn và siêu thực"],
        "answer": "Vừa nồng nàn táo bạo, vừa giàu đức hy sinh và lo âu",
        "explanation": "Thể hiện trọn vẹn bản năng yêu và sự nhạy cảm của người phụ nữ."
    },
    {
        "question": "Nghệ thuật 'bi tráng' trong bài thơ 'Tây Tiến' được hiểu là gì?",
        "options": ["Sự kết hợp giữa cái đau thương (bi) và cái hùng tráng", "Chỉ có sự đau thương, mất mát", "Chỉ có sự hào hùng, không có mất mát", "Sự hài hước trong chiến đấu"],
        "answer": "Sự kết hợp giữa cái đau thương (bi) và cái hùng tráng",
        "explanation": "Viết về cái chết nhưng không bi lụy, mà lồng lộng khí thế anh hùng."
    },
    {
        "question": "Trong 'Rừng xà nu', tại sao Tnú phải ra đi dù rất yêu làng?",
        "options": ["Để đi tìm con đường cứu nước lớn lao hơn cho dân làng", "Để trốn tránh sự truy đuổi của giặc", "Vì bị dân làng đuổi đi", "Để tìm gia đình mới"],
        "answer": "Để đi tìm con đường cứu nước lớn lao hơn cho dân làng",
        "explanation": "Cá nhân Tnú phải hòa vào cuộc chiến chung của cả dân tộc."
    },
    {
        "question": "Hình ảnh 'người đàn bà hàng chài' biểu tượng cho điều gì?",
        "options": ["Sự nhẫn nhục, lòng vị tha và tình mẫu tử thiêng liêng", "Sự nghèo đói và ngu dốt", "Sự cam chịu số phận một cách mù quáng", "Vẻ đẹp của lao động biển"],
        "answer": "Sự nhẫn nhục, lòng vị tha và tình mẫu tử thiêng liêng",
        "explanation": "Bà chấp nhận đau đớn thể xác để giữ gìn tổ ấm cho các con."
    },
    {
        "question": "Chi tiết 'đám cưới chuột' hoặc 'con gà con lợn' trong thơ Hoàng Cầm gợi lên không gian nào?",
        "options": ["Không gian văn hóa Kinh Bắc đậm chất dân gian", "Cảnh làng quê nghèo đói", "Sự giàu có của các hộ gia đình", "Sự hoang tàn của chiến tranh"],
        "answer": "Không gian văn hóa Kinh Bắc đậm chất dân gian",
        "explanation": "Gợi nhắc về vẻ đẹp truyền thống của tranh Đông Hồ và hồn quê Kinh Bắc."
    },
    {
        "question": "Trong văn nghị luận, 'dẫn chứng' cần đảm bảo các tiêu chí nào?",
        "options": ["Chính xác, tiêu biểu, toàn diện và có sức thuyết phục", "Càng nhiều càng tốt", "Phải là những dẫn chứng từ nước ngoài", "Chỉ cần dẫn chứng trong sách giáo khoa"],
        "answer": "Chính xác, tiêu biểu, toàn diện và có sức thuyết phục",
        "explanation": "Dẫn chứng tốt giúp lý lẽ trở nên thực tế và đáng tin cậy hơn."
    },
    {
        "question": "Câu thơ 'Mai sau con lớn cho con đi đâu' của Xuân Quỳnh thể hiện điều gì?",
        "options": ["Nỗi lo âu về sự hữu hạn của đời người và tương lai của con", "Sự hào hứng về hành trình sắp tới", "Sự lười biếng của người mẹ", "Sự ép buộc con cái"],
        "answer": "Nỗi lo âu về sự hữu hạn của đời người và tương lai của con",
        "explanation": "Bộc lộ bản năng lo xa và tình yêu thương vô bờ bến của người mẹ."
    },
    {
        "question": "Thao tác lập luận nào dùng để làm rõ các mặt, các thuộc tính của một vấn đề?",
        "options": ["Phân tích", "Bình luận", "So sánh", "Bác bỏ"],
        "answer": "Phân tích",
        "explanation": "Chia nhỏ đối tượng để tìm hiểu sâu hơn về bản chất bên trong."
    },
    {
        "question": "Hàm ý của hình ảnh 'vết sẹo' trong 'Chiếc lược ngà' là gì?",
        "options": ["Chứng tích của chiến tranh và rào cản ngăn cách tình phụ tử", "Sự hung dữ của nhân vật", "Sự thất bại trong chiến đấu", "Chỉ là một đặc điểm nhận dạng"],
        "answer": "Chứng tích của chiến tranh và rào cản ngăn cách tình phụ tử",
        "explanation": "Vết sẹo khiến bé Thu không nhận ra ba, đồng thời tố cáo tội ác của quân xâm lược."
    },
    {
        "question": "Tác phẩm 'Những đứa con trong gia đình' viết theo phương thức trần thuật nào?",
        "options": ["Trần thuật qua dòng tâm tư của nhân vật (Việt)", "Người kể chuyện ngôi thứ ba khách quan", "Trần thuật theo trình tự thời gian tuyến tính", "Trần thuật qua lời kể của nhân vật Chiến"],
        "answer": "Trần thuật qua dòng tâm tư của nhân vật (Việt)",
        "explanation": "Cách kể này tạo sự chân thực và chiều sâu tâm lý cho tác phẩm."
    }
,
    {
        "question": "Phương thức biểu đạt chính của một văn bản bàn về vấn đề 'Hiện tượng sống ảo của giới trẻ' là gì?",
        "options": ["Nghị luận", "Tự sự", "Thuyết minh", "Biểu cảm"],
        "answer": "Nghị luận",
        "explanation": "Văn bản đưa ra quan điểm, lý lẽ và dẫn chứng để thuyết phục người đọc về một vấn đề xã hội."
    },
    {
        "question": "Biện pháp tu từ nào được sử dụng trong câu: 'Tiếng suối trong như tiếng hát xa'?",
        "options": ["So sánh", "Ẩn dụ", "Hoán dụ", "Nhân hóa"],
        "answer": "So sánh",
        "explanation": "Sử dụng từ so sánh 'như' để đối chiếu âm thanh của suối và tiếng hát."
    },
    {
        "question": "Phong cách ngôn ngữ nào thường dùng trong các văn bản pháp luật, nghị định, thông tư?",
        "options": ["Hành chính", "Chính luận", "Khoa học", "Sinh hoạt"],
        "answer": "Hành chính",
        "explanation": "Dùng trong giao tiếp giữa các cơ quan nhà nước hoặc giữa nhà nước với cá nhân."
    },
    {
        "question": "Xác định thao tác lập luận chính trong đoạn văn bác bỏ một quan điểm sai lầm?",
        "options": ["Bác bỏ", "Chứng minh", "Bình luận", "Giải thích"],
        "answer": "Bác bỏ",
        "explanation": "Dùng lý lẽ và dẫn chứng để phủ nhận một ý kiến, quan điểm khác."
    },
    {
        "question": "Phép liên kết nào được dùng khi sử dụng các từ: 'vì vậy', 'do đó', 'tóm lại'?",
        "options": ["Phép nối", "Phép lặp", "Phép thế", "Phép liên tưởng"],
        "answer": "Phép nối",
        "explanation": "Sử dụng các từ ngữ có tác dụng kết nối các câu, các đoạn văn."
    },

    # --- PHẦN TÁC PHẨM VĂN HỌC (CÂU 16-50) ---
    {
        "question": "Hình ảnh 'Dốc lên khúc khuỷu dốc thăm thẳm' trong bài Tây Tiến gợi lên điều gì?",
        "options": ["Sự hiểm trở, gập ghềnh của địa hình Trường Sơn", "Vẻ đẹp trữ tình của núi rừng",
                    "Sự vui tươi của người lính", "Cảnh sinh hoạt của người dân Tây Bắc"],
        "answer": "Sự hiểm trở, gập ghềnh của địa hình Trường Sơn",
        "explanation": "Từ láy tượng hình tạo ấn tượng mạnh về sự khó khăn, gian khổ của chặng đường hành quân."
    },
    {
        "question": "Trong bài thơ 'Việt Bắc', hình ảnh nào tượng trưng cho người ra đi và người ở lại?",
        "options": ["Mình - Ta", "Anh - Em", "Ông - Cháu", "Thuyền - Bến"],
        "answer": "Mình - Ta",
        "explanation": "Lối xưng hô ngọt ngào như trong ca dao giao duyên, thể hiện tình nghĩa gắn bó giữa cán bộ và nhân dân."
    },
    {
        "question": "Tư tưởng cốt lõi của bài thơ 'Đất Nước' (Nguyễn Khoa Điềm) là gì?",
        "options": ["Đất Nước của Nhân dân", "Đất Nước của các vị vua", "Đất Nước của những anh hùng hào kiệt",
                    "Đất Nước của thần linh"],
        "answer": "Đất Nước của Nhân dân",
        "explanation": "Tác giả khẳng định nhân dân là người làm ra văn hóa, lịch sử và địa lý của đất nước."
    },
    {
        "question": "Trong truyện 'Vợ chồng A Phủ', hành động nào là đỉnh cao của sự phản kháng ở Mị?",
        "options": ["Cắt dây cởi trói cho A Phủ và cùng chạy trốn", "Ăn lá ngón tự tử", "Lấy rượu uống ực từng bát",
                    "Xắn mỡ bỏ vào đĩa đèn cho sáng"],
        "answer": "Cắt dây cởi trói cho A Phủ và cùng chạy trốn",
        "explanation": "Đây là sự bùng nổ của lòng yêu sống và khát vọng tự do sau bao năm bị kìm kẹp."
    },
    {
        "question": "Nhân vật Tràng trong 'Vợ nhặt' quyết định đưa người đàn bà về nhà trong bối cảnh nào?",
        "options": ["Nạn đói khủng khiếp năm 1945", "Thời kỳ bao cấp", "Kháng chiến chống Pháp",
                    "Trong một lễ hội làng"],
        "answer": "Nạn đói khủng khiếp năm 1945",
        "explanation": "Cái đói và cái chết bủa vây nhưng con người vẫn khao khát tổ ấm gia đình."
    },
    {
        "question": "Hình tượng con sông Đà trong tùy bút của Nguyễn Tuân được miêu tả với hai tính cách đối lập nào?",
        "options": ["Hung bạo và Trữ tình", "Hiền hòa và Dữ dội", "Sâu sắc và Nông cạn", "Vui vẻ và Buồn bã"],
        "answer": "Hung bạo và Trữ tình",
        "explanation": "Sông Đà vừa là 'kẻ thù số một' với thạch trận nguy hiểm, vừa đẹp như một 'cố nhân'."
    },
    {
        "question": "Tác phẩm 'Ai đã đặt tên cho dòng sông?' ca ngợi vẻ đẹp của dòng sông nào?",
        "options": ["Sông Hương", "Sông Đà", "Sông Đuống", "Sông Lô"],
        "answer": "Sông Hương",
        "explanation": "Hoàng Phủ Ngọc Tường đã miêu tả sông Hương gắn liền với văn hóa, lịch sử vùng đất cố đô Huế."
    },
    {
        "question": "Trong bài thơ 'Sóng', trạng thái nào của sóng được ví với tâm trạng người phụ nữ khi yêu?",
        "options": ["Dữ dội và dịu êm, ồn ào và lặng lẽ", "Mạnh mẽ và khô khan", "Luôn luôn đứng yên",
                    "Chỉ có sự lặng lẽ"],
        "answer": "Dữ dội và dịu êm, ồn ào và lặng lẽ",
        "explanation": "Sóng và em có những đối cực tâm trạng giống nhau khi đối diện với tình yêu."
    },
    {
        "question": "Chi tiết 'bát cháo hành' trong tác phẩm 'Chí Phèo' có ý nghĩa gì?",
        "options": ["Biểu tượng của tình thương, thức tỉnh nhân tính của Chí Phèo", "Món ăn yêu thích của Chí Phèo",
                    "Sự chăm sóc của bà cô dành cho Chí", "Món quà của dân làng Vũ Đại"],
        "answer": "Biểu tượng của tình thương, thức tỉnh nhân tính của Chí Phèo",
        "explanation": "Sự chăm sóc giản đơn của Thị Nở đã khơi dậy niềm khao khát làm người lương thiện của Chí."
    },
    {
        "question": "Bài thơ 'Đàn ghi ta của Lor-ca' sử dụng những âm thanh 'li-la li-la li-la' nhằm mục đích gì?",
        "options": ["Mô phỏng tiếng đàn và gợi sự bất tử của nghệ thuật", "Làm cho bài thơ vui nhộn",
                    "Miêu tả cảnh thiên nhiên Tây Ban Nha", "Thể hiện sự bối rối của tác giả"],
        "answer": "Mô phỏng tiếng đàn và gợi sự bất tử của nghệ thuật",
        "explanation": "Chuỗi âm thanh gợi nhắc về hình ảnh loài hoa li-la và sức sống mãnh liệt của cái đẹp."
    },
    {
        "question": "Lời phủ dụ của vua Quang Trung trong 'Hoàng Lê nhất thống chí' khẳng định điều gì?",
        "options": ["Chủ quyền dân tộc và quyết tâm đánh đuổi quân xâm lược", "Sự giàu có của đất nước",
                    "Lòng trung thành với nhà Lê", "Sự mệt mỏi vì chiến tranh"],
        "answer": "Chủ quyền dân tộc và quyết tâm đánh đuổi quân xâm lược",
        "explanation": "Lời dụ nhấn mạnh vào lằn ranh giới hạn giữa 'ta' và 'địch' và truyền tinh thần thép cho binh sĩ."
    },
    {
        "question": "Nguyên nhân chính dẫn đến bi kịch của Hộ trong 'Đời thừa' là gì?",
        "options": ["Sự mâu thuẫn giữa lý tưởng nghệ thuật cao cả và gánh nặng cơm áo gạo tiền", "Sự phản bội của vợ",
                    "Sự chèn ép của đồng nghiệp", "Sự lười biếng của chính mình"],
        "answer": "Sự mâu thuẫn giữa lý tưởng nghệ thuật cao cả và gánh nặng cơm áo gạo tiền",
        "explanation": "Hộ là một trí thức có tâm nhưng bị cuộc đời 'ghì sát đất' dẫn đến tha hóa nhân cách."
    },
    {
        "question": "Trong 'Chiếc thuyền ngoài xa', phát hiện thứ nhất của nghệ sĩ Phùng là gì?",
        "options": ["Cảnh đẹp 'trời cho' của chiếc thuyền trong sương sớm", "Cảnh người chồng đánh vợ dã man",
                    "Cảnh đứa con đánh bố", "Cảnh bãi biển đầy rác"],
        "answer": "Cảnh đẹp 'trời cho' của chiếc thuyền trong sương sớm",
        "explanation": "Đây là vẻ đẹp tuyệt mỹ về nghệ thuật mà anh hằng theo đuổi."
    },
    {
        "question": "Ý nghĩa cái tên truyện 'Vợ nhặt' của Kim Lân là gì?",
        "options": ["Giá trị con người bị rẻ rúng như rơm rác, nhưng vẫn khao khát hạnh phúc",
                    "Việc lấy vợ rất dễ dàng", "Sự may mắn của nhân vật Tràng",
                    "Phê phán thói tham ăn của người đàn bà"],
        "answer": "Giá trị con người bị rẻ rúng như rơm rác, nhưng vẫn khao khát hạnh phúc",
        "explanation": "Nhặt được vợ như nhặt vật rơi vãi dọc đường, phản ánh sự khốc liệt của nạn đói."
    },
    {
        "question": "Trong bài thơ 'Tây Tiến', từ 'đoàn binh không mọc tóc' phản ánh sự thật nào?",
        "options": ["Bệnh sốt rét rừng hiểm ác khiến lính rụng tóc", "Người lính chủ động cạo trọc để đánh giáp lá cà",
                    "Sở thích thời trang của lính Tây Tiến", "Thiếu thốn dụng cụ cắt tóc"],
        "answer": "Bệnh sốt rét rừng hiểm ác khiến lính rụng tóc",
        "explanation": "Quang Dũng không né tránh hiện thực gian khổ nhưng vẫn lồng ghép cái nhìn kiêu hùng (quân xanh màu lá dữ oai hùm)."
    },
    {
        "question": "Câu thơ 'Con sóng dưới lòng sâu / Con sóng trên mặt nước' trong bài 'Sóng' thể hiện điều gì?",
        "options": ["Nỗi nhớ thường trực, bao trùm cả không gian và thời gian", "Kiến thức địa lý về đại dương",
                    "Sự nguy hiểm của biển cả", "Sự luân hồi của tự nhiên"],
        "answer": "Nỗi nhớ thường trực, bao trùm cả không gian và thời gian",
        "explanation": "Sóng tồn tại ở mọi tầng lớp cũng như nỗi nhớ của em len lỏi vào cả tiềm thức và ý thức."
    },
    {
        "question": "Hồn Trương Ba trong vở kịch của Lưu Quang Vũ khát vọng điều gì?",
        "options": ["Được sống là chính mình, nguyên vẹn, thống nhất giữa xác và hồn", "Được sống mãi mãi",
                    "Được trở nên giàu có", "Được người đời kính trọng"],
        "answer": "Được sống là chính mình, nguyên vẹn, thống nhất giữa xác và hồn",
        "explanation": "Bi kịch 'bên trong một đằng, bên ngoài một nẻo' khiến Trương Ba lựa chọn cái chết để bảo vệ sự thanh cao."
    },
    {
        "question": "Chi tiết 'mùi thuốc súng' và 'tiếng đàn' trong bài 'Đàn ghi ta của Lor-ca' gợi lên sự giao thoa giữa:",
        "options": ["Chiến tranh và nghệ thuật", "Sự sống và cái chết", "Quá khứ và hiện tại", "Âm nhạc và hội họa"],
        "answer": "Chiến tranh và nghệ thuật",
        "explanation": " Lor-ca là nghệ sĩ chiến sĩ chết vì tự do trên tay vẫn ôm cây đàn."
    },
    {
        "question": "Vẻ đẹp của cụ Mết trong 'Rừng xà nu' đại diện cho điều gì?",
        "options": ["Sức mạnh truyền thống và niềm tin của dân tộc Tây Nguyên", "Sự bảo thủ của thế hệ già",
                    "Sự yếu đuối trước vũ khí hiện đại", "Tình yêu thiên nhiên hoang dã"],
        "answer": "Sức mạnh truyền thống và niềm tin của dân tộc Tây Nguyên",
        "explanation": "Cụ là chỗ dựa tinh thần, là người giữ lửa cho cuộc chiến đấu của làng Xô Man."
    },
    {
        "question": "Tại sao Nguyễn Tuân gọi người lái đò là một 'nghệ sĩ'?",
        "options": ["Vì ông lái đò bằng tài năng và phong thái ung dung, tài hoa trên thác dữ",
                    "Vì ông biết hát khi chèo thuyền", "Vì ông có vẻ ngoài đẹp trai",
                    "Vì ông thích vẽ tranh về sông Đà"],
        "answer": "Vì ông lái đò bằng tài năng và phong thái ung dung, tài hoa trên thác dữ",
        "explanation": "Trong quan niệm của Nguyễn Tuân, bất cứ ai làm công việc của mình một cách điêu luyện thì đều là nghệ sĩ."
    },
    {
        "question": "Phong cách thơ của Tố Hữu mang đậm tính chất gì?",
        "options": ["Trữ tình chính trị", "Lãng mạn thuần túy", "Triết lý sâu xa", "Hiện thực nghiệt ngã"],
        "answer": "Trữ tình chính trị",
        "explanation": "Thơ ông luôn gắn liền với những chặng đường cách mạng của dân tộc."
    },
    {
        "question": "Trong 'Vợ nhặt', buổi sáng đầu tiên sau khi có vợ, không gian ngôi nhà của Tràng thay đổi như thế nào?",
        "options": ["Sạch sẽ, gọn gàng, mang lại luồng sinh khí mới", "U ám, ẩm thấp hơn", "Vẫn rách nát như cũ",
                    "Đầy rẫy xác người chết đói"],
        "answer": "Sạch sẽ, gọn gàng, mang lại luồng sinh khí mới",
        "explanation": "Sự quét tước của hai người đàn bà biểu tượng cho hy vọng và sự đổi thay."
    },
    {
        "question": "Thông điệp chính từ lời thoại của nhân vật người đàn bà hàng chài ở tòa án huyện là gì?",
        "options": ["Cái nhìn đa diện về cuộc sống, đừng nhìn sự vật chỉ qua vẻ ngoài", "Phụ nữ phải biết chịu đựng",
                    "Nên bỏ chồng khi bị đánh", "Chánh án không biết gì về luật pháp"],
        "answer": "Cái nhìn đa diện về cuộc sống, đừng nhìn sự vật chỉ qua vẻ ngoài",
        "explanation": "Người đàn bà thấu hiểu nỗi khổ của chồng và lý do mình cần một người đàn ông để nuôi con."
    },
    {
        "question": "Phép điệp từ 'Đất Nước' trong bài thơ của Nguyễn Khoa Điềm có tác dụng gì?",
        "options": ["Nhấn mạnh sự hiện diện thiêng liêng và thường trực của đất nước", "Để bài thơ đủ số chữ",
                    "Làm cho người đọc cảm thấy nhàm chán", "Chỉ là thói quen của tác giả"],
        "answer": "Nhấn mạnh sự hiện diện thiêng liêng và thường trực của đất nước",
        "explanation": "Đất Nước không xa xôi mà hiện hữu trong từng mảnh tâm hồn, trong cái kèo cái cột."
    },
    {
        "question": "Câu thơ 'Rải rác biên cương mồ viễn xứ' trong bài Tây Tiến sử dụng nhiều từ Hán Việt nhằm:",
        "options": ["Tạo không khí trang trọng, cổ kính và giảm nhẹ đau thương", "Làm cho câu thơ khó hiểu",
                    "Khoe khoang kiến thức từ vựng", "Gợi sự xa lạ của vùng biên giới"],
        "answer": "Tạo không khí trang trọng, cổ kính và giảm nhẹ đau thương",
        "explanation": "Cái chết của người lính được khoác lên tấm áo bi tráng, thiêng liêng."
    },
    {
        "question": "Hình ảnh 'con sóng' và 'em' trong bài thơ của Xuân Quỳnh là mối quan hệ:",
        "options": ["Song hành, ẩn dụ cho nhau", "Đối lập gay gắt", "Không liên quan", "Chủ thể và khách thể"],
        "answer": "Song hành, ẩn dụ cho nhau",
        "explanation": "Sóng là em, em cũng là sóng, cả hai cùng soi sáng cho tâm trạng của người phụ nữ đang yêu."
    },
    {
        "question": "Tại sao Mị không ăn lá ngón tự tử trong đêm tình mùa xuân?",
        "options": ["Vì tiếng sáo đã đánh thức lòng yêu đời và ký ức tươi đẹp", "Vì không tìm thấy lá ngón",
                    "Vì sợ đau", "Vì A Sử đã lấy mất lá ngón của Mị"],
        "answer": "Vì tiếng sáo đã đánh thức lòng yêu đời và ký ức tươi đẹp",
        "explanation": "Tiếng sáo lửng lơ ngoài đường là chất xúc tác đưa Mị từ cõi chết trở về cõi sống."
    },
    {
        "question": "Chi tiết 'bàn tay bị cụt đốt' của Tnú trong 'Rừng xà nu' nói lên điều gì?",
        "options": ["Tội ác của kẻ thù và ý chí bất khuất của người chiến sĩ", "Sự vụng về của Tnú",
                    "Một tai nạn lao động", "Sự trừng phạt của dân làng"],
        "answer": "Tội ác của kẻ thù và ý chí bất khuất của người chiến sĩ",
        "explanation": "Dù bàn tay chỉ còn mỗi ngón hai đốt, Tnú vẫn cầm súng bóp cò giết giặc."
    },
    {
        "question": "Trong 'Người lái đò Sông Đà', Nguyễn Tuân quan sát con sông từ nhiều góc độ khác nhau để thấy:",
        "options": ["Vẻ đẹp đa dạng, biến hóa của sông Đà", "Sự dài rộng của con sông",
                    "Màu nước sông thay đổi theo mùa", "Sự phong phú của các loài cá"],
        "answer": "Vẻ đẹp đa dạng, biến hóa của sông Đà",
        "explanation": "Lúc thì như kẻ thù, lúc thì như một áng tóc trữ tình."
    },
    {
        "question": "Ý nghĩa nhan đề 'Chiếc thuyền ngoài xa' mang hàm ý:",
        "options": ["Khoảng cách giữa nghệ thuật và đời thực", "Vẻ đẹp của biển cả", "Sự khó khăn của nghề chài lưới",
                    "Sở thích đi xa của nghệ sĩ"],
        "answer": "Khoảng cách giữa nghệ thuật và đời thực",
        "explanation": "Cái đẹp ở xa có thể rất hoàn mỹ, nhưng khi lại gần có thể chứa đựng những bi kịch tàn nhẫn."
    },
    {
        "question": "Từ 'Đất Nước' trong thơ Nguyễn Khoa Điềm được viết hoa nhằm:",
        "options": ["Thể hiện sự tôn trọng và coi Đất Nước như một sinh thể sống", "Tuân thủ quy tắc chính tả mới",
                    "Gây chú ý cho người đọc", "Phân biệt với đất nước khác"],
        "answer": "Thể hiện sự tôn trọng và coi Đất Nước như một sinh thể sống",
        "explanation": "Đất Nước được cá thể hóa, trở nên gần gũi như một người thân thiết."
    },
    {
        "question": "Điểm chung của các nhân vật trong 'Những đứa con trong gia đình' là gì?",
        "options": ["Lòng căm thù giặc sâu sắc và truyền thống đánh giặc của gia đình", "Sự nhút nhát", "Thích đi chơi",
                    "Không nghe lời người lớn"],
        "answer": "Lòng căm thù giặc sâu sắc và truyền thống đánh giặc của gia đình",
        "explanation": "Chiến công của Việt và Chiến là sự tiếp nối dòng sông truyền thống của gia đình."
    },
    {
        "question": "Câu thơ 'Dốc pha lê bạn súng ngửi trời' sử dụng nghệ thuật:",
        "options": ["Nhân hóa và cách nói tạt ngang tinh nghịch", "So sánh", "Nói giảm nói tránh", "Liệt kê"],
        "answer": "Nhân hóa và cách nói tạt ngang tinh nghịch",
        "explanation": "Gợi tư thế hiên ngang, chiếm lĩnh đỉnh cao của người lính Tây Tiến."
    },
    {
        "question": "Mục đích của việc lập dàn ý cho bài văn nghị luận văn học là:",
        "options": ["Giúp bài viết mạch lạc, đủ ý, tránh lặp ý hoặc thiếu ý", "Làm cho bài viết dài hơn",
                    "Để không phải đọc lại tác phẩm", "Để copy từ bạn bè dễ hơn"],
        "answer": "Giúp bài viết mạch lạc, đủ ý, tránh lặp ý hoặc thiếu ý",
        "explanation": "Dàn ý là khung xương đảm bảo sự logic cho bài nghị luận."
    },
    {
        "question": "Hình ảnh 'rừng xà nu' trong tác phẩm cùng tên của Nguyễn Trung Thành là hình ảnh:",
        "options": ["Biểu tượng cho sức sống bất diệt của con người Tây Nguyên", "Một địa danh cụ thể",
                    "Nguồn tài nguyên gỗ quý", "Nơi ẩn nấp của quân đội"],
        "answer": "Biểu tượng cho sức sống bất diệt của con người Tây Nguyên",
        "explanation": "Cây xà nu ham ánh sáng, đạn đại bác không giết nổi, cũng như dân làng Xô Man."
    },
    {
        "question": "Trong bài thơ 'Tiếng hát con tàu' (Chế Lan Viên), 'con tàu' biểu tượng cho:",
        "options": ["Khát vọng lên đường, hòa nhập với nhân dân và cuộc sống mới", "Phương tiện giao thông thực tế",
                    "Sự chia ly", "Sự hiện đại của công nghiệp"],
        "answer": "Khát vọng lên đường, hòa nhập với nhân dân và cuộc sống mới",
        "explanation": "Dù thực tế chưa có đường tàu lên Tây Bắc, nhưng con tàu tâm tưởng đã khởi hành."
    },
    {
        "question": "Câu 'Nhà thơ là người thư ký trung thành của thời đại.' khẳng định điều gì?",
        "options": ["Văn học phải phản ánh chân thực cuộc sống và thời đại", "Nhà thơ phải biết ghi chép nhanh",
                    "Văn học chỉ là những con số", "Nhà thơ phải làm việc trong văn phòng"],
        "answer": "Văn học phải phản ánh chân thực cuộc sống và thời đại",
        "explanation": "Tác phẩm văn học là tấm gương soi bóng thời đại mà nó sinh ra."
    },
    {
        "question": "Nét độc đáo của thơ Xuân Quỳnh là gì?",
        "options": ["Tiếng nói của trái tim phụ nữ chân thành, giàu khao khát và lo âu", "Sự mạnh mẽ, khô khan",
                    "Sự hời hợt", "Sự bí ẩn, khó hiểu"],
        "answer": "Tiếng nói của trái tim phụ nữ chân thành, giàu khao khát và lo âu",
        "explanation": "Thơ bà là sự kết hợp giữa sự đằm thắm truyền thống và khát vọng hiện đại."
    },
    {
        "question": "Trong 'Vợ chồng A Phủ', tại sao Mị lại nói 'Ở lâu trong cái khổ, Mị quen khổ rồi'?",
        "options": ["Sự tê liệt về tinh thần và ý thức phản kháng", "Vì Mị thích sống khổ",
                    "Vì gia đình thống lý Pá Tra đối xử rất tốt", "Vì Mị là người lạc quan"],
        "answer": "Sự tê liệt về tinh thần và ý thức phản kháng",
        "explanation": "Sức ép của cường quyền và thần quyền đã làm mòn đi ý chí của người phụ nữ."
    },
    {
        "question": "Cụm từ 'mùi nồng mặn' trong 'Đất Nước' của Nguyễn Đình Thi gợi lên:",
        "options": ["Sự gian khổ và tình nghĩa gắn cốt của đất nước trong chiến tranh", "Vị của muối biển",
                    "Sự khó chịu của mùi thuốc súng", "Sự tươi mát của đồng quê"],
        "answer": "Sự gian khổ và tình nghĩa gắn cốt của đất nước trong chiến tranh",
        "explanation": "Gợi hình ảnh đất nước đau thương nhưng kiên cường nảy sinh từ máu và bùn lầy."
    },
    {
        "question": "Tác phẩm nào của Nguyễn Tuân được mệnh danh là 'tờ hoa', 'vật báu' của văn chương?",
        "options": ["Vang bóng một thời", "Sông Đà", "Hà Nội ta đánh Mỹ", "Một chuyến đi"],
        "answer": "Vang bóng một thời",
        "explanation": "Tác phẩm lưu giữ những vẻ đẹp văn hóa truyền thống đang dần mai một."
    },
    {
        "question": "Thông điệp của truyện ngắn 'Một người Hà Nội' (Nguyễn Khải) xoay quanh nhân vật nào?",
        "options": ["Bà Hiền", "Nhân vật tôi", "Anh con trai", "Người giúp việc"],
        "answer": "Bà Hiền",
        "explanation": "Bà là 'hạt bụi vàng' lưu giữ nếp sống và bản lĩnh văn hóa của người Hà Thành."
    },
    {
        "question": "Tại sao bài thơ 'Đất Nước' của Nguyễn Khoa Điềm lại sử dụng nhiều chất liệu văn hóa dân gian?",
        "options": ["Để làm cho Đất Nước trở nên gần gũi, thuộc về nhân dân",
                    "Vì tác giả không biết dùng chất liệu khác", "Để quảng bá du lịch",
                    "Để bài thơ mang tính giải trí"],
        "answer": "Để làm cho Đất Nước trở nên gần gũi, thuộc về nhân dân",
        "explanation": "Văn hóa dân gian là linh hồn của dân tộc, do nhân dân tạo ra và giữ gìn."
    },
    {
        "question": "Trong 'Đàn ghi ta của Lor-ca', hình ảnh ' Lor-ca bơi sang ngang / trên chiếc ghi ta màu bạc' gợi liên tưởng:",
        "options": ["Sự thăng hoa của nghệ thuật vượt qua cái chết", "Lor-ca đang đi tắm biển",
                    "Lor-ca dùng đàn làm thuyền", "Sự giàu có của Lor-ca"],
        "answer": "Sự thăng hoa của nghệ thuật vượt qua cái chết",
        "explanation": "Nghệ sĩ có thể ngã xuống nhưng tác phẩm và linh hồn nghệ thuật là bất tử."
    },
    {
        "question": "Yếu tố nào quan trọng nhất để làm nên một bài văn nghị luận xã hội đạt điểm cao?",
        "options": ["Lý lẽ sắc bén, dẫn chứng thực tế và trải nghiệm cá nhân", "Chép lại đúng văn mẫu",
                    "Viết càng dài càng tốt", "Dùng nhiều từ ngữ khó hiểu"],
        "answer": "Lý lẽ sắc bén, dẫn chứng thực tế và trải nghiệm cá nhân",
        "explanation": "Sự sáng tạo và góc nhìn riêng biệt luôn được đánh giá cao trong bài viết nghị luận."
    }

]