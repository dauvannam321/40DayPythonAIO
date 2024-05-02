# • Tạo Bag-Of-Word cho tập dataset sau: corpus = ["Tôi thích môn Toán", "Tôi
# thích AI", "Tôi thích âm nhạc"]. Sau đó tạo list có tên vector để lưu vector sau
# khi thực hiện bước Tokenization đoạn văn bản sau: Tôi thích AI thích Toán
corpus = ["Tôi thích môn Toán", "Tôi thích AI", "Tôi thích âm nhạc"]

vocab = []
for i in corpus:
    words = i.split(" ")
    for w in words:
        if w not in vocab:
            vocab.append(w)

print(vocab)

text = "Tôi thích AI thích Toán"
text = text.split(" ")
vector = []

for w in vocab:
    vector.append(text.count(w))

print(vector)