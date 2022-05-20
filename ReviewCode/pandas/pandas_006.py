import pandas as pd
import numpy as np

# file_path = r'E:\李震祥\PYGIT\PYref\ReviewCode\pandas\Data\各省市订单数据.csv'


# def file_reader(file_path):
#     df = pd.read_csv(file_path, encoding='utf-8')
#     return df


# df = file_reader(file_path)
# print(df.index)
# #     df 的列名
# a = df.loc[:, "name"]
# b = df['name']
# c = df.iloc[:, 0]


df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=[i for i in "abcd"], index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4)), columns=[i for i in "bcde"], index=[2, 3, 4])
print(df1)
print(df2)
print(pd.concat([df1, df2], axis=0))
df3 = pd.concat([df1, df2], axis=0, ignore_index=True, sort=False, join="outer")
# pd.concat([df1)

df4 = pd.Series([1, 2, 3, 4], index=[i for i in "abcd"])
res = df1.append(df4, ignore_index=True)
# indicator 显示merge的方式默认为False


data = pd.DataFrame(np.random.randn(1000, 4), columns=list("abcd"))
