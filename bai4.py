
s = input("Nhập số điện thoại (S): ")
tat_ca_so = set("0123456789")
so_da_nhap = set(s)
ket_qua = sorted(list(tat_ca_so - so_da_nhap))

print(f"Trong số điện thoại {s} không chứa các ký số: {ket_qua}")