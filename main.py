chuoi = input("Nhập 1 chuỗi: ")

ten = input("Nhập tên tệp: ") + ".txt"

f = open("D:\Bin\\"+ ten, mode = "w+", encoding = "utf-8")

f.write(chuoi)

print(f.read())

f.close()