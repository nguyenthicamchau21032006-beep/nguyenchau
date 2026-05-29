#Bai4_214
import math

is_perfect_square = lambda n: math.isqrt(n)**2 == n


is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))


is_perfect_number = lambda n: n > 0 and sum(i for i in range(1, n) if n % i == 0) == n

print("Các số từ 1 đến 100 thỏa mãn điều kiện:")
for i in range(1, 101):
    if is_perfect_square(i):
        print(f"Số {i} là số chính phương.")
    if is_prime(i):
        print(f"Số {i} là số nguyên tố.")
    if is_perfect_number(i):
        print(f"Số {i} là số hoàn thiện.")