import torch
import numpy as np
import tensorflow as tf

# Câu 1
# List 2D được cung cấp
list_2d = [[1, 0, 1],
           [0, 1, 0],
           [1, 0, 1]]

# Chuyển list 2D thành tensor PyTorch
tensor_2d = torch.tensor(list_2d)

# Lấy hàng thứ 2 (index=1) giữ nguyên số chiều
row_index_1 = tensor_2d[1].unsqueeze(0)
row_index_1_keep_dim = tensor_2d[1:2]

# Lấy cột thứ nhất (index=0) giữ nguyên số chiều
col_index_0 = tensor_2d[:, 0].unsqueeze(1)
col_index_0_keep_dim = tensor_2d[:, :1]

print("Row index 1:")
print(row_index_1)
print(row_index_1_keep_dim)

print("\nColumn index 0:")
print(col_index_0)
print(col_index_0_keep_dim)

# Câu 2
# Set seed for reproducibility
# Đặt seed
np.random.seed(2024)

# Tạo mảng numpy
numpy_array = np.random.randint(-10, 10, size=(3, 3))

# Lọc các phần tử lớn hơn 0
filtered_numpy_array = numpy_array[numpy_array > 0]

print("Numpy Array:")
print(numpy_array)
print("Filtered Array:")
print(filtered_numpy_array)

# Đặt seed
torch.manual_seed(2024)

# Tạo tensor PyTorch
torch_tensor = torch.randint(-10, 10, size=(3, 3))

# Lọc các phần tử lớn hơn 0
filtered_torch_tensor = torch_tensor[torch_tensor > 0]

print("\nPyTorch Tensor:")
print(torch_tensor)
print("Filtered Tensor:")
print(filtered_torch_tensor)

# Đặt seed
tf.random.set_seed(2024)

# Tạo tensor TensorFlow
tf_tensor = tf.random.uniform((3, 3), minval=-10, maxval=10, dtype=tf.int32)

# Lọc các phần tử lớn hơn 0
filtered_tf_tensor = tf.boolean_mask(tf_tensor, tf_tensor > 0)

print("\nTensorFlow Tensor:")
print(tf_tensor)
print("Filtered Tensor:")
print(filtered_tf_tensor)