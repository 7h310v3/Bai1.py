tentep = input("Nhập tên tệp: ") + ".txt"

chuoi1 =" " + input("Nhập 1 chuỗi: ")

with open(tentep, "r+") as f:
    tmp = f.read()

    f.seek(len(tmp))

    f.write(chuoi1)