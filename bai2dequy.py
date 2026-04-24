def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)

# Ví dụ: 5! = 120
print(f"Giai thừa của 5 là: {giai_thua(5)}")