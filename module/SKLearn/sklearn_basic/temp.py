from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
import pickle

X, y = make_classification(n_samples=300, n_features=2, n_redundant=0, n_informative=2, random_state=22,
                           n_clusters_per_class=1, scale=100)

plt.scatter(X[:, 0], X[:, 1])
plt.show()
# X = preprocessing.minmax_scale(X, feature_range=(-1, 1))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)

classfier = SVC()
classfier.fit(X_train, y_train)
classfier.score(X_test, y_test)
with open(r'E:\李震祥\PYGIT\PYref\module\SKLearn\model_save\temp.pickle', 'wb') as f:
    pickle.dump(classfier, f)
with open(r'E:\李震祥\PYGIT\PYref\module\SKLearn\model_save\temp.pickle', 'rb')as f:
    model = pickle.load(f)
model.predict(X_test)
