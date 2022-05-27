import pandas as pd
import time
import os
import datetime
import random
from string import ascii_lowercase
from functools import reduce
from collections import Counter
import re
import random


class A(object):
    class_a = [i for i in range(100)]

    def __init__(self, a, *args, **kwargs):
        '''
        获取class_a的前多个元素的和
        :param a:
        '''
        self.a = a

    def print_a(self):
        '''
        显示a的数字
        :return:
        '''
        print(self.a)

    def cal_sum(self, number):
        result = sum(self.class_a[0:number])
        return result


class B(object):
    class_b = ascii_lowercase

    def __init__(self, b, *args, **kwargs):
        '''
        获取calss_b前多个元素
        '''
        self.b = b

    def pri_b(self):
        print(self.b)

    def show_str(self, number):
        result = self.class_b[0:number]
        return result


class C(A, B):
    list_alpha = [_ for _ in range(10)]
    list_beta = [_ for _ in ascii_lowercase]
    class_c = dict(zip(list_beta, list_alpha))

    def __init__(self, a, b, c):
        super(C, self).__init__(a, b)
        self.c = c

    def pri_c(self):
        print(self.c)

    def show_dict(self, key):
        result = self.class_c[key]
        return result


def answer():
    ...


if __name__ == "__main__":
    answer()
