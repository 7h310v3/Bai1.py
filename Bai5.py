import random
ghi = []

def taodulieu():
    count = 0
    while (count < 1000):
        ghi.append(int(random.uniform(-1000, 1000)))
        count += 1

def ghidulieuvaofile(ghi):
    with open(tentep, "a+") as f:
        f.seek(0)

        count = 0
        count1 = 0
        while (count < (len(ghi))):
            if (count1 == 10):
                count1 = 0
                f.write("\n")
            elif (count1 < 9):
                f.write(str(ghi[count]))
                f.write(",")
                count1 += 1
                count += 1
            else:
                f.write(str(ghi[count]))
                count1 += 1
                count += 1

def docdulieu(doc):
    with open(tentep, mode = "r") as f:
        line = f.readline().strip()
        while line:
            doc += line.split(",")
            line = f.readline().strip()
    return doc

def main():
    doc = []
    global tentep
    tentep = input("Nhập tên tệp: ") + ".txt"

    with open(tentep, "a+") as f:
        #taodulieu()

        #ghidulieuvaofile(ghi)

        doc = docdulieu(doc)
    print(doc)

if __name__ == "__main__":
    main()