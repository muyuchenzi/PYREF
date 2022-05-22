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
