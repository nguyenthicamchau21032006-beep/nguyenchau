def tinh_P2(n):
    if n == 1:
        return 2.0
    
    return tinh_P2(n - 1) * (1 + 1 / (n ** 2))

if __name__ == "__main__":
    print(f"Kết quả P(2): {tinh_P2(2):.4f}")