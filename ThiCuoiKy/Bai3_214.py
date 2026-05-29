import math
is_perfect_square = lambda n: math.isqrt(n)**2 == n


check_triangle = lambda a, b, c: (
    "Không phải là tam giác" if (a + b <= c or a + c <= b or b + c <= a) else
    "Tam giác đều" if a == b == c else
    "Tam giác vuông" if (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2) else
    "Tam giác cân" if (a == b or b == c or a == c) else "Tam giác thường"
)


n = int(input("Nhập số nguyên n để kiểm tra chính phương: "))
print(f"Số {n} {'là' if is_perfect_square(n) else 'không phải là'} số chính phương.")


print("\nNhập 3 cạnh của tam giác:")
a = float(input("Cạnh a: "))
b = float(input("Cạnh b: "))
c = float(input("Cạnh c: "))
print(f"Kết quả: {check_triangle(a, b, c)}")