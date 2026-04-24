def tong_chu_so(n):
    if n < 10:
        return n
    return (n % 10) + tong_chu_so(n // 10)

# Ví dụ: n = 345 => 12
print(f"Tổng chữ số của 345 là: {tong_chu_so(345)}")