import math

# Hàm kiểm tra số nguyên tố (Câu a)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    ds_so = []
    
    # Nhập dữ liệu nhiều lần
    while True:
        try:
            num = int(input("Mời bạn nhập một số nguyên: "))
            ds_so.append(num)
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ!")
            continue

        choice = input("Bạn có muốn nhập tiếp không? (Y/N): ").strip().upper()
        if choice != 'Y':
            break

    print("\nKẾT QUẢ THỰC HIỆN")

    # a) In ra các số nguyên tố
    primes = [x for x in ds_so if is_prime(x)]
    print(f"a) Các số nguyên tố trong list: {primes}")

    # b) Trung bình cộng số âm và số dương
    so_am = [x for x in ds_so if x < 0]
    so_duong = [x for x in ds_so if x > 0]

    tbc_am = sum(so_am) / len(so_am) if so_am else "Không có số âm"
    tbc_duong = sum(so_duong) / len(so_duong) if so_duong else "Không có số dương"

    print(f"b) TBC số âm: {tbc_am}")
    print(f"   TBC số dương: {tbc_duong}")

    # c) Số lớn nhất, số nhỏ nhất
    if ds_so:
        print(f"c) Số lớn nhất: {max(ds_so)}")
        print(f"   Số nhỏ nhất: {min(ds_so)}")

    # d) Kiểm tra sắp xếp tăng dần
    is_sorted = ds_so == sorted(ds_so)
    print(f"d) Danh sách đã được sắp xếp tăng dần chưa? {'Rồi' if is_sorted else 'Chưa'}")

if __name__ == "__main__":
    main()