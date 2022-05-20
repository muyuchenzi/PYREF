import numpy as np
import pandas as pd
import copy

# 根据多个字典序列创建DataFrame
file_path = r'E:\李震祥\PYGIT\PYref\ReviewCode\pandas\Data\各省市订单数据.csv'
df = pd.read_csv(file_path, encoding='utf-8')
df.set_index(['name'], inplace=True)
df.reset_index(inplace=True, drop=False)

# 大概就是有六种方法
df['temp'] = df.apply(lambda x: str(x['name']) + "t", axis=1)
df['temp1'] = df['name'] + "s"
df['temp2'] = df['name'].apply(lambda x: str(x) + "v")

df.loc[:, "temp3"] = df.apply(lambda x: x['name'] + "e", axis=1)
df.loc[:, 'temp4'] = df.loc[:, "name"] + "q"
df.loc[:, "temp5"] = df.loc[:, "name"].apply(lambda x: x + "x")

# 查询云南贵州
df2 = df[df['省'] == "云南省"]
df2 = df.loc[df.loc[:, "省"] == "云南省"][['name', '订单数']]

df2 = df.loc[df.loc[:, '订单数'] > 1000000]
df3 = df.loc[(df.loc[:, "省"] == "云南省") | (df.loc[:, "省"] == "贵州省")]

df3 = df[(df['省'] == "云南省") | (df['省'] == "贵州省")]
df["ss"] = df["订单数"] * df["包邮率"]

df['区域'].value_counts()
sst = df.loc[df['包邮率'] > 0.95]
sst.loc[:"sssf"] = "98"
ppp = copy.copy(sst)
ppp.loc[:, 'ttsx'] = "高包邮率"
