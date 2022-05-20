import pandas as pd
import numpy as np

# pd.read_csv()
# head() index
file_path = r'E:\李震祥\PYGIT\PYref\ReviewCode\pandas\Data\各省市订单数据.csv'
df = pd.read_csv(file_path, encoding='utf-8')

df.set_index('name', inplace=True, drop=True)
df.reset_index(drop=False, inplace=True)
df.loc[5, :].head()
