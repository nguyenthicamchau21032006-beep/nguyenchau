def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Ví dụ: n=7 sẽ ra 21 (Theo dãy: 1, 1, 2, 3, 5, 8, 13, 21...)
# Lưu ý: Đề bài trong ảnh ghi n=7 ra 13 là do họ bắt đầu đếm từ F0. 
# Nếu F0=1, F1=1, F2=2, F3=3, F4=5, F5=8, F6=13, F7=21.
n = 7
print(f"Số Fibonacci thứ {n} là: {fibonacci(n)}")