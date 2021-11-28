tentep = input("Nhập tên tệp: ") + ".txt"

with open(tentep, "a+") as f:
    chuoi1 = input("Nhập 1 chuỗi: ")

    f.write(chuoi1)
