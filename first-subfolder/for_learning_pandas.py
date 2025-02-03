# import pandas as pd
"""
city = {"Город" : ['Москва', 'Питер', 'Новосибирск'],
        "Year" : [1147, 1703, 1893],
        "The population" : [11.9, 4.9, 1.5]
        }
datfr_ex = pd.DataFrame(city)
print(datfr_ex)
"""
# import pandas as pd

# students_performance = pd.read_csv('StudentsPerformance.csv') 
# # print(students_performance.groupby('race').aggregate({'writing score' : 'mean'}))
# # s_p_with_names = students_performance.iloc[[0, 3, 4, 7, 8]]
# s_p_with_names.index = ['Puki', 'Naki', 'Kaki', 'Lyaa']
# # print(s_p_with_names.loc[['Maikl', 'Lyaa'], ['gender', 'writing score']])
# first = pd.Series([1, 2, 3], index=['one', 'two', 'three'])
# second = pd.Series([4, 5, 6], index=['one', 'two', 'three'])
# united = pd.DataFrame({'column_1' : first,
#                         'column_2' : second})
# print(united['column_1'])
# print(len(students_performance[students_performance['lunch'] == 'free/reduced']) / len(students_performance['lunch']))

# print(students_performance.groupby('lunch').aggregate({'math score':['count', 'mean', 'std'],
#                                                         'reading score':['count', 'mean', 'std'],
#                                                          'writing score':['count', 'mean', 'std']}))
# print(students_performance.groupby('lunch').describe())

# students_performance = students_performance.rename( columns={'parental level of education' : 'parental_level_of_education',
#                                                              'test preparation course' : 'test_preparation_course',
#                                                             'math score' : 'math_score', 'reading score' : 'reading_score',
#                                                             'writing score' : 'writing_score'
#                                                             })
# writed_mean = 99
# print(students_performance.query("writing_score > @writed_mean"))
# columns_name = [ i for i in students_performance if 'score' in i]

# print(students_performance.filter(like='c', axis=1))
# cut_students = students_performance.rename(index= {0 : 'zero', 1 : 'first'}).iloc[:5]
# print(cut_students.filter(like='first'))
# sub_1 = students_performance.loc[(students_performance['writing_score'] > 70) & (students_performance['reading_score'] >= 90)]
# print(students_performance.query('writing_score >= 70 & reading_score >= 90'))

# my_stat = pd.read_csv('my_stat.csv')
# subset_1 = my_stat[(my_stat['V1'] > 0) & (my_stat['V3'] == 'A')]
# subset_2 = my_stat.query('V2 != 10 | V4 <= 1')



# import pandas as pd
# import numpy as np


# mean_scores.set_index(['gender', 'race/ethnicity'], inplace=True)
# print(mean_scores.loc[('female', 'group A')])
# print(students_performance.groupby(['gender', 'race/ethnicity']).math_score.nunique())
# print(students_performance.sort_values(['gender', 'writing_score'], ascending=False).groupby('gender').head(5))

# students_performance = pd.read_csv('StudentsPerformance.csv')
# students_performance = students_performance.rename(columns= {'parental level of education' : 'parental_level_of_education',
#                                                              'test preparation course' : 'test_preparation_course',
#                                                             'math score' : 'math_score', 'reading score' : 'reading_score',
#                                                             'writing score' : 'writing_score'})
# mean_scores = students_performance.groupby(['gender', 'race/ethnicity'], as_index=False).aggregate({'writing_score' : 'mean', 'reading_score' : 'mean'}).rename(
#     columns={'writing_score' : 'mean_w_sc', 'reading_score' : 'mean_r_sc'}
# )

# students_performance['total_score'] = students_performance.math_score + students_performance.reading_score


# students_performance = students_performance.assign(total_score_log = np.log(students_performance.total_score))
# print(students_performance.drop(['total_score'], axis=1))

# my_stat = pd.read_csv('my_stat.csv')
# subset_1 = my_stat.iloc[:10, [0, 2]]
# subset_2 = my_stat.iloc[:, [1, 3]].drop([0, 4], axis=0)
# print(subset_2)

# my_stat = pd.read_csv('my_stat.csv')

# my_stat['V5'] = my_stat.V1 + my_stat.V4
# my_stat = my_stat.assign(V6 = np.log(my_stat.V2))
# print(my_stat)

# my_stat = pd.read_csv('my_stat.csv')

# my_stat.rename(columns={
#         'V1' : 'session_value',
#         'V2' : 'group',
#         'V3' : 'time',
#         'V4' : 'n_users'
# }, inplace=True)
# print(my_stat)

# dota = pd.read_csv('dota_hero_stats.csv')
# groups = dota.nunique()
# print(groups)

# salary = pd.read_csv('accountancy.csv')
# income = salary.groupby(['Executor', 'Type']).Salary.mean()
# print(income)

# dota = pd.read_csv('dota_hero_stats.csv')
# des = dota.groupby(['attack_type', 'primary_attr']).agg({'id' : 'count'}).idxmax()
# print(des)

"""
import pandas as pd

# Пример DataFrame
data = {
    'attack_type': ['melee', 'ranged', 'melee', 'magic', 'ranged'],
    'primary_attr': ['strength', 'agility', 'strength', 'intelligence', 'agility'],
    'other_column': [1, 2, 3, 4, 5]
}

df = pd.DataFrame(data)

# Применение кода
result = df.filter(items=['attack_type', 'primary_attr']).mode()
print(result)
Данный код ищет моды представленных колонок и выводит их
"""

# concentrations = pd.read_csv('algae(1).csv')
# mean_concentrations = concentrations.groupby('genus').agg({'sucrose' : 'mean', 'alanin' : 'mean', 'citrate' : 'mean',
# 'glucose' : 'mean', 'oleic_acid' : 'mean'})
# print(mean_concentrations)

# concentrations = pd.read_csv('algae(1).csv')
# conc = concentrations.query('genus=="Fucus"').agg({'alanin': ['min', 'mean', 'max']}).round(2)
# print(conc)

# df = pd.read_csv('algae(2).csv')
# print(df.groupby('group').agg(res = ('sucrose', lambda x: x.max() - x.min())))

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# students_performance = pd.read_csv('StudentsPerformance.csv')
# # students_performance.plot.scatter(x = 'math score', y = 'reading score')
# # plt.show()

# ax = sns.lmplot(x = 'math score', y = 'reading score', data=students_performance, hue='lunch', fit_reg=False)
# ax.set_xlabels('Mathematics')
# ax.set_ylabels('Reading')
# plt.show()

# salary = pd.read_csv('income.csv')

# # plt.plot(salary.index, salary.income)
# # salary.plot(kind='line')
# # salary['income'].plot()
# # sns.lineplot(data=salary)
# # salary.income.plot()
# # salary.plot()
# # sns.lineplot(x=salary.index, y = salary.income)
# plt.show()

# df = pd.read_csv("genome_matrix(1).csv", index_col=0)
# g = sns.heatmap(df, cmap='rainbow')
# g.xaxis.set_ticks_position('top')
# g.xaxis.set_tick_params(rotation=90)
# plt.show()

# np.random.seed(255)
# data = np.random.rand(28, 28)
# plt.imshow(data, cmap='rainbow')
# plt.show()

# dota = pd.read_csv('dota_hero_stats(1).csv')
# dota['count roles '] = dota['roles'].map(lambda x: len(x.split(',')))
# dota['count roles '].hist()
# plt.show()

iris = pd.read_csv('iris.csv')
gist = iris.groupby(['sepal length','sepal width','petal length','petal width']).agg(('sepal length'))
plt.show()

