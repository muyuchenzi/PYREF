import pandas as pd
import copy

# 根据多个字典序列创建DataFrame
file_path = r'E:\李震祥\PYGIT\PYref\ReviewCode\pandas\Data\各省市订单数据.csv'
df = pd.read_csv(file_path, encoding='utf-8')
list_alpha = list(df['省'].unique())

# A value is trying to be set on a copy of a slice from a DataFrame.
# Try using .loc[row_indexer,col_indexer] = value instead
df[df['包邮率'] > 0.95]['区域'] = "高包邮率"
# REVIEW这个办法分为两步：第一步是df[df['包邮率'] > 0.95] ，这一步是get ,后面["区域"]是set
# get得到的结果可能是一个view 也可能是一个copy，所以发出警告，也就是可能是在元数据上改，也可能是复制
# 新的数据后改，解决办法就是使用loc来把两步变成一步
df.loc[df['包邮率'] > 0.95, "区域"] = "高包邮率"

# axis的理解
# axis =0
# 如果是单行操作，就是指某一行，如果是聚合操作，就是指跨行cross rows

# axis=1
# 如果是单列操作，就是指某一列，如果是聚合操作，就是指跨列cross columns

# 按照哪个axis 就是这个axis要动起来(类似被for遍历），其他的axis保持不动。
import numpy as np

df = pd.DataFrame(np.arange(12).reshape(3, 4), columns=[i for i in "ABCD"])

# 单行或者单列操作
df.drop(columns=['A'], inplace=True, axis=1)
df.drop(index=1, inplace=True, axis=0)

df = pd.DataFrame(np.arange(12).reshape(3, 4), columns=[i for i in "ABCD"])
# 跨行操作
df.mean(axis=0)
df.mean(axis=1)
df['sum'] = df.apply(lambda x: x["A"] + x["B"] + x["C"] + x['D'], axis=1)
