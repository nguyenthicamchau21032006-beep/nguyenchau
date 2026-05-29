#Bai2_214
import math

def la_so_nguyen_to(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def liet_ke_uoc_so(n):
    uocs = [i for i in range(1, n + 1) if n % i == 0]
    return uocs

n = int(input("Nhập số nguyên dương n: "))

print(f"Số {n} {'là' if la_so_nguyen_to(n) else 'không là'} số nguyên tố.")
uocs = liet_ke_uoc_so(n)
print(f"Các ước số của {n} là: {uocs}")
print(f"Các ước số là số nguyên tố của {n} là: {[x for x in uocs if la_so_nguyen_to(x)]}")