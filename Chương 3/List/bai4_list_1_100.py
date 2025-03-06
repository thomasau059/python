#Viết chương trình tạo danh sách từ 1 đến 100 và in ra các số chia hết cho 5
my_list = []
for i in range(1,101):
    my_list.append(i)

print(my_list)
for i in range (5,101):
    if i%5==0:
        print(i)