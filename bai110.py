def tinh_An(n):
    
    if n == 1:
        return 1
    
    return n * tinh_An(n - 1)


if __name__ == "__main__":
    n = 4
    ket_qua = tinh_An(n)
    print(f"Giá trị của A_{n} là: {ket_qua}")