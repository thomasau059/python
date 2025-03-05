# #dem chanle
# count = 0
# for i in range(1,50):
#     if i%2==0:
#         print('nhung so chan la',i)
#     else:
#         continue
#     count += 1
#     print('so luong so chan la',    count)


#dem chanle
def countChanLe(max):
    countChan = 0
    countle = 0
    for i in range(1,max):
        if i%2==0:
            print('nhung so chan la',i)
            countChan += 1
        else:
            countle += 1
        
    print('so luong so chan la',    countChan)
    print('so luong so le la',    countle)
number = int(input("nhap so max"))
countChanLe(number)