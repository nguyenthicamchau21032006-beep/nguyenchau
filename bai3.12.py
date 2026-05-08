from collections import Counter

def main():
    
    s1 = input("Nhập chuỗi S1: ")
    s2 = input("Nhập chuỗi S2: ")

    dict1 = Counter(s1)
    dict2 = Counter(s2)

    print("\n--- KẾT QUẢ ---")

    common = dict1 & dict2
    print(f"a) Ký tự xuất hiện trong cả 2 chuỗi: {list(common.keys())}")

    s1_not_s2 = [char for char in dict1 if char not in dict2]
    
    s2_not_s1 = [char for char in dict2 if char not in dict1]

    print(f"c) Có trong S1 nhưng không có trong S2: {s1_not_s2}")
    print(f"   Có trong S2 nhưng không có trong S1: {s2_not_s1}")


    count_s1_not_s2 = len(s1_not_s2)
    count_s2_not_s1 = len(s2_not_s1)
    
    print(f"b) Số lượng ký tự trong S1 nhưng không có trong S2: {count_s1_not_s2}")
    print(f"   Số lượng ký tự trong S2 nhưng không có trong S1: {count_s2_not_s1}")

if __name__ == "__main__":
    main()
