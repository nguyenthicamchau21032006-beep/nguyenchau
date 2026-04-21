from datetime import datetime

now = datetime.now()

print(f"Năm hiện tại: {now.year}")
print(f"Tháng hiện tại bằng chữ: {now.strftime('%B')}")
print(f"Tuần hiện tại là tuần thứ mấy trong năm: {now.strftime('%U')}")
# Tuần trong tháng cần tính toán một chút:
print(f"Tuần hiện tại là tuần thứ mấy trong tháng: {(now.day - 1) // 7 + 1}")
print(f"Ngày hiện tại là ngày thứ mấy trong năm: {now.strftime('%j')}")
print(f"Ngày dương lịch hiện tại là ngày: {now.day}")
print(f"Thứ của ngày hiện tại: {now.strftime('%A')}")
print(f"Giờ phút giây hiện tại: {now.strftime('%H:%M:%S')}")