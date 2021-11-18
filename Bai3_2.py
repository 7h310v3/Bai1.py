tentep = input("Nhập tên tệp: ") + ".txt"

f = open(tentep, mode = "r+")

chuoi1 =" " + input("Nhập 1 chuỗi: ")

c = f.read()

f.seek(len(c))

f.write(chuoi1)

f.close()