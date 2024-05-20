import torch
import numpy as np
import tensorflow as tf

# Câu 1: Hãy viết chương trình tạo Numpy 2 array, Pytorch tensor với từ list 1 có giá trị [1, 2, 3], list 2
#  có giá trị [4, 5, 6]. Sau đó sử dụng hàm hstack để nối theo trục ngang và vstack để nối theo trục dọc?

# Tạo list 1 và list 2
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Tạo mảng NumPy từ list 1 và list 2
numpy_array1 = np.array(list1)
numpy_array2 = np.array(list2)

# Tạo tensor PyTorch từ list 1 và list 2
torch_tensor1 = torch.tensor(list1)
torch_tensor2 = torch.tensor(list2)

# Sử dụng hstack để nối theo trục ngang (axis=1)
numpy_horizontal_stack = np.hstack((numpy_array1.reshape(-1, 1), numpy_array2.reshape(-1, 1)))
torch_horizontal_stack = torch.stack((torch_tensor1, torch_tensor2), dim=1)

# Sử dụng vstack để nối theo trục dọc (axis=0)
numpy_vertical_stack = np.vstack((numpy_array1, numpy_array2))
torch_vertical_stack = torch.stack((torch_tensor1, torch_tensor2))

print("Nối theo trục ngang (NumPy):")
print(numpy_horizontal_stack)

print("\nNối theo trục ngang (PyTorch):")
print(torch_horizontal_stack)

print("\nNối theo trục dọc (NumPy):")
print(numpy_vertical_stack)

print("\nNối theo trục dọc (PyTorch):")
print(torch_vertical_stack)

#  Câu 2: Hãy viết chương trình tạo Numpy 2 array, Pytorch tensor, Tensorflow tensor từ list 2D là [[1 ,
#  2 , 3] , [4 , 5 , 6]] và [[7 , 8 , 9] , [10 , 11 , 12]]. Sau đó sử dụng hàm concanate để nối theo trục ngang
#  và vstack để nối theo trục dọc?

# List 2D đã cho
list_2d_1 = [[1, 2, 3], [4, 5, 6]]
list_2d_2 = [[7, 8, 9], [10, 11, 12]]

# Tạo mảng NumPy từ list 2D đã cho
numpy_array1 = np.array(list_2d_1)
numpy_array2 = np.array(list_2d_2)

# Tạo tensor PyTorch từ list 2D đã cho
torch_tensor1 = torch.tensor(list_2d_1)
torch_tensor2 = torch.tensor(list_2d_2)

# Tạo tensor TensorFlow từ list 2D đã cho
tf_tensor1 = tf.constant(list_2d_1)
tf_tensor2 = tf.constant(list_2d_2)

# Sử dụng concatenate để nối theo trục ngang
numpy_concatenate = np.concatenate((numpy_array1, numpy_array2), axis=1)
torch_concatenate = torch.cat((torch_tensor1, torch_tensor2), dim=1)
tf_concatenate = tf.concat([tf_tensor1, tf_tensor2], axis=1)

# Sử dụng vstack để nối theo trục dọc
numpy_vstack = np.vstack((numpy_array1, numpy_array2))
torch_vstack = torch.cat((torch_tensor1, torch_tensor2), dim=0)
tf_vstack = tf.concat([tf_tensor1, tf_tensor2], axis=0)

print("Nối theo trục ngang (NumPy):")
print(numpy_concatenate)

print("\nNối theo trục ngang (PyTorch):")
print(torch_concatenate)

print("\nNối theo trục ngang (TensorFlow):")
print(tf_concatenate)

print("\nNối theo trục dọc (NumPy):")
print(numpy_vstack)

print("\nNối theo trục dọc (PyTorch):")
print(torch_vstack)

print("\nNối theo trục dọc (TensorFlow):")
print(tf_vstack)