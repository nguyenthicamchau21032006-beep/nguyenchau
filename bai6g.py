# g) Kiểm tra số chính phương
is_perfect_square = lambda n: n >= 0 and math.isqrt(n)**2 == n

# h) Kiểm tra số nguyên tố
def is_prime_func(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

is_prime = lambda n: is_prime_func(n)