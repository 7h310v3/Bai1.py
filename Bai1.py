chuoi1 = input("Nhập 1 chuỗi: ")

tentep = input("Nhập tên tệp: ") + ".txt"

with open (tentep, "w") as f:
    f.write(chuoi1)
