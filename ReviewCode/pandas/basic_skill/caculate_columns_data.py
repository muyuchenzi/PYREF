import pandas as pd
import re

ssx = '上海市'
fff = ssx.replace('市', '')

df = pd.read_csv(r'E:\李震祥\temp\pandas\Data\各省市订单数据.csv')
df['sss'] = df.apply(lambda x: x['name'].replace("市", ''), axis=1)
