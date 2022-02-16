import pandas as pd

df = pd.read_csv(r'E:\李震祥\temp\pandas\Data\各省市订单数据.csv')
df2 = df.copy()

res = pd.merge(df, df2, left_on='name', right_on='name',
               suffixes=("_df", "_df2"),
               how='inner',
               sort=True)

# one-to-many
right = pd.DataFrame(data=[['东北', "hhahaha"],
                           ["华东", "hehehe"],
                           ["华南", "lalala"],
                           ["华北", "gegege"],
                           ["华北", "wwwwwww"]], columns=['name', 'expre'])
result = pd.merge(df, right, left_on='区域', right_on='name', how='left')

# pandas concat
# append 只能按行合并

concat_alpha = pd.concat([df, df2], axis=0, ignore_index=True)
