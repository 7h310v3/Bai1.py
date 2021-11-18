tentep = input("Nhập tên tệp: ") + ".txt"

f = open(tentep, mode = "a+")

chuoi1 = input("Nhập 1 chuỗi: ")

f.write(chuoi1)

f.close()