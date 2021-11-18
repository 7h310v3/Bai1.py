tentep = input("Nhập tên tệp: ") + ".txt"

f = open(tentep, mode = "r")

f.seek(0)

c = f.read()

print((c))

f.close()

