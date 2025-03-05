#kiemtrasonguyento
#gọi số nguyên tố là a ....lấy a chia cho i i chạy từ 2 tới a-1 


check = 0 
a = int(input('nhap sp a:'))
if a>1 :
    for i in range(2,a):
        if a%i==0 :
            print(a,'khong phai la so nguyen to ')
            check = 1 
            break 
    if check == 0 :
        print(a,'la so nguyen to')
else :
    print(a,'khong phai la so nguyen to ')
     
            
            
            
            
            