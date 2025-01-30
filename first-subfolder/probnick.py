# import numpy as np 

# arr = np.array([[[1, 2, 3], [4, 5, 6]],
#                 [[7, 8, 9], [10, 11, 12]],
#                 [[13, 14, 15], [16, 17, 18]]]
#                 )
# arr[:, :, 1] = [123, 456]
# print(arr)

# z1 = np.complex128(3, 4)    # Это будет равно 3 + 4j
# z2 = np.complex128(1, 2)    # Это будет равно 1 + 2j

# # Сложение
# z_sum = z1 + z2
# print("Сумма:", z_sum)

# # Умножение
# z_product = z1 * z2
# print("Произведение:", z_product)

# Модуль (длина) комплексного числа
# modulus = np.abs(z1)
# print("Модуль z1:", modulus)

# # Аргумент (угол) комплексного числа

# print(np.eye(N=3, M=5, k=-1))

# print(np.empty((3, 3)))


# matrix_2 = np.array([6, 7, 8, 9, 10])
# print(np.cos(matrix_2))

# перемножение матрицы по правилам линейной алгебры:
# |||||||||||||||||||||||||||||||||||||
# matrix_1 = np.array([1, 2, 3, 4, 5])
# matrix_2 = np.array([6, 7, 8, 9, 10])  
# print(np.multiply(matrix_1, matrix_2))
# |||||||||||||||||||||||||||||||||||||||

# В NumPy агрегатные функции — это методы, которые применяются к массиву и возвращают одно итоговое значение. Общая формула: агрегатор.массив().

# matrix = np.array([[1, 2, 3,], [4, 5, 6]])
# meann = matrix.mean(axis=1)
# print(meann)

# dis = matrix.var()
# print(dis)

# mul = matrix.prod(axis=0)
# print(mul)

# new_mat = matrix.copy()
# new_mat[new_mat == 1] = 10
# print(matrix)
# print(new_mat)

# changed_matrix = matrix.reshape(3, 2)
# print(changed_matrix)

# print(np.resize(matrix, (5, 1)))
# print(np.random.randn(3, 2))

from for_learning_pandas import calc

res = calc(5, 3)
print(res)