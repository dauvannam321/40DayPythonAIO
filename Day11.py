import numpy as np
import tensorflow as tf
import torch

# Câu 1: Viết chương trình tạo hai Numpy array, Pytorch tensor, Tensorflow tensor với các giá trị số
# nguyên ngẫu nhiên trong khoảng [-10, 10) với kích thước (3, 4). Sau đó chuyển vị array, tensor thứ 2
# và thực hiện phép nhân matrix multiplication. Lưu ý: sử dụng seed=2024

# Set random seed
np.random.seed(2024)
torch.manual_seed(2024)
tf.random.set_seed(2024)

numpy_array = np.random.randint(-10, 10, size=(3, 4))
torch_tensor = torch.randint(-10, 10, size=(3, 4))
tensorflow_tensor = tf.random.uniform((3, 4), minval=-10, maxval=10, dtype=tf.int32)

numpy_array_transpose = np.transpose(numpy_array)
torch_tensor_transpose = torch_tensor.t()
tensorflow_tensor_transpose = tf.transpose(tensorflow_tensor)

result_numpy = np.dot(numpy_array_transpose, numpy_array)
result_torch = torch.matmul(torch_tensor_transpose, torch_tensor)
result_tensorflow = tf.matmul(tensorflow_tensor_transpose, tensorflow_tensor)

print("NumPy Result:")
print(result_numpy)
print("\nPyTorch Result:")
print(result_torch)
print("\nTensorFlow Result:")
print(result_tensorflow)

# Câu 2: Viết chương trình tạo một Numpy array, Pytorch tensor, Tensorflow tensor với các giá trị số
# nguyên ngẫu nhiên trong khoảng [-10, 10) với kích thước (3, 3). Sau đó hãy tính tổng của toàn bộ
# tensor, array, tiếp theo tính tổng theo chiều dọc, chiều ngang . Lưu ý: sử dụng seed=2024
numpy_array = np.random.randint(-10, 10, size=(3, 3))
torch_tensor = torch.randint(-10, 10, size=(3, 3))
tensorflow_tensor = tf.random.uniform((3, 3), minval=-10, maxval=10, dtype=tf.int32)

# Calculate sum of the entire tensor/array
sum_numpy_all = np.sum(numpy_array)
sum_torch_all = torch.sum(torch_tensor)
sum_tensorflow_all = tf.reduce_sum(tensorflow_tensor)

# Calculate sum along axis 0 (vertical sum)
sum_numpy_axis0 = np.sum(numpy_array, axis=0)
sum_torch_axis0 = torch.sum(torch_tensor, dim=0)
sum_tensorflow_axis0 = tf.reduce_sum(tensorflow_tensor, axis=0)

# Calculate sum along axis 1 (horizontal sum)
sum_numpy_axis1 = np.sum(numpy_array, axis=1)
sum_torch_axis1 = torch.sum(torch_tensor, dim=1)
sum_tensorflow_axis1 = tf.reduce_sum(tensorflow_tensor, axis=1)

print("Sum of the entire array/tensor:")
print("NumPy:", sum_numpy_all)
print("PyTorch:", sum_torch_all)
print("TensorFlow:", sum_tensorflow_all)

print("\nSum along axis 0 (vertical sum):")
print("NumPy:", sum_numpy_axis0)
print("PyTorch:", sum_torch_axis0)
print("TensorFlow:", sum_tensorflow_axis0)

print("\nSum along axis 1 (horizontal sum):")
print("NumPy:", sum_numpy_axis1)
print("PyTorch:", sum_torch_axis1)
print("TensorFlow:", sum_tensorflow_axis1)