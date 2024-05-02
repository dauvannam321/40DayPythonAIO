# • Câu 1: Tạo mới một List có tên là lst_data, gồm các số từ 1 đến 10.
lst_data = [x for x in range(1,11)]
print("Câu 1:", lst_data)

# • Câu 2: Tính giá trị trung vị từ lst_data vừa tạo. (Không sử dụng numpy)
median = (lst_data[4] + lst_data[5])/2
print("Câu 2: Median:", median)

# • Câu 3: Lọc các giá trị số lẻ trong lst_data và lưu ra list mới có tên là: lst_odd_filter
# với thứ tự giảm dần ( Sử dụng phương thức reverse=True trong hàm sort/sorted).
lst_odd_filter = list(filter(lambda x: x%2 == 1, lst_data))
print("Câu 3:", sorted(lst_odd_filter, reverse=True))