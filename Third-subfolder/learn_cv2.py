"""
Для преобразования между BGR и RGB в OpenCV

import cv2

# Загрузка изображения в BGR
image_bgr = cv2.imread('image.jpg')

# Преобразование BGR в RGB
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
"""

"""
Сохраняет изменённое изображение в отдельный файл
cv2.imwrite('gray_photo.png', gray_image)
"""
"""
С помощью этого можем узнать размер изображения 
height, width, channels = image.shape
print(f"Ширина: {width}, Высота: {height}, Каналы: {channels}")
"""
# image[220, 35] = [0, 0, 0] - так мы можем менять цвет пикселя, обращаясь к нему

# blue, green, red = image[20, 35] 
# print(blue, green, red) - так мы можем узнать цвет пикселя, обратившись к нему

# reduce_image = cv2.resize(image, (1280, 720), cv2.INTER_AREA) - для уменьшения формата изображения

import cv2

image = cv2.imread('for_test.png')
cut_image = image[400:1055, 230:1305]

height = cut_image.shape[0]
for frame in range(height):
    for t_b in range(0, 5):
        cut_image[frame, t_b] = [0, 0, 0]
        cut_image[frame, -t_b] = [0, 0, 0]
width = cut_image.shape[1]
for frame_2 in range(width):
    for l_r in range(0, 5):
        cut_image[frame_2, l_r] = [0, 0, 0]
        cut_image[frame_2, -l_r] = [0, 0, 0]

cv2.imshow('screen', cut_image)
cv2.waitKey(0)




