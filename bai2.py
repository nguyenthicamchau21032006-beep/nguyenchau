from datetime import date

print("Nhập ngày thứ nhất:")
d1 = int(input("Ngày: "))
m1 = int(input("Tháng: "))
y1 = int(input("Năm: "))

print("Nhập ngày thứ hai:")
d2 = int(input("Ngày: "))
m2 = int(input("Tháng: "))
y2 = int(input("Năm: "))

date_start = date(y1, m1, d1)
date_end = date(y2, m2, d2)

delta = abs(date_end - date_start)
print(f"Số ngày cách nhau giữa 2 ngày là: {delta.days} ngày")