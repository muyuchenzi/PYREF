import pandas as pd

df = pd.read_csv(r'E:\李震祥\temp\pandas\Data\各省市订单数据.csv')
# 直接赋值


df.loc[:, 'tt'] = df.loc[:, '省'] + df.loc[:, '城市简称']
df['xx'] = df['省'] + df['城市简称']

df = df.loc[0:3, :]


# 利用apply
def data_pre(df):
    print(df)
    return df['省'] + df['城市简称']


df['xy'] = df.apply(data_pre, axis=1)
# 使用assign
xxf = df.assign(
    tp=lambda x: x['省'] + x['城市简称'],
    xt=lambda x: x['省'] + x['区域'])

# 增加空白
xxf['space_columns'] = ''
xxf.columns
