# pandas 中 SettingWithCopyWarning


import pandas as pd

df = pd.read_excel(r'E:\李震祥\PYGIT\PYref\ReviewCode\pandas\Data\contain_na_data.xlsx',
                   skiprows=3)
df.dropna(how='all', axis=1, inplace=True)
df.fillna(method='ffill', axis=0, inplace=True)

# 常见错误
# df[df['城市等级'] == '三线及以下']['num'] = df['订单数'] * df['包邮率']
# df[condition][columns]=df[column1] +_*/ df[column2]
# 这一步操作分为了两步，df.get(condition).set(columns) get可能是子view

# 使用loc
df.loc[df['城市等级'] == '三线及以下', 'num'] = df['订单数'] * df['包邮率']
