def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)

# Ví dụ: GCD(48, 18) = 6
print(f"Ước chung lớn nhất của 48 và 18 là: {ucln(48, 18)}")