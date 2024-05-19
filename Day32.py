import cv2
import matplotlib.pyplot as plt

image = cv2.imread('data\\2.jpg', flags=0)

# Bước 2: Chuyển đổi ảnh từ BGR sang RGB (vì OpenCV sử dụng BGR, còn matplotlib sử dụng RGB)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Bước 3: Thay đổi kích thước của ảnh theo kích thước tùy chỉnh
# Ví dụ: đặt kích thước tùy chỉnh là 300x200 pixels
width = 300
height = 200
dim = (width, height)

# Thay đổi kích thước ảnh
resized_image = cv2.resize(image_rgb, dim, interpolation=cv2.INTER_AREA)
img_filtered1 = cv2.GaussianBlur(resized_image, (5, 5), 2.5)
img_filtered2 = cv2.GaussianBlur(resized_image, (5, 5), 5.0)
img_filtered3 = cv2.GaussianBlur(resized_image, (5, 5), 10.0)

# Bước 4: Hiển thị ảnh bằng matplotlib
# Hiển thị ảnh bằng matplotlib
plt.figure(figsize=(10, 5))  # Đặt kích thước của cửa sổ hiển thị (15x10 inches)

# Ảnh 1
plt.subplot(2, 2, 1)
plt.imshow(resized_image)
plt.title('Origin Image')
plt.axis('off')  # Ẩn trục

# Ảnh 2
plt.subplot(2, 2, 2)
plt.imshow(img_filtered1)
plt.title('Sigma = 2.5')
plt.axis('off')  # Ẩn trục

# Ảnh 3
plt.subplot(2, 2, 3)
plt.imshow(img_filtered2)
plt.title('Sigma = 5.0')
plt.axis('off')  # Ẩn trục

# Ảnh 4
plt.subplot(2, 2, 4)
plt.imshow(img_filtered3)
plt.title('Sigma = 10.0')
plt.axis('off')  # Ẩn trục

plt.show()
