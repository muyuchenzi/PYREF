import pandas as pd
import numpy as np

# 32. 创建Series s，将2015所有工作日作为随机值的索引
pd_date = pd.date_range(start='20100101', end='2010-04-03', freq="B")
s = pd.Series(np.random.rand(len(pd_date)), index=pd_date)

# 33. 所有礼拜三的值求和
s[s.index.weekday == 2].sum()

# 34. 求每个自然月的平均数

s.resample('M').mean()
# 35. 每连续4个月为一组，求最大值所在的日期

s.groupby(pd.Grouper(freq='4M')).idxmax()

# 36. 创建2015-2016每月第三个星期四的序列

pd.date_range('2015-01-01', '2016-12-31', freq='WOM-3THU')

# 数据清洗
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
                               'Budapest_PaRis', 'Brussels_londOn'],
                   'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                   'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
                               '12. Air France', '"Swiss Air"']})
# 37. FlightNumber列中有些值缺失了，他们本来应该是每一行增加10，填充缺失的数值，并且令数据类型为整数
for ind in list(range(1, len(df.index))):
    df.loc[ind, 'FlightNumber'] = df.loc[ind - 1, 'FlightNumber'] + 10
df["FlightNumber"] = df['FlightNumber'].astype(np.int64)

# 38. 将From_To列从_分开，分成From, To两列，并删除原始列
temp = df["From_To"].str.split("_", expand=True).rename(columns={0: "From", 1: "To"})
result = pd.concat([df, temp], axis=1)
result.drop('From_To', inplace=True, axis=1)

# 39. 将From, To大小写统一首字母大写其余小写
result['From'] = result["From"].str.capitalize()

import re


# 40. Airline列，有一些多余的标点符号，需要提取出正确的航司名称。举例：'(British Airways. )' 应该改为 'British Airways'.
def re_proc(x):
    # x= '"Swiss Air"'
    print(x)
    res = re.findall(r'([a-zA-Z\s]+)', x)
    print(res)
    return res[0]


def temp(x):
    return "result"


result['temp'] = result['To'].apply(lambda x: temp(x))

df["As"] = df["Airline"].apply(lambda x: re_proc(x))

result['Airline'] = result['Airline'].str.extract('[a-zA-Z]+', expand=False)
# 41. NOTE Airline列，数据被以列表的形式录入，但是我们希望每个数字被录入成单独一列，delay_1, delay_2, ...没有的用NAN替代
temp = df['RecentDelays'].apply(pd.Series)
for i in temp:
    print(len(i))

# 42. 用 letters = ['A', 'B', 'C']和 numbers = list(range(10))的组合作为系列随机值的层次化索引
letters = ['A', 'B', 'C']
numbers = list(range(4))
mi = pd.MultiIndex.from_product([letters, numbers])
s = pd.Series(np.random.rand(12), index=mi)

# 43. 检查s是否是字典顺序排序的

s.index.is_lexsorted()

# 44. 选择二级索引为1, 3的行
s.loc[:, [1, 3]][:]

import matplotlib.pyplot as plt

df = pd.DataFrame({"xs": [1, 5, 2, 8, 1], "ys": [4, 2, 1, 9, 6]})
plt.style.use('ggplot')

df.plot.scatter("xs", "ys", color="black", marker="x")
