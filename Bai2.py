tentep = input("Nhập tên tệp: ") + ".txt"

with open (tentep, "r") as f:
    f.seek(0)
    tmp = f.read()

print(tmp)


