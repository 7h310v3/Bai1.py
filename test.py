import random

def taodulieu():
    count = 0
    while (count < 1000):
        ghi.append(int(random.uniform(-1000, 1000)))
        count += 1


#main
ghi = []
taodulieu()

print(ghi[999])