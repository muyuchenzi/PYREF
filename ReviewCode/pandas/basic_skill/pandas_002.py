import pandas as pd
import copy

# 根据多个字典序列创建DataFrame
file_path = r'E:\李震祥\PYGIT\PYref\ReviewCode\pandas\Data\各省市订单数据.csv'
df = pd.read_csv(file_path, encoding='utf-8')
