import pandas as pd
import numpy as np

np.random.seed(80)
df = pd.DataFrame(np.random.rand(4, 4), columns=list("ABCD"))

#  1、pandas的版本号
print(pd.__version__)

# 2、从列表创建Series
list_alpha = [i for i in range(10)]
series_alpha = pd.Series(list_alpha)

# 3、字典创建Series
key_alpha = [i for i in "abcd"]
val_alpha = [i for i in range(5)]
dict_alpha = dict(zip(key_alpha, val_alpha))
series_beta = pd.Series(dict_alpha)

# 5、 Numpy 数组创建DataFrame
dates = pd.date_range('20200101', periods=88)
columns = [i for i in "abcd"]
num_arr = np.random.randn(88, 4)
df_alpha = pd.DataFrame(data=num_arr, index=dates, columns=columns)
df_alpha.reset_index(drop=False, inplace=True)
df_alpha.rename(columns={"index": 'date'}, inplace=True)

# 6、从字典对象创建DataFrame，并设置索引

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df_beta = pd.DataFrame(data=data, index=labels)

# 7、 显示dataFrame的基础信息
df_beta.info
df_beta.describe

# 8、 显示前列
df_beta.head(3)
df_beta.iloc[:3]

# 9、 取出df的某个列
print(df_beta[['age', 'animal']])
df_beta.loc[:, ['age', 'animal']]

# 10、取出索引为[3, 4, 8]行的animal和age列
df_beta.loc[df_beta.index[[3, 4, 8]], ['age', 'animal']]

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df_beta = pd.DataFrame(data=data, index=labels)

# 11. 取出age值大于3的行
xx = df_beta[df_beta['age'] > 3]

# 12. 取出age值缺失的行

xx = df_beta[df_beta['age'].isnull()]

# 13.取出age在2,4间的行（不含）
xx = df_beta[(df_beta['age'] > 2) & (df_beta['age'] < 4)]

# 14. `f行的age改为1.5
df_beta.loc['f', 'age'] = 1.5

# 15. 计算visits的总和
df_beta['visits'].sum()

# 16. 计算每个不同种类animal的age的平均数
res = df_beta.groupby('animal')['age'].mean()

# 17. 计算df中每个种类animal的数量
res = df_beta.nunique()
res_1 = df_beta['animal'].value_counts()

# 18. 先按age降序排列，后按visits升序排列
df_beta.sort_values(by=['age', 'visits'], ascending=[False, True])

# 19. 将priority列中的yes, no替换为布尔值True, False
dict_alpha = {"yes": True, "no": False}

df_beta['test'] = df_beta.apply(lambda x: dict_alpha.get(x['priority'], 'no_data'), axis=1)
df_beta['temp'] = df_beta['priority'].map(dict_alpha)

# 20. 将animal列中的snake替换为python
df_beta['animal'] = df_beta['animal'].str.replace("snake", "python")

# 21. 对每种animal的每种不同数量visits，计算平均age，即，返回一个表格，行是aniaml种类，列是visits数量，
# 表格值是行动物种类列访客数量的平均年龄
res = pd.pivot_table(data=df_beta, index="visits", columns='animal', values='age', aggfunc='mean')

# 22. 在df中插入新行k，然后删除该行

# result = df_beta.append([[5.5, 'dog', 'no', 2]])# 这样是错的
df_beta.loc['k'] = [5.5, 'dog', 'no', 2, False, False]

df_beta.drop('k')
