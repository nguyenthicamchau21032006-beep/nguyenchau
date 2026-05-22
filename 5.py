def tinh_S1(n):

    if n == 0:
        return 1.0
    
    
    return tinh_S1(n - 1) + (1 / (2 * n + 1))

if __name__ == "__main__":
    print(f"Kết quả S(2): {tinh_S1(2):.4f}")