import math

def tinh_S3(n):
    
    if n == 1:
        return 1.0
    
    return math.sqrt(n + tinh_S3(n - 1))

if __name__ == "__main__":
    print(f"Kết quả S(2): {tinh_S3(2):.4f}")