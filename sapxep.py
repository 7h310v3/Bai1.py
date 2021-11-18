#Sắp xếp mảng tăng dần / giảm dần trong python
num = []

#nhập dữ liệu cho mảng
def enter_num():
    global num
    print('Nhập dữ liệu xong thì nhập (Done) hoặc (done)')
    while True:
        x = input('Dữ liệu cần nhập cho mảng: ').upper()
        if x == 'DONE':
            print('Dữ liệu đã nhập thành công')
            break
        num.append(float(x))

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

#chạy chương trình
enter_num()

print("Mảng trước khi sắp xếp")
print(num)

print('Kiểu sắp xếp bạn muốn:\n (1)Tăng dần \n (2)Giảm dần')
choice = int(input('Lựa chọn của bạn: '))

if(choice == 1):
    print("Dữ liệu của mảng sau khi sắp xếp:",tangdan(num))
if(choice == 2):
    print("Dữ liệu của mảng sau khi sắp xếp:",giamdan(num))