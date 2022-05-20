import pandas as pd
import numpy as np

data_path=r'E:\李震祥\PYGIT\PYref\ReviewCode\pandas\Data\各省市订单数据.csv'
s=pd.Series([i for i in range(10)]+[np.nan,False])
print(s)

dates=pd.date_range("20200101",periods=6)
print(dates)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=[i for i in 'abcd'])
print(df)
# df1=pd.DataFrame(np.arange(12).reshape(3,4),columns=[i for i in "abcd"])
# print(df1)
# print(df1.index)
# print(df1.columns)
# print(df1.values)
# print(df1.describe())
# print(df1.T)
# print(df1.T.columns)
# print(df1.T.index)

# print(df1.sort_index(axis=1,ascending=False))

# DataFrame的选择
# print(dates)
df.iloc[0,1]=np.nan
df.iloc[1,2]=np.nan
print(df)
# print(df.dropna(how='any',axis=1))
df1=df.fillna(value=0)
print(df1)
print(df.isnull())