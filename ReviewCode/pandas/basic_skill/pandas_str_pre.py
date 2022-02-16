import pandas as pd

df = pd.read_excel(r'E:\李震祥\temp\pandas\Data\contain_na_data.xlsx',
                   skiprows=3)
df.dropna(axis=1, how='all', inplace=True)
df.fillna(axis=0, method='ffill', inplace=True)
# pandas series有str
df['city'] = df.apply(lambda x: x['name'].replace("市", ''), axis=1)
df['city2'] = df['name'].str.replace('市', '')

# pandas axis 单行操作与聚合操作
df.drop(['lng', 'lat'], inplace=True, axis=1)
df.drop([i for i in range(10)], inplace=True, axis=0)

df['订单数'].mean()

# pandas index

df.reset_index(drop=True, inplace=True)
df.set_index(keys='name', inplace=True, drop=False)
# 设置完index的时候，可以直接利用这个index进行选择

print(df.loc['丽江市', '订单数'])
# 这样写更美观。
print(df[df['name'] == '丽江市']['订单数'])
