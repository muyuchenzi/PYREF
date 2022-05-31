from sklearn import datasets
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.datasets._samples_generator import make_classification
from sklearn import preprocessing
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import learning_curve
from sklearn.model_selection import validation_curve
import pickle
import joblib


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


def model_normalization():
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


def cross_validation():
    '''
    交叉验证
    '''
    # NOTE常规验证
    iris_X, iris_Y, house_price_X, house_price_Y = dataset_get()
    X_train, X_test, Y_train, Y_test = train_test_split(iris_X, iris_Y, random_state=4)
    model_knn = KNeighborsClassifier(n_neighbors=5)
    model_knn.fit(X_train, Y_train)
    y_predict = model_knn.predict(X_test)
    print(model_knn.score(X_test, Y_test))
    print('-' * 25)
    # 使用交叉验证
    scores = cross_val_score(model_knn, iris_X, iris_Y, cv=5, scoring='accuracy')
    print(scores.mean())
    # 验证参数
    k_range = range(1, 31)
    k_scores = []
    for i in k_range:
        model = KNeighborsClassifier(n_neighbors=i)
        score = cross_val_score(model, X=iris_X, y=iris_Y, cv=10, scoring='accuracy')
        # score = -cross_val_score(model, X=iris_X, y=iris_Y, cv=10, scoring='mean_squared_error')
        k_scores.append(score.mean())
    plt.plot(k_range, k_scores)
    plt.xlabel("KNN model n_neighbors value")
    plt.ylabel('Cross-validated Accuracy')
    plt.show()


def cross_validating_two():
    '''
    查看学习曲线，本质上就是不断调整模型的参数来进行观察模型预测的准确度
    '''
    digits = datasets.load_digits()
    X = digits.data
    y = digits.target
    train_sizes, train_loss, test_loss = learning_curve(
        SVC(gamma=0.001), X=X, y=y, cv=10, scoring='accuracy',
        train_sizes=[0.1, 0.25, 0.5, 0.75, 1]
    )
    train_loss_mean = np.mean(train_loss, axis=1)
    test_loss_mean = np.mean(test_loss, axis=1)
    plt.plot(train_sizes, train_loss_mean, 'o-', color='r', label='Training')
    plt.plot(train_sizes, test_loss_mean, 'o-', color='g', label='Cross-validated')
    plt.xlabel("Training example")
    plt.ylabel("accuracy")
    plt.legend(loc='best')
    plt.show()


def cross_validating_three():
    '''

    '''
    digits = datasets.load_digits()
    X = digits.data
    y = digits.target
    param_range = np.logspace(-6, -2.3, 5)
    train_loss, test_loss = validation_curve(
        SVC(), X=X, y=y, param_name='gamma', param_range=param_range,
        cv=10, scoring='accuracy'
    )
    train_loss_mean = np.mean(train_loss, axis=1)
    test_loss_mean = np.mean(test_loss, axis=1)
    plt.plot(param_range, train_loss_mean, 'o-', color='r', label='Training')
    plt.plot(param_range, test_loss_mean, 'o-', color='g', label='Cross-validated')
    plt.xlabel("gamma")
    plt.ylabel("accure")
    plt.legend(loc='best')
    plt.show()


def model_save():
    '''
    模型的保存与加载pickle与joblib
    '''
    iris_data = datasets.load_iris()
    X, y = iris_data.data, iris_data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    model = SVC()
    model.fit(X_train, y_train)
    predict_result = list(model.predict(X_test[:]))
    with open(r"E:\李震祥\PYGIT\PYref\module\SKLearn\model_save\svc_pickle.pickle", 'wb') as f:
        pickle.dump(model, f)

    with open(r"E:\李震祥\PYGIT\PYref\module\SKLearn\model_save\svc_pickle.pickle", 'rb')as f:
        model_load = pickle.load(f)
    model_load_predict_res = list(model_load.predict(X_test[:]))  # 加载后可以看到还是能预测
    assert model_load_predict_res == predict_result  # 模型最后可以观测到时完全一致的。

    # NOTE 另外一种保存方法，更快速
    joblib.dump(model, "E:\李震祥\PYGIT\PYref\module\SKLearn\model_save\svc_joblib.pickle")
    modle_load_joblib = joblib.load("E:\李震祥\PYGIT\PYref\module\SKLearn\model_save\svc_joblib.pickle")
    modle_load_joblib_result = list(modle_load_joblib.predict(X_test[:]))
    assert modle_load_joblib_result == predict_result


if __name__ == "__main__":
    # model_build()
    cross_validation()
