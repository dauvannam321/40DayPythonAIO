import numpy as np
import tensorflow as tf
import torch
# Câu 1: Hãy viết chương trình sử dụng hàm zeros tạo Numpy array, Tensorflow tensor, Pytorch tensor
# chỉ chứa giá trị là số 0 với kích thước (3, 4)?
print("--- Câu 1 ---")
np_arr = np.zeros((3,4))
print("Numpy array: \n", np_arr)

tf_tensor = tf.zeros((3,4))
print("Tensorflow tensor: \n", tf_tensor)

torch_tensor = torch.zeros((3,4))
print("Torch tensor: \n", torch_tensor)

# Câu 2: Hãy viết chương trình sử dụng hàm ones tạo Numpy array, Tensorflow tensor, Pytorch tensor
# chỉ chứa giá trị là số 1 với kích thước (3, 4)?
print("--- Câu 2 ---")
np_arr = np.ones((3,4))
print("Numpy array: \n", np_arr)

tf_tensor = tf.ones((3,4))
print("Tensorflow tensor: \n", tf_tensor)

torch_tensor = torch.ones((3,4))
print("Torch tensor: \n", torch_tensor)

# Câu 3: Hãy viết chương trình tạo Numpy array, Tensorflow tensor, Pytorch tensor chỉ chứa giá trị là
# số 5 với kích thước (3, 4)?
print("--- Câu 3 ---")
np_arr = np.full((3,4), 5)
print("Numpy array: \n", np_arr)

tf_tensor = tf.fill((3,4), 5)
print("Tensorflow tensor: \n", tf_tensor)

torch_tensor = torch.full((3,4), 5)
print("Torch tensor: \n", torch_tensor)
