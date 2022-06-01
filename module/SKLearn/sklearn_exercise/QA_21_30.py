import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


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
    X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_target, train_size=0.7)

    los_model = LogisticRegression(max_iter=1000)
    los_model.fit(X_train, y_train)
    los_model.score(X_train, y_train)

    predict_res = los_model.predict(X_test)
    return los_model


def qa_23():
    '''混淆矩阵'''
    ...
