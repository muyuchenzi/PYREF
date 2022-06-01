import pandas as pd
import sklearn
import numpy as np


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


def qa_11():
    '''
    数值离散化，虚拟编码 
    '''
    df = get_data()
    df['weight_cut'] = pd.cut(df['weight'], bins=(200, 300, 400, 500), labels=['light', 'normal', 'heavy'])
    df = pd.get_dummies(df)

    return df


def qa_12():
    '''
    特征提取，就是利用某一列的数据然后创建新的列，这个其实都是没必要的
    :return:
    '''
    data = {
        'currency': [['PLN', "USD"],
                     ['EUR', 'USD', "PLN", 'CAD'],
                     ['GBP'],
                     ['JPY', 'CZK', "HUF"],
                     []]
    }
    df = pd.DataFrame(data)
    df['number'] = df['currency'].apply(lambda x: len(x))


def qa_13():
    '''
    是否包含某元素
    :return:
    '''
    data = {
        'currency': [['PLN', "USD"],
                     ['EUR', 'USD', "PLN", 'CAD'],
                     ['GBP'],
                     ['JPY', 'CZK', "HUF"],
                     []]
    }
    df = pd.DataFrame(data)
    # xx = df.loc[1, 'currency']
    df['test'] = df['currency'].apply(lambda x: 1 if 'USD' in x else 0)
    return df


def qa_14():
    '''
    对某一列进行处理
    :return:
    '''
    data = {
        'currency': ['#good#vibes', '#hot#summer#holiday', '#street#food', '#workout']
    }
    df = pd.DataFrame(data)
    dt = df['currency'].str.split('#', expand=True)
    dt.rename(columns={0: 'one', 1: 'tow', 2: 'three', 3: 'four'}, inplace=True)
    result = pd.concat([df, dt], axis=1)
    return result


def qa_15():
    '''
    每一行有些空值，计算这一行空值的个数
    :return:
    '''
    data = qa_14()
    # data.isnull().sum(axis=1)

    data['number'] = data.apply(lambda x: x.isnull().sum(), axis=1)
    return data


def qa_16():
    '''字符串转换数字'''
    data = {
        'currency': ['1000_000_000', '10_000', '30_000_000', '100_500_000']
    }
    df = pd.DataFrame(data)
    df['currency'] = df['currency'].str.replace('_', '')
    df['currency'] = df['currency'].astype(np.int64)
    return df


if __name__ == '__main__':
    qa_16()
