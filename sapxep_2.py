num = [2, 5, 9, 8, 4, 3]


#sắp xếp
def tangdan(num):
    for i in range (0, len(num)-1):
        for j in range (i+1, len(num)):
            if num[i] > num[j]:
                tmp = num[i]
                num[i] = num[j]
                num[j] = tmp
    return num

def giamdan(num):
    for i in range (0, len(num)-1):
        for j in range (i+1, len(num)):
            if num[i] < num[j]:
                tmp = num[i]
                num[i] = num[j]
                num[j] = tmp
    return num

print("Ban đầu:")
print(num)

print('Kiểu sắp xếp bạn muốn:\n (1)Tăng dần \n (2)Giảm dần')
choice = int(input('Lựa chọn của bạn: '))

if(choice == 1):
    print("Dữ liệu của mảng sau khi sắp xếp:")
    print(tangdan(num))
if(choice == 2):
    print("Dữ liệu của mảng sau khi sắp xếp:")
    print(giamdan(num))