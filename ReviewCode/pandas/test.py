import pandas as pd
import numpy as np

data = pd.read_csv(r'E:\李震祥\PYGIT\PYref\ReviewCode\pandas\Data\各省市订单数据.csv', encoding='utf-8')
data.columns.to_list()
datax = data.rename(columns={"name": "名称"})
