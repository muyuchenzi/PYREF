import pandas as pd
import random
import numpy as np

from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV


def qa_46():
    np.random.seed(42)
    raw_data = make_moons(n_samples=2000, noise=0.25, random_state=42)
    data = raw_data[0]
    target = raw_data[1]
    X_train, X_test, y_train, y_test = train_test_split(data, target)
    classifer = DecisionTreeClassifier()
    classifer.fit(X_train, y_train)
    classifer.score(X_test, y_test)

    classifer_2 = DecisionTreeClassifier(max_depth=6, min_samples_leaf=6)
    classifer_2.fit(X_train, y_train)
    classifer_2.score(X_test, y_test)
    # 网格搜索最优参数
    paras = {
        "max_depth": np.arange(1, 10),
        "min_samples_leaf": np.arange(1, 20)
    }
    grid_search = GridSearchCV(
        classifer,
        param_grid=paras,
        scoring='accuracy',
        cv=5
    )
    grid_search.fit(X_train, y_train)
    grid_search.best_params_
