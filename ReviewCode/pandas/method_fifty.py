import pandas as pd
import os
print(os.getcwd())


data = pd.read_csv('E:\李震祥\PYGIT\PYref\ReviewCode\pandas\Data\data.csv')
# 查看数据
print(data.head(10))
print(data.tail())
print(data.dtypes)
gender_dict = {
    "F": "女性",
    "M": "男性"
}
data['gender'] = data.apply(lambda x: gender_dict.get(x['gender']), axis=1)
print(data.head())
