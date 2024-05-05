# • Câu 1: Hãy đọc file data.txt có trong dataset phía trên và lưu vào biến data sau
#  khi loại bỏ các ký tự \n và thay thế bằng khoảng trắng, đồng thời chuyển về chữ
#  cái thường toàn bộ văn bản
with open("data\data.txt", "r") as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = data[i].lower()
    data[i] = data[i].replace("\n", " ")

print("Câu 1:\n",data)

#  • Câu 2: Phân tích văn bản trên và lưu vào biến có tên distinct_words các chữ
#  cái duy nhất trong câu
distinct_words = []
BoW= []
for i in data:
    words = i.split(" ")
    for w in words:
        if w != '':
            BoW.append(w)
            if w not in distinct_words:
                distinct_words.append(w)

print("Câu 2:\n", distinct_words)

#  • Câu 3: Đếm số lần từng chữ trong distinct_words xuất hiện trong văn bản. Và
#  cho biết chữ nào xuất hiện nhiều nhất và ít nhất.

freq = {item:BoW.count(item) for item in distinct_words}
freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
print("Câu 3:")
for i in freq:
    print("\"{}\" in data is {}".format(i[0], i[1]))
print("\"{}\" is most frequent word \n \"{}\" is the least common word".format(freq[0][0], freq[-1][0]))
