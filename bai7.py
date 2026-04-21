
chuoi_vao = "   Quê  hương   là  chùm khế   ngọt .   "

def lam_sach_chuoi(s):
    # Bước 1: Tách các từ và loại bỏ khoảng trắng thừa
    cac_tu = s.split()
    
    # Bước 2: Nối lại với 1 khoảng trắng duy nhất giữa các từ
    ket_qua = ' '.join(cac_tu)
    
    # Bước 3: Xử lý quy tắc dấu câu (xóa khoảng trắng trước dấu chấm, phẩy)
    # Ví dụ: "ngọt ." thành "ngọt."
    ket_qua = ket_qua.replace(" ,", ",").replace(" .", ".")
    
    return ket_qua

# Chạy thử
chuoi_ra = lam_sach_chuoi(chuoi_vao)

print("Chuỗi gốc:", f"'{chuoi_vao}'")
print("Chuỗi hoàn chỉnh:", f"'{chuoi_ra}'")