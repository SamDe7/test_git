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

# import cv2

# image = cv2.imread('for_test.png')
# cut_image = image[400:1055, 230:1305]

# height = cut_image.shape[0]
# for frame in range(height):
#     for t_b in range(0, 5):
#         cut_image[frame, t_b] = [0, 0, 0]
#         cut_image[frame, -t_b] = [0, 0, 0]
# width = cut_image.shape[1]
# for frame_2 in range(width):
#     for l_r in range(0, 5):
#         cut_image[l_r, frame_2] = [0, 0, 0]
#         cut_image[-l_r, frame_2] = [0, 0, 0]

# cv2.imshow('screen', cut_image)
# cv2.waitKey(0)

# import cv2

# picture = cv2.imread('for_learning.png', cv2.IMREAD_GRAYSCALE)

# height = picture.shape[0]
# width = picture.shape[1]

# # height = picture.shape[0]
# # width = picture.shape[1]
# # reduced_img = cv2.resize(picture,  (int(width/2), int(height/2)), cv2.INTER_AREA)
# matrix = cv2.getRotationMatrix2D((int(height/2), int(width/2)), 90, 0.6)
# rotation_img = cv2.warpAffine(picture, matrix, (picture.shape[1], picture.shape[0]))
# stat = cv2.namedWindow('logo', cv2.WINDOW_NORMAL)
# static_pictire = cv2.resizeWindow('logo', (1280, 720))
# cv2.imshow('logo', rotation_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2

# def click(event, x, y, flags, params):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         blue = img[y, x, 0]
#         green = img[y, x, 1]
#         red = img[y, x, 2]

#         print(f'Координаты точки: x = {x}; y = {y}')
#         print(f'BGR код точки: b = {blue}; g = {green}; r = {red}\n')

#         font = cv2.FONT_ITALIC
#         cv2.putText(img, f"{x}, {y}", (x, y),
#                     font, 4, (0, 0, 0), 2)

#         cv2.imshow('logo', img)


#     if event == cv2.EVENT_RBUTTONDOWN:
#         blue = img[y, x, 0]
#         green = img[y, x, 1]
#         red = img[y, x, 2]

#         print(f'Координаты точки: x = {x}; y = {y}')
#         print(f'BGR код точки: b = {blue}; g = {green}; r = {red}\n')

#         font = cv2.FONT_ITALIC
#         cv2.putText(img, f"x = {x}, y = {y}", (x, y), font, 4, (0, 0, 0), 2)
#         cv2.imshow('logo', img)


# img = cv2.imread('for_learning.png')
#     # stat = cv2.namedWindow('pica', cv2.WINDOW_NORMAL)
#     # static = cv2.resizeWindow('pica', (1280, 720))
# cv2.imshow('pica', img)
# cv2.setMouseCallback('pica', click)
# cv2.waitKey(0)
# cv2.imwrite('position_click.png', img)

# import pandas as pd
# import matplotlib as plt


# def click(event, x, y, flags, param):
#     if event == cv2.EVENT_RBUTTONDOWN:
#         b = img[y, x, 0]
#         g = img[y, x, 1]
#         r = img[y, x, 2]
#         font = cv2.FONT_HERSHEY_COMPLEX
#         cv2.putText(img, f'b {b}, g {g}, r {r}', (x, y), font, 2, (0, 0, 220), 2)
#         cv2.imshow('pica', img)

#     if event == cv2.EVENT_LBUTTONDOWN:
#         img[y, x]
#         font = cv2.FONT_HERSHEY_COMPLEX
#         cv2.putText(img, f'x {x}, y {y}', (x, y), font, 2, (192, 210, 43), 3)
#         cv2.imshow('pica', img)

# img = cv2.imread('for_test.png')
# cv2.namedWindow('pica', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('pica', (1280, 720))
# cv2.imshow('pica', img)
# cv2.setMouseCallback('pica', click)
# while True: 
#     if cv2.waitKey(0) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()

# import cv2

# # создаём переменную с файлом модели
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# # читаем изображение
# image = cv2.imread('for_learning.png')

# # обесцвечиваем изображение
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # находим лица на обесцвеченном изображении
# faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

# # на цветном изображении рисуем квадраты там, где нашли лица на обесцвеченном
# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

# # открываем изображение в отдельном окне
# cv2.namedWindow('found_faces', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('found_faces', (1280, 720))
# cv2.imshow('found_faces', image)
# while True:
#     if cv2.waitKey(0) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()

class MyList:
    def __init__(self, data_list):
        self._data = data_list

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

# Пример использования
my_list = MyList([10, 15, 20])
my_list[1, 2] = 16  # Теперь это будет работать
print(my_list._data)  # Вывод: [10, 16, 20]
