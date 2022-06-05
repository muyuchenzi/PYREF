import pandas as pd
from sklearn.model_selection import train_test_split
import time
import random
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler


def qa_31():
    data = datasets.load_breast_cancer().data
    target = datasets.load_breast_cancer().target
    X_train, X_test, y_train, y_test = train_test_split(data, target, train_size=0.8)
    for name, array in zip(['target', 'y_train', 'y_test'], [target, y_train, y_test]):
        print(name)
        print(pd.Series(array).value_counts(normalize=True))


def qa_32():
    data = datasets.load_breast_cancer().data
    df_1 = pd.DataFrame(data, columns=datasets.load_breast_cancer()['feature_names'])
    target = datasets.load_breast_cancer().target
    df_2 = pd.DataFrame(data=target, columns=['target'])
    df = pd.concat([df_1, df_2], axis=1)
    df['target'].value_counts()


def qa_33():
    '''让target保持的一样的比例'''
    data = datasets.load_breast_cancer().data
    target = datasets.load_breast_cancer().target
    X_train, X_test, y_train, y_test = train_test_split(data, target, train_size=0.8, stratify=target)
    for name, array in zip(['target', 'y_train', 'y_test'], [target, y_train, y_test]):
        print(name)
        print(pd.Series(array).value_counts(normalize=True))


def qa_34():
    ...


def qa_35():
    dict_alpha = {
        'year': [i for i in range(6)],
        'salary': [4000, 4250, 4500, 4750, 5000, 5250]
    }
    df = pd.DataFrame(dict_alpha)
    model = LinearRegression()
    model.fit(df[['year']], df[['salary']])
    # model.intercept_
    # model.coef_


def qa_36():
    ...


def qa_37():
    '''
    通过增加数据的非线性特征，增加特征来使模型更加准确
    :return: 
    '''
    df = pd.DataFrame(
        data=range(10),
        columns=['x']
    )
    poly = PolynomialFeatures(degree=2)
    df_poly = poly.fit_transform(df)


def qa_38():
    '''两个特征转换成六个特征'''
    df = pd.DataFrame({
        'x': range(10),
        'y': range(10, 20)})
    poly = PolynomialFeatures(degree=3)
    df_poly = poly.fit_transform(df)


def qa_39():
    '''多列数据标准化'''
    data = np.random.randint(1, 100, (30, 5))
    columns = [_ for _ in 'abcde']
    df = pd.DataFrame(data, columns=columns)
    scaler = StandardScaler()
    scaler.fit(df[['a', 'b']])  # 这里只是用了两个个列来作为测试
    df_scaled = scaler.transform(df[['a', 'b']])


def qa_40():
    ...
