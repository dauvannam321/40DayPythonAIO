import numpy as np
import tensorflow as tf
import torch

# Câu 1: Hãy viết chương trình tạo Numpy array, Tensorflow tensor, Pytorch tensor trong khoảng [0, 10)
# với step=1?
numpy_array = np.arange(0, 10, 1)

print("NumPy array:")
print(numpy_array)

tensorflow_tensor = tf.constant(list(range(0, 10)), dtype=tf.float32)

print("TensorFlow tensor:")
print(tensorflow_tensor)

pytorch_tensor = torch.arange(0, 10, 1)

print("\PyTorch tensor:")
print(pytorch_tensor)

# Câu 2: Hãy viết chương trình tạo Numpy array, Tensorflow tensor, Pytorch tensor là ma trận đơn vị
# với kích thước (3, 3).
numpy_identity_matrix = np.eye(3)

print("NumPy array - Identity matrix:")
print(numpy_identity_matrix)

tensorflow_identity_matrix = tf.eye(3)

print("\nTensorFlow tensor - Identity matrix:")
print(tensorflow_identity_matrix)

pytorch_identity_matrix = torch.eye(3)

print("\nPyTorch tensor - Identity matrix:")
print(pytorch_identity_matrix)


# Câu 3: Hãy viết chương trình tạo Numpy array, Tensorflow tensor, Pytorch tensor ngẫu nhiên trong
# khoảng giá trị [0, 1] với kích thước (3, 4). Tiếp theo hãy tạo array, tensor với các giá trị là số nguyên
# trong khoảng [-10, 10]. Lưu ý trong bài tập này, các bạn sẽ sử dụng seed = 2024 để dảm bảo ra kết quả
# giống đáp án, cách sử dụng như sau:
np.random.seed(2024)

numpy_random_array = np.random.rand(3, 4)

print("NumPy array - Random values in [0, 1]:")
print(numpy_random_array)

numpy_random_integer_array = np.random.randint(-10, 11, size=(3, 4))

print("NumPy array - Random integers in [-10, 10]:")
print(numpy_random_integer_array)


tf.random.set_seed(2024)
tensorflow_random_tensor = tf.random.uniform((3, 4), minval=0, maxval=1)

print("TensorFlow tensor - Random values in [0, 1]:")
print(tensorflow_random_tensor)

tensorflow_random_integer_tensor = tf.random.uniform((3, 4), minval=-10, maxval=11, dtype=tf.int32)

print("\nTensorFlow tensor - Random integers in [-10, 10]:")
print(tensorflow_random_integer_tensor)


torch.manual_seed(2024)
pytorch_random_tensor = torch.rand(3, 4)

print("PyTorch tensor - Random values in [0, 1]:")
print(pytorch_random_tensor)

pytorch_random_integer_tensor = torch.randint(-10, 11, (3, 4))

print("\nPyTorch tensor - Random integers in [-10, 10]:")
print(pytorch_random_integer_tensor)