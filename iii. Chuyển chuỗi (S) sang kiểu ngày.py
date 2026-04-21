from datetime import datetime

s = "Sep 18 2019 2:43PM"
# %b: Tháng viết tắt, %d: Ngày, %Y: Năm 4 chữ số, %I: Giờ 12h, %M: Phút, %p: AM/PM
date_obj = datetime.strptime(s, "%b %d %Y %I:%M%p")

print(f"Chuỗi sau khi chuyển sang kiểu ngày: {date_obj}")
print(f"Kiểu dữ liệu: {type(date_obj)}")