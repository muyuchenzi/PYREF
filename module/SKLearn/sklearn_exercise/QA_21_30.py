import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder


def load_data():
    '''
    测试数据 鸢尾花数据
    :return:
    '''
    iris_data = datasets.load_iris().data
    iris_target = datasets.load_iris().target
    return iris_data, iris_target


def qa_21():
    '''
    拆分训练，验证数据
    :return:
    '''
    iris_data, iris_target = load_data()
    X_train, X_test, y_train, y_test = train_test_split(
        iris_data, iris_target, train_size=0.7)

    los_model = LogisticRegression(max_iter=1000)
    los_model.fit(X_train, y_train)
    los_model.score(X_train, y_train)

    predict_res = los_model.predict(X_test)
    return los_model


def qa_23():
    '''混淆矩阵'''
    ...


def qa_25():
    data = {
        'size': ["XL", 'L', "M", "L", "M"],
        'color': ['red', 'green', 'blue', 'green', 'red'],
        'gender': ['female', 'male', 'male', 'female', 'femal'],
        'price': [199.00, 89.0, 99.0, 129.0, 79.0],
        'weight': [500, 450, 300, 380, 410],
        'bought': ['yes', 'no', 'yes', 'no', 'yes']
    }
    df = pd.DataFrame(data=data)
    dict_alpha = {'yes': 1, 'no': 0}
    df['bought'] = df['bought'].apply(lambda x: dict_alpha.get(x))
    print(df)


def qa_26_pro(df):
    # 这个还没解决
    df = df.copy()
    list_column = list(set(df['size'].to_list()))
    dict_alpha = {k: 1 for k in list_column}
    zeros_df = pd.DataFrame(np.zeros(shape=(df.shape[0], len(list_column))))
    concat_df = pd.concat([df[['size']], zeros_df], axis=1)

    ...


def qa_26():
    '''分类特征编码'''
    data = {
        'size': ["XL", 'L', "M", "L", "M"],
        'color': ['red', 'green', 'blue', 'green', 'red'],
        'gender': ['female', 'male', 'male', 'female', 'femal'],
        'price': [199.00, 89.0, 99.0, 129.0, 79.0],
        'weight': [500, 450, 300, 380, 410],
        'bought': ['yes', 'no', 'yes', 'no', 'yes']
    }
    df = pd.DataFrame(data)
    one_hot_code = OneHotEncoder(sparse=False)
    one_hot_code.fit(df[['size']])
    one_hot_code.categories_
    result = one_hot_code.transform(df[['size']])
    res = pd.DataFrame(result)


def qa_27():
    data = datasets.load_breast_cancer().data
    target = datasets.load_breast_cancer().target
    X_train, X_test, y_train, y_test = train_test_split(data, target, train_size=0.8)
    return X_train, X_test, y_train, y_test


def qa_28():
    ...


def qa_29():
    ...
    data = datasets.load_breast_cancer().data
    df_1 = pd.DataFrame(data, columns=datasets.load_breast_cancer()['feature_names'])
    target = datasets.load_breast_cancer().target
    df_2 = pd.DataFrame(data=target, columns=['target'])
    df = pd.concat([df_1, df_2], axis=1)


def qa_30():
    ...
