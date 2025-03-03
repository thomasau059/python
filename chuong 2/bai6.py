a = int(input('moi nhap so nguyen duong a: '))  
if a > 0:
    b=a
    for i in range(1,a-1):
        b = b*(a-i-1)
    print('giai thua cua a : ', b)
else:
    print('a khong phai la so nguyen duong')