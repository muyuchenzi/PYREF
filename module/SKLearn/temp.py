# Q&A
import numpy as np
import pandas as pd
# 1、构建一个dataFrame，输出每列缺失值的bili


def q_a_01():
    '''
    '''
    data = {
        'size': ['XL', 'L', 'M', np.nan, 'M', 'M'],
        'color': ['red', "green", 'blue', 'green', 'red', 'green'],
        'gender': ['female', 'male', np.nan, 'female', 'female', 'male'],
        'price': [199.0, 89.0, np.nan, 129.0, 79.0, 89.0],
        'weight': [500, 450, 300, np.nan, 410, np.nan],
        'bought': ['yes', 'no', 'yes', 'no', 'yes', 'no']
    }
    df = pd.DataFrame(data=data)
