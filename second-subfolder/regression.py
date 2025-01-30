import numpy as np
import matplotlib.pyplot as mat 

years = [2020, 2021, 2022, 2023]
users_android = [65, 77, 82, 84]
users_ios = [34, 56, 64, 71]

# mat.pie(coef, labels=libs, autopct='%1.1f') - для создания круговой диаграммы
# mat.bar(x, y, color='black') - для создания гистограммы
# mat.scatter(x, y) - для создания графика рассеивания
# mat.plot(x, y, color='green', marker='o', markersize=7) - для создания грфика функции
width = 0.35
fig, ax = mat.subplots()
ax.bar(years, users_android, width, label='Устройства android')
ax.bar(years, users_ios, width, bottom=users_android, label='Устройства ios')

ax.set_ylabel('Процентное соотношение')
ax.set_title('Устройства andriod и ios')
ax.legend(loc='best', title='Устройства')

mat.show()