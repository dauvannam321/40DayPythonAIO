A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[2, 4, 6], [1, 3, 5], [1, 0, 1]]

# Sử dụng Python,không dùng thư viện numpy
# Câu 1. Hãy tính tổng và hiệu 2 ma trận A + B và A - B
sumAB = []
for i in range(3):
    temp = []
    for j in range(3):
        temp.append(A[i][j] + B[i][j])
    sumAB.append(temp)
print("Tổng:",sumAB)

subAB = []
for i in range(3):
    temp = []
    for j in range(3):
        temp.append(A[i][j] - B[i][j])
    subAB.append(temp)
print("Hiệu:",subAB)

# Câu 2. Hãy tính dot product 2 ma trận A và B
dotAB = []
for i in range(3):
    temp = []
    for j in range(3):
        sumij = 0
        for k in range(3):
            sumij += A[i][k] * B[k][j]
        temp.append(sumij)
    dotAB.append(temp)

print("Dot Product:", dotAB)