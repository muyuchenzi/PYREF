import pandas as pd
from sklearn.model_selection import train_test_split
import time
import random
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


def qa_40():
    '''平均绝对误差'''
    # y_true,y_predict
    # abs(y_true-y_predict).sum()/len(y_true)


def qa_41():
    '''
    均方误差
    '''
    # ((y_true-y_predict)**2).sum()/len(y_true)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def qa_42():
    '''
    sigmoid函数，将变量映射到0-1区间
    '''
    df = pd.DataFrame(data=np.random.randn(10), columns=['var1'])
    df['var2'] = df['var1'].apply(lambda x: sigmoid(x))
    # df['var3'] = df['var1'].map(lambda x: sigmoid(x))
    # df['var4'] = df.apply(lambda x: sigmoid(x['var1']), axis=1)


def entropy(x):
    return -np.sum(x * np.log2(x))


def qa_43():
    '''
    熵：对于不确定的测量，越随机熵越大
    '''
    df = pd.DataFrame(
        {
            'var1': np.arange(0.01, 1, 0.1),
            'var2': 1 - np.arange(0.01, 1, 0.1)
        }
    )
    df['entropy'] = df.apply(lambda x: entropy([x['var1'], x['var2']]), axis=1)


def qa_45():
    '''
    计算准确率
    :return:
    '''
    list_alpha = [0, 1]
    data = [[random.choice(list_alpha) for _ in range(2)] for _ in range(10)]
    df = pd.DataFrame(data=data, columns=['y_true', 'y_predict'])
    accuracy_rest = accuracy_score(df['y_true'], df['y_predict'])


def qa_46():
    '''混淆矩阵
    行：实际值，
    列：预测值
    '''
    list_alpha = [0, 1]
    data = [[random.choice(list_alpha) for _ in range(2)] for _ in range(20)]
    df = pd.DataFrame(data=data, columns=['y_true', 'y_predict'])
    cm = confusion_matrix(df['y_true'], df['y_predict'])
    cm
