import pandas as pd
import time
import os
import datetime
import random
from string import ascii_lowercase
from functools import reduce
import re


def answer():
    '''
    re模块的两种匹配模式，一种是贪婪模式一种是非贪婪模式
    1、字符
    \w 字符 \W
    \d 数字 \D
    \s space\S
    数量词：
    ？
    +
    *
    {m,n}
    组
    []
    ()
    ^开头
    $结尾
    函数：
    最常用 findall 查找并以list返回
    sub 将匹配到的字符进行替换
    match 从开头第一个字符进行匹配
    search 查找一遍，有group函数

    '''


def func(str_in):
    temp = str_in.group()
    dict_alpha = dict(zip([i for i in 'abc'], [i for i in range(10)]))
    print(dict_alpha.get(temp, '0'))
    return str(dict_alpha.get(temp, '0'))


if __name__ == "__main__":
    answer()
