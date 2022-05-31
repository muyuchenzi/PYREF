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
    gender_most_common = list(gender_counts.keys())[0]
    df['gender'] = df['gender'].fillna(value=gender_most_common)
    print(df)
    # 使用Counter来进行处理
    most_value = Counter(df['gender']).most_common()[0][0]
    df['gender'] = df['gender'].fillna(value=most_value)


def qa_06():
    '''
    对一个某几列进行非na选择，然后选择其数据类型为float的数据列
    :return:
    '''
    df = get_data().copy()
    df = df.loc[(df.loc[:, 'price'].notna()) & (df.loc[:, 'weight'].notna())]
    res = df.dtypes.to_dict()
    column_list = []
    for k, v in res.items():
        if v == 'float64':
            column_list.append(k)
    result = df[column_list]
    return result
    # 第二种就是根据df select_dtypes函数进行选择。
    # data_df = df.select_dtypes(include=['float'])


def qa_07():
    '''
    查找数据类型为object的列，然后根据这些列用字符串进行填充
    :return:
    '''
    df = get_data().copy()
    df = df.select_dtypes(include=['object'])
    df.fillna(value='empty', inplace=True)
    return df


def qa_08_cut(df, columns, cut_number):
    '''常规办法处理对某一列进行离散化处理
    可以看到这里非常麻烦，而且容易出错，所以pandas.cut这个函数就显得非常好用
    '''
    # columns = 'weight'
    columns_max = max(df[columns])
    columns_min = min(df[columns])
    step = (columns_max - columns_min) / cut_number
    for i in range(df.shape[0]):
        if columns_min <= df.loc[i, columns] < step + columns_min:
            return f"[{columns_min},{step + columns_min})"
        elif columns_min + step <= df.loc[i, columns] < columns_min + columns_min * step * 2:
            return f"({columns_min + step},{columns_min + step * 2}]"
        else:
            return f"({columns_min + step * 2},{columns_max}]"
    return df


def qa_08():
    '''
    某列连续数字进行离散化
    :return:
    '''

    df = get_data().copy()
    df['weight_cut'] = pd.cut(df['weight'], bins=3)
    return df


def qa_09():
    '''数值离散化'''
    df = get_data().copy()
    df['weight_cut'] = pd.cut(df['weight'], bins=[300 + 50 * i for i in range(1, 5)])
    return df


def qa_10():
    '''数值离散化
    这里使用标签来进行处理'''
    df = get_data().copy()
    df['weight_cut'] = pd.cut(df['weight'], bins=[300 + 50 * i for i in range(1, 5)],
                              labels=['light', 'normal', 'heavy'])
    return df


if __name__ == '__main__':
    qa_05()
