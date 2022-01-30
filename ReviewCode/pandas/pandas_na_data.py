import pandas as pd

df = pd.read_excel(r'E:\李震祥\temp\pandas\Data\contain_na_data.xlsx'
                   , skiprows=3)

# df.isnull()

# todo 删除行或者列里的空白数据
# df.dropna(how='any', axis=0, inplace=True)
df.dropna(how='all', axis=1, inplace=True)
#  向后填充空白数据forward 与 backward
# DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)
# df["name"] = df['name'].fillna(method='ffill')
# df['城市简称'].fillna(method='ffill', inplace=True)
df.fillna(method='ffill', inplace=True, axis=0)
