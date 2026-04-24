def luy_thua(a, b):
    if b == 0:
        return 1
    return a * luy_thua(a, b - 1)

# Ví dụ: 2^3 = 8
print(f"2 mũ 3 bằng: {luy_thua(2, 3)}")