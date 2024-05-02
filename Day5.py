# Câu 1 Tạo mới một List có tên là lst_data, gồm các số chẵn từ 1 đến 12.
lst_data = [x for x in range(2, 13, 2)]
print("Câu 1:", lst_data)

# Câu 2: Xóa tất cả các số chia hết cho 3 trong lst_data vừa tạo
for i in lst_data:
    if i % 3 == 0:
        lst_data.remove(i)

print("Câu 2:", lst_data)

# Câu 3: Thêm vào cuối lst_data các số từ 1 đến 3, và thêm vào vị trí index = 3
# một chuỗi các số từ 6 đến 8
lst_data.append(1)
lst_data.append(2)
lst_data.append(3)
lst_data = lst_data[0:3] + [6, 7, 8] + lst_data[3:]

print("Câu 3:", lst_data)

# Câu 4: Nếu các số trong list lst_data chia hết cho 2 hoặc chia hết cho 5 thì cập
# nhật thành số 0
for i in range(len(lst_data)):
    if lst_data[i] % 2 == 0 or lst_data[i] % 5 == 0:
        lst_data[i] = 0
print("Câu 4:", lst_data)
