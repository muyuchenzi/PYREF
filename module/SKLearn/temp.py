# Q&A
import numpy as np
import pandas as pd
import random
# 1、构建一个dataFrame，输出每列缺失值的bili
import datetime
import string
import time
from functools import reduce, partial
import copy
import os

a = 1


def temp(*args, **kwargs):
    '''
    下划线，_一个下划线就是一般是指私有变量
    __两个是指内置函数
    函数式编程 lambda、reduce、filter、map
    :return:
    '''
    f = [i for i in range(10)]
    t = []
    for i in f.copy():
        t.append(i)
        f.remove(i)
    print(f)
    print(t)


if __name__ == '__main__':
    temp()
