import numpy as np
import torch
import tensorflow as tf

# List 3D
lst_3d = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]]

# Numpy array
np_array = np.array(lst_3d)

# Slicing để lấy một phần của array, tensor tại vị trí index (0, 1) của mảng 2D trong mảng 3D và giữ nguyên số chiều
np_sliced_keep_dim = np_array[:, 0:2, :]

# Slicing để lấy một phần của array, tensor tại vị trí index (0, 1) của mảng 2D trong mảng 3D, nhưng giảm dim một chiều
np_sliced_reduce_dim = np_array[:, 0:2, :].reshape(3, 6)

# PyTorch tensor
torch_tensor = torch.tensor(lst_3d)

# Slicing để lấy một phần của tensor tại vị trí index (0, 1) của mảng 2D trong mảng 3D và giữ nguyên số chiều
torch_sliced_keep_dim = torch_tensor[:, 0:2, :]

# Slicing để lấy một phần của tensor tại vị trí index (0, 1) của mảng 2D trong mảng 3D, nhưng giảm dim một chiều
torch_sliced_reduce_dim = torch_tensor[:, 0:2, :].view(3, 6)

# Tensorflow tensor
tf_tensor = tf.constant(lst_3d)

# Slicing để lấy một phần của tensor tại vị trí index (0, 1) của mảng 2D trong mảng 3D và giữ nguyên số chiều
tf_sliced_keep_dim = tf_tensor[:, 0:2, :]

# Slicing để lấy một phần của tensor tại vị trí index (0, 1) của mảng 2D trong mảng 3D, nhưng giảm dim một chiều
tf_sliced_reduce_dim = tf.reshape(tf_tensor[:, 0:2, :], (3, 6))

print("Numpy array sliced (keep dim):\n", np_sliced_keep_dim)
print("\nNumpy array sliced (reduce dim):\n", np_sliced_reduce_dim)
print("\nPytorch tensor sliced (keep dim):\n", torch_sliced_keep_dim)
print("\nPytorch tensor sliced (reduce dim):\n", torch_sliced_reduce_dim)
print("\nTensorflow tensor sliced (keep dim):\n", tf_sliced_keep_dim)
print("\nTensorflow tensor sliced (reduce dim):\n", tf_sliced_reduce_dim)
