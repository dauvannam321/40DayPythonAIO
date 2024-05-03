from math import sqrt

# Câu 1
my_tuple1 = (2, 3)
my_tuple2 = (3, 6)

# Câu 2
print("Sum:",tuple([a + b for a,b in zip(my_tuple1,my_tuple2)]))
print("Mul:",tuple([a * b for a,b in zip(my_tuple1,my_tuple2)]))

# Câu 3
print("Distance:", sqrt(sum([(a - b) ** 2 for a,b in zip(my_tuple1, my_tuple2)])))

# Câu 4
print("index=({},{})".format(my_tuple1.index(3), my_tuple2.index(3)))