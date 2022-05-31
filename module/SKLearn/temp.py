import sklearn
from sklearn import datasets
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.linear_model import LinearRegression
from sklearn.datasets._samples_generator import make_classification
from sklearn import preprocessing
from sklearn.svm import SVC
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


def classify_KN():
    '''
    对数据进行标准化 能对结果产生很大的影响
    '''
    X, y = make_classification(n_samples=300, n_features=2, n_redundant=0, n_informative=2,
                               random_state=22, n_clusters_per_class=1, scale=100)
    X = preprocessing.scale(X)
    # X = preprocessing.minmax_scale(X, feature_range=(-1, 1))
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)
    model_svc = SVC()
    model_svc.fit(X_train, y_train)
    print(model_svc.score(X_test, y_test))
    # plt.scatter(X[:, 0], X[:, 1], c=y)
    # plt.xlabel()
    # plt.show()


if __name__ == "__main__":
    classify_KN()
