# • Tạo List có tên là lst_data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]. Sau đó, áp
# dụng phương pháp tìm kiếm để tìm vị trí có giá trị None có trong lst_data theo
# 2 cách: tìm vị trí None đầu tiên, và tìm tất cả vị trí có giá trị None
lst_data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]

first_pos = None
lst_pos = []
for i in range(len(lst_data)):
    if lst_data[i] is None and first_pos is None:
        first_pos = i
        lst_pos.append(i)
    elif lst_data[i] == None:
        lst_pos.append(i)

print("- Vị trí None đầu tiên: {} - Danh sách vị trí có giá trị None: {}".format(first_pos, lst_pos))