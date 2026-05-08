Nhập chuỗi S
s = input("Nhập chuỗi (S): ")

danh_sach_tu = s.split()

tu_da_thay = set()
tu_lap_lai = None

for tu in danh_sach_tu:
    if tu in tu_da_thay:
        tu_lap_lai = tu
        break 
    tu_da_thay.add(tu)

print(f"Từ đầu tiên lặp lại là: {tu_lap_lai}")