# Câu 1 Tạo list gồm các số từ 1 đến 10
my_list = [i for i in range(1,11)]

# Câu 2 in ra 5 phần tử đầu
print(my_list[:5])

# Câu 3 in ra phần tử có giá trị không chia hết cho 2 (dùng vòng lặp for)
for i in my_list:
    if i % 2 == 0:
        print(i, end=" ")

# Câu 4 in tổng các phần tử trong list (dùng vòng lặp for)
sum = 0
for i in my_list:
    sum += i
print("\nSum of list:", sum)
