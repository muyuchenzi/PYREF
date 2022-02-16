import pandas as pd

df = pd.read_csv(r'E:\李震祥\temp\pandas\Data\各省市订单数据.csv')

df['订单数'].describe()

# 去重---非数值
xx = df['name'].unique()

xy = df['name'].value_counts()
