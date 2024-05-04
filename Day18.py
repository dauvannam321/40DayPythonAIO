#  • Câu 1: Tạo List có tên lst_data gồm các số từ 1 đến 10, sau đó ghi toàn bộ list
#  trên vào file có tên: data.txt với nội dung là 1 chuỗi số từ list trên nối với nhau
#  bằng dấu
lst_data = [ x for x in range(1, 11)]
with open('data.txt', "w") as f:
    data = ''
    for i in lst_data:
        data += str(i) +"-"
    data = data[:-1]
    f.write(data)

# • Câu 2: Đọc file data.txt vừa tạo ở câu 1 và lưu vào List mới có tên lst_filter
#  gồm các số chia hết cho 3
with open('data.txt', "r") as f:
    data = f.read()
    data = list(map(int, data.split("-")))
    data = list(filter(lambda x : x % 3 == 0, data))

print(data)