chuoi = input("Nhập 1 chuỗi: ")

tentep = input("Nhập tên tệp: ") + ".txt"

f = open(tentep, mode = "w+")

f.write(chuoi)

f.close()