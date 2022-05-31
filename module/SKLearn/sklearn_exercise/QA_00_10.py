# Q&A
import numpy as np
import pandas as pd
from collections import Counter


def get_data():
    '''
    构建一个案例函数
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
    return df


def qa_01():
    '''
    1、构建一个dataFrame，输出每列缺失值的
    '''
    df = get_data().copy()
    nan_value = df.isna().sum()
    print(nan_value / df.shape[0])
    return df


def qa_02():
    '''
    对于某些数据进行平均值填充
    :return:
    '''
    df = get_data().copy()
    df.loc[df['weight'].isna(), 'weight'] = df['weight'].mean()
    df['weight'] = df['weight'].fillna(value=df['weight'].mean())
    return df


def qa_03():
    '''
    统计填充的数量
    :return:
    '''
    pass


def qa_04():
    '''
    使用常量进行填充
    :return:
    '''
    df = get_data().copy()
    # df.loc[5,'price']=np.nan
    df['price'] = df['price'].fillna(value=100.00)  # 常数进行填充
    df['price'] = df['price'].fillna(method='ffill')
    df['price'] = df['price'].fillna(method='bfill')


def qa_05():
    '''
    对某一个列采用出现最多的来进行填充
    :return:
    '''
    df = get_data().copy()
    gender_counts = df['gender'].value_counts(ascending=False).to_dict()
    gender_most_coment = list(gender_counts.keys())[0]
    df['gender'] = df['gender'].fillna(value=gender_most_coment)
    print(df)
    # 使用Counter来进行处理
    most_value = Counter(df['gender']).most_common()[0][0]
    

if __name__ == '__main__':
    qa_05()
