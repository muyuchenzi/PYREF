
import pandas as pd
import random 
import numpy as np
# 当前pandas 版本
print(pd.__version__)
# list创建Series
arr = [i for i in range(10)]
df = pd.Series(arr)
# dict创建Series
dict_key = [i for i in 'abcde']
dict_value = arr.copy()
dict_alpha = dict(zip(dict_key, dict_value))
# print(dict_alpha)
dates=pd.date_range('today',periods=6)
num_arr=np.random.randn(6,4)
print(num_arr)
print(dates)
