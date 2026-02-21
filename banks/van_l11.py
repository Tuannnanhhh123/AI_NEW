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
        "question": "Vở kịch 'Vũ Như Tô' của Nguyễn Huy Tưởng thuộc thể loại nào?",
        "options": ["Bi kịch", "Hài kịch", "Kịch dân gian", "Kịch thơ"],
        "answer": "Bi kịch",
        "explanation": "Đây là vở bi kịch lịch sử nổi tiếng nhất của Nguyễn Huy Tưởng."
    },
    {
        "question": "Trong văn bản 'Cải ơi' (Nguyễn Ngọc Tư), nhân vật ông Năm Nhỏ đi tìm con tên là gì?",
        "options": ["Cải", "Thà", "Mận", "Đào"],
        "answer": "Cải",
        "explanation": "Ông Năm Nhỏ dành cả đời đi tìm đứa con gái riêng của vợ tên là Cải."
    },
    {
        "question": "Tác phẩm 'Tôi đã học tập như thế nào' là của tác giả nào?",
        "options": ["M. Gorki", "Lỗ Tấn", "Nam Cao", "Thạch Lam"],
        "answer": "M. Gorki",
        "explanation": "Đây là văn bản tự truyện tiêu biểu của nhà văn Nga Maxim Gorki."
    },
    {
        "question": "Bài thơ 'Tràng giang' của Huy Cận mang đậm phong cách nghệ thuật nào?",
        "options": ["Cổ điển và Hiện đại", "Hậu hiện đại", "Hiện thực nghiêm ngặt", "Siêu thực"],
        "answer": "Cổ điển và Hiện đại",
        "explanation": "Bài thơ kết hợp thi liệu cổ điển với cái tôi cô đơn của Thơ mới."
    },
    {
        "question": "Trong chương trình Ngữ văn 11 mới, thể thơ 'Sonnet' thường có bao nhiêu dòng?",
        "options": ["14 dòng", "10 dòng", "12 dòng", "16 dòng"],
        "answer": "14 dòng",
        "explanation": "Sonnet là thể thơ châu Âu truyền thống gồm 14 dòng."
    },
    {
        "question": "Văn bản 'Lời tiễn dặn' là truyện thơ của dân tộc nào?",
        "options": ["Dân tộc Thái", "Dân tộc Mường", "Dân tộc Tày", "Dân tộc H'Mông"],
        "answer": "Dân tộc Thái",
        "explanation": "'Xống chụ xon xao' (Lời tiễn dặn) là truyện thơ nổi tiếng của người Thái."
    },
    {
        "question": "Ai là tác giả của bài thơ 'Vội vàng'?",
        "options": ["Xuân Diệu", "Huy Cận", "Hàn Mặc Tử", "Chế Lan Viên"],
        "answer": "Xuân Diệu",
        "explanation": "Xuân Diệu được mệnh danh là nhà thơ mới nhất trong các nhà thơ mới."
    },
    {
        "question": "Khái niệm 'Chỉnh thể' trong tiếp nhận văn học nghĩa là gì?",
        "options": ["Tính toàn vẹn của tác phẩm", "Một phần của đoạn văn", "Cách ngắt nhịp thơ", "Tên một nhân vật"],
        "answer": "Tính toàn vẹn của tác phẩm",
        "explanation": "Chỉnh thể văn học là một đơn vị thống nhất giữa nội dung và hình thức."
    },
    {
        "question": "Trong 'Chữ người tử tù', Huấn Cao nổi tiếng với tài năng gì?",
        "options": ["Viết chữ đẹp", "Làm thơ", "Vẽ tranh", "Đánh đàn"],
        "answer": "Viết chữ đẹp",
        "explanation": "Tài viết chữ của Huấn Cao là biểu tượng cho cái Đẹp."
    },
    {
        "question": "Truyện ngắn 'Chí Phèo' lúc mới in có tên là gì?",
        "options": ["Cái lò gạch cũ", "Đôi lứa xứng đôi", "Chí Phèo", "Làng Vũ Đại ngày ấy"],
        "answer": "Cái lò gạch cũ",
        "explanation": "Nhan đề đầu tiên do nhà xuất bản đặt là 'Cái lò gạch cũ'."
    },
    {
        "question": "Bài thơ 'Đây thôn Vĩ Dạ' lấy cảm hứng từ vùng đất nào?",
        "options": ["Huế", "Hà Nội", "Đà Lạt", "Quảng Bình"],
        "answer": "Huế",
        "explanation": "Thôn Vĩ Dạ nằm bên bờ sông Hương, thuộc cố đô Huế."
    },
    {
        "question": "Phong cách ngôn ngữ nào được dùng trong các văn bản tin tức, báo chí?",
        "options": ["Phong cách ngôn ngữ báo chí", "Phong cách ngôn ngữ sinh hoạt", "Phong cách ngôn ngữ khoa học",
                    "Phong cách ngôn ngữ nghệ thuật"],
        "answer": "Phong cách ngôn ngữ báo chí",
        "explanation": "Đây là phong cách dùng để thông tin về các sự kiện thời sự."
    },
    {
        "question": "Trong văn bản 'Vĩnh biệt Cửu Trùng Đài', nhân vật Đan Thiềm khuyên Vũ Như Tô làm gì khi quân phản loạn đến?",
        "options": ["Bỏ trốn", "Ở lại xây tiếp", "Tự tử", "Đi gặp vua"],
        "answer": "Bỏ trốn",
        "explanation": "Đan Thiềm tỉnh táo hơn Vũ Như Tô, bà khuyên ông lánh nạn để bảo toàn tài năng."
    },
    {
        "question": "Đặc điểm nổi bật của nhân vật trong Bi kịch là gì?",
        "options": ["Thường rơi vào mâu thuẫn không thể hóa giải", "Luôn có kết thúc hạnh phúc",
                    "Là người nông dân hiền lành", "Luôn chiến thắng mọi kẻ thù"],
        "answer": "Thường rơi vào mâu thuẫn không thể hóa giải",
        "explanation": "Nhân vật bi kịch thường có khát vọng cao cả nhưng gặp phải rào cản thực tại khốc liệt."
    },
    {
        "question": "Tác phẩm 'Vợ nhặt' (Kim Lân) lấy bối cảnh thời gian nào?",
        "options": ["Nạn đói năm 1945", "Kháng chiến chống Pháp", "Kháng chiến chống Mỹ", "Thời bao cấp"],
        "answer": "Nạn đói năm 1945",
        "explanation": "Bối cảnh là nạn đói khủng khiếp năm Ất Tỵ."
    },
    {
        "question": "Trong bài thơ 'Tình ca' (Hoàng Trung Thông), tác giả ca ngợi điều gì?",
        "options": ["Tình yêu quê hương, đất nước", "Tình yêu đôi lứa", "Vẻ đẹp của thiên nhiên",
                    "Cuộc sống thành thị"],
        "answer": "Tình yêu quê hương, đất nước",
        "explanation": "Bài thơ thể hiện tình cảm thiết tha với mảnh đất quê hương."
    },
    {
        "question": "Phép lặp là một biện pháp giúp văn bản có tính chất gì?",
        "options": ["Tính liên kết", "Tính hài hước", "Tính trừu tượng", "Tính đa nghĩa"],
        "answer": "Tính liên kết",
        "explanation": "Phép lặp giúp các câu văn kết nối chặt chẽ về mặt hình thức."
    },
    {
        "question": "Tác giả của tác phẩm 'Sống mòn' là ai?",
        "options": ["Nam Cao", "Vũ Trọng Phụng", "Nguyễn Tuân", "Tô Hoài"],
        "answer": "Nam Cao",
        "explanation": "Sống mòn là tiểu thuyết tiêu biểu về cuộc sống bế tắc của trí thức tiểu tư sản."
    },
    {
        "question": "Trong chương trình mới, văn bản nghị luận xã hội đòi hỏi điều gì nhất?",
        "options": ["Lý lẽ và bằng chứng thuyết phục", "Cốt truyện li kỳ", "Vần nhịp thơ ca", "Nhiều từ láy"],
        "answer": "Lý lẽ và bằng chứng thuyết phục",
        "explanation": "Nghị luận phải dựa trên các luận cứ thực tế để thuyết phục người đọc."
    },
    {
        "question": "Nghĩa của từ 'Thiên lương' trong 'Chữ người tử tù' là gì?",
        "options": ["Bản tính tốt lành do trời phú", "Sự giàu sang", "Tài năng viết chữ", "Quyền lực tối cao"],
        "answer": "Bản tính tốt lành do trời phú",
        "explanation": "Huấn Cao trọng cái 'thiên lương' của con người hơn là vàng ngọc."
    },
    {
        "question": "Dòng nào sau đây là đặc điểm của 'Cái tôi' trong Thơ mới?",
        "options": ["Khẳng định cá tính và cảm xúc cá nhân", "Luôn giấu mình sau cái 'ta' chung",
                    "Chỉ viết về đề tài yêu nước", "Sử dụng ngôn ngữ cung đình"],
        "answer": "Khẳng định cá tính và cảm xúc cá nhân",
        "explanation": "Thơ mới là cuộc cách mạng giải phóng cái 'tôi' cá nhân."
    },
    {
        "question": "Bài thơ 'Tôi yêu em' của Pu-skin thuộc nền văn học nào?",
        "options": ["Văn học Nga", "Văn học Pháp", "Văn học Anh", "Văn học Đức"],
        "answer": "Văn học Nga",
        "explanation": "Pu-skin là 'Mặt trời của thi ca Nga'."
    },
    {
        "question": "Văn bản 'Tiếng hát con tàu' (Chế Lan Viên) nói về sự kiện gì?",
        "options": ["Cuộc vận động đi xây dựng kinh tế miền Bắc", "Cuộc kháng chiến chống Mỹ",
                    "Sự ra đời của ngành đường sắt", "Chuyến du lịch Sa Pa"],
        "answer": "Cuộc vận động đi xây dựng kinh tế miền Bắc",
        "explanation": "Bài thơ kêu gọi thanh niên lên đường lên Tây Bắc xây dựng tổ quốc."
    },
    {
        "question": "Yếu tố nào quan trọng nhất trong một bản tin?",
        "options": ["Tính xác thực", "Tính hư cấu", "Sự bay bổng của ngôn từ", "Cảm xúc cá nhân"],
        "answer": "Tính xác thực",
        "explanation": "Bản tin phải cung cấp thông tin chính xác về sự kiện."
    },
    {
        "question": "Nhân vật chính trong truyện 'Đời thừa' là ai?",
        "options": ["Hộ", "Từ", "Chí Phèo", "Giáo Thứ"],
        "answer": "Hộ",
        "explanation": "Hộ là một nhà văn có khát vọng cao đẹp nhưng bị gánh nặng cơm áo ghì sát đất."
    },
    {
        "question": "Trong 'Vợ nhặt', chi tiết bát cháo cám thể hiện điều gì?",
        "options": ["Sự khốn cùng của người dân trong nạn đói", "Sự giàu có của bà cụ Tứ", "Món ăn yêu thích của Tràng",
                    "Sự lãng phí"],
        "answer": "Sự khốn cùng của người dân trong nạn đói",
        "explanation": "Bát cháo chát xít là biểu tượng cho sự sống mong manh giữa cái chết."
    },
    {
        "question": "Thành phần biệt lập trong câu có chức năng gì?",
        "options": ["Bày tỏ thái độ, cách đánh giá của người nói", "Làm chủ ngữ trong câu",
                    "Bổ sung ý nghĩa cho động từ chính", "Kết nối các đoạn văn"],
        "answer": "Bày tỏ thái độ, cách đánh giá của người nói",
        "explanation": "Thành phần biệt lập (như cảm thán, tình thái) không tham gia cấu trúc cú pháp chính."
    },
    {
        "question": "Câu thơ 'Mơ khách đường xa, khách đường xa' thuộc bài thơ nào?",
        "options": ["Đây thôn Vĩ Dạ", "Vội vàng", "Tràng giang", "Tây Tiến"],
        "answer": "Đây thôn Vĩ Dạ",
        "explanation": "Câu thơ thể hiện nỗi khắc khoải và khoảng cách vô hình của Hàn Mặc Tử."
    },
    {
        "question": "Phong cách ngôn ngữ nghệ thuật có chức năng gì?",
        "options": ["Chức năng thông tin và chức năng thẩm mỹ", "Chức năng chỉ đạo", "Chức năng giao tiếp hàng ngày",
                    "Chức năng chứng minh"],
        "answer": "Chức năng thông tin và chức năng thẩm mỹ",
        "explanation": "Vừa truyền đạt nội dung, vừa gợi cảm xúc và cái đẹp."
    },
    {
        "question": "Ai là tác giả của truyện ngắn 'Hai đứa trẻ'?",
        "options": ["Thạch Lam", "Nam Cao", "Nguyễn Tuân", "Tô Hoài"],
        "answer": "Thạch Lam",
        "explanation": "Thạch Lam nổi tiếng với những truyện không có cốt truyện, giàu chất thơ."
    },
    {
        "question": "Hình ảnh 'con tàu' trong bài 'Tiếng hát con tàu' là biểu tượng cho điều gì?",
        "options": ["Khát vọng lên đường, đi xa đến với nhân dân", "Một phương tiện giao thông thực tế",
                    "Sự chia ly đau khổ", "Sự giàu sang"],
        "answer": "Khát vọng lên đường, đi xa đến với nhân dân",
        "explanation": "Con tàu là biểu tượng tâm tưởng của nhà thơ."
    },
    {
        "question": "Mục đích của việc tóm tắt văn bản nghị luận là gì?",
        "options": ["Nắm bắt hệ thống luận điểm và ý chính", "Làm bài văn dài hơn", "Thay đổi ý kiến của tác giả",
                    "Biến bài văn thành bài thơ"],
        "answer": "Nắm bắt hệ thống luận điểm và ý chính",
        "explanation": "Giúp người đọc hiểu nhanh nội dung cốt lõi của lập luận."
    },
    {
        "question": "Nhà văn nào nổi tiếng với tập 'Vang bóng một thời'?",
        "options": ["Nguyễn Tuân", "Vũ Trọng Phụng", "Nam Cao", "Thạch Lam"],
        "answer": "Nguyễn Tuân",
        "explanation": "Tập truyện ngắn tôn vinh những vẻ đẹp văn hóa cổ truyền đã suy tàn."
    },
    {
        "question": "Câu thơ 'Đưa người, ta không đưa qua sông' nằm trong bài thơ nào?",
        "options": ["Tống biệt hành", "Tràng giang", "Tây Tiến", "Vội vàng"],
        "answer": "Tống biệt hành",
        "explanation": "Bài thơ của Thâm Tâm về sự chia ly của người chí sĩ."
    },
    {
        "question": "Trong kịch, 'Xung đột kịch' là gì?",
        "options": ["Sự mâu thuẫn giữa các lực lượng, nhân vật", "Hành động đánh nhau trên sân khấu",
                    "Việc các nhân vật nói nhiều", "Sự thay đổi cảnh trí"],
        "answer": "Sự mâu thuẫn giữa các lực lượng, nhân vật",
        "explanation": "Xung đột kịch là linh hồn của tác phẩm sân khấu."
    },
    {
        "question": "Hàm ý trong câu văn là gì?",
        "options": ["Phần thông tin không nói ra trực tiếp nhưng có thể suy ra", "Nghĩa đen của từ ngữ",
                    "Lỗi sai về ngữ pháp", "Cách phát âm của từ"],
        "answer": "Phần thông tin không nói ra trực tiếp nhưng có thể suy ra",
        "explanation": "Hàm ý giúp lời nói trở nên tinh tế, sâu sắc hơn."
    },
    {
        "question": "Bài thơ 'Thu điếu' (Nguyễn Khuyến) thuộc chùm thơ nào?",
        "options": ["Chùm thơ thu", "Chùm thơ quê hương", "Chùm thơ trào phúng", "Chùm thơ đi hát"],
        "answer": "Chùm thơ thu",
        "explanation": "Gồm 3 bài: Thu điếu, Thu vịnh, Thu ẩm."
    },
    {
        "question": "Dấu ngoặc kép trong văn bản thường được dùng để làm gì?",
        "options": ["Dẫn lời nói trực tiếp hoặc nhấn mạnh từ ngữ", "Ngắt câu dài", "Kết thúc đoạn văn",
                    "Giải thích cho từ đứng trước"],
        "answer": "Dẫn lời nói trực tiếp hoặc nhấn mạnh từ ngữ",
        "explanation": "Đây là công dụng phổ biến nhất của dấu ngoặc kép."
    },
    {
        "question": "Từ ngữ nào dùng để chỉ 'Sự tương đồng giữa hai đối tượng'?",
        "options": ["So sánh", "Ẩn dụ", "Hoán dụ", "Điệp từ"],
        "answer": "So sánh",
        "explanation": "So sánh là đối chiếu hai sự vật có nét tương đồng."
    },
    {
        "question": "Ai là người đã viết 'Tuyên ngôn Độc lập' của nước Việt Nam Dân chủ Cộng hòa?",
        "options": ["Hồ Chí Minh", "Phan Bội Châu", "Phan Châu Trinh", "Võ Nguyên Giáp"],
        "answer": "Hồ Chí Minh",
        "explanation": "Người đọc bản tuyên ngôn tại quảng trường Ba Đình ngày 2/9/1945."
    },
    {
        "question": "Trong 'Hai đứa trẻ', hai chị em Liên và An chờ đợi điều gì mỗi đêm?",
        "options": ["Chuyến tàu đêm đi ngang phố huyện", "Mẹ đi chợ về", "Bố đi làm xa về", "Ông tiên hiện lên"],
        "answer": "Chuyến tàu đêm đi ngang phố huyện",
        "explanation": "Con tàu mang đến ánh sáng và âm thanh rộn rã cho phố huyện nghèo."
    },
    {
        "question": "Nghĩa của từ 'Tự trọng' là gì?",
        "options": ["Coi trọng và giữ gìn phẩm giá của mình", "Tự đánh giá mình cao hơn người khác", "Sống độc lập",
                    "Không cần sự giúp đỡ"],
        "answer": "Coi trọng và giữ gìn phẩm giá của mình",
        "explanation": "Tự trọng là nền tảng đạo đức của con người."
    },
    {
        "question": "Bài thơ 'Sóng' của Xuân Quỳnh mang âm hưởng của thể loại nào?",
        "options": ["Hát ru và dân ca", "Hùng ca", "Kịch", "Ngụ ngôn"],
        "answer": "Hát ru và dân ca",
        "explanation": "Nhịp thơ 5 chữ đều đặn như sóng biển và hơi thở tình yêu nồng nàn."
    },
    {
        "question": "Phong cách ngôn ngữ khoa học có đặc điểm gì nổi bật?",
        "options": ["Tính logic, trừu tượng và khách quan", "Tính gợi hình, gợi cảm", "Tính thời sự",
                    "Tính truyền cảm mạnh"],
        "answer": "Tính logic, trừu tượng và khách quan",
        "explanation": "Khoa học đòi hỏi sự chính xác và lập luận chặt chẽ."
    },
    {
        "question": "Trong 'Cải ơi', vì sao ông Năm Nhỏ lại chọn nghề diễn kịch rong?",
        "options": ["Để hy vọng con gái nhìn thấy ông qua tivi hoặc sân khấu", "Vì ông thích hát",
                    "Vì ông không có nhà", "Vì ông muốn kiếm nhiều tiền"],
        "answer": "Để hy vọng con gái nhìn thấy ông qua tivi hoặc sân khấu",
        "explanation": "Một nỗ lực tìm con vô vọng nhưng đầy tình thương."
    },
    {
        "question": "Yếu tố chính cấu thành nên văn bản thuyết minh là gì?",
        "options": ["Tri thức khách quan và hữu ích", "Sự tưởng tượng bay bổng", "Cảm xúc mãnh liệt",
                    "Sự hư cấu nhân vật"],
        "answer": "Tri thức khách quan và hữu ích",
        "explanation": "Thuyết minh nhằm cung cấp kiến thức chính xác cho người đọc."
    },
    {
        "question": "Thơ 'Tự do' khác thơ 'Cổ điển' ở điểm nào nhất?",
        "options": ["Không bị gò bó bởi số câu, số chữ và vần điệu", "Không có vần", "Luôn ngắn hơn",
                    "Chỉ nói về cuộc sống hiện đại"],
        "answer": "Không bị gò bó bởi số câu, số chữ và vần điệu",
        "explanation": "Thơ tự do ưu tiên nhịp điệu cảm xúc hơn là quy tắc."
    },
    {
        "question": "Trong 'Chí Phèo', chi tiết con đường hoàn lương của Chí bị chặn đứng bởi ai?",
        "options": ["Bà cô Thị Nở và định kiến xã hội", "Bá Kiến", "Lý Cường", "Dân làng Vũ Đại"],
        "answer": "Bà cô Thị Nở và định kiến xã hội",
        "explanation": "Định kiến xã hội không cho Chí làm người lương thiện."
    },
    {
        "question": "Câu thơ 'Tôi muốn tắt nắng đi' nằm trong khổ thơ nào bài Vội vàng?",
        "options": ["Khổ 1", "Khổ 2", "Khổ 3", "Khổ cuối"],
        "answer": "Khổ 1",
        "explanation": "Mở đầu bài thơ thể hiện khát vọng đoạt quyền tạo hóa để giữ lại cái đẹp."
    },
    {
        "question": "Nhân vật Vũ Như Tô trong kịch của Nguyễn Huy Tưởng là một:",
        "options": ["Kiến trúc sư thiên tài", "Người nông dân", "Vị vua anh minh", "Người lính"],
        "answer": "Kiến trúc sư thiên tài",
        "explanation": "Vũ Như Tô là nghệ sĩ tài năng với khát vọng xây Cửu Trùng Đài."
    }
,
    {
        "question": "Vở kịch 'Vũ Như Tô' của Nguyễn Huy Tưởng thuộc thể loại nào?",
        "options": ["Bi kịch", "Hài kịch", "Kịch dân gian", "Kịch thơ"],
        "answer": "Bi kịch",
        "explanation": "Đây là vở bi kịch lịch sử nổi tiếng nhất của Nguyễn Huy Tưởng."
    },
    {
        "question": "Trong văn bản 'Cải ơi' (Nguyễn Ngọc Tư), nhân vật ông Năm Nhỏ đi tìm con tên là gì?",
        "options": ["Cải", "Thà", "Mận", "Đào"],
        "answer": "Cải",
        "explanation": "Ông Năm Nhỏ dành cả đời đi tìm đứa con gái riêng của vợ tên là Cải."
    },
    {
        "question": "Tác phẩm 'Tôi đã học tập như thế nào' là của tác giả nào?",
        "options": ["M. Gorki", "Lỗ Tấn", "Nam Cao", "Thạch Lam"],
        "answer": "M. Gorki",
        "explanation": "Đây là văn bản tự truyện tiêu biểu của nhà văn Nga Maxim Gorki."
    },
    {
        "question": "Bài thơ 'Tràng giang' của Huy Cận mang đậm phong cách nghệ thuật nào?",
        "options": ["Cổ điển và Hiện đại", "Hậu hiện đại", "Hiện thực nghiêm ngặt", "Siêu thực"],
        "answer": "Cổ điển và Hiện đại",
        "explanation": "Bài thơ kết hợp thi liệu cổ điển với cái tôi cô đơn của Thơ mới."
    },
    {
        "question": "Trong chương trình Ngữ văn 11 mới, thể thơ 'Sonnet' thường có bao nhiêu dòng?",
        "options": ["14 dòng", "10 dòng", "12 dòng", "16 dòng"],
        "answer": "14 dòng",
        "explanation": "Sonnet là thể thơ châu Âu truyền thống gồm 14 dòng."
    },
    {
        "question": "Văn bản 'Lời tiễn dặn' là truyện thơ của dân tộc nào?",
        "options": ["Dân tộc Thái", "Dân tộc Mường", "Dân tộc Tày", "Dân tộc H'Mông"],
        "answer": "Dân tộc Thái",
        "explanation": "'Xống chụ xon xao' (Lời tiễn dặn) là truyện thơ nổi tiếng của người Thái."
    },
    {
        "question": "Ai là tác giả của bài thơ 'Vội vàng'?",
        "options": ["Xuân Diệu", "Huy Cận", "Hàn Mặc Tử", "Chế Lan Viên"],
        "answer": "Xuân Diệu",
        "explanation": "Xuân Diệu được mệnh danh là nhà thơ mới nhất trong các nhà thơ mới."
    },
    {
        "question": "Khái niệm 'Chỉnh thể' trong tiếp nhận văn học nghĩa là gì?",
        "options": ["Tính toàn vẹn của tác phẩm", "Một phần của đoạn văn", "Cách ngắt nhịp thơ", "Tên một nhân vật"],
        "answer": "Tính toàn vẹn của tác phẩm",
        "explanation": "Chỉnh thể văn học là một đơn vị thống nhất giữa nội dung và hình thức."
    },
    {
        "question": "Trong 'Chữ người tử tù', Huấn Cao nổi tiếng với tài năng gì?",
        "options": ["Viết chữ đẹp", "Làm thơ", "Vẽ tranh", "Đánh đàn"],
        "answer": "Viết chữ đẹp",
        "explanation": "Tài viết chữ của Huấn Cao là biểu tượng cho cái Đẹp."
    },
    {
        "question": "Truyện ngắn 'Chí Phèo' lúc mới in có tên là gì?",
        "options": ["Cái lò gạch cũ", "Đôi lứa xứng đôi", "Chí Phèo", "Làng Vũ Đại ngày ấy"],
        "answer": "Cái lò gạch cũ",
        "explanation": "Nhan đề đầu tiên do nhà xuất bản đặt là 'Cái lò gạch cũ'."
    },
    {
        "question": "Bài thơ 'Đây thôn Vĩ Dạ' lấy cảm hứng từ vùng đất nào?",
        "options": ["Huế", "Hà Nội", "Đà Lạt", "Quảng Bình"],
        "answer": "Huế",
        "explanation": "Thôn Vĩ Dạ nằm bên bờ sông Hương, thuộc cố đô Huế."
    },
    {
        "question": "Phong cách ngôn ngữ nào được dùng trong các văn bản tin tức, báo chí?",
        "options": ["Phong cách ngôn ngữ báo chí", "Phong cách ngôn ngữ sinh hoạt", "Phong cách ngôn ngữ khoa học", "Phong cách ngôn ngữ nghệ thuật"],
        "answer": "Phong cách ngôn ngữ báo chí",
        "explanation": "Đây là phong cách dùng để thông tin về các sự kiện thời sự."
    },
    {
        "question": "Trong văn bản 'Vĩnh biệt Cửu Trùng Đài', nhân vật Đan Thiềm khuyên Vũ Như Tô làm gì khi quân phản loạn đến?",
        "options": ["Bỏ trốn", "Ở lại xây tiếp", "Tự tử", "Đi gặp vua"],
        "answer": "Bỏ trốn",
        "explanation": "Đan Thiềm tỉnh táo hơn Vũ Như Tô, bà khuyên ông lánh nạn để bảo toàn tài năng."
    },
    {
        "question": "Đặc điểm nổi bật của nhân vật trong Bi kịch là gì?",
        "options": ["Thường rơi vào mâu thuẫn không thể hóa giải", "Luôn có kết thúc hạnh phúc", "Là người nông dân hiền lành", "Luôn chiến thắng mọi kẻ thù"],
        "answer": "Thường rơi vào mâu thuẫn không thể hóa giải",
        "explanation": "Nhân vật bi kịch thường có khát vọng cao cả nhưng gặp phải rào cản thực tại khốc liệt."
    },
    {
        "question": "Tác phẩm 'Vợ nhặt' (Kim Lân) lấy bối cảnh thời gian nào?",
        "options": ["Nạn đói năm 1945", "Kháng chiến chống Pháp", "Kháng chiến chống Mỹ", "Thời bao cấp"],
        "answer": "Nạn đói năm 1945",
        "explanation": "Bối cảnh là nạn đói khủng khiếp năm Ất Tỵ."
    },
    {
        "question": "Trong bài thơ 'Tình ca' (Hoàng Trung Thông), tác giả ca ngợi điều gì?",
        "options": ["Tình yêu quê hương, đất nước", "Tình yêu đôi lứa", "Vẻ đẹp của thiên nhiên", "Cuộc sống thành thị"],
        "answer": "Tình yêu quê hương, đất nước",
        "explanation": "Bài thơ thể hiện tình cảm thiết tha với mảnh đất quê hương."
    },
    {
        "question": "Phép lặp là một biện pháp giúp văn bản có tính chất gì?",
        "options": ["Tính liên kết", "Tính hài hước", "Tính trừu tượng", "Tính đa nghĩa"],
        "answer": "Tính liên kết",
        "explanation": "Phép lặp giúp các câu văn kết nối chặt chẽ về mặt hình thức."
    },
    {
        "question": "Tác giả của tác phẩm 'Sống mòn' là ai?",
        "options": ["Nam Cao", "Vũ Trọng Phụng", "Nguyễn Tuân", "Tô Hoài"],
        "answer": "Nam Cao",
        "explanation": "Sống mòn là tiểu thuyết tiêu biểu về cuộc sống bế tắc của trí thức tiểu tư sản."
    },
    {
        "question": "Trong chương trình mới, văn bản nghị luận xã hội đòi hỏi điều gì nhất?",
        "options": ["Lý lẽ và bằng chứng thuyết phục", "Cốt truyện li kỳ", "Vần nhịp thơ ca", "Nhiều từ láy"],
        "answer": "Lý lẽ và bằng chứng thuyết phục",
        "explanation": "Nghị luận phải dựa trên các luận cứ thực tế để thuyết phục người đọc."
    },
    {
        "question": "Nghĩa của từ 'Thiên lương' trong 'Chữ người tử tù' là gì?",
        "options": ["Bản tính tốt lành do trời phú", "Sự giàu sang", "Tài năng viết chữ", "Quyền lực tối cao"],
        "answer": "Bản tính tốt lành do trời phú",
        "explanation": "Huấn Cao trọng cái 'thiên lương' của con người hơn là vàng ngọc."
    },
    {
        "question": "Dòng nào sau đây là đặc điểm của 'Cái tôi' trong Thơ mới?",
        "options": ["Khẳng định cá tính và cảm xúc cá nhân", "Luôn giấu mình sau cái 'ta' chung", "Chỉ viết về đề tài yêu nước", "Sử dụng ngôn ngữ cung đình"],
        "answer": "Khẳng định cá tính và cảm xúc cá nhân",
        "explanation": "Thơ mới là cuộc cách mạng giải phóng cái 'tôi' cá nhân."
    },
    {
        "question": "Bài thơ 'Tôi yêu em' của Pu-skin thuộc nền văn học nào?",
        "options": ["Văn học Nga", "Văn học Pháp", "Văn học Anh", "Văn học Đức"],
        "answer": "Văn học Nga",
        "explanation": "Pu-skin là 'Mặt trời của thi ca Nga'."
    },
    {
        "question": "Văn bản 'Tiếng hát con tàu' (Chế Lan Viên) nói về sự kiện gì?",
        "options": ["Cuộc vận động đi xây dựng kinh tế miền Bắc", "Cuộc kháng chiến chống Mỹ", "Sự ra đời của ngành đường sắt", "Chuyến du lịch Sa Pa"],
        "answer": "Cuộc vận động đi xây dựng kinh tế miền Bắc",
        "explanation": "Bài thơ kêu gọi thanh niên lên đường lên Tây Bắc xây dựng tổ quốc."
    },
    {
        "question": "Yếu tố nào quan trọng nhất trong một bản tin?",
        "options": ["Tính xác thực", "Tính hư cấu", "Sự bay bổng của ngôn từ", "Cảm xúc cá nhân"],
        "answer": "Tính xác thực",
        "explanation": "Bản tin phải cung cấp thông tin chính xác về sự kiện."
    },
    {
        "question": "Nhân vật chính trong truyện 'Đời thừa' là ai?",
        "options": ["Hộ", "Từ", "Chí Phèo", "Giáo Thứ"],
        "answer": "Hộ",
        "explanation": "Hộ là một nhà văn có khát vọng cao đẹp nhưng bị gánh nặng cơm áo ghì sát đất."
    },
    {
        "question": "Trong 'Vợ nhặt', chi tiết bát cháo cám thể hiện điều gì?",
        "options": ["Sự khốn cùng của người dân trong nạn đói", "Sự giàu có của bà cụ Tứ", "Món ăn yêu thích của Tràng", "Sự lãng phí"],
        "answer": "Sự khốn cùng của người dân trong nạn đói",
        "explanation": "Bát cháo chát xít là biểu tượng cho sự sống mong manh giữa cái chết."
    },
    {
        "question": "Thành phần biệt lập trong câu có chức năng gì?",
        "options": ["Bày tỏ thái độ, cách đánh giá của người nói", "Làm chủ ngữ trong câu", "Bổ sung ý nghĩa cho động từ chính", "Kết nối các đoạn văn"],
        "answer": "Bày tỏ thái độ, cách đánh giá của người nói",
        "explanation": "Thành phần biệt lập (như cảm thán, tình thái) không tham gia cấu trúc cú pháp chính."
    },
    {
        "question": "Câu thơ 'Mơ khách đường xa, khách đường xa' thuộc bài thơ nào?",
        "options": ["Đây thôn Vĩ Dạ", "Vội vàng", "Tràng giang", "Tây Tiến"],
        "answer": "Đây thôn Vĩ Dạ",
        "explanation": "Câu thơ thể hiện nỗi khắc khoải và khoảng cách vô hình của Hàn Mặc Tử."
    },
    {
        "question": "Phong cách ngôn ngữ nghệ thuật có chức năng gì?",
        "options": ["Chức năng thông tin và chức năng thẩm mỹ", "Chức năng chỉ đạo", "Chức năng giao tiếp hàng ngày", "Chức năng chứng minh"],
        "answer": "Chức năng thông tin và chức năng thẩm mỹ",
        "explanation": "Vừa truyền đạt nội dung, vừa gợi cảm xúc và cái đẹp."
    },
    {
        "question": "Ai là tác giả của truyện ngắn 'Hai đứa trẻ'?",
        "options": ["Thạch Lam", "Nam Cao", "Nguyễn Tuân", "Tô Hoài"],
        "answer": "Thạch Lam",
        "explanation": "Thạch Lam nổi tiếng với những truyện không có cốt truyện, giàu chất thơ."
    },
    {
        "question": "Hình ảnh 'con tàu' trong bài 'Tiếng hát con tàu' là biểu tượng cho điều gì?",
        "options": ["Khát vọng lên đường, đi xa đến với nhân dân", "Một phương tiện giao thông thực tế", "Sự chia ly đau khổ", "Sự giàu sang"],
        "answer": "Khát vọng lên đường, đi xa đến với nhân dân",
        "explanation": "Con tàu là biểu tượng tâm tưởng của nhà thơ."
    },
    {
        "question": "Mục đích của việc tóm tắt văn bản nghị luận là gì?",
        "options": ["Nắm bắt hệ thống luận điểm và ý chính", "Làm bài văn dài hơn", "Thay đổi ý kiến của tác giả", "Biến bài văn thành bài thơ"],
        "answer": "Nắm bắt hệ thống luận điểm và ý chính",
        "explanation": "Giúp người đọc hiểu nhanh nội dung cốt lõi của lập luận."
    },
    {
        "question": "Nhà văn nào nổi tiếng với tập 'Vang bóng một thời'?",
        "options": ["Nguyễn Tuân", "Vũ Trọng Phụng", "Nam Cao", "Thạch Lam"],
        "answer": "Nguyễn Tuân",
        "explanation": "Tập truyện ngắn tôn vinh những vẻ đẹp văn hóa cổ truyền đã suy tàn."
    },
    {
        "question": "Câu thơ 'Đưa người, ta không đưa qua sông' nằm trong bài thơ nào?",
        "options": ["Tống biệt hành", "Tràng giang", "Tây Tiến", "Vội vàng"],
        "answer": "Tống biệt hành",
        "explanation": "Bài thơ của Thâm Tâm về sự chia ly của người chí sĩ."
    },
    {
        "question": "Trong kịch, 'Xung đột kịch' là gì?",
        "options": ["Sự mâu thuẫn giữa các lực lượng, nhân vật", "Hành động đánh nhau trên sân khấu", "Việc các nhân vật nói nhiều", "Sự thay đổi cảnh trí"],
        "answer": "Sự mâu thuẫn giữa các lực lượng, nhân vật",
        "explanation": "Xung đột kịch là linh hồn của tác phẩm sân khấu."
    },
    {
        "question": "Hàm ý trong câu văn là gì?",
        "options": ["Phần thông tin không nói ra trực tiếp nhưng có thể suy ra", "Nghĩa đen của từ ngữ", "Lỗi sai về ngữ pháp", "Cách phát âm của từ"],
        "answer": "Phần thông tin không nói ra trực tiếp nhưng có thể suy ra",
        "explanation": "Hàm ý giúp lời nói trở nên tinh tế, sâu sắc hơn."
    },
    {
        "question": "Bài thơ 'Thu điếu' (Nguyễn Khuyến) thuộc chùm thơ nào?",
        "options": ["Chùm thơ thu", "Chùm thơ quê hương", "Chùm thơ trào phúng", "Chùm thơ đi hát"],
        "answer": "Chùm thơ thu",
        "explanation": "Gồm 3 bài: Thu điếu, Thu vịnh, Thu ẩm."
    },
    {
        "question": "Dấu ngoặc kép trong văn bản thường được dùng để làm gì?",
        "options": ["Dẫn lời nói trực tiếp hoặc nhấn mạnh từ ngữ", "Ngắt câu dài", "Kết thúc đoạn văn", "Giải thích cho từ đứng trước"],
        "answer": "Dẫn lời nói trực tiếp hoặc nhấn mạnh từ ngữ",
        "explanation": "Đây là công dụng phổ biến nhất của dấu ngoặc kép."
    },
    {
        "question": "Từ ngữ nào dùng để chỉ 'Sự tương đồng giữa hai đối tượng'?",
        "options": ["So sánh", "Ẩn dụ", "Hoán dụ", "Điệp từ"],
        "answer": "So sánh",
        "explanation": "So sánh là đối chiếu hai sự vật có nét tương đồng."
    },
    {
        "question": "Ai là người đã viết 'Tuyên ngôn Độc lập' của nước Việt Nam Dân chủ Cộng hòa?",
        "options": ["Hồ Chí Minh", "Phan Bội Châu", "Phan Châu Trinh", "Võ Nguyên Giáp"],
        "answer": "Hồ Chí Minh",
        "explanation": "Người đọc bản tuyên ngôn tại quảng trường Ba Đình ngày 2/9/1945."
    },
    {
        "question": "Trong 'Hai đứa trẻ', hai chị em Liên và An chờ đợi điều gì mỗi đêm?",
        "options": ["Chuyến tàu đêm đi ngang phố huyện", "Mẹ đi chợ về", "Bố đi làm xa về", "Ông tiên hiện lên"],
        "answer": "Chuyến tàu đêm đi ngang phố huyện",
        "explanation": "Con tàu mang đến ánh sáng và âm thanh rộn rã cho phố huyện nghèo."
    },
    {
        "question": "Nghĩa của từ 'Tự trọng' là gì?",
        "options": ["Coi trọng và giữ gìn phẩm giá của mình", "Tự đánh giá mình cao hơn người khác", "Sống độc lập", "Không cần sự giúp đỡ"],
        "answer": "Coi trọng và giữ gìn phẩm giá của mình",
        "explanation": "Tự trọng là nền tảng đạo đức của con người."
    },
    {
        "question": "Bài thơ 'Sóng' của Xuân Quỳnh mang âm hưởng của thể loại nào?",
        "options": ["Hát ru và dân ca", "Hùng ca", "Kịch", "Ngụ ngôn"],
        "answer": "Hát ru và dân ca",
        "explanation": "Nhịp thơ 5 chữ đều đặn như sóng biển và hơi thở tình yêu nồng nàn."
    },
    {
        "question": "Phong cách ngôn ngữ khoa học có đặc điểm gì nổi bật?",
        "options": ["Tính logic, trừu tượng và khách quan", "Tính gợi hình, gợi cảm", "Tính thời sự", "Tính truyền cảm mạnh"],
        "answer": "Tính logic, trừu tượng và khách quan",
        "explanation": "Khoa học đòi hỏi sự chính xác và lập luận chặt chẽ."
    },
    {
        "question": "Trong 'Cải ơi', vì sao ông Năm Nhỏ lại chọn nghề diễn kịch rong?",
        "options": ["Để hy vọng con gái nhìn thấy ông qua tivi hoặc sân khấu", "Vì ông thích hát", "Vì ông không có nhà", "Vì ông muốn kiếm nhiều tiền"],
        "answer": "Để hy vọng con gái nhìn thấy ông qua tivi hoặc sân khấu",
        "explanation": "Một nỗ lực tìm con vô vọng nhưng đầy tình thương."
    },
    {
        "question": "Yếu tố chính cấu thành nên văn bản thuyết minh là gì?",
        "options": ["Tri thức khách quan và hữu ích", "Sự tưởng tượng bay bổng", "Cảm xúc mãnh liệt", "Sự hư cấu nhân vật"],
        "answer": "Tri thức khách quan và hữu ích",
        "explanation": "Thuyết minh nhằm cung cấp kiến thức chính xác cho người đọc."
    },
    {
        "question": "Thơ 'Tự do' khác thơ 'Cổ điển' ở điểm nào nhất?",
        "options": ["Không bị gò bó bởi số câu, số chữ và vần điệu", "Không có vần", "Luôn ngắn hơn", "Chỉ nói về cuộc sống hiện đại"],
        "answer": "Không bị gò bó bởi số câu, số chữ và vần điệu",
        "explanation": "Thơ tự do ưu tiên nhịp điệu cảm xúc hơn là quy tắc."
    },
    {
        "question": "Trong 'Chí Phèo', chi tiết con đường hoàn lương của Chí bị chặn đứng bởi ai?",
        "options": ["Bà cô Thị Nở và định kiến xã hội", "Bá Kiến", "Lý Cường", "Dân làng Vũ Đại"],
        "answer": "Bà cô Thị Nở và định kiến xã hội",
        "explanation": "Định kiến xã hội không cho Chí làm người lương thiện."
    },
    {
        "question": "Câu thơ 'Tôi muốn tắt nắng đi' nằm trong khổ thơ nào bài Vội vàng?",
        "options": ["Khổ 1", "Khổ 2", "Khổ 3", "Khổ cuối"],
        "answer": "Khổ 1",
        "explanation": "Mở đầu bài thơ thể hiện khát vọng đoạt quyền tạo hóa để giữ lại cái đẹp."
    },
    {
        "question": "Nhân vật Vũ Như Tô trong kịch của Nguyễn Huy Tưởng là một:",
        "options": ["Kiến trúc sư thiên tài", "Người nông dân", "Vị vua anh minh", "Người lính"],
        "answer": "Kiến trúc sư thiên tài",
        "explanation": "Vũ Như Tô là nghệ sĩ tài năng với khát vọng xây Cửu Trùng Đài."
    }
# ============================================================
# banks/van_l11_moi_kho.py — 50 Câu KHÓ (Vận dụng cao)
# ============================================================
,
    {
        "question": "Xung đột kịch trong 'Vĩnh biệt Cửu Trùng Đài' được đẩy lên cao trào dựa trên mâu thuẫn cốt lõi nào?",
        "options": [
            "Mâu thuẫn giữa khát vọng nghệ thuật thuần túy muôn đời và lợi ích thiết thân của nhân dân",
            "Mâu thuẫn giữa lòng trung thành với nhà vua và tình yêu quê hương",
            "Mâu thuẫn giữa tài năng hội họa và tài năng kiến trúc của Vũ Như Tô",
            "Mâu thuẫn giữa Đan Thiềm và quân phiến loạn"
        ],
        "answer": "Mâu thuẫn giữa khát vọng nghệ thuật thuần túy muôn đời và lợi ích thiết thân của nhân dân",
        "explanation": "Đây là bi kịch mang tính nhân loại: Nghệ thuật vị nghệ thuật hay Nghệ thuật vị nhân sinh."
    },
    {
        "question": "Tính chất 'tượng trưng' trong bài thơ 'Đây thôn Vĩ Dạ' thể hiện rõ nhất qua chi tiết nào?",
        "options": [
            "Hình ảnh chiếc thuyền đậu bến sông trăng",
            "Hình ảnh nắng hàng cau",
            "Hình ảnh lá trúc che ngang",
            "Hình ảnh khách đường xa"
        ],
        "answer": "Hình ảnh chiếc thuyền đậu bến sông trăng",
        "explanation": "Sông trăng và thuyền chở trăng là những thi liệu mang tính tượng trưng cao, gợi sự huyền ảo và nỗi cô đơn tuyệt vọng."
    },
    {
        "question": "Trong văn bản 'Tôi đã học tập như thế nào', hành động đọc sách của Gorki mang ý nghĩa biểu tượng gì?",
        "options": [
            "Sự phản kháng lại hiện thực tăm tối và nỗ lực tự giải phóng con người",
            "Sự tìm kiếm sự giàu có về vật chất",
            "Sự tuân thủ các quy tắc giáo dục của giáo hội",
            "Sự bắt chước lối sống thượng lưu"
        ],
        "answer": "Sự phản kháng lại hiện thực tăm tối và nỗ lực tự giải phóng con người",
        "explanation": "Sách không chỉ là kiến thức mà là cứu cánh để ông thoát khỏi kiếp sống 'dưới đáy'."
    },
    {
        "question": "Đặc điểm của cái 'Tôi' trong bài thơ 'Vội vàng' (Xuân Diệu) có gì khác biệt với cái tôi của thơ trung đại?",
        "options": [
            "Là cái tôi cá nhân ham sống, khát khao tận hưởng giá trị trần thế thay vì hướng về tiên giới hay quá khứ",
            "Là cái tôi ẩn dật, xa lánh bụi trần",
            "Là cái tôi chỉ biết tuân theo mệnh trời (Thiên mệnh)",
            "Là cái tôi hòa tan vào cái ta chung của cộng đồng"
        ],
        "answer": "Là cái tôi cá nhân ham sống, khát khao tận hưởng giá trị trần thế thay vì hướng về tiên giới hay quá khứ",
        "explanation": "Xuân Diệu khẳng định con người là chuẩn mực của vũ trụ, đề cao sự sống ngay hiện tại."
    },
    {
        "question": "Bản chất của tiếng cười trong các tác phẩm trào phúng của Vũ Trọng Phụng là gì?",
        "options": [
            "Tiếng cười xót xa, đau đớn trước sự băng hoại đạo đức của xã hội thượng lưu 'rởm'",
            "Tiếng cười sảng khoái, vô tư",
            "Tiếng cười mang tính giáo dục nhẹ nhàng",
            "Tiếng cười ngợi ca cuộc sống mới"
        ],
        "answer": "Tiếng cười xót xa, đau đớn trước sự băng hoại đạo đức của xã hội thượng lưu 'rởm'",
        "explanation": "Đó là tiếng cười phủ định thực tại đen tối, giả dối của xã hội đương thời."
    },
    {
        "question": "Tại sao nói 'Chí Phèo' là một tác phẩm có kết cấu 'vòng tròn'?",
        "options": [
            "Vì kết thúc truyện bằng hình ảnh cái lò gạch cũ bỏ hoang, gợi lại sự lặp lại của số phận",
            "Vì Chí Phèo chết đúng tại nơi hắn sinh ra",
            "Vì Bá Kiến và Chí Phèo đều cùng chết",
            "Vì câu chuyện bắt đầu và kết thúc đều vào buổi sáng"
        ],
        "answer": "Vì kết thúc truyện bằng hình ảnh cái lò gạch cũ bỏ hoang, gợi lại sự lặp lại của số phận",
        "explanation": "Hình ảnh 'cái lò gạch cũ' ở cuối truyện gợi ra sự bế tắc: sẽ lại có những 'Chí Phèo con' ra đời."
    },
    {
        "question": "Trong bi kịch 'Hamlet', câu thoại 'To be or not to be' (Tồn tại hay không tồn tại) thể hiện trạng thái gì của nhân vật?",
        "options": [
            "Sự giằng xé giữa hành động trả thù và sự cam chịu, suy ngẫm về ý nghĩa sự sống",
            "Sự quyết tâm giết chết nhà vua ngay lập tức",
            "Nỗi sợ hãi trước cái chết",
            "Sự hối hận vì đã yêu Ophelia"
        ],
        "answer": "Sự giằng xé giữa hành động trả thù và sự cam chịu, suy ngẫm về ý nghĩa sự sống",
        "explanation": "Đây là đỉnh cao của sự tự vấn về sự tồn tại và trách nhiệm của con người trước cái ác."
    },
    {
        "question": "Nét độc đáo trong thi pháp của truyện ngắn Thạch Lam là gì?",
        "options": [
            "Truyện không có cốt truyện gay cấn, chủ yếu khai thác thế giới nội tâm và cảm giác",
            "Xây dựng những tình huống trinh thám phức tạp",
            "Sử dụng nhiều từ ngữ địa phương thô mộc",
            "Tập trung vào các cuộc đấu tranh giai cấp quyết liệt"
        ],
        "answer": "Truyện không có cốt truyện gay cấn, chủ yếu khai thác thế giới nội tâm và cảm giác",
        "explanation": "Văn Thạch Lam tinh tế, đi sâu vào những biến chuyển mong manh của cảm xúc."
    },
    {
        "question": "Sự kết hợp giữa 'Thực' và 'Mộng' trong thơ Hàn Mặc Tử mang lại hiệu quả gì?",
        "options": [
            "Tạo nên một thế giới nghệ thuật huyền ảo, đau đớn nhưng đầy khao khát sống",
            "Làm cho bài thơ trở nên khó hiểu đối với người đọc",
            "Thể hiện sự mất trí nhớ của tác giả",
            "Chỉ là sự trang trí cho câu chữ"
        ],
        "answer": "Tạo nên một thế giới nghệ thuật huyền ảo, đau đớn nhưng đầy khao khát sống",
        "explanation": "Càng đau đớn về thể xác, hồn thơ Hàn Mặc Tử càng bay bổng vào thế giới siêu thực để tìm sự sống."
    },
    {
        "question": "Trong văn nghị luận xã hội, việc sử dụng 'Phản đề' có tác dụng gì?",
        "options": [
            "Giúp cái nhìn về vấn đề trở nên đa chiều, khách quan và sâu sắc hơn",
            "Làm cho người đọc bị bối rối",
            "Chứng tỏ người viết không có lập trường vững vàng",
            "Để bài viết dài hơn cho đủ dung lượng"
        ],
        "answer": "Giúp cái nhìn về vấn đề trở nên đa chiều, khách quan và sâu sắc hơn",
        "explanation": "Phản đề giúp bao quát các khía cạnh ngược lại của vấn đề, từ đó khẳng định luận điểm chính vững chắc hơn."
    },
    # ... (Tiếp tục soạn tương tự cho đủ 50 câu)
    {
        "question": "Tư tưởng nghệ thuật của Nguyễn Tuân sau Cách mạng có sự chuyển dịch như thế nào?",
        "options": [
            "Từ việc tìm kiếm vẻ đẹp ở những cá nhân 'ngông' sang vẻ đẹp của quần chúng lao động và sự hùng vĩ của đất nước",
            "Từ việc viết truyện ngắn sang chỉ viết tiểu thuyết",
            "Từ cảm hứng lãng mạn sang cảm hứng phê phán gay gắt",
            "Ông không còn quan tâm đến cái Đẹp nữa"
        ],
        "answer": "Từ việc tìm kiếm vẻ đẹp ở những cá nhân 'ngông' sang vẻ đẹp của quần chúng lao động và sự hùng vĩ của đất nước",
        "explanation": "Cái Đẹp của Nguyễn Tuân sau 1945 gắn liền với nhân dân và cuộc sống xây dựng CNXH."
    },
    {
        "question": "Tại sao trong bài 'Tràng giang', Huy Cận lại dùng hình ảnh 'Củi một cành khô lạc mấy dòng' thay vì hình ảnh con thuyền?",
        "options": [
            "Để nhấn mạnh thân phận nhỏ bé, trôi dạt và vô định của kiếp người giữa dòng đời",
            "Vì ông không thích hình ảnh con thuyền",
            "Để tạo ra sự khác biệt với thơ Đường",
            "Vì 'củi' gợi cảm giác ấm áp hơn"
        ],
        "answer": "Để nhấn mạnh thân phận nhỏ bé, trôi dạt và vô định của kiếp người giữa dòng đời",
        "explanation": "Một cành củi khô là sự vật tầm thường, gợi sự rẻ rúng, cô độc hơn hẳn con thuyền."
    }

]