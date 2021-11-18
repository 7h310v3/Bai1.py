import random

def taodulieu():
    count = 0
    while (count < 1000):
        ghi.append(int(random.uniform(-1000, 1000)))
        count += 1

def ghidulieuvaofile(ghi):
    f = open(tentep, mode = "a+")
    f.seek(0)

    count = 0
    count1 = 0
    while(count < (len(ghi)-2)):
        while (count1 <= 10):
            if (count1 == 10):
                count1 = 0
                f.write("\n")
            else:
                f.write(str(ghi[count]))
                f.write("  ")
                count1 += 1
                count += 1

    f.close()

#main
ghi = []
tentep = input("Nhập tên tệp: ") + ".txt"
f = open(tentep, mode = "a+")

taodulieu()

ghidulieuvaofile(ghi)

f.close()