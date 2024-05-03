# Bài tập: Trong NLP, chúng ta cần loại bỏ 1 số từ không quan trọng (stopwords) ra
# khỏi câu để tránh gây nhiễu trong việc xử lý. Hãy loại bỏ các từ có trong stop_words
# = ["I", "love", "and", "to"] câu đầu vào "I love AI and listen to music". Hãy áp
# dụng List comprehension và For truyền thống để thực hiện
stop_words = ["I", "love", "and", "to"]
text = "I love AI and listen to music"

res = [x for x in text.split(" ") if x not in stop_words]
print(res)