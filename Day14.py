# • Tạo List 2D có tên là lst_data có dạng 3 x 3, gồm các số từ 1 đến 9, ứng với các
# vị trí trong List. Sau đó tạo list khác có tên lst_sub_data là 2D List để lưu giá
# trị tại vị trí index thứ 0 và thứ 2 của lst_data (Chỉ sử dụng For). In ra màn hình
# kết quả của lst_sub_data

lst_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

lst_sub_data = []
for i in lst_data:
    lst_sub_data.append([i[0], i[2]])
print(lst_sub_data)