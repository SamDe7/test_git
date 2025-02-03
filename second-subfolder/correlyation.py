# import numpy as np
# # x = np.array([1, 2, 10, 1, 5])
# # y = np.array([4, 6, 4, 12, 6])

# # correlation = np.corrcoef(x, y)
# # corr = correlation[0, 1]
# # print(corr)

# x = np.array([1, 3, 5])
# y = np.array([[10, 11, 10], [12, 14, 12]])
# correlaytion = np.correlate(y)
# # corr = correlaytion[0, 1]
# print(correlaytion)

# import numpy as np
# import matplotlib.pyplot as plt

# # Определение коэффициентов параболы
# a = -1
# b = 0
# c = 0

# # Создание массива значений x
# x = np.linspace(-5, 3, 50)  # от -10 до 10, 400 точек

# # Вычисление значений y
# y = a * x**2 + b * x + c

# # Построение графика
# plt.figure(figsize=(8, 6))
# plt.plot(x, y, label=f'y = {a}x² + {b}x + {c}', color='red')
# plt.title('График параболы')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.axhline(10, color='yellow',linewidth=0.5, ls='--')  # ось X
# plt.axvline(10, color='blue',linewidth=0.5, ls='--')  # ось Y
# plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
# plt.legend()
# plt.xlim(-10, 10)
# plt.ylim(-100, 1)
# plt.show()
