import sklearn
from sklearn import datasets
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def dataset_get():
    '''
    这里用sklearn自带的经典数据来进行:一般来说有两种：分类与拟合。鸢尾花为用来分类的数据，房价数据为拟合数据
    鸢尾花数据
    波士顿房价数据

    '''
    iris_data = pd.DataFrame(datasets.load_iris().data)
    iris_target = pd.DataFrame(datasets.load_iris().target)

    house_price_data = pd.DataFrame(datasets.load_boston().data)
    house_price_target = pd.DataFrame(datasets.load_boston().target)
    return iris_data, iris_target, house_price_data, house_price_target


def model_build():
    '''
    使用K近邻分类法与线性回归
    '''
    iris_X, iris_Y, house_price_X, house_price_Y = dataset_get()
    X_train, X_test, Y_train, Y_test = train_test_split(iris_X, iris_Y, test_size=0.3)
    knn = KNeighborsClassifier()
    model_class = knn.fit(X_train, Y_train)
    Y_predict = model_class.predict(X_test)
    print(Y_predict, Y_test[0].tolist(), sep='\n')

    # 线性回归模型拟合波士顿房价数据
    X_price_train, X_price_test, Y_price_train, Y_price_test = train_test_split(house_price_X, house_price_Y,
                                                                                test_size=0.25)
    line_reg = LinearRegression()
    model_line_reg = line_reg.fit(X_price_train, Y_price_train)
    Y_price_pridict = model_line_reg.predict(X_price_test)
    print(Y_price_pridict)


if __name__ == "__main__":
    model_build()
