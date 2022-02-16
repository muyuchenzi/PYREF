import pandas as pd

df = pd.read_csv(r'E:\李震祥\temp\pandas\Data\各省市订单数据.csv',
                 encoding='utf-8')

df_groupby = df.groupby(by=['省']).agg({'订单数': "mean", '包邮率': 'min'}).reset_index(drop=False)
df_groupby2 = df.groupby(by=['省', '城市等级']).agg({'订单数': "mean", '包邮率': 'min'}).reset_index(drop=False)
