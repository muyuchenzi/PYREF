import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def data_load():
    '''对数据进行导入'''
    iris = datasets.load_iris()
    iris_X = iris['data']
    iris_y = iris['target']
    return iris_X, iris_y


def split_train_test(data_X, data_y):
    X_train, X_test, y_train, y_test = train_test_split(data_X, data_y, test_size=0.2)

    return X_train, X_test, y_train, y_test


def model_train(X_train, y_train):
    knn_model = KNeighborsClassifier()
    knn_model.fit(X_train, y_train)
    return knn_model


def vertify(model, X_test, y_test):
    model.predict(X_test)
    res = model.score(X_test, y_test)
    print(res)


def entry():
    data_X, data_y = data_load()
    X_train, X_test, y_train, y_test = split_train_test(data_X=data_X, data_y=data_y)
    model = model_train(X_train, y_train)
    vertify(model, X_test=X_train, y_test=y_train)


if __name__ == '__main__':
    entry()
