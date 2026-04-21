# --- BÀI TẬP 6: ĐẾM TỪ TRONG CHUỖI ---

# 1. Khai báo chuỗi văn bản (Dùng 3 dấu nháy để viết nhiều dòng)
s = '''Chiều chiều trước bến Văn Lâu
Ai ngồi, ai câu, ai sầu, ai thảm
Ai thương, ai cảm, ai nhớ, ai trông
Thuyền ai thấp thoáng ven sông
Đưa câu mái vẩy chạnh lòng nước non '''

# 2. Nhập từ cần đếm (Theo ví dụ là từ 'ai')
word = 'ai'

# 3. Xử lý đếm: 
# Chuyển s về chữ thường (.lower()) để đếm được cả chữ "Ai" viết hoa và "ai" viết thường
so_lan = s.lower().count(word.lower())

# 4. In kết quả ra màn hình đúng định dạng ví dụ
print(f"số từ {word} là {so_lan}")