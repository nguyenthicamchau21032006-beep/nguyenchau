def tim_chu_so_max(n):

    if n < 10:
        return n
    
    chu_so_cuoi = n % 10
    
    max_phan_con_lai = tim_chu_so_max(n // 10)
    
    return max(chu_so_cuoi, max_phan_con_lai)

if __name__ == "__main__":
    n = 1952
    print(f"Chữ số lớn nhất của {n} là: {tim_chu_so_max(n)}")