import pandas as pd

df = pd.read_csv(r'E:\李震祥\temp\pandas\Data\各省市订单数据.csv',
                 engine='python', encoding='utf-8')

dict_alpha = {'华南': 'x',
              '西南': 'y',
              '西北': 'z',
              '华东': 't',
              }

# 使用apply对某一列进行操作
df['name2'] = df.apply(lambda x: x['name'].replace('市', ''), axis=1)
df['name1'] = df['name'].str.replace('市', '')
# series 有map
df['name3'] = df['name'].map(lambda x: x.replace('市', ''))

#
# df['name4'] = df.apply(lambda x: dict_alpha[x['区域']], axis=1) #字典取不到
df['name4'] = df.apply(lambda x: dict_alpha.get(x['区域'], 's'), axis=1)

# DataFrame的applymap函数，是对所有区域进行


df_2 = df[['常住人口2010', '订单数', 'lng', 'lat']]

df_3 = df_2.applymap(lambda x: '-' + str(x) + '-')
