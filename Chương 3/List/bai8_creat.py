# 8.	Tạo một danh sách gồm 10 phần tử, sau đó xóa tất cả các phần tử lẻ.
my_list = []
for i in range(1,11):

    my_list.append(i)
print(my_list)
while my_list%2==0:
    print(my_list)