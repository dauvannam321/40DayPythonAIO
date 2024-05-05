# • Chọn ngẫu nhiên hai số a và b thuộc từ 1 đến 20 sao cho tổng của a + b bằng
#  40, câu hỏi đặt ra rằng, chúng ta phải tạo ngẫu nhiên bao nhiêu lần để thỏa mản
#  điều kiện trên ?
import random

def random_number_with_condition(total):
    random.seed(0)
    count = 0
    while True:
        a = random.randint(1,20)
        b = random.randint(1,20)
        count += 1
        if a+b==total:
            print("random_number_with_condition({}) → {} lần".format(total, count))
            return count
        
random_number_with_condition(40)
random_number_with_condition(20)
random_number_with_condition(35)