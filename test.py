import random

def taodulieu():
    count = 0
    while (count < 1000):
        ghi.append(int(random.uniform(-1000, 1000)))
        count += 1

#main
ghi = []
taodulieu()

count = 0
count1 = 0
while(count < (len(ghi))):
    if (count1 == 10):
        count1 = 0
        print("\n")
    else:
        print(count)
        print("  ")
        count1 += 1
        count += 1
