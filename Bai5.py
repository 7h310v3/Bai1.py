import random

def taodulieu():
    a = []
    count = 0
    while (count < 1000):
        a.append(random.randint(-1000, 1000))
        count += 1
    return a

def ghidulieuvaofile(ghi):
    with open(tentep, "a+") as f:
        f.seek(0)

        count = 0
        check = 0
        while (count < (len(ghi))):
            if (check < 9):
                f.write(str(ghi[count]))
                f.write(",")
                check += 1
                count += 1
            else:
                f.write(str(ghi[count]))
                check = 0
                f.write("\n")
                count += 1

def docdulieu(doc):
    with open(tentep, mode = "r") as f:
        line = f.readline().strip()
        while line:
            doc += line.split(",")
            line = f.readline().strip()
    return doc

def In(a):
    count = 0
    check = 0
    while (count < (len(a))):
        if (check < 9):
            print(a[count], end = "\t ")
            check += 1
            count += 1
        else:
            print(a[count])
            check = 0
            count += 1

def main():
    doc = []
    global tentep
    tentep = input("Nhập tên tệp: ") + ".txt"

    with open(tentep, "a+") as f:
        ghi = taodulieu()

        ghidulieuvaofile(ghi)

        doc = docdulieu(doc)

    In(doc)

if __name__ == "__main__":
    main()