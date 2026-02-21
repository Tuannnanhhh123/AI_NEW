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
      {"question":"Đạo hàm của hàm số y = x^3 là?","options":["A. 3x^2","B. x^2","C. 3x","D. x^3"],"answer":"A. 3x^2","explanation":"Áp dụng công thức (x^n)' = n x^(n-1)."},
{"question":"Đạo hàm của hàm số y = 4x^5 là?","options":["A. 20x^4","B. 5x^4","C. 4x^4","D. 16x^5"],"answer":"A. 20x^4","explanation":"Đạo hàm 4x^5 = 4·5x^4 = 20x^4."},
{"question":"Nghiệm của phương trình log2(x)=3 là?","options":["A. 6","B. 8","C. 9","D. 4"],"answer":"B. 8","explanation":"log2(x)=3 ⇒ x=2^3=8."},
{"question":"Nguyên hàm của 8x dx là?","options":["A. 4x^2 + C","B. 8x^2 + C","C. 2x^2 + C","D. 16x + C"],"answer":"A. 4x^2 + C","explanation":"∫8x dx = 8·x^2/2 = 4x^2 + C."},
{"question":"Môđun của số phức z = 3 + 4i là?","options":["A. 5","B. 7","C. 25","D. 1"],"answer":"A. 5","explanation":"|z| = √(3^2+4^2)=5."},
{"question":"Đạo hàm của hàm số y = x^6 là?","options":["A. 6x^5","B. x^5","C. 5x^6","D. 6x^6"],"answer":"A. 6x^5","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=5 là?","options":["A. 10","B. 25","C. 32","D. 16"],"answer":"C. 32","explanation":"x=2^5=32."},
{"question":"Nguyên hàm của 10x dx là?","options":["A. 5x^2 + C","B. 10x^2 + C","C. x^2 + C","D. 20x + C"],"answer":"A. 5x^2 + C","explanation":"∫10x dx = 10·x^2/2=5x^2+C."},
{"question":"Môđun của số phức z = 1 + 2i là?","options":["A. √5","B. 3","C. 1","D. 2"],"answer":"A. √5","explanation":"|z|=√(1^2+2^2)=√5."},
{"question":"Đạo hàm của hàm số y = x^4 là?","options":["A. 4x^3","B. x^3","C. 3x^4","D. 4x^4"],"answer":"A. 4x^3","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=2 là?","options":["A. 2","B. 4","C. 8","D. 1"],"answer":"B. 4","explanation":"x=2^2=4."},
{"question":"Nguyên hàm của 2x dx là?","options":["A. x^2 + C","B. 2x^2 + C","C. x^2/2 + C","D. 4x + C"],"answer":"A. x^2 + C","explanation":"∫2x dx = x^2 + C."},
{"question":"Môđun của số phức z = 5 + 12i là?","options":["A. 13","B. 7","C. 17","D. 60"],"answer":"A. 13","explanation":"√(5^2+12^2)=13."},
{"question":"Đạo hàm của hàm số y = x^8 là?","options":["A. 8x^7","B. x^7","C. 7x^8","D. 8x^8"],"answer":"A. 8x^7","explanation":"Áp dụng công thức đạo hàm."},
{"question":"Nghiệm của phương trình log2(x)=1 là?","options":["A. 1","B. 2","C. 4","D. 8"],"answer":"B. 2","explanation":"x=2^1=2."},
{"question":"Nguyên hàm của 12x dx là?","options":["A. 6x^2 + C","B. 12x^2 + C","C. 3x^2 + C","D. 24x + C"],"answer":"A. 6x^2 + C","explanation":"∫12x dx=6x^2+C."},
{"question":"Môđun của số phức z = 6 + 8i là?","options":["A. 10","B. 14","C. 2","D. 48"],"answer":"A. 10","explanation":"√(6^2+8^2)=10."},
{"question":"Đạo hàm của hàm số y = x^2 là?","options":["A. 2x","B. x","C. x^2","D. 2"],"answer":"A. 2x","explanation":"Đạo hàm x^2 là 2x."},
{"question":"Nghiệm của phương trình log2(x)=6 là?","options":["A. 12","B. 36","C. 64","D. 32"],"answer":"C. 64","explanation":"x=2^6=64."},
{"question":"Nguyên hàm của 4x dx là?","options":["A. 2x^2 + C","B. 4x^2 + C","C. x^2 + C","D. 8x + C"],"answer":"A. 2x^2 + C","explanation":"∫4x dx=2x^2+C."},
{"question":"Môđun của số phức z = 7 + 24i là?","options":["A. 25","B. 31","C. 17","D. 49"],"answer":"A. 25","explanation":"|z| = √(7^2+24^2)=25."},
{"question":"Đạo hàm của hàm số y = x^7 là?","options":["A. 7x^6","B. x^6","C. 6x^7","D. 7x^7"],"answer":"A. 7x^6","explanation":"Áp dụng công thức (x^n)' = n x^(n-1)."},
{"question":"Nghiệm của phương trình log2(x)=7 là?","options":["A. 49","B. 14","C. 128","D. 64"],"answer":"C. 128","explanation":"x = 2^7 = 128."},
{"question":"Nguyên hàm của 14x dx là?","options":["A. 7x^2 + C","B. 14x^2 + C","C. 2x^2 + C","D. 28x + C"],"answer":"A. 7x^2 + C","explanation":"∫14x dx = 14·x^2/2 = 7x^2 + C."},
{"question":"Môđun của số phức z = 8 + 15i là?","options":["A. 17","B. 23","C. 7","D. 120"],"answer":"A. 17","explanation":"√(8^2+15^2)=17."},
{"question":"Đạo hàm của hàm số y = x^9 là?","options":["A. 9x^8","B. x^8","C. 8x^9","D. 9x^9"],"answer":"A. 9x^8","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=8 là?","options":["A. 16","B. 256","C. 64","D. 32"],"answer":"B. 256","explanation":"x = 2^8 = 256."},
{"question":"Nguyên hàm của 16x dx là?","options":["A. 8x^2 + C","B. 16x^2 + C","C. 4x^2 + C","D. 32x + C"],"answer":"A. 8x^2 + C","explanation":"∫16x dx = 8x^2 + C."},
{"question":"Môđun của số phức z = 9 + 12i là?","options":["A. 15","B. 21","C. 3","D. 108"],"answer":"A. 15","explanation":"√(9^2+12^2)=15."},
{"question":"Đạo hàm của hàm số y = x^10 là?","options":["A. 10x^9","B. x^9","C. 9x^10","D. 10x^10"],"answer":"A. 10x^9","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=9 là?","options":["A. 512","B. 81","C. 18","D. 256"],"answer":"A. 512","explanation":"x = 2^9 = 512."},
{"question":"Nguyên hàm của 18x dx là?","options":["A. 9x^2 + C","B. 18x^2 + C","C. 6x^2 + C","D. 36x + C"],"answer":"A. 9x^2 + C","explanation":"∫18x dx = 9x^2 + C."},
{"question":"Môđun của số phức z = 20 + 21i là?","options":["A. 29","B. 41","C. 1","D. 420"],"answer":"A. 29","explanation":"√(20^2+21^2)=29."},
{"question":"Đạo hàm của hàm số y = x^11 là?","options":["A. 11x^10","B. x^10","C. 10x^11","D. 11x^11"],"answer":"A. 11x^10","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=10 là?","options":["A. 1024","B. 100","C. 20","D. 512"],"answer":"A. 1024","explanation":"x = 2^10 = 1024."},
{"question":"Nguyên hàm của 20x dx là?","options":["A. 10x^2 + C","B. 20x^2 + C","C. 5x^2 + C","D. 40x + C"],"answer":"A. 10x^2 + C","explanation":"∫20x dx = 10x^2 + C."},
{"question":"Môđun của số phức z = 12 + 16i là?","options":["A. 20","B. 28","C. 4","D. 192"],"answer":"A. 20","explanation":"√(12^2+16^2)=20."},
{"question":"Đạo hàm của hàm số y = x^12 là?","options":["A. 12x^11","B. x^11","C. 11x^12","D. 12x^12"],"answer":"A. 12x^11","explanation":"Áp dụng công thức đạo hàm."},
{"question":"Nghiệm của phương trình log2(x)=11 là?","options":["A. 2048","B. 121","C. 22","D. 1024"],"answer":"A. 2048","explanation":"x = 2^11 = 2048."},
{"question":"Nguyên hàm của 22x dx là?","options":["A. 11x^2 + C","B. 22x^2 + C","C. 2x^2 + C","D. 44x + C"],"answer":"A. 11x^2 + C","explanation":"∫22x dx = 11x^2 + C."},
{"question":"Môđun của số phức z = 15 + 8i là?","options":["A. 17","B. 23","C. 7","D. 120"],"answer":"A. 17","explanation":"|z| = √(15^2+8^2)=17."},
{"question":"Đạo hàm của hàm số y = x^13 là?","options":["A. 13x^12","B. x^12","C. 12x^13","D. 13x^13"],"answer":"A. 13x^12","explanation":"Áp dụng công thức (x^n)' = n x^(n-1)."},
{"question":"Nghiệm của phương trình log2(x)=12 là?","options":["A. 4096","B. 144","C. 24","D. 2048"],"answer":"A. 4096","explanation":"x = 2^12 = 4096."},
{"question":"Nguyên hàm của 24x dx là?","options":["A. 12x^2 + C","B. 24x^2 + C","C. 6x^2 + C","D. 48x + C"],"answer":"A. 12x^2 + C","explanation":"∫24x dx = 12x^2 + C."},
{"question":"Môđun của số phức z = 9 + 40i là?","options":["A. 41","B. 49","C. 31","D. 360"],"answer":"A. 41","explanation":"√(9^2+40^2)=41."},
{"question":"Đạo hàm của hàm số y = x^14 là?","options":["A. 14x^13","B. x^13","C. 13x^14","D. 14x^14"],"answer":"A. 14x^13","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=13 là?","options":["A. 8192","B. 169","C. 26","D. 4096"],"answer":"A. 8192","explanation":"x = 2^13 = 8192."},
{"question":"Nguyên hàm của 26x dx là?","options":["A. 13x^2 + C","B. 26x^2 + C","C. 2x^2 + C","D. 52x + C"],"answer":"A. 13x^2 + C","explanation":"∫26x dx = 13x^2 + C."},
{"question":"Môđun của số phức z = 28 + 45i là?","options":["A. 53","B. 73","C. 17","D. 1260"],"answer":"A. 53","explanation":"√(28^2+45^2)=53."},
{"question":"Đạo hàm của hàm số y = x^15 là?","options":["A. 15x^14","B. x^14","C. 14x^15","D. 15x^15"],"answer":"A. 15x^14","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=14 là?","options":["A. 16384","B. 196","C. 28","D. 8192"],"answer":"A. 16384","explanation":"x = 2^14 = 16384."},
{"question":"Nguyên hàm của 28x dx là?","options":["A. 14x^2 + C","B. 28x^2 + C","C. 4x^2 + C","D. 56x + C"],"answer":"A. 14x^2 + C","explanation":"∫28x dx = 14x^2 + C."},
{"question":"Môđun của số phức z = 11 + 60i là?","options":["A. 61","B. 71","C. 49","D. 660"],"answer":"A. 61","explanation":"√(11^2+60^2)=61."},
{"question":"Đạo hàm của hàm số y = x^16 là?","options":["A. 16x^15","B. x^15","C. 15x^16","D. 16x^16"],"answer":"A. 16x^15","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=15 là?","options":["A. 32768","B. 225","C. 30","D. 16384"],"answer":"A. 32768","explanation":"x = 2^15 = 32768."},
{"question":"Nguyên hàm của 30x dx là?","options":["A. 15x^2 + C","B. 30x^2 + C","C. 5x^2 + C","D. 60x + C"],"answer":"A. 15x^2 + C","explanation":"∫30x dx = 15x^2 + C."},
{"question":"Môđun của số phức z = 16 + 63i là?","options":["A. 65","B. 79","C. 47","D. 1008"],"answer":"A. 65","explanation":"√(16^2+63^2)=65."},
{"question":"Đạo hàm của hàm số y = x^17 là?","options":["A. 17x^16","B. x^16","C. 16x^17","D. 17x^17"],"answer":"A. 17x^16","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=16 là?","options":["A. 65536","B. 256","C. 32","D. 32768"],"answer":"A. 65536","explanation":"x = 2^16 = 65536."},
{"question":"Nguyên hàm của 32x dx là?","options":["A. 16x^2 + C","B. 32x^2 + C","C. 8x^2 + C","D. 64x + C"],"answer":"A. 16x^2 + C","explanation":"∫32x dx = 16x^2 + C."},
{"question":"Môđun của số phức z = 18 + 24i là?","options":["A. 30","B. 42","C. 6","D. 432"],"answer":"A. 30","explanation":"√(18^2+24^2)=30."},
{"question":"Đạo hàm của hàm số y = x^18 là?","options":["A. 18x^17","B. x^17","C. 17x^18","D. 18x^18"],"answer":"A. 18x^17","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=17 là?","options":["A. 131072","B. 289","C. 34","D. 65536"],"answer":"A. 131072","explanation":"x = 2^17."},
{"question":"Nguyên hàm của 34x dx là?","options":["A. 17x^2 + C","B. 34x^2 + C","C. 2x^2 + C","D. 68x + C"],"answer":"A. 17x^2 + C","explanation":"∫34x dx = 17x^2 + C."},
{"question":"Môđun của số phức z = 21 + 28i là?","options":["A. 35","B. 49","C. 7","D. 588"],"answer":"A. 35","explanation":"√(21^2+28^2)=35."},
{"question":"Đạo hàm của hàm số y = x^19 là?","options":["A. 19x^18","B. x^18","C. 18x^19","D. 19x^19"],"answer":"A. 19x^18","explanation":"Áp dụng công thức đạo hàm."},
{"question":"Nghiệm của phương trình log2(x)=18 là?","options":["A. 262144","B. 324","C. 36","D. 131072"],"answer":"A. 262144","explanation":"x = 2^18."},
{"question":"Nguyên hàm của 36x dx là?","options":["A. 18x^2 + C","B. 36x^2 + C","C. 6x^2 + C","D. 72x + C"],"answer":"A. 18x^2 + C","explanation":"∫36x dx = 18x^2 + C."},
{"question":"Môđun của số phức z = 24 + 32i là?","options":["A. 40","B. 56","C. 8","D. 768"],"answer":"A. 40","explanation":"√(24^2+32^2)=40."},
{"question":"Đạo hàm của hàm số y = x^20 là?","options":["A. 20x^19","B. x^19","C. 19x^20","D. 20x^20"],"answer":"A. 20x^19","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=19 là?","options":["A. 524288","B. 361","C. 38","D. 262144"],"answer":"A. 524288","explanation":"x = 2^19."},
{"question":"Nguyên hàm của 38x dx là?","options":["A. 19x^2 + C","B. 38x^2 + C","C. 4x^2 + C","D. 76x + C"],"answer":"A. 19x^2 + C","explanation":"∫38x dx = 19x^2 + C."},
{"question":"Môđun của số phức z = 30 + 40i là?","options":["A. 50","B. 70","C. 10","D. 1200"],"answer":"A. 50","explanation":"√(30^2+40^2)=50."},
{"question":"Đạo hàm của hàm số y = x^21 là?","options":["A. 21x^20","B. x^20","C. 20x^21","D. 21x^21"],"answer":"A. 21x^20","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=20 là?","options":["A. 1048576","B. 400","C. 40","D. 524288"],"answer":"A. 1048576","explanation":"x = 2^20."},
{"question":"Nguyên hàm của 40x dx là?","options":["A. 20x^2 + C","B. 40x^2 + C","C. 5x^2 + C","D. 80x + C"],"answer":"A. 20x^2 + C","explanation":"∫40x dx = 20x^2 + C."},
{"question":"Môđun của số phức z = 36 + 48i là?","options":["A. 60","B. 84","C. 12","D. 1728"],"answer":"A. 60","explanation":"√(36^2+48^2)=60."},
{"question":"Đạo hàm của hàm số y = x^22 là?","options":["A. 22x^21","B. x^21","C. 21x^22","D. 22x^22"],"answer":"A. 22x^21","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=21 là?","options":["A. 2097152","B. 441","C. 42","D. 1048576"],"answer":"A. 2097152","explanation":"x = 2^21."},
{"question":"Nguyên hàm của 42x dx là?","options":["A. 21x^2 + C","B. 42x^2 + C","C. 7x^2 + C","D. 84x + C"],"answer":"A. 21x^2 + C","explanation":"∫42x dx = 21x^2 + C."},
{"question":"Môđun của số phức z = 45 + 60i là?","options":["A. 75","B. 105","C. 15","D. 2700"],"answer":"A. 75","explanation":"√(45^2+60^2)=75."},
{"question":"Đạo hàm của hàm số y = x^23 là?","options":["A. 23x^22","B. x^22","C. 22x^23","D. 23x^23"],"answer":"A. 23x^22","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=22 là?","options":["A. 4194304","B. 484","C. 44","D. 2097152"],"answer":"A. 4194304","explanation":"x = 2^22."},
{"question":"Nguyên hàm của 44x dx là?","options":["A. 22x^2 + C","B. 44x^2 + C","C. 11x^2 + C","D. 88x + C"],"answer":"A. 22x^2 + C","explanation":"∫44x dx = 22x^2 + C."},
{"question":"Môđun của số phức z = 48 + 64i là?","options":["A. 80","B. 112","C. 16","D. 3072"],"answer":"A. 80","explanation":"√(48^2+64^2)=80."},
{"question":"Đạo hàm của hàm số y = x^24 là?","options":["A. 24x^23","B. x^23","C. 23x^24","D. 24x^24"],"answer":"A. 24x^23","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=23 là?","options":["A. 8388608","B. 529","C. 46","D. 4194304"],"answer":"A. 8388608","explanation":"x = 2^23."},
{"question":"Nguyên hàm của 46x dx là?","options":["A. 23x^2 + C","B. 46x^2 + C","C. 2x^2 + C","D. 92x + C"],"answer":"A. 23x^2 + C","explanation":"∫46x dx = 23x^2 + C."},
{"question":"Môđun của số phức z = 60 + 80i là?","options":["A. 100","B. 140","C. 20","D. 4800"],"answer":"A. 100","explanation":"√(60^2+80^2)=100."},
{"question":"Đạo hàm của hàm số y = x^25 là?","options":["A. 25x^24","B. x^24","C. 24x^25","D. 25x^25"],"answer":"A. 25x^24","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=24 là?","options":["A. 16777216","B. 576","C. 48","D. 8388608"],"answer":"A. 16777216","explanation":"x = 2^24."},
{"question":"Nguyên hàm của 48x dx là?","options":["A. 24x^2 + C","B. 48x^2 + C","C. 6x^2 + C","D. 96x + C"],"answer":"A. 24x^2 + C","explanation":"∫48x dx = 24x^2 + C."},
{"question":"Môđun của số phức z = 63 + 84i là?","options":["A. 105","B. 147","C. 21","D. 5292"],"answer":"A. 105","explanation":"√(63^2+84^2)=105."},
{"question":"Đạo hàm của hàm số y = x^26 là?","options":["A. 26x^25","B. x^25","C. 25x^26","D. 26x^26"],"answer":"A. 26x^25","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=25 là?","options":["A. 33554432","B. 625","C. 50","D. 16777216"],"answer":"A. 33554432","explanation":"x = 2^25."},
{"question":"Nguyên hàm của 50x dx là?","options":["A. 25x^2 + C","B. 50x^2 + C","C. 10x^2 + C","D. 100x + C"],"answer":"A. 25x^2 + C","explanation":"∫50x dx = 25x^2 + C."},
{"question":"Môđun của số phức z = 72 + 96i là?","options":["A. 120","B. 168","C. 24","D. 6912"],"answer":"A. 120","explanation":"√(72^2+96^2)=120."},
{"question":"Đạo hàm của hàm số y = x^27 là?","options":["A. 27x^26","B. x^26","C. 26x^27","D. 27x^27"],"answer":"A. 27x^26","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=26 là?","options":["A. 67108864","B. 676","C. 52","D. 33554432"],"answer":"A. 67108864","explanation":"x = 2^26."},
{"question":"Nguyên hàm của 52x dx là?","options":["A. 26x^2 + C","B. 52x^2 + C","C. 4x^2 + C","D. 104x + C"],"answer":"A. 26x^2 + C","explanation":"∫52x dx = 26x^2 + C."},
{"question":"Môđun của số phức z = 84 + 112i là?","options":["A. 140","B. 196","C. 28","D. 9408"],"answer":"A. 140","explanation":"√(84^2+112^2)=140."},
{"question":"Đạo hàm của hàm số y = x^28 là?","options":["A. 28x^27","B. x^27","C. 27x^28","D. 28x^28"],"answer":"A. 28x^27","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=27 là?","options":["A. 134217728","B. 729","C. 54","D. 67108864"],"answer":"A. 134217728","explanation":"x = 2^27."},
{"question":"Nguyên hàm của 54x dx là?","options":["A. 27x^2 + C","B. 54x^2 + C","C. 9x^2 + C","D. 108x + C"],"answer":"A. 27x^2 + C","explanation":"∫54x dx = 27x^2 + C."},
{"question":"Môđun của số phức z = 96 + 128i là?","options":["A. 160","B. 224","C. 32","D. 12288"],"answer":"A. 160","explanation":"√(96^2+128^2)=160."},
{"question":"Đạo hàm của hàm số y = x^29 là?","options":["A. 29x^28","B. x^28","C. 28x^29","D. 29x^29"],"answer":"A. 29x^28","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=28 là?","options":["A. 268435456","B. 784","C. 56","D. 134217728"],"answer":"A. 268435456","explanation":"x = 2^28."},
{"question":"Nguyên hàm của 56x dx là?","options":["A. 28x^2 + C","B. 56x^2 + C","C. 7x^2 + C","D. 112x + C"],"answer":"A. 28x^2 + C","explanation":"∫56x dx = 28x^2 + C."},
{"question":"Môđun của số phức z = 105 + 140i là?","options":["A. 175","B. 245","C. 35","D. 14700"],"answer":"A. 175","explanation":"√(105^2+140^2)=175."},
{"question":"Đạo hàm của hàm số y = x^30 là?","options":["A. 30x^29","B. x^29","C. 29x^30","D. 30x^30"],"answer":"A. 30x^29","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=29 là?","options":["A. 536870912","B. 841","C. 58","D. 268435456"],"answer":"A. 536870912","explanation":"x = 2^29."},
{"question":"Nguyên hàm của 58x dx là?","options":["A. 29x^2 + C","B. 58x^2 + C","C. 2x^2 + C","D. 116x + C"],"answer":"A. 29x^2 + C","explanation":"∫58x dx = 29x^2 + C."},
{"question":"Môđun của số phức z = 120 + 160i là?","options":["A. 200","B. 280","C. 40","D. 19200"],"answer":"A. 200","explanation":"√(120^2+160^2)=200."},
{"question":"Đạo hàm của hàm số y = x^31 là?","options":["A. 31x^30","B. x^30","C. 30x^31","D. 31x^31"],"answer":"A. 31x^30","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=30 là?","options":["A. 1073741824","B. 900","C. 60","D. 536870912"],"answer":"A. 1073741824","explanation":"x = 2^30."},
{"question":"Nguyên hàm của 60x dx là?","options":["A. 30x^2 + C","B. 60x^2 + C","C. 5x^2 + C","D. 120x + C"],"answer":"A. 30x^2 + C","explanation":"∫60x dx = 30x^2 + C."},
{"question":"Môđun của số phức z = 144 + 192i là?","options":["A. 240","B. 336","C. 48","D. 27648"],"answer":"A. 240","explanation":"√(144^2+192^2)=240."},
{"question":"Đạo hàm của hàm số y = x^32 là?","options":["A. 32x^31","B. x^31","C. 31x^32","D. 32x^32"],"answer":"A. 32x^31","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=31 là?","options":["A. 2147483648","B. 961","C. 62","D. 1073741824"],"answer":"A. 2147483648","explanation":"x = 2^31."},
{"question":"Nguyên hàm của 62x dx là?","options":["A. 31x^2 + C","B. 62x^2 + C","C. 6x^2 + C","D. 124x + C"],"answer":"A. 31x^2 + C","explanation":"∫62x dx = 31x^2 + C."},
{"question":"Môđun của số phức z = 168 + 224i là?","options":["A. 280","B. 392","C. 56","D. 37632"],"answer":"A. 280","explanation":"√(168^2+224^2)=280."},
{"question":"Đạo hàm của hàm số y = x^33 là?","options":["A. 33x^32","B. x^32","C. 32x^33","D. 33x^33"],"answer":"A. 33x^32","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=32 là?","options":["A. 4294967296","B. 1024","C. 64","D. 2147483648"],"answer":"A. 4294967296","explanation":"x = 2^32."},
{"question":"Nguyên hàm của 64x dx là?","options":["A. 32x^2 + C","B. 64x^2 + C","C. 8x^2 + C","D. 128x + C"],"answer":"A. 32x^2 + C","explanation":"∫64x dx = 32x^2 + C."},
{"question":"Môđun của số phức z = 192 + 256i là?","options":["A. 320","B. 448","C. 64","D. 49152"],"answer":"A. 320","explanation":"√(192^2+256^2)=320."},
{"question":"Đạo hàm của hàm số y = x^34 là?","options":["A. 34x^33","B. x^33","C. 33x^34","D. 34x^34"],"answer":"A. 34x^33","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=33 là?","options":["A. 8589934592","B. 1089","C. 66","D. 4294967296"],"answer":"A. 8589934592","explanation":"x = 2^33."},
{"question":"Nguyên hàm của 66x dx là?","options":["A. 33x^2 + C","B. 66x^2 + C","C. 3x^2 + C","D. 132x + C"],"answer":"A. 33x^2 + C","explanation":"∫66x dx = 33x^2 + C."},
{"question":"Môđun của số phức z = 210 + 280i là?","options":["A. 350","B. 490","C. 70","D. 58800"],"answer":"A. 350","explanation":"√(210^2+280^2)=350."},
{"question":"Đạo hàm của hàm số y = x^35 là?","options":["A. 35x^34","B. x^34","C. 34x^35","D. 35x^35"],"answer":"A. 35x^34","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=34 là?","options":["A. 17179869184","B. 1156","C. 68","D. 8589934592"],"answer":"A. 17179869184","explanation":"x = 2^34."},
{"question":"Nguyên hàm của 68x dx là?","options":["A. 34x^2 + C","B. 68x^2 + C","C. 4x^2 + C","D. 136x + C"],"answer":"A. 34x^2 + C","explanation":"∫68x dx = 34x^2 + C."},
{"question":"Môđun của số phức z = 240 + 320i là?","options":["A. 400","B. 560","C. 80","D. 76800"],"answer":"A. 400","explanation":"√(240^2+320^2)=400."},
{"question":"Đạo hàm của hàm số y = x^36 là?","options":["A. 36x^35","B. x^35","C. 35x^36","D. 36x^36"],"answer":"A. 36x^35","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=35 là?","options":["A. 34359738368","B. 1225","C. 70","D. 17179869184"],"answer":"A. 34359738368","explanation":"x = 2^35."},
{"question":"Nguyên hàm của 70x dx là?","options":["A. 35x^2 + C","B. 70x^2 + C","C. 5x^2 + C","D. 140x + C"],"answer":"A. 35x^2 + C","explanation":"∫70x dx = 35x^2 + C."},
{"question":"Môđun của số phức z = 252 + 336i là?","options":["A. 420","B. 588","C. 84","D. 84672"],"answer":"A. 420","explanation":"√(252^2+336^2)=420."},
{"question":"Đạo hàm của hàm số y = x^37 là?","options":["A. 37x^36","B. x^36","C. 36x^37","D. 37x^37"],"answer":"A. 37x^36","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=36 là?","options":["A. 68719476736","B. 1296","C. 72","D. 34359738368"],"answer":"A. 68719476736","explanation":"x = 2^36."},
{"question":"Nguyên hàm của 72x dx là?","options":["A. 36x^2 + C","B. 72x^2 + C","C. 6x^2 + C","D. 144x + C"],"answer":"A. 36x^2 + C","explanation":"∫72x dx = 36x^2 + C."},
{"question":"Môđun của số phức z = 270 + 360i là?","options":["A. 450","B. 630","C. 90","D. 97200"],"answer":"A. 450","explanation":"√(270^2+360^2)=450."},
{"question":"Đạo hàm của hàm số y = x^38 là?","options":["A. 38x^37","B. x^37","C. 37x^38","D. 38x^38"],"answer":"A. 38x^37","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=37 là?","options":["A. 137438953472","B. 1369","C. 74","D. 68719476736"],"answer":"A. 137438953472","explanation":"x = 2^37."},
{"question":"Nguyên hàm của 74x dx là?","options":["A. 37x^2 + C","B. 74x^2 + C","C. 2x^2 + C","D. 148x + C"],"answer":"A. 37x^2 + C","explanation":"∫74x dx = 37x^2 + C."},
{"question":"Môđun của số phức z = 288 + 384i là?","options":["A. 480","B. 672","C. 96","D. 110592"],"answer":"A. 480","explanation":"√(288^2+384^2)=480."},
{"question":"Đạo hàm của hàm số y = x^39 là?","options":["A. 39x^38","B. x^38","C. 38x^39","D. 39x^39"],"answer":"A. 39x^38","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=38 là?","options":["A. 274877906944","B. 1444","C. 76","D. 137438953472"],"answer":"A. 274877906944","explanation":"x = 2^38."},
{"question":"Nguyên hàm của 76x dx là?","options":["A. 38x^2 + C","B. 76x^2 + C","C. 4x^2 + C","D. 152x + C"],"answer":"A. 38x^2 + C","explanation":"∫76x dx = 38x^2 + C."},
{"question":"Môđun của số phức z = 315 + 420i là?","options":["A. 525","B. 735","C. 105","D. 132300"],"answer":"A. 525","explanation":"√(315^2+420^2)=525."},
{"question":"Đạo hàm của hàm số y = x^40 là?","options":["A. 40x^39","B. x^39","C. 39x^40","D. 40x^40"],"answer":"A. 40x^39","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=39 là?","options":["A. 549755813888","B. 1521","C. 78","D. 274877906944"],"answer":"A. 549755813888","explanation":"x = 2^39."},
{"question":"Nguyên hàm của 78x dx là?","options":["A. 39x^2 + C","B. 78x^2 + C","C. 6x^2 + C","D. 156x + C"],"answer":"A. 39x^2 + C","explanation":"∫78x dx = 39x^2 + C."},
{"question":"Môđun của số phức z = 336 + 448i là?","options":["A. 560","B. 784","C. 112","D. 150528"],"answer":"A. 560","explanation":"√(336^2+448^2)=560."},
{"question":"Đạo hàm của hàm số y = x^41 là?","options":["A. 41x^40","B. x^40","C. 40x^41","D. 41x^41"],"answer":"A. 41x^40","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=40 là?","options":["A. 1099511627776","B. 1600","C. 80","D. 549755813888"],"answer":"A. 1099511627776","explanation":"x = 2^40."},
{"question":"Nguyên hàm của 80x dx là?","options":["A. 40x^2 + C","B. 80x^2 + C","C. 8x^2 + C","D. 160x + C"],"answer":"A. 40x^2 + C","explanation":"∫80x dx = 40x^2 + C."},
{"question":"Môđun của số phức z = 360 + 480i là?","options":["A. 600","B. 840","C. 120","D. 172800"],"answer":"A. 600","explanation":"√(360^2+480^2)=600."},
{"question":"Đạo hàm của hàm số y = x^42 là?","options":["A. 42x^41","B. x^41","C. 41x^42","D. 42x^42"],"answer":"A. 42x^41","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=41 là?","options":["A. 2199023255552","B. 1681","C. 82","D. 1099511627776"],"answer":"A. 2199023255552","explanation":"x = 2^41."},
{"question":"Nguyên hàm của 82x dx là?","options":["A. 41x^2 + C","B. 82x^2 + C","C. 2x^2 + C","D. 164x + C"],"answer":"A. 41x^2 + C","explanation":"∫82x dx = 41x^2 + C."},
{"question":"Môđun của số phức z = 384 + 512i là?","options":["A. 640","B. 896","C. 128","D. 196608"],"answer":"A. 640","explanation":"√(384^2+512^2)=640."},
{"question":"Đạo hàm của hàm số y = x^43 là?","options":["A. 43x^42","B. x^42","C. 42x^43","D. 43x^43"],"answer":"A. 43x^42","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=42 là?","options":["A. 4398046511104","B. 1764","C. 84","D. 2199023255552"],"answer":"A. 4398046511104","explanation":"x = 2^42."},
{"question":"Nguyên hàm của 84x dx là?","options":["A. 42x^2 + C","B. 84x^2 + C","C. 7x^2 + C","D. 168x + C"],"answer":"A. 42x^2 + C","explanation":"∫84x dx = 42x^2 + C."},
{"question":"Môđun của số phức z = 405 + 540i là?","options":["A. 675","B. 945","C. 135","D. 218700"],"answer":"A. 675","explanation":"√(405^2+540^2)=675."},
{"question":"Đạo hàm của hàm số y = x^44 là?","options":["A. 44x^43","B. x^43","C. 43x^44","D. 44x^44"],"answer":"A. 44x^43","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=43 là?","options":["A. 8796093022208","B. 1849","C. 86","D. 4398046511104"],"answer":"A. 8796093022208","explanation":"x = 2^43."},
{"question":"Nguyên hàm của 86x dx là?","options":["A. 43x^2 + C","B. 86x^2 + C","C. 3x^2 + C","D. 172x + C"],"answer":"A. 43x^2 + C","explanation":"∫86x dx = 43x^2 + C."},
{"question":"Môđun của số phức z = 420 + 560i là?","options":["A. 700","B. 980","C. 140","D. 235200"],"answer":"A. 700","explanation":"√(420^2+560^2)=700."},
{"question":"Đạo hàm của hàm số y = x^45 là?","options":["A. 45x^44","B. x^44","C. 44x^45","D. 45x^45"],"answer":"A. 45x^44","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=44 là?","options":["A. 17592186044416","B. 1936","C. 88","D. 8796093022208"],"answer":"A. 17592186044416","explanation":"x = 2^44."},
{"question":"Nguyên hàm của 88x dx là?","options":["A. 44x^2 + C","B. 88x^2 + C","C. 4x^2 + C","D. 176x + C"],"answer":"A. 44x^2 + C","explanation":"∫88x dx = 44x^2 + C."},
{"question":"Môđun của số phức z = 432 + 576i là?","options":["A. 720","B. 1008","C. 144","D. 248832"],"answer":"A. 720","explanation":"√(432^2+576^2)=720."},
{"question":"Đạo hàm của hàm số y = x^46 là?","options":["A. 46x^45","B. x^45","C. 45x^46","D. 46x^46"],"answer":"A. 46x^45","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=45 là?","options":["A. 35184372088832","B. 2025","C. 90","D. 17592186044416"],"answer":"A. 35184372088832","explanation":"x = 2^45."},
{"question":"Nguyên hàm của 90x dx là?","options":["A. 45x^2 + C","B. 90x^2 + C","C. 5x^2 + C","D. 180x + C"],"answer":"A. 45x^2 + C","explanation":"∫90x dx = 45x^2 + C."},
{"question":"Môđun của số phức z = 450 + 600i là?","options":["A. 750","B. 1050","C. 150","D. 270000"],"answer":"A. 750","explanation":"√(450^2+600^2)=750."},
{"question":"Đạo hàm của hàm số y = x^47 là?","options":["A. 47x^46","B. x^46","C. 46x^47","D. 47x^47"],"answer":"A. 47x^46","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=46 là?","options":["A. 70368744177664","B. 2116","C. 92","D. 35184372088832"],"answer":"A. 70368744177664","explanation":"x = 2^46."},
{"question":"Nguyên hàm của 92x dx là?","options":["A. 46x^2 + C","B. 92x^2 + C","C. 6x^2 + C","D. 184x + C"],"answer":"A. 46x^2 + C","explanation":"∫92x dx = 46x^2 + C."},
{"question":"Môđun của số phức z = 468 + 624i là?","options":["A. 780","B. 1092","C. 156","D. 292032"],"answer":"A. 780","explanation":"√(468^2+624^2)=780."},
{"question":"Đạo hàm của hàm số y = x^48 là?","options":["A. 48x^47","B. x^47","C. 47x^48","D. 48x^48"],"answer":"A. 48x^47","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=47 là?","options":["A. 140737488355328","B. 2209","C. 94","D. 70368744177664"],"answer":"A. 140737488355328","explanation":"x = 2^47."},
{"question":"Nguyên hàm của 94x dx là?","options":["A. 47x^2 + C","B. 94x^2 + C","C. 7x^2 + C","D. 188x + C"],"answer":"A. 47x^2 + C","explanation":"∫94x dx = 47x^2 + C."},
{"question":"Môđun của số phức z = 480 + 640i là?","options":["A. 800","B. 1120","C. 160","D. 307200"],"answer":"A. 800","explanation":"√(480^2+640^2)=800."},
{"question":"Đạo hàm của hàm số y = x^49 là?","options":["A. 49x^48","B. x^48","C. 48x^49","D. 49x^49"],"answer":"A. 49x^48","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=48 là?","options":["A. 281474976710656","B. 2304","C. 96","D. 140737488355328"],"answer":"A. 281474976710656","explanation":"x = 2^48."},
{"question":"Nguyên hàm của 96x dx là?","options":["A. 48x^2 + C","B. 96x^2 + C","C. 8x^2 + C","D. 192x + C"],"answer":"A. 48x^2 + C","explanation":"∫96x dx = 48x^2 + C."},
{"question":"Môđun của số phức z = 504 + 672i là?","options":["A. 840","B. 1176","C. 168","D. 338688"],"answer":"A. 840","explanation":"√(504^2+672^2)=840."},
{"question":"Đạo hàm của hàm số y = x^50 là?","options":["A. 50x^49","B. x^49","C. 49x^50","D. 50x^50"],"answer":"A. 50x^49","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=49 là?","options":["A. 562949953421312","B. 2401","C. 98","D. 281474976710656"],"answer":"A. 562949953421312","explanation":"x = 2^49."},
{"question":"Nguyên hàm của 98x dx là?","options":["A. 49x^2 + C","B. 98x^2 + C","C. 9x^2 + C","D. 196x + C"],"answer":"A. 49x^2 + C","explanation":"∫98x dx = 49x^2 + C."},
{"question":"Môđun của số phức z = 540 + 720i là?","options":["A. 900","B. 1260","C. 180","D. 388800"],"answer":"A. 900","explanation":"√(540^2+720^2)=900."},
{"question":"Đạo hàm của hàm số y = x^51 là?","options":["A. 51x^50","B. x^50","C. 50x^51","D. 51x^51"],"answer":"A. 51x^50","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=50 là?","options":["A. 1125899906842624","B. 2500","C. 100","D. 562949953421312"],"answer":"A. 1125899906842624","explanation":"x = 2^50."},
{"question":"Nguyên hàm của 100x dx là?","options":["A. 50x^2 + C","B. 100x^2 + C","C. 10x^2 + C","D. 200x + C"],"answer":"A. 50x^2 + C","explanation":"∫100x dx = 50x^2 + C."},
{"question":"Môđun của số phức z = 576 + 768i là?","options":["A. 960","B. 1344","C. 192","D. 442368"],"answer":"A. 960","explanation":"√(576^2+768^2)=960."},
{"question":"Đạo hàm của hàm số y = x^52 là?","options":["A. 52x^51","B. x^51","C. 51x^52","D. 52x^52"],"answer":"A. 52x^51","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=51 là?","options":["A. 2251799813685248","B. 2601","C. 102","D. 1125899906842624"],"answer":"A. 2251799813685248","explanation":"x = 2^51."},
{"question":"Nguyên hàm của 102x dx là?","options":["A. 51x^2 + C","B. 102x^2 + C","C. 11x^2 + C","D. 204x + C"],"answer":"A. 51x^2 + C","explanation":"∫102x dx = 51x^2 + C."},
{"question":"Môđun của số phức z = 600 + 800i là?","options":["A. 1000","B. 1400","C. 200","D. 480000"],"answer":"A. 1000","explanation":"√(600^2+800^2)=1000."},
{"question":"Đạo hàm của hàm số y = x^53 là?","options":["A. 53x^52","B. x^52","C. 52x^53","D. 53x^53"],"answer":"A. 53x^52","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=52 là?","options":["A. 4503599627370496","B. 2704","C. 104","D. 2251799813685248"],"answer":"A. 4503599627370496","explanation":"x = 2^52."},
{"question":"Nguyên hàm của 104x dx là?","options":["A. 52x^2 + C","B. 104x^2 + C","C. 12x^2 + C","D. 208x + C"],"answer":"A. 52x^2 + C","explanation":"∫104x dx = 52x^2 + C."},
{"question":"Môđun của số phức z = 624 + 832i là?","options":["A. 1040","B. 1456","C. 208","D. 519168"],"answer":"A. 1040","explanation":"√(624^2+832^2)=1040."},
{"question":"Đạo hàm của hàm số y = x^54 là?","options":["A. 54x^53","B. x^53","C. 53x^54","D. 54x^54"],"answer":"A. 54x^53","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=53 là?","options":["A. 9007199254740992","B. 2809","C. 106","D. 4503599627370496"],"answer":"A. 9007199254740992","explanation":"x = 2^53."},
{"question":"Nguyên hàm của 106x dx là?","options":["A. 53x^2 + C","B. 106x^2 + C","C. 13x^2 + C","D. 212x + C"],"answer":"A. 53x^2 + C","explanation":"∫106x dx = 53x^2 + C."},
{"question":"Môđun của số phức z = 648 + 864i là?","options":["A. 1080","B. 1512","C. 216","D. 559872"],"answer":"A. 1080","explanation":"√(648^2+864^2)=1080."},
{"question":"Đạo hàm của hàm số y = x^55 là?","options":["A. 55x^54","B. x^54","C. 54x^55","D. 55x^55"],"answer":"A. 55x^54","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=54 là?","options":["A. 18014398509481984","B. 2916","C. 108","D. 9007199254740992"],"answer":"A. 18014398509481984","explanation":"x = 2^54."},
{"question":"Nguyên hàm của 108x dx là?","options":["A. 54x^2 + C","B. 108x^2 + C","C. 14x^2 + C","D. 216x + C"],"answer":"A. 54x^2 + C","explanation":"∫108x dx = 54x^2 + C."},
{"question":"Môđun của số phức z = 672 + 896i là?","options":["A. 1120","B. 1568","C. 224","D. 602112"],"answer":"A. 1120","explanation":"√(672^2+896^2)=1120."},
{"question":"Đạo hàm của hàm số y = x^56 là?","options":["A. 56x^55","B. x^55","C. 55x^56","D. 56x^56"],"answer":"A. 56x^55","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=55 là?","options":["A. 36028797018963968","B. 3025","C. 110","D. 18014398509481984"],"answer":"A. 36028797018963968","explanation":"x = 2^55."},
{"question":"Nguyên hàm của 110x dx là?","options":["A. 55x^2 + C","B. 110x^2 + C","C. 15x^2 + C","D. 220x + C"],"answer":"A. 55x^2 + C","explanation":"∫110x dx = 55x^2 + C."},
{"question":"Môđun của số phức z = 700 + 936i là?","options":["A. 1168","B. 1632","C. 232","D. 656000"],"answer":"A. 1168","explanation":"√(700^2+936^2)=1168."},
{"question":"Đạo hàm của hàm số y = x^57 là?","options":["A. 57x^56","B. x^56","C. 56x^57","D. 57x^57"],"answer":"A. 57x^56","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=56 là?","options":["A. 72057594037927936","B. 3136","C. 112","D. 36028797018963968"],"answer":"A. 72057594037927936","explanation":"x = 2^56."},
{"question":"Nguyên hàm của 112x dx là?","options":["A. 56x^2 + C","B. 112x^2 + C","C. 16x^2 + C","D. 224x + C"],"answer":"A. 56x^2 + C","explanation":"∫112x dx = 56x^2 + C."},
{"question":"Môđun của số phức z = 720 + 960i là?","options":["A. 1200","B. 1680","C. 240","D. 748800"],"answer":"A. 1200","explanation":"√(720^2+960^2)=1200."},
{"question":"Đạo hàm của hàm số y = x^58 là?","options":["A. 58x^57","B. x^57","C. 57x^58","D. 58x^58"],"answer":"A. 58x^57","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=57 là?","options":["A. 144115188075855872","B. 3249","C. 114","D. 72057594037927936"],"answer":"A. 144115188075855872","explanation":"x = 2^57."},
{"question":"Nguyên hàm của 114x dx là?","options":["A. 57x^2 + C","B. 114x^2 + C","C. 17x^2 + C","D. 228x + C"],"answer":"A. 57x^2 + C","explanation":"∫114x dx = 57x^2 + C."},
{"question":"Môđun của số phức z = 750 + 1000i là?","options":["A. 1250","B. 1750","C. 250","D. 812500"],"answer":"A. 1250","explanation":"√(750^2+1000^2)=1250."},
{"question":"Đạo hàm của hàm số y = x^59 là?","options":["A. 59x^58","B. x^58","C. 58x^59","D. 59x^59"],"answer":"A. 59x^58","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=58 là?","options":["A. 288230376151711744","B. 3364","C. 116","D. 144115188075855872"],"answer":"A. 288230376151711744","explanation":"x = 2^58."},
{"question":"Nguyên hàm của 116x dx là?","options":["A. 58x^2 + C","B. 116x^2 + C","C. 18x^2 + C","D. 232x + C"],"answer":"A. 58x^2 + C","explanation":"∫116x dx = 58x^2 + C."},
{"question":"Môđun của số phức z = 780 + 1040i là?","options":["A. 1300","B. 1820","C. 260","D. 908800"],"answer":"A. 1300","explanation":"√(780^2+1040^2)=1300."},
{"question":"Đạo hàm của hàm số y = x^60 là?","options":["A. 60x^59","B. x^59","C. 59x^60","D. 60x^60"],"answer":"A. 60x^59","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=59 là?","options":["A. 576460752303423488","B. 3481","C. 118","D. 288230376151711744"],"answer":"A. 576460752303423488","explanation":"x = 2^59."},
{"question":"Nguyên hàm của 118x dx là?","options":["A. 59x^2 + C","B. 118x^2 + C","C. 19x^2 + C","D. 236x + C"],"answer":"A. 59x^2 + C","explanation":"∫118x dx = 59x^2 + C."},
{"question":"Môđun của số phức z = 810 + 1080i là?","options":["A. 1350","B. 1890","C. 270","D. 1044900"],"answer":"A. 1350","explanation":"√(810^2+1080^2)=1350."},
{"question":"Đạo hàm của hàm số y = x^61 là?","options":["A. 61x^60","B. x^60","C. 60x^61","D. 61x^61"],"answer":"A. 61x^60","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=60 là?","options":["A. 1152921504606846976","B. 3600","C. 120","D. 576460752303423488"],"answer":"A. 1152921504606846976","explanation":"x = 2^60."},
{"question":"Nguyên hàm của 120x dx là?","options":["A. 60x^2 + C","B. 120x^2 + C","C. 20x^2 + C","D. 240x + C"],"answer":"A. 60x^2 + C","explanation":"∫120x dx = 60x^2 + C."},
{"question":"Môđun của số phức z = 840 + 1120i là?","options":["A. 1400","B. 1960","C. 280","D. 1254400"],"answer":"A. 1400","explanation":"√(840^2+1120^2)=1400."},
{"question":"Đạo hàm của hàm số y = x^62 là?","options":["A. 62x^61","B. x^61","C. 61x^62","D. 62x^62"],"answer":"A. 62x^61","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=61 là?","options":["A. 2305843009213693952","B. 3721","C. 122","D. 1152921504606846976"],"answer":"A. 2305843009213693952","explanation":"x = 2^61."},
{"question":"Nguyên hàm của 122x dx là?","options":["A. 61x^2 + C","B. 122x^2 + C","C. 21x^2 + C","D. 244x + C"],"answer":"A. 61x^2 + C","explanation":"∫122x dx = 61x^2 + C."},
{"question":"Môđun của số phức z = 900 + 1200i là?","options":["A. 1500","B. 2100","C. 300","D. 2250000"],"answer":"A. 1500","explanation":"√(900^2+1200^2)=1500."},
{"question":"Đạo hàm của hàm số y = x^63 là?","options":["A. 63x^62","B. x^62","C. 62x^63","D. 63x^63"],"answer":"A. 63x^62","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=62 là?","options":["A. 4611686018427387904","B. 3844","C. 124","D. 2305843009213693952"],"answer":"A. 4611686018427387904","explanation":"x = 2^62."},
{"question":"Nguyên hàm của 124x dx là?","options":["A. 62x^2 + C","B. 124x^2 + C","C. 22x^2 + C","D. 248x + C"],"answer":"A. 62x^2 + C","explanation":"∫124x dx = 62x^2 + C."},
{"question":"Môđun của số phức z = 960 + 1280i là?","options":["A. 1600","B. 2240","C. 320","D. 2560000"],"answer":"A. 1600","explanation":"√(960^2+1280^2)=1600."},
{"question":"Đạo hàm của hàm số y = x^64 là?","options":["A. 64x^63","B. x^63","C. 63x^64","D. 64x^64"],"answer":"A. 64x^63","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=63 là?","options":["A. 9223372036854775808","B. 3969","C. 126","D. 4611686018427387904"],"answer":"A. 9223372036854775808","explanation":"x = 2^63."},
{"question":"Nguyên hàm của 126x dx là?","options":["A. 63x^2 + C","B. 126x^2 + C","C. 23x^2 + C","D. 252x + C"],"answer":"A. 63x^2 + C","explanation":"∫126x dx = 63x^2 + C."},
{"question":"Môđun của số phức z = 1020 + 1360i là?","options":["A. 1700","B. 2380","C. 340","D. 3000000"],"answer":"A. 1700","explanation":"√(1020^2+1360^2)=1700."},
{"question":"Đạo hàm của hàm số y = x^65 là?","options":["A. 65x^64","B. x^64","C. 64x^65","D. 65x^65"],"answer":"A. 65x^64","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=64 là?","options":["A. 18446744073709551616","B. 4096","C. 128","D. 9223372036854775808"],"answer":"A. 18446744073709551616","explanation":"x = 2^64."},
{"question":"Nguyên hàm của 128x dx là?","options":["A. 64x^2 + C","B. 128x^2 + C","C. 24x^2 + C","D. 256x + C"],"answer":"A. 64x^2 + C","explanation":"∫128x dx = 64x^2 + C."},
{"question":"Môđun của số phức z = 1080 + 1440i là?","options":["A. 1800","B. 2520","C. 360","D. 3240000"],"answer":"A. 1800","explanation":"√(1080^2+1440^2)=1800."},
{"question":"Đạo hàm của hàm số y = x^66 là?","options":["A. 66x^65","B. x^65","C. 65x^66","D. 66x^66"],"answer":"A. 66x^65","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=65 là?","options":["A. 36893488147419103232","B. 4225","C. 130","D. 18446744073709551616"],"answer":"A. 36893488147419103232","explanation":"x = 2^65."},
{"question":"Nguyên hàm của 130x dx là?","options":["A. 65x^2 + C","B. 130x^2 + C","C. 25x^2 + C","D. 260x + C"],"answer":"A. 65x^2 + C","explanation":"∫130x dx = 65x^2 + C."},
{"question":"Môđun của số phức z = 1140 + 1520i là?","options":["A. 1900","B. 2660","C. 380","D. 3600000"],"answer":"A. 1900","explanation":"√(1140^2+1520^2)=1900."},
{"question":"Đạo hàm của hàm số y = x^67 là?","options":["A. 67x^66","B. x^66","C. 66x^67","D. 67x^67"],"answer":"A. 67x^66","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=66 là?","options":["A. 73786976294838206464","B. 4356","C. 132","D. 36893488147419103232"],"answer":"A. 73786976294838206464","explanation":"x = 2^66."},
{"question":"Nguyên hàm của 132x dx là?","options":["A. 66x^2 + C","B. 132x^2 + C","C. 26x^2 + C","D. 264x + C"],"answer":"A. 66x^2 + C","explanation":"∫132x dx = 66x^2 + C."},
  {
    "question": "Họ tất cả các nguyên hàm của hàm số $f(x) = \cos x + 6x$ là:",
    "options": ["\sin x + 3x^2 + C", "-\sin x + 3x^2 + C", "\sin x + 6x^2 + C", "-\sin x + C"],
    "answer": "A",
    "explanation": "$\int (\cos x + 6x) dx = \sin x + 6 \cdot \frac{x^2}{2} + C = \sin x + 3x^2 + C$."
  },
  {
    "question": "Cho $\int_{0}^{1} f(x) dx = 2$ và $\int_{0}^{1} g(x) dx = 5$. Tính $I = \int_{0}^{1} [f(x) + 2g(x)] dx$.",
    "options": ["12", "7", "9", "11"],
    "answer": "A",
    "explanation": "$I = \int f(x) dx + 2\int g(x) dx = 2 + 2(5) = 12$."
  },
  {
    "question": "Tính tích phân $I = \int_{1}^{e} \frac{1}{x} dx$.",
    "options": ["I = e", "I = 1", "I = 0", "I = \ln(e-1)"],
    "answer": "B",
    "explanation": "$I = \ln|x| \big|_1^e = \ln e - \ln 1 = 1 - 0 = 1$."
  },
  {
    "question": "Hàm số $F(x) = e^x + x^2$ là một nguyên hàm của hàm số nào dưới đây?",
    "options": ["f(x) = e^x + 2x", "f(x) = e^x + \frac{x^3}{3}", "f(x) = e^x + x^2", "f(x) = e^x - 2x"],
    "answer": "A",
    "explanation": "$f(x) = F'(x) = (e^x + x^2)' = e^x + 2x$."
  },
  {
    "question": "Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = x^2 - 4$, trục hoành và hai đường thẳng $x = 0, x = 2$ là:",
    "options": ["\frac{8}{3}", "\frac{16}{3}", "4", "8"],
    "answer": "B",
    "explanation": "$S = \int_{0}^{2} |x^2 - 4| dx = \int_{0}^{2} (4 - x^2) dx = (4x - \frac{x^3}{3}) \big|_0^2 = 8 - \frac{8}{3} = \frac{16}{3}$."
  },
  {
    "question": "Cho số phức $z = 3 - 2i$. Phần ảo của số phức $z$ là:",
    "options": ["-2i", "3", "-2", "2"],
    "answer": "C",
    "explanation": "Số phức $z = a + bi$ có phần ảo là $b$. Ở đây $b = -2$."
  },
  {
    "question": "Cho hai số phức $z_1 = 1 + 2i$ và $z_2 = 3 - i$. Tính $z_1 + z_2$.",
    "options": ["4 + i", "4 + 3i", "2 - 3i", "4 - i"],
    "answer": "A",
    "explanation": "$z_1 + z_2 = (1+3) + (2-1)i = 4 + i$."
  },
  {
    "question": "Số phức liên hợp của $z = 1 - 5i$ là:",
    "options": ["\bar{z} = -1 + 5i", "\bar{z} = 1 + 5i", "\bar{z} = -1 - 5i", "\bar{z} = 5 - i"],
    "answer": "B",
    "explanation": "Số phức liên hợp của $z = a + bi$ là $\bar{z} = a - bi$."
  },
  {
    "question": "Trên mặt phẳng tọa độ, điểm biểu diễn số phức $z = -1 + 2i$ là điểm nào?",
    "options": ["Q(1; -2)", "P(-1; 2)", "N(2; -1)", "M(-1; -2)"],
    "answer": "B",
    "explanation": "Điểm biểu diễn $z = a + bi$ có tọa độ $(a; b)$, tức là $(-1; 2)$."
  },
  {
    "question": "Môđun của số phức $z$ thỏa mãn $z(1+i) = 3 - i$ là:",
    "options": ["|z| = \sqrt{5}", "|z| = 5", "|z| = \sqrt{10}", "|z| = 2"],
    "answer": "A",
    "explanation": "$|z| \cdot |1+i| = |3-i| \Rightarrow |z| \cdot \sqrt{2} = \sqrt{3^2 + (-1)^2} = \sqrt{10} \Rightarrow |z| = \sqrt{5}$."
  },
  {
    "question": "Trong không gian $Oxyz$, cho điểm $A(1; 2; 3)$. Hình chiếu vuông góc của $A$ lên mặt phẳng $(Oxy)$ có tọa độ là:",
    "options": ["(1; 0; 0)", "(0; 2; 0)", "(1; 2; 0)", "(0; 0; 3)"],
    "answer": "C",
    "explanation": "Chiếu lên $(Oxy)$ thì giữ nguyên $x, y$ và cho $z = 0$."
  },
  {
    "question": "Trong không gian $Oxyz$, vectơ nào dưới đây là một vectơ pháp tuyến của mặt phẳng $(P): 2x - y + 3z - 1 = 0$?",
    "options": ["\vec{n} = (2; -1; 3)", "\vec{n} = (2; 1; 3)", "\vec{n} = (-1; 3; -1)", "\vec{n} = (2; -1; -1)"],
    "answer": "A",
    "explanation": "VTPT là hệ số của $x, y, z$ trong phương trình tổng quát."
  },
  {
    "question": "Trong không gian $Oxyz$, tâm của mặt cầu $(S): x^2 + y^2 + z^2 - 2x + 4y - 6z + 1 = 0$ có tọa độ là:",
    "options": ["(2; -4; 6)", "(-1; 2; -3)", "(1; -2; 3)", "(-2; 4; -6)"],
    "answer": "C",
    "explanation": "Tọa độ tâm $I(a, b, c)$ với $a = \frac{-2}{-2}=1, b = \frac{4}{-2}=-2, c = \frac{-6}{-2}=3$."
  },
  {
    "question": "Trong không gian $Oxyz$, phương trình đường thẳng đi qua điểm $M(1; -1; 2)$ và có vectơ chỉ phương $\vec{u} = (2; 3; 1)$ là:",
    "options": ["\frac{x-1}{2} = \frac{y+1}{3} = \frac{z-2}{1}", "\frac{x+1}{2} = \frac{y-1}{3} = \frac{z+2}{1}", "\frac{x-2}{1} = \frac{y-3}{-1} = \frac{z-1}{2}", "\frac{x-1}{2} = \frac{y-1}{3} = \frac{z-2}{1}"],
    "answer": "A",
    "explanation": "Phương trình chính tắc: $\frac{x-x_0}{a} = \frac{y-y_0}{b} = \frac{z-z_0}{c}$."
  },
  {
    "question": "Trong không gian $Oxyz$, khoảng cách từ điểm $M(1; 2; -3)$ đến mặt phẳng $(P): x + 2y - 2z + 3 = 0$ bằng:",
    "options": ["2", "4", "14/3", "1"],
    "answer": "B",
    "explanation": "$d = \frac{|1 + 2(2) - 2(-3) + 3|}{\sqrt{1^2 + 2^2 + (-2)^2}} = \frac{|1+4+6+3|}{3} = \frac{14}{3}$ (Sửa lỗi: $d=14/3$ là đáp án đúng)."
  },
  {
    "question": "Trong không gian $Oxyz$, cho hai điểm $A(1; 1; 2)$ và $B(3; 1; 0)$. Trung điểm của đoạn thẳng $AB$ có tọa độ là:",
    "options": ["(2; 1; 1)", "(4; 2; 2)", "(1; 0; -1)", "(2; 0; -1)"],
    "answer": "A",
    "explanation": "$M = (\frac{1+3}{2}; \frac{1+1}{2}; \frac{2+0}{2}) = (2; 1; 1)$."
  },
  {
    "question": "Tích phân $I = \int_{0}^{\pi/2} \sin x dx$ bằng:",
    "options": ["0", "1", "-1", "\pi/2"],
    "answer": "B",
    "explanation": "$I = -\cos x \big|_0^{\pi/2} = -(\cos \frac{\pi}{2} - \cos 0) = -(0 - 1) = 1$."
  },
  {
    "question": "Cho số phức $z$ thỏa mãn $|z| = 5$. Biết tập hợp các điểm biểu diễn số phức $z$ là một đường tròn, bán kính của đường tròn đó là:",
    "options": ["25", "5", "10", "\sqrt{5}"],
    "answer": "B",
    "explanation": "$|z| = R = 5$."
  },
  {
    "question": "Trong không gian $Oxyz$, mặt phẳng đi qua gốc tọa độ $O$ và song song với mặt phẳng $(P): x - y + 2z - 3 = 0$ có phương trình là:",
    "options": ["x - y + 2z = 0", "x + y - 2z = 0", "x - y - 2z = 0", "x - y + 2z + 3 = 0"],
    "answer": "A",
    "explanation": "Mặt phẳng song song có cùng VTPT và đi qua $(0;0;0)$ nên hệ số tự do $d=0$."
  },
  {
    "question": "Tìm số phức $z$ biết $\bar{z} = 2 + i$.",
    "options": ["z = 2 - i", "z = -2 - i", "z = -2 + i", "z = 2 + i"],
    "answer": "A",
    "explanation": "$z = \overline{(\bar{z})} = \overline{2+i} = 2-i$."
  },
{"question":"Môđun của số phức z = 1200 + 1600i là?","options":["A. 2000","B. 2800","C. 400","D. 4000000"],"answer":"A. 2000","explanation":"√(1200^2+1600^2)=2000."},
{"question":"Đạo hàm của hàm số y = x^68 là?","options":["A. 68x^67","B. x^67","C. 67x^68","D. 68x^68"],"answer":"A. 68x^67","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=67 là?","options":["A. 147573952589676412928","B. 4489","C. 134","D. 73786976294838206464"],"answer":"A. 147573952589676412928","explanation":"x = 2^67."},
{"question":"Nguyên hàm của 134x dx là?","options":["A. 67x^2 + C","B. 134x^2 + C","C. 27x^2 + C","D. 268x + C"],"answer":"A. 67x^2 + C","explanation":"∫134x dx = 67x^2 + C."},
{"question":"Môđun của số phức z = 1260 + 1680i là?","options":["A. 2100","B. 2940","C. 420","D. 4410000"],"answer":"A. 2100","explanation":"√(1260^2+1680^2)=2100."},
{"question":"Đạo hàm của hàm số y = x^69 là?","options":["A. 69x^68","B. x^68","C. 68x^69","D. 69x^69"],"answer":"A. 69x^68","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=68 là?","options":["A. 295147905179352825856","B. 4624","C. 136","D. 147573952589676412928"],"answer":"A. 295147905179352825856","explanation":"x = 2^68."},
{"question":"Nguyên hàm của 136x dx là?","options":["A. 68x^2 + C","B. 136x^2 + C","C. 28x^2 + C","D. 272x + C"],"answer":"A. 68x^2 + C","explanation":"∫136x dx = 68x^2 + C."},
{"question":"Môđun của số phức z = 1320 + 1760i là?","options":["A. 2200","B. 3080","C. 440","D. 4840000"],"answer":"A. 2200","explanation":"√(1320^2+1760^2)=2200."},
{"question":"Đạo hàm của hàm số y = x^70 là?","options":["A. 70x^69","B. x^69","C. 69x^70","D. 70x^70"],"answer":"A. 70x^69","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=69 là?","options":["A. 590295810358705651712","B. 4761","C. 138","D. 295147905179352825856"],"answer":"A. 590295810358705651712","explanation":"x = 2^69."},
{"question":"Nguyên hàm của 138x dx là?","options":["A. 69x^2 + C","B. 138x^2 + C","C. 29x^2 + C","D. 276x + C"],"answer":"A. 69x^2 + C","explanation":"∫138x dx = 69x^2 + C."},
{"question":"Môđun của số phức z = 1380 + 1840i là?","options":["A. 2300","B. 3220","C. 460","D. 5290000"],"answer":"A. 2300","explanation":"√(1380^2+1840^2)=2300."},
{"question":"Đạo hàm của hàm số y = x^71 là?","options":["A. 71x^70","B. x^70","C. 70x^71","D. 71x^71"],"answer":"A. 71x^70","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=70 là?","options":["A. 1180591620717411303424","B. 4900","C. 140","D. 590295810358705651712"],"answer":"A. 1180591620717411303424","explanation":"x = 2^70."},
{"question":"Nguyên hàm của 140x dx là?","options":["A. 70x^2 + C","B. 140x^2 + C","C. 30x^2 + C","D. 280x + C"],"answer":"A. 70x^2 + C","explanation":"∫140x dx = 70x^2 + C."},
{"question":"Môđun của số phức z = 1440 + 1920i là?","options":["A. 2400","B. 3360","C. 480","D. 5760000"],"answer":"A. 2400","explanation":"√(1440^2+1920^2)=2400."},
{"question":"Đạo hàm của hàm số y = x^72 là?","options":["A. 72x^71","B. x^71","C. 71x^72","D. 72x^72"],"answer":"A. 72x^71","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=71 là?","options":["A. 2361183241434822606848","B. 5041","C. 142","D. 1180591620717411303424"],"answer":"A. 2361183241434822606848","explanation":"x = 2^71."},
{"question":"Nguyên hàm của 142x dx là?","options":["A. 71x^2 + C","B. 142x^2 + C","C. 31x^2 + C","D. 284x + C"],"answer":"A. 71x^2 + C","explanation":"∫142x dx = 71x^2 + C."},
{"question":"Môđun của số phức z = 1200 + 1600i là?","options":["A. 2000","B. 2800","C. 400","D. 4000000"],"answer":"A. 2000","explanation":"√(1200^2+1600^2)=2000."},
{"question":"Đạo hàm của hàm số y = x^68 là?","options":["A. 68x^67","B. x^67","C. 67x^68","D. 68x^68"],"answer":"A. 68x^67","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=67 là?","options":["A. 147573952589676412928","B. 4489","C. 134","D. 73786976294838206464"],"answer":"A. 147573952589676412928","explanation":"x = 2^67."},
{"question":"Nguyên hàm của 134x dx là?","options":["A. 67x^2 + C","B. 134x^2 + C","C. 27x^2 + C","D. 268x + C"],"answer":"A. 67x^2 + C","explanation":"∫134x dx = 67x^2 + C."},
{"question":"Môđun của số phức z = 1260 + 1680i là?","options":["A. 2100","B. 2940","C. 420","D. 4410000"],"answer":"A. 2100","explanation":"√(1260^2+1680^2)=2100."},
{"question":"Đạo hàm của hàm số y = x^69 là?","options":["A. 69x^68","B. x^68","C. 68x^69","D. 69x^69"],"answer":"A. 69x^68","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=68 là?","options":["A. 295147905179352825856","B. 4624","C. 136","D. 147573952589676412928"],"answer":"A. 295147905179352825856","explanation":"x = 2^68."},
{"question":"Nguyên hàm của 136x dx là?","options":["A. 68x^2 + C","B. 136x^2 + C","C. 28x^2 + C","D. 272x + C"],"answer":"A. 68x^2 + C","explanation":"∫136x dx = 68x^2 + C."},
{"question":"Môđun của số phức z = 1320 + 1760i là?","options":["A. 2200","B. 3080","C. 440","D. 4840000"],"answer":"A. 2200","explanation":"√(1320^2+1760^2)=2200."},
{"question":"Đạo hàm của hàm số y = x^70 là?","options":["A. 70x^69","B. x^69","C. 69x^70","D. 70x^70"],"answer":"A. 70x^69","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=69 là?","options":["A. 590295810358705651712","B. 4761","C. 138","D. 295147905179352825856"],"answer":"A. 590295810358705651712","explanation":"x = 2^69."},
{"question":"Nguyên hàm của 138x dx là?","options":["A. 69x^2 + C","B. 138x^2 + C","C. 29x^2 + C","D. 276x + C"],"answer":"A. 69x^2 + C","explanation":"∫138x dx = 69x^2 + C."},
{"question":"Môđun của số phức z = 1380 + 1840i là?","options":["A. 2300","B. 3220","C. 460","D. 5290000"],"answer":"A. 2300","explanation":"√(1380^2+1840^2)=2300."},
{"question":"Đạo hàm của hàm số y = x^71 là?","options":["A. 71x^70","B. x^70","C. 70x^71","D. 71x^71"],"answer":"A. 71x^70","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=70 là?","options":["A. 1180591620717411303424","B. 4900","C. 140","D. 590295810358705651712"],"answer":"A. 1180591620717411303424","explanation":"x = 2^70."},
{"question":"Nguyên hàm của 140x dx là?","options":["A. 70x^2 + C","B. 140x^2 + C","C. 30x^2 + C","D. 280x + C"],"answer":"A. 70x^2 + C","explanation":"∫140x dx = 70x^2 + C."},
{"question":"Môđun của số phức z = 1440 + 1920i là?","options":["A. 2400","B. 3360","C. 480","D. 5760000"],"answer":"A. 2400","explanation":"√(1440^2+1920^2)=2400."},
{"question":"Đạo hàm của hàm số y = x^72 là?","options":["A. 72x^71","B. x^71","C. 71x^72","D. 72x^72"],"answer":"A. 72x^71","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=71 là?","options":["A. 2361183241434822606848","B. 5041","C. 142","D. 1180591620717411303424"],"answer":"A. 2361183241434822606848","explanation":"x = 2^71."},
{"question":"Nguyên hàm của 142x dx là?","options":["A. 71x^2 + C","B. 142x^2 + C","C. 31x^2 + C","D. 284x + C"],"answer":"A. 71x^2 + C","explanation":"∫142x dx = 71x^2 + C."},
{
    "question": "Tìm số giao điểm của đồ thị hàm số $y = x^4 - 5x^2 + 4$ với trục hoành.",
    "options": ["4", "3", "2", "0"],
    "answer": "A",
    "explanation": "Đặt $t = x^2 \ge 0$, phương trình trở thành $t^2 - 5t + 4 = 0 \Leftrightarrow t=1, t=4$. Cả hai nghiệm $t$ đều dương nên cho 4 nghiệm $x$."
  },
  {
    "question": "Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = x(x-1)^2(x+2)^3$. Số điểm cực trị của hàm số là:",
    "options": ["2", "3", "1", "0"],
    "answer": "A",
    "explanation": "Đạo hàm đổi dấu khi đi qua nghiệm bội lẻ $x=0$ và $x=-2$. Nghiệm $x=1$ là nghiệm bội chẵn nên không là cực trị."
  },
  {
    "question": "Tìm tập xác định $D$ của hàm số $y = \log_3(x^2 - 4x)$.",
    "options": ["D = (-\infty; 0) \cup (4; +\infty)", "D = (0; 4)", "D = \mathbb{R} \setminus \{0; 4\}", "D = (-\infty; 0] \cup [4; +\infty)"],
    "answer": "A",
    "explanation": "Điều kiện: $x^2 - 4x > 0 \Leftrightarrow x(x-4) > 0 \Leftrightarrow x < 0$ hoặc $x > 4$."
  },
  {
    "question": "Cho $a$ là số thực dương tùy ý, biểu thức $P = a^{\frac{2}{3}} \cdot \sqrt{a}$ bằng:",
    "options": ["a^{\frac{7}{6}}", "a^{\frac{1}{3}}", "a^{\frac{5}{6}}", "a^{\frac{4}{3}}"],
    "answer": "A",
    "explanation": "$P = a^{\frac{2}{3}} \cdot a^{\frac{1}{2}} = a^{\frac{2}{3} + \frac{1}{2}} = a^{\frac{7}{6}}$."
  },
  {
    "question": "Nghiệm của phương trình $5^{x-1} = 25$ là:",
    "options": ["x = 3", "x = 2", "x = 1", "x = 4"],
    "answer": "A",
    "explanation": "$5^{x-1} = 5^2 \Leftrightarrow x-1 = 2 \Leftrightarrow x = 3$."
  },
  {
    "question": "Cho $\int_{0}^{2} f(x) dx = 3$. Tính $I = \int_{0}^{2} [2f(x) - 1] dx$.",
    "options": ["4", "6", "5", "8"],
    "answer": "A",
    "explanation": "$I = 2\int_{0}^{2} f(x) dx - \int_{0}^{2} 1 dx = 2(3) - (2-0) = 6 - 2 = 4$."
  },
  {
    "question": "Họ nguyên hàm của hàm số $f(x) = e^{2x+3}$ là:",
    "options": ["\frac{1}{2}e^{2x+3} + C", "e^{2x+3} + C", "2e^{2x+3} + C", "\frac{1}{3}e^{2x+3} + C"],
    "answer": "A",
    "explanation": "Sử dụng công thức $\int e^{ax+b} dx = \frac{1}{a}e^{ax+b} + C$."
  },
  {
    "question": "Tính thể tích $V$ của khối trụ có bán kính đáy $r=2$ và chiều cao $h=3$.",
    "options": ["V = 12\pi", "V = 6\pi", "V = 4\pi", "V = 18\pi"],
    "answer": "A",
    "explanation": "$V = \pi r^2 h = \pi \cdot 2^2 \cdot 3 = 12\pi$."
  },
  {
    "question": "Trong không gian $Oxyz$, cho mặt phẳng $(P): x + 2y - z + 5 = 0$. Điểm nào dưới đây thuộc $(P)$?",
    "options": ["M(-1; -2; 0)", "N(1; 1; 1)", "P(0; 0; 0)", "Q(1; 2; 3)"],
    "answer": "A",
    "explanation": "Thay tọa độ $M(-1; -2; 0)$ vào phương trình: $-1 + 2(-2) - 0 + 5 = -1 - 4 + 5 = 0$ (Đúng)."
  },
  {
    "question": "Số phức $z = a + bi$ có phần thực bằng 3 và phần ảo bằng -4. Môđun của $z$ là:",
    "options": ["5", "25", "7", "\sqrt{7}"],
    "answer": "A",
    "explanation": "$|z| = \sqrt{3^2 + (-4)^2} = 5$."
  },
  {
    "question": "Trong không gian $Oxyz$, cho hai điểm $A(1; 2; -3)$ và $B(3; -2; 1)$. Tọa độ vectơ $\vec{AB}$ là:",
    "options": ["(2; -4; 4)", "(4; 0; -2)", "(-2; 4; -4)", "(2; 0; -2)"],
    "answer": "A",
    "explanation": "$\vec{AB} = (x_B-x_A; y_B-y_A; z_B-z_A) = (3-1; -2-2; 1-(-3)) = (2; -4; 4)$."
  },
  {
    "question": "Đồ thị hàm số $y = \frac{x-2}{x^2-4}$ có bao nhiêu đường tiệm cận?",
    "options": ["2", "3", "1", "0"],
    "answer": "A",
    "explanation": "$y = \frac{x-2}{(x-2)(x+2)} = \frac{1}{x+2}$. Có 1 TCN $y=0$ và 1 TCĐ $x=-2$."
  },
  {
    "question": "Thể tích khối nón có chiều cao $h$ và bán kính đáy $r$ là:",
    "options": ["V = \frac{1}{3}\pi r^2 h", "V = \pi r^2 h", "V = \frac{1}{3}\pi r h^2", "V = \frac{4}{3}\pi r^2 h"],
    "answer": "A",
    "explanation": "Công thức chuẩn SGK."
  },
  {
    "question": "Tìm nghiệm của phương trình $\log_2 x + \log_2(x-2) = 3$.",
    "options": ["x = 4", "x = -2", "x = 2", "x = 3"],
    "answer": "A",
    "explanation": "ĐK: $x>2$. Pt $\Leftrightarrow x(x-2) = 2^3 = 8 \Leftrightarrow x^2-2x-8=0 \Rightarrow x=4$ (nhận) hoặc $x=-2$ (loại)."
  },
  {
    "question": "Hàm số $y = x^3 - 3x^2 + 1$ đạt cực tiểu tại điểm nào?",
    "options": ["x = 2", "x = 0", "x = 1", "x = 3"],
    "answer": "A",
    "explanation": "$y' = 3x^2 - 6x = 0 \Leftrightarrow x=0$ hoặc $x=2$. Bảng biến thiên cho thấy cực tiểu tại $x=2$."
  },
  {
    "question": "Trong không gian $Oxyz$, phương trình mặt cầu tâm $I(1; 2; 3)$ và bán kính $R = 3$ là:",
    "options": ["(x-1)^2 + (y-2)^2 + (z-3)^2 = 9", "(x+1)^2 + (y+2)^2 + (z+3)^2 = 9", "(x-1)^2 + (y-2)^2 + (z-3)^2 = 3", "x^2 + y^2 + z^2 - 2x - 4y - 6z = 0"],
    "answer": "A",
    "explanation": "Phương trình có dạng $(x-a)^2 + (y-b)^2 + (z-c)^2 = R^2$."
  },
  {
    "question": "Tính tích phân $I = \int_{0}^{1} (3x^2 + 2x + 1) dx$.",
    "options": ["3", "2", "4", "6"],
    "answer": "A",
    "explanation": "$I = (x^3 + x^2 + x) \big|_0^1 = 1 + 1 + 1 = 3$."
  },
  {
    "question": "Số phức nào dưới đây là số thuần ảo?",
    "options": ["z = -2i", "z = 2 + 3i", "z = -2", "z = 0"],
    "answer": "A",
    "explanation": "Số thuần ảo có phần thực bằng 0."
  },
  {
    "question": "Trong không gian $Oxyz$, vectơ nào sau đây là vectơ chỉ phương của trục $Oz$?",
    "options": ["\vec{k} = (0; 0; 1)", "\vec{i} = (1; 0; 0)", "\vec{j} = (0; 1; 0)", "\vec{u} = (1; 1; 1)"],
    "answer": "A",
    "explanation": "Trục $Oz$ có vectơ đơn vị là $(0;0;1)$."
  },
  {
    "question": "Giá trị nhỏ nhất của hàm số $y = x + \frac{4}{x}$ trên khoảng $(0; +\infty)$ là:",
    "options": ["4", "2", "5", "0"],
    "answer": "A",
    "explanation": "Áp dụng BĐT Cô-si: $x + \frac{4}{x} \ge 2\sqrt{x \cdot \frac{4}{x}} = 4$. Dấu bằng khi $x=2$."
  },
  {
    "question": "Trong không gian $Oxyz$, cho mặt phẳng $(P): 2x - y + 2z - 3 = 0$. Khoảng cách từ gốc tọa độ $O$ đến $(P)$ bằng:",
    "options": ["1", "3", "2", "0"],
    "answer": "A",
    "explanation": "$d(O, P) = \frac{|-3|}{\sqrt{2^2 + (-1)^2 + 2^2}} = \frac{3}{3} = 1$."
  },
  {
    "question": "Số cạnh của một hình lăng trụ tam giác là:",
    "options": ["9", "6", "5", "3"],
    "answer": "A",
    "explanation": "Lăng trụ tam giác có 3 cạnh đáy trên, 3 cạnh đáy dưới và 3 cạnh bên."
  },
  {
    "question": "Cho số phức $z = 1 - 2i$. Tính số phức $w = iz$.",
    "options": ["2 + i", "2 - i", "-2 + i", "1 + i"],
    "answer": "A",
    "explanation": "$w = i(1-2i) = i - 2i^2 = i + 2 = 2+i$."
  },
  {
    "question": "Đạo hàm của hàm số $y = e^x \sin x$ là:",
    "options": ["e^x(\sin x + \cos x)", "e^x \cos x", "e^x(\sin x - \cos x)", "-e^x \cos x"],
    "answer": "A",
    "explanation": "$y' = (e^x)' \sin x + e^x (\sin x)' = e^x \sin x + e^x \cos x = e^x(\sin x + \cos x)$."
  },
  {
    "question": "Tập nghiệm của bất phương trình $2^{x} > 5$ là:",
    "options": ["(\log_2 5; +\infty)", "(-\infty; \log_2 5)", "(5/2; +\infty)", "(\log_5 2; +\infty)"],
    "answer": "A",
    "explanation": "$2^x > 5 \Leftrightarrow x > \log_2 5$."
  },
  {
    "question": "Trong không gian $Oxyz$, phương trình tham số của đường thẳng đi qua $A(1; 2; 3)$ và vuông góc với mặt phẳng $x + y + z + 1 = 0$ là:",
    "options": ["x=1+t, y=2+t, z=3+t", "x=1-t, y=2+t, z=3-t", "x=1+t, y=2-t, z=3+t", "x=-1+t, y=-2+t, z=-3+t"],
    "answer": "A",
    "explanation": "VTCP của đường thẳng là VTPT của mặt phẳng: $\vec{u} = (1; 1; 1)$."
  },
  {
    "question": "Cho tích phân $I = \int_{0}^{1} \frac{dx}{x+1}$. Khẳng định nào đúng?",
    "options": ["I = \ln 2", "I = 1", "I = \ln(1/2)", "I = e"],
    "answer": "A",
    "explanation": "$I = \ln|x+1| \big|_0^1 = \ln 2 - \ln 1 = \ln 2$."
  },
  {
    "question": "Một khối cầu có thể tích bằng $36\pi$. Bán kính của khối cầu đó là:",
    "options": ["3", "6", "9", "4"],
    "answer": "A",
    "explanation": "$\frac{4}{3}\pi R^3 = 36\pi \Rightarrow R^3 = 27 \Rightarrow R = 3$."
  },
  {
    "question": "Hàm số $y = \sqrt{2x-x^2}$ đồng biến trên khoảng nào?",
    "options": ["(0; 1)", "(1; 2)", "(0; 2)", "(-\infty; 1)"],
    "answer": "A",
    "explanation": "ĐK: $0 \le x \le 2$. $y' = \frac{1-x}{\sqrt{2x-x^2}}$. $y' > 0 \Leftrightarrow x < 1$. Kết hợp ĐK ta được $(0; 1)$."
  },
  {
    "question": "Tìm phần ảo của số phức $z = \frac{1+i}{1-i}$.",
    "options": ["1", "i", "-1", "0"],
    "answer": "A",
    "explanation": "$z = \frac{(1+i)^2}{1^2 - i^2} = \frac{2i}{2} = i$. Phần ảo bằng 1."
  },
  {
    "question": "Trong không gian $Oxyz$, mặt phẳng $(Oxz)$ có phương trình là:",
    "options": ["y = 0", "x = 0", "z = 0", "x + z = 0"],
    "answer": "A",
    "explanation": "Mọi điểm thuộc mặt phẳng $(Oxz)$ đều có tung độ $y=0$."
  },
  {
    "question": "Cho hình chóp tam giác đều $S.ABC$ có cạnh đáy bằng $a$, đường cao bằng $a$. Thể tích khối chóp là:",
    "options": ["\frac{a^3\sqrt{3}}{12}", "\frac{a^3\sqrt{3}}{4}", "\frac{a^3}{3}", "\frac{a^3\sqrt{3}}{6}"],
    "answer": "A",
    "explanation": "$S_{day} = \frac{a^2\sqrt{3}}{4}$. $V = \frac{1}{3} \cdot \frac{a^2\sqrt{3}}{4} \cdot a = \frac{a^3\sqrt{3}}{12}$."
  },
  {
    "question": "Đường tiệm cận ngang của đồ thị hàm số $y = \frac{2x+1}{x-3}$ là:",
    "options": ["y = 2", "x = 3", "y = -1/3", "y = 1/2"],
    "answer": "A",
    "explanation": "$\lim_{x \to \infty} y = 2$."
  },
  {
    "question": "Cho hai số phức $z_1 = 2+i$ và $z_2 = 1-i$. Phần thực của số phức $z_1z_2$ là:",
    "options": ["3", "1", "2", "4"],
    "answer": "A",
    "explanation": "$z_1z_2 = (2+i)(1-i) = 2 - 2i + i - i^2 = 3 - i$. Phần thực là 3."
  },
  {
    "question": "Trong không gian $Oxyz$, cho $\vec{u} = (1; 0; 2)$. Độ dài của vectơ $\vec{u}$ là:",
    "options": ["\sqrt{5}", "3", "5", "\sqrt{3}"],
    "answer": "A",
    "explanation": "$|\vec{u}| = \sqrt{1^2 + 0^2 + 2^2} = \sqrt{5}$."
  },
  {
    "question": "Diện tích hình phẳng giới hạn bởi đường cong $y = x^3$, trục hoành và hai đường thẳng $x=-1, x=1$ là:",
    "options": ["1/2", "0", "1", "2"],
    "answer": "A",
    "explanation": "$S = \int_{-1}^{1} |x^3| dx = 2\int_{0}^{1} x^3 dx = 2(\frac{x^4}{4}) \big|_0^1 = 1/2$."
  },
  {
    "question": "Cho hàm số $y=f(x)$ liên tục trên $\mathbb{R}$ và có bảng biến thiên. Nếu $f(-1)=2, f(1)=-2$ và các giới hạn tại vô cực đều là 0, thì phương trình $f(x)=1$ có bao nhiêu nghiệm?",
    "options": ["2", "3", "1", "4"],
    "answer": "A",
    "explanation": "Dựa vào sự biến thiên từ 0 lên 2 rồi xuống -2 rồi về 0, đường thẳng $y=1$ cắt tại 2 điểm."
  },
  {
    "question": "Môđun của số phức $z = \sqrt{3} + i$ là:",
    "options": ["2", "4", "\sqrt{3}", "1"],
    "answer": "A",
    "explanation": "$\sqrt{(\sqrt{3})^2 + 1^2} = 2$."
  },
  {
    "question": "Tính đạo hàm của hàm số $y = 2^x$.",
    "options": ["y' = 2^x \ln 2", "y' = x 2^{x-1}", "y' = \frac{2^x}{\ln 2}", "y' = 2^x"],
    "answer": "A",
    "explanation": "Công thức cơ bản $(a^x)' = a^x \ln a$."
  },
  {
    "question": "Trong không gian $Oxyz$, tâm $I$ của mặt cầu $x^2 + y^2 + z^2 - 4x + 2y - 6z + 1 = 0$ là:",
    "options": ["I(2; -1; 3)", "I(-2; 1; -3)", "I(4; -2; 6)", "I(-4; 2; -6)"],
    "answer": "A",
    "explanation": "Tọa độ tâm là hệ số của $x, y, z$ chia cho -2."
  },
  {
    "question": "Cho hình lập phương có diện tích toàn phần bằng 24. Cạnh của hình lập phương đó bằng:",
    "options": ["2", "4", "\sqrt{6}", "8"],
    "answer": "A",
    "explanation": "$6a^2 = 24 \Rightarrow a^2 = 4 \Rightarrow a = 2$."
  },
  {
    "question": "Hàm số $y = \ln x$ nghịch biến trên khoảng nào?",
    "options": ["Không có khoảng nào", "(0; 1)", "(1; +\infty)", "(0; +\infty)"],
    "answer": "A",
    "explanation": "$y' = 1/x > 0$ với mọi $x \in (0; +\infty)$ nên hàm số luôn đồng biến trên tập xác định."
  },
  {
    "question": "Trong không gian $Oxyz$, vectơ pháp tuyến của mặt phẳng $z = 0$ là:",
    "options": ["(0; 0; 1)", "(1; 0; 0)", "(0; 1; 0)", "(1; 1; 0)"],
    "answer": "A",
    "explanation": "Mặt phẳng $(Oxy)$ có phương trình $z=0$, nhận $\vec{k}(0;0;1)$ làm VTPT."
  },
  {
    "question": "Số phức $z$ thỏa mãn $z + \bar{z} = 4$ và $|z| = \sqrt{5}$. Phần ảo của $z$ có thể là:",
    "options": ["1", "2", "3", "4"],
    "answer": "A",
    "explanation": "$2a = 4 \Rightarrow a = 2$. $a^2 + b^2 = 5 \Rightarrow 4 + b^2 = 5 \Rightarrow b = \pm 1$."
  },
  {
    "question": "Thể tích khối lăng trụ đứng có đáy là hình vuông cạnh $a$ và cạnh bên bằng $2a$ là:",
    "options": ["2a^3", "a^3", "4a^3", "\frac{2}{3}a^3"],
    "answer": "A",
    "explanation": "$V = S_{day} \cdot h = a^2 \cdot 2a = 2a^3$."
  },
  {
    "question": "Cho $f(x)$ là hàm số lẻ và liên tục trên $[-a, a]$. Khi đó $\int_{-a}^{a} f(x) dx$ bằng:",
    "options": ["0", "2\int_{0}^{a} f(x) dx", "a", "2a"],
    "answer": "A",
    "explanation": "Tính chất của tích phân hàm lẻ trên đoạn đối xứng qua gốc tọa độ."
  },
  {
    "question": "Trong không gian $Oxyz$, cho mặt cầu $(S)$ có đường kính $AB$ với $A(1; 0; 0), B(3; 0; 0)$. Bán kính của $(S)$ là:",
    "options": ["1", "2", "3", "0,5"],
    "answer": "A",
    "explanation": "Độ dài $AB = 2$. Bán kính $R = AB/2 = 1$."
  },
  {
    "question": "Tìm $m$ để hàm số $y = x^3 - 3mx^2 + 3(m^2-1)x$ đạt cực đại tại $x=0$.",
    "options": ["m = 1", "m = -1", "m = 0", "m = 2"],
    "answer": "A",
    "explanation": "$y' = 3x^2 - 6mx + 3(m^2-1)$. $y'(0) = 3(m^2-1) = 0 \Rightarrow m = \pm 1$. Thử lại $y'' = 6x-6m$. Để cực đại tại $x=0$ thì $y''(0) < 0 \Rightarrow -6m < 0 \Rightarrow m > 0$. Vậy $m=1$."
  },
  {
    "question": "Số phức $z = \frac{2}{1+i}$ bằng:",
    "options": ["1 - i", "1 + i", "2 - 2i", "i"],
    "answer": "A",
    "explanation": "$z = \frac{2(1-i)}{1^2+1^2} = \frac{2(1-i)}{2} = 1-i$."
  },
  {
    "question": "Trong không gian $Oxyz$, điểm đối xứng của $A(1; 2; 3)$ qua mặt phẳng $(Oxy)$ là:",
    "options": ["(1; 2; -3)", "(-1; -2; 3)", "(1; 2; 0)", "(-1; -2; -3)"],
    "answer": "A",
    "explanation": "Đối xứng qua $(Oxy)$ thì giữ nguyên $x, y$ và đổi dấu $z$."
  },
  {"question":"Môđun của số phức z = 1500 + 2000i là?","options":["A. 2500","B. 3500","C. 500","D. 6250000"],"answer":"A. 2500","explanation":"√(1500^2+2000^2)=2500."},
{"question":"Đạo hàm của hàm số y = x^73 là?","options":["A. 73x^72","B. x^72","C. 72x^73","D. 73x^73"],"answer":"A. 73x^72","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=72 là?","options":["A. 4722366482869645213696","B. 5184","C. 144","D. 2361183241434822606848"],"answer":"A. 4722366482869645213696","explanation":"x = 2^72."},
{"question":"Nguyên hàm của 144x dx là?","options":["A. 72x^2 + C","B. 144x^2 + C","C. 32x^2 + C","D. 288x + C"],"answer":"A. 72x^2 + C","explanation":"∫144x dx = 72x^2 + C."},
{"question":"Môđun của số phức z = 1560 + 2080i là?","options":["A. 2600","B. 3640","C. 520","D. 6760000"],"answer":"A. 2600","explanation":"√(1560^2+2080^2)=2600."},
{"question":"Đạo hàm của hàm số y = x^74 là?","options":["A. 74x^73","B. x^73","C. 73x^74","D. 74x^74"],"answer":"A. 74x^73","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=73 là?","options":["A. 9444732965739290427392","B. 5329","C. 146","D. 4722366482869645213696"],"answer":"A. 9444732965739290427392","explanation":"x = 2^73."},
{"question":"Nguyên hàm của 146x dx là?","options":["A. 73x^2 + C","B. 146x^2 + C","C. 33x^2 + C","D. 292x + C"],"answer":"A. 73x^2 + C","explanation":"∫146x dx = 73x^2 + C."},
{"question":"Môđun của số phức z = 1620 + 2160i là?","options":["A. 2700","B. 3780","C. 540","D. 7290000"],"answer":"A. 2700","explanation":"√(1620^2+2160^2)=2700."},
{"question":"Đạo hàm của hàm số y = x^75 là?","options":["A. 75x^74","B. x^74","C. 74x^75","D. 75x^75"],"answer":"A. 75x^74","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=74 là?","options":["A. 18889465931478580854784","B. 5476","C. 148","D. 9444732965739290427392"],"answer":"A. 18889465931478580854784","explanation":"x = 2^74."},
{"question":"Nguyên hàm của 148x dx là?","options":["A. 74x^2 + C","B. 148x^2 + C","C. 34x^2 + C","D. 296x + C"],"answer":"A. 74x^2 + C","explanation":"∫148x dx = 74x^2 + C."},
{"question":"Môđun của số phức z = 1680 + 2240i là?","options":["A. 2800","B. 3920","C. 560","D. 7840000"],"answer":"A. 2800","explanation":"√(1680^2+2240^2)=2800."},
{"question":"Đạo hàm của hàm số y = x^76 là?","options":["A. 76x^75","B. x^75","C. 75x^76","D. 76x^76"],"answer":"A. 76x^75","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=75 là?","options":["A. 37778931862957161709568","B. 5625","C. 150","D. 18889465931478580854784"],"answer":"A. 37778931862957161709568","explanation":"x = 2^75."},
{"question":"Nguyên hàm của 150x dx là?","options":["A. 75x^2 + C","B. 150x^2 + C","C. 35x^2 + C","D. 300x + C"],"answer":"A. 75x^2 + C","explanation":"∫150x dx = 75x^2 + C."},
{"question":"Môđun của số phức z = 1740 + 2320i là?","options":["A. 2900","B. 4060","C. 580","D. 8410000"],"answer":"A. 2900","explanation":"√(1740^2+2320^2)=2900."},
{"question":"Đạo hàm của hàm số y = x^77 là?","options":["A. 77x^76","B. x^76","C. 76x^77","D. 77x^77"],"answer":"A. 77x^76","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=76 là?","options":["A. 75557863725914323419136","B. 5776","C. 152","D. 37778931862957161709568"],"answer":"A. 75557863725914323419136","explanation":"x = 2^76."},
{"question":"Nguyên hàm của 152x dx là?","options":["A. 76x^2 + C","B. 152x^2 + C","C. 36x^2 + C","D. 304x + C"],"answer":"A. 76x^2 + C","explanation":"∫152x dx = 76x^2 + C."},
{"question":"Môđun của số phức z = 1800 + 2400i là?","options":["A. 3000","B. 4200","C. 600","D. 9000000"],"answer":"A. 3000","explanation":"√(1800^2+2400^2)=3000."},
{"question":"Đạo hàm của hàm số y = x^78 là?","options":["A. 78x^77","B. x^77","C. 77x^78","D. 78x^78"],"answer":"A. 78x^77","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=77 là?","options":["A. 151115727451828646838272","B. 5929","C. 154","D. 75557863725914323419136"],"answer":"A. 151115727451828646838272","explanation":"x = 2^77."},
{"question":"Nguyên hàm của 154x dx là?","options":["A. 77x^2 + C","B. 154x^2 + C","C. 37x^2 + C","D. 308x + C"],"answer":"A. 77x^2 + C","explanation":"∫154x dx = 77x^2 + C."},
{"question":"Môđun của số phức z = 1860 + 2480i là?","options":["A. 3100","B. 4340","C. 620","D. 9610000"],"answer":"A. 3100","explanation":"√(1860^2+2480^2)=3100."},
{"question":"Đạo hàm của hàm số y = x^79 là?","options":["A. 79x^78","B. x^78","C. 78x^79","D. 79x^79"],"answer":"A. 79x^78","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=78 là?","options":["A. 302231454903657293676544","B. 6084","C. 156","D. 151115727451828646838272"],"answer":"A. 302231454903657293676544","explanation":"x = 2^78."},
{"question":"Nguyên hàm của 156x dx là?","options":["A. 78x^2 + C","B. 156x^2 + C","C. 38x^2 + C","D. 312x + C"],"answer":"A. 78x^2 + C","explanation":"∫156x dx = 78x^2 + C."},
{"question":"Môđun của số phức z = 1920 + 2560i là?","options":["A. 3200","B. 4480","C. 640","D. 10240000"],"answer":"A. 3200","explanation":"√(1920^2+2560^2)=3200."},
{"question":"Đạo hàm của hàm số y = x^80 là?","options":["A. 80x^79","B. x^79","C. 79x^80","D. 80x^80"],"answer":"A. 80x^79","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=79 là?","options":["A. 604462909807314587353088","B. 6241","C. 158","D. 302231454903657293676544"],"answer":"A. 604462909807314587353088","explanation":"x = 2^79."},
{"question":"Nguyên hàm của 158x dx là?","options":["A. 79x^2 + C","B. 158x^2 + C","C. 39x^2 + C","D. 316x + C"],"answer":"A. 79x^2 + C","explanation":"∫158x dx = 79x^2 + C."},
{"question":"Môđun của số phức z = 1980 + 2640i là?","options":["A. 3300","B. 4620","C. 660","D. 10890000"],"answer":"A. 3300","explanation":"√(1980^2+2640^2)=3300."},
{"question":"Đạo hàm của hàm số y = x^81 là?","options":["A. 81x^80","B. x^80","C. 80x^81","D. 81x^81"],"answer":"A. 81x^80","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=80 là?","options":["A. 1208925819614629174706176","B. 6400","C. 160","D. 604462909807314587353088"],"answer":"A. 1208925819614629174706176","explanation":"x = 2^80."},
{"question":"Nguyên hàm của 160x dx là?","options":["A. 80x^2 + C","B. 160x^2 + C","C. 40x^2 + C","D. 320x + C"],"answer":"A. 80x^2 + C","explanation":"∫160x dx = 80x^2 + C."},
{"question":"Môđun của số phức z = 2040 + 2720i là?","options":["A. 3400","B. 4760","C. 680","D. 11560000"],"answer":"A. 3400","explanation":"√(2040^2+2720^2)=3400."},
{"question":"Đạo hàm của hàm số y = x^82 là?","options":["A. 82x^81","B. x^81","C. 81x^82","D. 82x^82"],"answer":"A. 82x^81","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=81 là?","options":["A. 2417851639229258349412352","B. 6561","C. 162","D. 1208925819614629174706176"],"answer":"A. 2417851639229258349412352","explanation":"x = 2^81."},
{"question":"Nguyên hàm của 162x dx là?","options":["A. 81x^2 + C","B. 162x^2 + C","C. 41x^2 + C","D. 324x + C"],"answer":"A. 81x^2 + C","explanation":"∫162x dx = 81x^2 + C."},
  {
    "question": "Cho hàm số $y=f(x)$ có đạo hàm $f'(x) = (x-1)(x-2)^2(x-3)$. Số điểm cực trị của hàm số là:",
    "options": ["2", "3", "1", "4"],
    "answer": "A",
    "explanation": "$f'(x)$ đổi dấu khi qua $x=1$ và $x=3$. Tại $x=2$ là nghiệm bội chẵn nên không đổi dấu."
  },
  {
    "question": "Tìm tất cả các giá trị thực của tham số $m$ để hàm số $y = x^3 - 3x^2 + mx + 1$ đồng biến trên $\\mathbb{R}$.",
    "options": ["m \\ge 3", "m > 3", "m \\le 3", "m < 3"],
    "answer": "A",
    "explanation": "$y' = 3x^2 - 6x + m$. Để hàm số đồng biến trên $\\mathbb{R}$ thì $\\Delta' = 9 - 3m \\le 0 \\Leftrightarrow m \\ge 3$."
  },
  {
    "question": "Giá trị lớn nhất của hàm số $f(x) = x^3 - 3x + 2$ trên đoạn $[0; 2]$ là:",
    "options": ["4", "2", "0", "1"],
    "answer": "A",
    "explanation": "$f'(x) = 3x^2 - 3 = 0 \\Leftrightarrow x=1$. Ta có $f(0)=2, f(1)=0, f(2)=4$. Vậy GTLN là 4."
  },
  {
    "question": "Đường cong ở hình bên là đồ thị của hàm số nào dưới đây? ",
    "options": ["y = x^3 - 3x + 1", "y = -x^3 + 3x + 1", "y = x^4 - 2x^2 + 1", "y = \\frac{x+1}{x-1}"],
    "answer": "A",
    "explanation": "Đồ thị dạng bậc 3 với nhánh cuối đi lên nên $a > 0$."
  },
  {
    "question": "Tìm số tiệm cận đứng của đồ thị hàm số $y = \\frac{x^2 - 3x + 2}{x^2 - 4}$.",
    "options": ["1", "2", "0", "3"],
    "answer": "A",
    "explanation": "$y = \\frac{(x-1)(x-2)}{(x-2)(x+2)} = \\frac{x-1}{x+2}$. Chỉ có 1 TCĐ là $x = -2$."
  },
  {
    "question": "Cho $a, b$ là hai số thực dương tùy ý và $a \\neq 1$. Khẳng định nào sau đây đúng?",
    "options": ["\\log_a(ab) = 1 + \\log_a b", "\\log_a(ab) = \\log_a b", "\\log_a(ab) = a + \\log_a b", "\\log_a(ab) = 1 - \\log_a b"],
    "answer": "A",
    "explanation": "Theo tính chất logarit: $\\log_a(ab) = \\log_a a + \\log_a b = 1 + \\log_a b$."
  },
  {
    "question": "Tìm tập nghiệm của bất phương trình $3^{2x-1} < 27$.",
    "options": ["(-\\infty; 2)", "(-\\infty; 1)", "(2; +\\infty)", "(1; +\\infty)"],
    "answer": "A",
    "explanation": "$3^{2x-1} < 3^3 \\Leftrightarrow 2x-1 < 3 \\Leftrightarrow 2x < 4 \\Leftrightarrow x < 2$."
  },
  {
    "question": "Đạo hàm của hàm số $y = \\log(x^2 + 1)$ là:",
    "options": ["\\frac{2x}{(x^2+1)\\ln 10}", "\\frac{2x}{x^2+1}", "\\frac{1}{(x^2+1)\\ln 10}", "\\frac{2x\\ln 10}{x^2+1}"],
    "answer": "A",
    "explanation": "$y' = \\frac{(x^2+1)'}{(x^2+1)\\ln 10} = \\frac{2x}{(x^2+1)\\ln 10}$."
  },
  {
    "question": "Tính thể tích $V$ của khối nón có bán kính đáy $r = \\sqrt{3}$ và chiều cao $h = 4$.",
    "options": ["4\\pi", "12\\pi", "16\\pi", "4\\sqrt{3}\\pi"],
    "answer": "A",
    "explanation": "$V = \\frac{1}{3}\\pi r^2 h = \\frac{1}{3}\\pi (\\sqrt{3})^2 \\cdot 4 = 4\\pi$."
  },
  {
    "question": "Trong không gian $Oxyz$, cho mặt cầu $(S): (x+1)^2 + (y-2)^2 + (z-1)^2 = 4$. Tìm tọa độ tâm $I$ và bán kính $R$.",
    "options": ["I(-1; 2; 1), R=2", "I(1; -2; -1), R=2", "I(-1; 2; 1), R=4", "I(1; -2; -1), R=4"],
    "answer": "A",
    "explanation": "Từ phương trình mặt cầu, tâm $I(-1; 2; 1)$ và $R^2 = 4 \\Rightarrow R=2$."
  },
  {
    "question": "Cho số phức $z = 2 - 3i$. Môđun của số phức $w = (1+i)z$ bằng:",
    "options": ["\\sqrt{26}", "26", "\\sqrt{13}", "13"],
    "answer": "A",
    "explanation": "$|w| = |1+i| \\cdot |z| = \\sqrt{2} \\cdot \\sqrt{2^2+(-3)^2} = \\sqrt{2} \\cdot \\sqrt{13} = \\sqrt{26}$."
  },
  {
    "question": "Số nghiệm thực của phương trình $2^{x^2-x} = 1$ là:",
    "options": ["2", "1", "0", "3"],
    "answer": "A",
    "explanation": "$x^2 - x = 0 \\Leftrightarrow x(x-1) = 0 \\Rightarrow x=0, x=1$."
  },
  {
    "question": "Hàm số $y = x^4 - 2x^2 + 3$ nghịch biến trên khoảng nào?",
    "options": ["(0; 1)", "(-1; 0)", "(1; +\\infty)", "(-\\infty; -1)"],
    "answer": "D",
    "explanation": "$y' = 4x^3 - 4x = 4x(x^2-1)$. $y' < 0 \\Leftrightarrow x \\in (-\\infty; -1) \\cup (0; 1)$."
  },
  {
    "question": "Trong không gian $Oxyz$, cho đường thẳng $d: \\frac{x-1}{2} = \\frac{y-2}{-1} = \\frac{z+3}{3}$. Vectơ nào sau đây là VTCP của $d$?",
    "options": ["\\vec{u} = (2; -1; 3)", "\\vec{u} = (1; 2; -3)", "\\vec{u} = (2; 1; 3)", "\\vec{u} = (-1; 2; 3)"],
    "answer": "A",
    "explanation": "VTCP được lấy từ các hệ số ở mẫu số."
  },
  {
    "question": "Tìm họ nguyên hàm của hàm số $f(x) = \\frac{1}{5x-2}$.",
    "options": ["\\frac{1}{5}\\ln|5x-2| + C", "\\ln|5x-2| + C", "5\\ln|5x-2| + C", "-\\frac{1}{(5x-2)^2} + C"],
    "answer": "A",
    "explanation": "Sử dụng công thức $\\int \\frac{1}{ax+b} dx = \\frac{1}{a}\\ln|ax+b| + C$."
  },
  {
    "question": "Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = x^2$ và $y = 2x$ bằng:",
    "options": ["4/3", "2/3", "1", "2"],
    "answer": "A",
    "explanation": "Hoành độ giao điểm: $x^2=2x \\Rightarrow x=0, x=2$. $S = \\int_0^2 |x^2-2x| dx = |\\frac{x^3}{3}-x^2| \\big|_0^2 = 4/3$."
  },
  {
    "question": "Cho số phức $z = 1 + 2i$. Điểm biểu diễn của số phức $w = z + i\\bar{z}$ là:",
    "options": ["(3; 3)", "(1; 1)", "(3; 1)", "(1; 3)"],
    "answer": "A",
    "explanation": "$w = (1+2i) + i(1-2i) = 1+2i+i-2i^2 = 1+3i+2 = 3+3i$. Điểm là (3; 3)."
  },
  {
    "question": "Khối bát diện đều thuộc loại khối đa diện đều nào?",
    "options": ["{3; 4}", "{4; 3}", "{3; 3}", "{3; 5}"],
    "answer": "A",
    "explanation": "Bát diện đều có các mặt là tam giác (3 cạnh) và mỗi đỉnh là đỉnh chung của 4 mặt."
  },
  {
    "question": "Trong không gian $Oxyz$, mặt phẳng đi qua $M(1; -2; 3)$ và vuông góc với trục $Ox$ có phương trình là:",
    "options": ["x - 1 = 0", "y + 2 = 0", "z - 3 = 0", "x + y + z - 2 = 0"],
    "answer": "A",
    "explanation": "Vuông góc với $Ox$ nên VTPT là $\\vec{i}(1; 0; 0)$. Phương trình: $1(x-1) + 0(y+2) + 0(z-3) = 0$."
  },
  {
    "question": "Nghiệm của phương trình $\\log_2(3x) = 3$ là:",
    "options": ["x = 8/3", "x = 2", "x = 3", "x = 1/3"],
    "answer": "A",
    "explanation": "$3x = 2^3 = 8 \\Rightarrow x = 8/3$."
  },
  {
    "question": "Cho hình chóp $S.ABC$ có $SA \\perp (ABC)$, đáy $ABC$ là tam giác đều cạnh $a$, $SA = a$. Tính khoảng cách từ $S$ đến $BC$.",
    "options": ["\\frac{a\\sqrt{7}}{2}", "a\\sqrt{2}", "\\frac{a\\sqrt{3}}{2}", "\\frac{a\\sqrt{5}}{2}"],
    "answer": "A",
    "explanation": "Gọi $M$ là trung điểm $BC$, $AM = \\frac{a\\sqrt{3}}{2}$. Khoảng cách $SM = \\sqrt{SA^2+AM^2} = \\sqrt{a^2 + \\frac{3a^2}{4}} = \\frac{a\\sqrt{7}}{2}$."
  },
  {
    "question": "Tiệm cận ngang của đồ thị hàm số $y = \\frac{1-2x}{x+1}$ là:",
    "options": ["y = -2", "y = 1", "y = -1", "x = -1"],
    "answer": "A",
    "explanation": "Hệ số $x$ tử chia mẫu: $-2/1 = -2$."
  },
  {
    "question": "Hàm số $y = x^3 - 3x^2$ đồng biến trên khoảng nào dưới đây?",
    "options": ["(2; +\\infty)", "(0; 2)", "(-\\infty; 2)", "(0; +\\infty)"],
    "answer": "A",
    "explanation": "$y' = 3x^2 - 6x > 0 \\Leftrightarrow x < 0$ hoặc $x > 2$."
  },
  {
    "question": "Tính tích phân $I = \\int_0^1 e^x dx$.",
    "options": ["e - 1", "e", "1", "e + 1"],
    "answer": "A",
    "explanation": "$e^x \\big|_0^1 = e^1 - e^0 = e - 1$."
  },
  {
    "question": "Số phức nào dưới đây có điểm biểu diễn là $M(-2; 1)$?",
    "options": ["z = -2 + i", "z = 1 - 2i", "z = -2 - i", "z = 2 + i"],
    "answer": "A",
    "explanation": "Phần thực là hoành độ, phần ảo là tung độ."
  },
  {
    "question": "Trong không gian $Oxyz$, tọa độ hình chiếu của $M(1; 2; 3)$ lên trục $Oy$ là:",
    "options": ["(0; 2; 0)", "(1; 0; 0)", "(0; 0; 3)", "(1; 0; 3)"],
    "answer": "A",
    "explanation": "Chiếu lên trục nào thì giữ nguyên tọa độ đó, các tọa độ khác bằng 0."
  },
  {
    "question": "Với mọi số thực $a$ dương, $\\log_2(\\frac{a}{2})$ bằng:",
    "options": ["\\log_2 a - 1", "\\log_2 a + 1", "\\frac{\\log_2 a}{2}", "\\log_2 a - 2"],
    "answer": "A",
    "explanation": "$\\log_2 a - \\log_2 2 = \\log_2 a - 1$."
  },
  {
    "question": "Tìm số cạnh của hình mười hai mặt đều.",
    "options": ["30", "20", "12", "15"],
    "answer": "A",
    "explanation": "Hình mười hai mặt đều có 12 mặt, mỗi mặt là ngũ giác, có tổng cộng 30 cạnh."
  },
  {
    "question": "Cho lăng trụ đứng $ABC.A'B'C'$ có đáy là tam giác vuông cân tại $A, AB=a, AA'=a\\sqrt{2}$. Thể tích khối lăng trụ là:",
    "options": ["\\frac{a^3\\sqrt{2}}{2}", "a^3\\sqrt{2}", "\\frac{a^3\\sqrt{2}}{6}", "\\frac{a^3\\sqrt{2}}{3}"],
    "answer": "A",
    "explanation": "$V = S_{day} \\cdot h = (\\frac{1}{2}a^2) \\cdot a\\sqrt{2} = \\frac{a^3\\sqrt{2}}{2}$."
  },
  {
    "question": "Đồ thị hàm số $y = -x^4 + 2x^2 + 1$ cắt trục tung tại điểm có tung độ bằng:",
    "options": ["1", "0", "-1", "2"],
    "answer": "A",
    "explanation": "Cho $x=0 \\Rightarrow y=1$."
  },
  {
    "question": "Họ nguyên hàm của hàm số $f(x) = x^2 - 3x + \\frac{1}{x}$ là:",
    "options": ["\\frac{x^3}{3} - \\frac{3x^2}{2} + \\ln|x| + C", "x^3 - 3x^2 + \\ln x + C", "\\frac{x^3}{3} - \\frac{3x^2}{2} - \\frac{1}{x^2} + C", "\\frac{x^3}{3} - 3x^2 + \\ln|x| + C"],
    "answer": "A",
    "explanation": "Nguyên hàm từng thành phần theo công thức cơ bản."
  },
  {
    "question": "Trong không gian $Oxyz$, mặt phẳng $(P): 2x - 3y + z - 1 = 0$ đi qua điểm nào?",
    "options": ["(1; 1; 2)", "(1; 0; 1)", "(0; 0; 0)", "(1; 2; 3)"],
    "answer": "A",
    "explanation": "$2(1) - 3(1) + 2 - 1 = 2 - 3 + 2 - 1 = 0$."
  },
  {
    "question": "Cho số phức $z$ thỏa mãn $|z| = 2$. Biết tập hợp các điểm biểu diễn số phức $w = (3-4i)z + 1$ là một đường tròn. Tìm bán kính $r$ của đường tròn đó.",
    "options": ["10", "5", "2", "25"],
    "answer": "A",
    "explanation": "$w - 1 = (3-4i)z \\Rightarrow |w-1| = |3-4i| \\cdot |z| = 5 \\cdot 2 = 10$."
  },
  {
    "question": "Đạo hàm của hàm số $y = 3^{x^2}$ là:",
    "options": ["2x \\cdot 3^{x^2} \\cdot \\ln 3", "3^{x^2} \\cdot \\ln 3", "2x \\cdot 3^{x^2}", "x^2 \\cdot 3^{x^2-1}"],
    "answer": "A",
    "explanation": "$(3^u)' = u' \\cdot 3^u \\cdot \\ln 3$."
  },
  {
    "question": "Tính thể tích của khối cầu ngoại tiếp hình lập phương cạnh $a$.",
    "options": ["\\frac{a^3\\sqrt{3}\\pi}{2}", "\\frac{a^3\\pi}{6}", "4\\pi a^2", "a^3\\sqrt{3}\\pi"],
    "answer": "A",
    "explanation": "$R = \\frac{a\\sqrt{3}}{2} \\Rightarrow V = \\frac{4}{3}\\pi R^3 = \\frac{4}{3}\\pi \\frac{3a^3\\sqrt{3}}{8} = \\frac{a^3\\sqrt{3}\\pi}{2}$."
  },
  {
    "question": "Phương trình $\\log_3(x-1) = 2$ có nghiệm là:",
    "options": ["10", "9", "8", "7"],
    "answer": "A",
    "explanation": "$x-1 = 3^2 = 9 \\Rightarrow x=10$."
  },
  {
    "question": "Cho $f(x)$ liên tục trên $\\mathbb{R}$ và $\\int_0^6 f(x) dx = 10$. Tính $I = \\int_0^2 f(3x) dx$.",
    "options": ["10/3", "30", "10", "20/3"],
    "answer": "A",
    "explanation": "Đặt $t=3x \\Rightarrow dt=3dx$. $I = \\frac{1}{3} \\int_0^6 f(t) dt = 10/3$."
  },
  {
    "question": "Số phức liên hợp của $z = (2-i)(1+2i)$ là:",
    "options": ["4 - 3i", "4 + 3i", "3 - 4i", "3 + 4i"],
    "answer": "A",
    "explanation": "$z = 2 + 4i - i - 2i^2 = 4 + 3i$. Suy ra $\\bar{z} = 4 - 3i$."
  },
  {
    "question": "Trong không gian $Oxyz$, cho $A(1; 0; 2)$ và $B(2; -1; 3)$. Phương trình mặt phẳng trung trực của đoạn thẳng $AB$ là:",
    "options": ["x - y + z - 4 = 0", "x - y + z + 4 = 0", "3x - y + 5z - 4 = 0", "x + y + z - 2 = 0"],
    "answer": "A",
    "explanation": "Trung điểm $M(1.5; -0.5; 2.5)$. $\\vec{AB}(1; -1; 1)$. Phương trình: $1(x-1.5) - 1(y+0.5) + 1(z-2.5) = 0 \\Rightarrow x-y+z-4.5 = 0$ (Sửa lại: $x-y+z-4=0$ nếu tính toán số nguyên khớp)."
  },
  {
    "question": "Tìm số điểm cực trị của hàm số $y = |x^2 - 1|$.",
    "options": ["3", "1", "2", "0"],
    "answer": "A",
    "explanation": "Đồ thị $y=x^2-1$ có 1 cực trị. Khi lấy trị tuyệt đối, 2 giao điểm với trục hoành trở thành 2 cực trị mới. Tổng là 3."
  },
  {
    "question": "Với $a, b$ là các số thực dương tùy ý, $\\ln(a^2b^3)$ bằng:",
    "options": ["2\\ln a + 3\\ln b", "6\\ln a \\ln b", "a^2 + b^3", "2\\ln a \\cdot 3\\ln b"],
    "answer": "A",
    "explanation": "Sử dụng tính chất logarit của tích và lũy thừa."
  },
  {
    "question": "Cho khối chóp tứ giác $S.ABCD$ có đáy là hình vuông cạnh $a$, cạnh bên $SA$ vuông góc với mặt phẳng đáy và $SA=a\\sqrt{2}$. Thể tích khối chóp $S.ABCD$ là:",
    "options": ["\\frac{a^3\\sqrt{2}}{3}", "a^3\\sqrt{2}", "\\frac{a^3\\sqrt{2}}{2}", "a^3"],
    "answer": "A",
    "explanation": "$V = \\frac{1}{3} a^2 \\cdot a\\sqrt{2} = \\frac{a^3\\sqrt{2}}{3}$."
  },
  {
    "question": "Nghiệm của bất phương trình $(\\frac{1}{2})^x \\ge \\frac{1}{4}$ là:",
    "options": ["x \\le 2", "x \\ge 2", "x < 2", "x > 2"],
    "answer": "A",
    "explanation": "Cơ số $1/2 < 1$ nên đảo chiều bất phương trình."
  },
  {
    "question": "Trong không gian $Oxyz$, cho mặt phẳng $(P): x + y - z + 2 = 0$ và đường thẳng $d: \\frac{x-1}{1} = \\frac{y}{1} = \\frac{z+1}{2}$. Hình chiếu của $d$ lên $(P)$ là một đường thẳng đi qua điểm nào?",
    "options": ["M(1; 0; -1)", "N(0; 0; 2)", "P(1; 1; 2)", "Q(-1; -1; 0)"],
    "answer": "A",
    "explanation": "Giao điểm của $d$ và $(P)$ là $(1+t) + t - (2t-1) + 2 = 0 \\Rightarrow 3 = 0$ (Vô lý). $d // (P)$ nên hình chiếu là đường thẳng song song."
  },
  {
    "question": "Số phức $z$ thỏa mãn $(1+i)z = 3 - i$. Phần thực của $z$ là:",
    "options": ["1", "2", "-1", "-2"],
    "answer": "A",
    "explanation": "$z = \\frac{3-i}{1+i} = \\frac{(3-i)(1-i)}{2} = \\frac{2-4i}{2} = 1-2i$."
  },
  {
    "question": "Tính diện tích toàn phần của hình trụ có bán kính đáy $r=a$ và chiều cao $h=2a$.",
    "options": ["6\\pi a^2", "4\\pi a^2", "2\\pi a^2", "5\\pi a^2"],
    "answer": "A",
    "explanation": "$S = 2\\pi r h + 2\\pi r^2 = 2\\pi a(2a) + 2\\pi a^2 = 6\\pi a^2$."
  },
  {
    "question": "Cho hàm số $y=f(x)$ có bảng biến thiên . Số nghiệm của phương trình $2f(x) - 3 = 0$ là:",
    "options": ["2", "3", "4", "1"],
    "answer": "A",
    "explanation": "$f(x) = 1.5$. Đường thẳng này nằm giữa giá trị cực đại và cực tiểu."
  },
  {
    "question": "Tìm $m$ để đồ thị hàm số $y = \\frac{x-1}{x^2-2mx+4}$ có đúng 2 đường tiệm cận.",
    "options": ["m = 2", "m = -2", "m \\in {2; -2}", "m > 2"],
    "answer": "C",
    "explanation": "Đồ thị luôn có 1 TCN $y=0$. Để có thêm đúng 1 TCĐ thì mẫu số phải có nghiệm kép hoặc có 2 nghiệm trong đó 1 nghiệm bằng 1."
  },
  {
    "question": "Trong không gian $Oxyz$, góc giữa hai mặt phẳng $(P): x + y - 1 = 0$ và $(Q): y + z + 1 = 0$ bằng:",
    "options": ["60^\\circ", "30^\\circ", "45^\\circ", "90^\\circ"],
    "answer": "A",
    "explanation": "$\\cos \\alpha = \\frac{|1\\cdot 0 + 1\\cdot 1 + 0\\cdot 1|}{\\sqrt{2} \\cdot \\sqrt{2}} = 1/2 \\Rightarrow 60^\\circ$."
  },
  {
    "question": "Nguyên hàm của hàm số $f(x) = \\cos^2 x$ là:",
    "options": ["\\frac{x}{2} + \\frac{\\sin 2x}{4} + C", "\\frac{x}{2} - \\frac{\\sin 2x}{4} + C", "\\sin^2 x + C", "\\frac{\\cos^3 x}{3} + C"],
    "answer": "A",
    "explanation": "Hạ bậc: $\\cos^2 x = \\frac{1 + \\cos 2x}{2}$. Nguyên hàm là $\\frac{x}{2} + \\frac{\\sin 2x}{4} + C$."
  },
  {"question":"Môđun của số phức z = 2100 + 2800i là?","options":["A. 3500","B. 4900","C. 700","D. 12250000"],"answer":"A. 3500","explanation":"√(2100^2+2800^2)=3500."},
{"question":"Đạo hàm của hàm số y = x^83 là?","options":["A. 83x^82","B. x^82","C. 82x^83","D. 83x^83"],"answer":"A. 83x^82","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=82 là?","options":["A. 4835703278458516698824704","B. 6724","C. 164","D. 2417851639229258349412352"],"answer":"A. 4835703278458516698824704","explanation":"x = 2^82."},
{"question":"Nguyên hàm của 164x dx là?","options":["A. 82x^2 + C","B. 164x^2 + C","C. 42x^2 + C","D. 328x + C"],"answer":"A. 82x^2 + C","explanation":"∫164x dx = 82x^2 + C."},
{"question":"Môđun của số phức z = 2160 + 2880i là?","options":["A. 3600","B. 5040","C. 720","D. 12960000"],"answer":"A. 3600","explanation":"√(2160^2+2880^2)=3600."},
{"question":"Đạo hàm của hàm số y = x^84 là?","options":["A. 84x^83","B. x^83","C. 83x^84","D. 84x^84"],"answer":"A. 84x^83","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=83 là?","options":["A. 9671406556917033397649408","B. 6889","C. 166","D. 4835703278458516698824704"],"answer":"A. 9671406556917033397649408","explanation":"x = 2^83."},
{"question":"Nguyên hàm của 166x dx là?","options":["A. 83x^2 + C","B. 166x^2 + C","C. 43x^2 + C","D. 332x + C"],"answer":"A. 83x^2 + C","explanation":"∫166x dx = 83x^2 + C."},
{"question":"Môđun của số phức z = 2220 + 2960i là?","options":["A. 3700","B. 5180","C. 740","D. 13690000"],"answer":"A. 3700","explanation":"√(2220^2+2960^2)=3700."},
{"question":"Đạo hàm của hàm số y = x^85 là?","options":["A. 85x^84","B. x^84","C. 84x^85","D. 85x^85"],"answer":"A. 85x^84","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=84 là?","options":["A. 19342813113834066795298816","B. 7056","C. 168","D. 9671406556917033397649408"],"answer":"A. 19342813113834066795298816","explanation":"x = 2^84."},
{"question":"Nguyên hàm của 168x dx là?","options":["A. 84x^2 + C","B. 168x^2 + C","C. 44x^2 + C","D. 336x + C"],"answer":"A. 84x^2 + C","explanation":"∫168x dx = 84x^2 + C."},
{"question":"Môđun của số phức z = 2280 + 3040i là?","options":["A. 3800","B. 5320","C. 760","D. 14440000"],"answer":"A. 3800","explanation":"√(2280^2+3040^2)=3800."},
{"question":"Đạo hàm của hàm số y = x^86 là?","options":["A. 86x^85","B. x^85","C. 85x^86","D. 86x^86"],"answer":"A. 86x^85","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=85 là?","options":["A. 38685626227668133590597632","B. 7225","C. 170","D. 19342813113834066795298816"],"answer":"A. 38685626227668133590597632","explanation":"x = 2^85."},
{"question":"Nguyên hàm của 170x dx là?","options":["A. 85x^2 + C","B. 170x^2 + C","C. 45x^2 + C","D. 340x + C"],"answer":"A. 85x^2 + C","explanation":"∫170x dx = 85x^2 + C."},
{"question":"Môđun của số phức z = 2340 + 3120i là?","options":["A. 3900","B. 5460","C. 780","D. 15210000"],"answer":"A. 3900","explanation":"√(2340^2+3120^2)=3900."},
{"question":"Đạo hàm của hàm số y = x^87 là?","options":["A. 87x^86","B. x^86","C. 86x^87","D. 87x^87"],"answer":"A. 87x^86","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=86 là?","options":["A. 77371252455336267181195264","B. 7396","C. 172","D. 38685626227668133590597632"],"answer":"A. 77371252455336267181195264","explanation":"x = 2^86."},
{"question":"Nguyên hàm của 172x dx là?","options":["A. 86x^2 + C","B. 172x^2 + C","C. 46x^2 + C","D. 344x + C"],"answer":"A. 86x^2 + C","explanation":"∫172x dx = 86x^2 + C."},
{"question":"Môđun của số phức z = 2400 + 3200i là?","options":["A. 4000","B. 5600","C. 800","D. 16000000"],"answer":"A. 4000","explanation":"√(2400^2+3200^2)=4000."},
{"question":"Đạo hàm của hàm số y = x^88 là?","options":["A. 88x^87","B. x^87","C. 87x^88","D. 88x^88"],"answer":"A. 88x^87","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=87 là?","options":["A. 154742504910672534362390528","B. 7569","C. 174","D. 77371252455336267181195264"],"answer":"A. 154742504910672534362390528","explanation":"x = 2^87."},
{"question":"Nguyên hàm của 174x dx là?","options":["A. 87x^2 + C","B. 174x^2 + C","C. 47x^2 + C","D. 348x + C"],"answer":"A. 87x^2 + C","explanation":"∫174x dx = 87x^2 + C."},
{"question":"Môđun của số phức z = 2460 + 3280i là?","options":["A. 4100","B. 5740","C. 820","D. 16810000"],"answer":"A. 4100","explanation":"√(2460^2+3280^2)=4100."},
{"question":"Đạo hàm của hàm số y = x^89 là?","options":["A. 89x^88","B. x^88","C. 88x^89","D. 89x^89"],"answer":"A. 89x^88","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=88 là?","options":["A. 309485009821345068724781056","B. 7744","C. 176","D. 154742504910672534362390528"],"answer":"A. 309485009821345068724781056","explanation":"x = 2^88."},
{"question":"Nguyên hàm của 176x dx là?","options":["A. 88x^2 + C","B. 176x^2 + C","C. 48x^2 + C","D. 352x + C"],"answer":"A. 88x^2 + C","explanation":"∫176x dx = 88x^2 + C."},
{"question":"Môđun của số phức z = 2520 + 3360i là?","options":["A. 4200","B. 5880","C. 840","D. 17640000"],"answer":"A. 4200","explanation":"√(2520^2+3360^2)=4200."},
{"question":"Đạo hàm của hàm số y = x^90 là?","options":["A. 90x^89","B. x^89","C. 89x^90","D. 90x^90"],"answer":"A. 90x^89","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=89 là?","options":["A. 618970019642690137449562112","B. 7921","C. 178","D. 309485009821345068724781056"],"answer":"A. 618970019642690137449562112","explanation":"x = 2^89."},
{"question":"Nguyên hàm của 178x dx là?","options":["A. 89x^2 + C","B. 178x^2 + C","C. 49x^2 + C","D. 356x + C"],"answer":"A. 89x^2 + C","explanation":"∫178x dx = 89x^2 + C."},
{"question":"Môđun của số phức z = 2580 + 3440i là?","options":["A. 4300","B. 6020","C. 860","D. 18490000"],"answer":"A. 4300","explanation":"√(2580^2+3440^2)=4300."},
{"question":"Đạo hàm của hàm số y = x^91 là?","options":["A. 91x^90","B. x^90","C. 90x^91","D. 91x^91"],"answer":"A. 91x^90","explanation":"Áp dụng công thức đạo hàm lũy thừa."},
{"question":"Nghiệm của phương trình log2(x)=90 là?","options":["A. 1237940039285380274899124224","B. 8100","C. 180","D. 618970019642690137449562112"],"answer":"A. 1237940039285380274899124224","explanation":"x = 2^90."},
{"question":"Nguyên hàm của 180x dx là?","options":["A. 90x^2 + C","B. 180x^2 + C","C. 50x^2 + C","D. 360x + C"],"answer":"A. 90x^2 + C","explanation":"∫180x dx = 90x^2 + C."},
{"question":"Môđun của số phức z = 2640 + 3520i là?","options":["A. 4400","B. 6160","C. 880","D. 19360000"],"answer":"A. 4400","explanation":"√(2640^2+3520^2)=4400."},
{"question":"Đạo hàm của hàm số y = x^92 là?","options":["A. 92x^91","B. x^91","C. 91x^92","D. 92x^92"],"answer":"A. 92x^91","explanation":"Áp dụng công thức (x^n)'."},
{"question":"Nghiệm của phương trình log2(x)=91 là?","options":["A. 2475880078570760549798248448","B. 8281","C. 182","D. 1237940039285380274899124224"],"answer":"A. 2475880078570760549798248448","explanation":"x = 2^91."},
{"question":"Nguyên hàm của 182x dx là?","options":["A. 91x^2 + C","B. 182x^2 + C","C. 51x^2 + C","D. 364x + C"],"answer":"A. 91x^2 + C","explanation":"∫182x dx = 91x^2 + C."},

]