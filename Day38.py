import numpy as np
import torch
import tensorflow as tf

# Câu 1: Viết chương trình tạo một Numpy array, Pytorch tensor, Tensorflow tensor từ list 1D có giá
# trị [2, 3, 5, 7]. Sau đó thực hiện thêm một chiều mới ở vị trí 0 để tạo array, tensor 2D. Sau đó tiếp tục
# thêm các chiều mới ở vị trí 1, 3 và 4 để tạo array, tensor 5D.

# List 1D
lst = [2, 3, 5, 7]

# Numpy array
np_array = np.array(lst)
np_array_2d = np.expand_dims(np_array, axis=0)
np_array_5d = np.expand_dims(np_array_2d, axis=(1, 3, 4))

# Pytorch tensor
torch_tensor = torch.tensor(lst)
torch_tensor_2d = torch_tensor.unsqueeze(0)
torch_tensor_5d = torch_tensor_2d.unsqueeze(1).unsqueeze(3).unsqueeze(4)

# Tensorflow tensor
tf_tensor = tf.constant(lst)
tf_tensor_2d = tf.expand_dims(tf_tensor, axis=0)
tf_tensor_5d = tf.expand_dims(tf.expand_dims(tf.expand_dims(tf_tensor_2d, axis=1), axis=3), axis=4)

print("Numpy array 5D:\n", np_array_5d)
print("\nPytorch tensor 5D:\n", torch_tensor_5d)
print("\nTensorflow tensor 5D:\n", tf_tensor_5d)


# # Câu 2: Hãy viết chương trình để tạo một numpy array, một PyTorch tensor và một TensorFlow tensor
# # từ một list 3D có giá trị như sau: [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]]. Sau đó, sử dụng hàm reshape để thay đổi hình dạng của array và tensor 3D vừa tạo có shape (3, 2, 3)
# # thành array và tensor 2D có shape (3, 6).
# List 3D
lst_3d = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]]

# Numpy array
np_array = np.array(lst_3d)
np_array_reshaped = np_array.reshape(3, 6)

# PyTorch tensor
torch_tensor = torch.tensor(lst_3d)
torch_tensor_reshaped = torch_tensor.view(3, 6)

# Tensorflow tensor
tf_tensor = tf.constant(lst_3d)
tf_tensor_reshaped = tf.reshape(tf_tensor, (3, 6))

print("Numpy array 2D:\n", np_array_reshaped)
print("\nPytorch tensor 2D:\n", torch_tensor_reshaped)
print("\nTensorflow tensor 2D:\n", tf_tensor_reshaped)
