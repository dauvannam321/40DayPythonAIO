import numpy as np
import tensorflow as tf
import torch
# Câu 1: Hãy viết chương trình tạo Numpy array, Tensorflow tensor, Pytorch tensor từ danh sách 1
# chiều?
lst_1D = [1, 2, 3]

np_arr = np.array(lst_1D)
print("Numpy array 1D:", np_arr)

tf_arr = tf.convert_to_tensor(lst_1D)
print("Tensorflow array 1D:", tf_arr)

torch_arr = torch.tensor(lst_1D)
print("Torch array 1D:", torch_arr)

# Câu 2: Hãy viết chương trình tạo Numpy array, Tensorflow tensor, Pytorch tensor từ danh sách 2
# chiều. Sau đó thực hiện kiểm tra thuộc tính shape, dtype, type, device từ các array, tensor vừa tạo ?
lst_2D = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

arr_2D = np.array(lst_2D)
print("Hình dạng của mảng:", arr_2D.shape )
print("Kiểu dữ liệu của mảng: ", arr_2D.dtype)
print("Loại của mảng:", type(arr_2D))
print ("Mảng :\n", arr_2D )

arr_2D = tf.convert_to_tensor(lst_2D)
print("Hình dạng của mảng:", arr_2D.shape )
print("Kiểu dữ liệu của mảng: ", arr_2D.dtype)
print("Loại của mảng:", type(arr_2D))
print ("Mảng :\n", arr_2D )

arr_2D = torch.tensor(lst_2D)
print("Hình dạng của mảng:", arr_2D.shape )
print("Kiểu dữ liệu của mảng: ", arr_2D.dtype)
print("Loại của mảng:", type(arr_2D))
print ("Mảng :\n", arr_2D )