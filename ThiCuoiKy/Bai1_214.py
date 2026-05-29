# Bai1_214.py
try:
    dai = float(input("Nhập chiều dài hình khối chữ nhật (cm): "))
    rong = float(input("Nhập chiều rộng hình khối chữ nhật (cm): "))
    cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))
    
    dien_tich_day = dai * rong
    the_tich = dai * rong * cao
    
    print(f"Diện tích đáy hình chữ nhật = {dien_tich_day:.2f} cm^2")
    print(f"Thể tích hình khối = {the_tich:.2f} cm^3")
except ValueError:
    print("Vui lòng nhập số hợp lệ.")