import pandas as pd
import time
import os
import datetime
import random
from string import ascii_lowercase
from functools import reduce


class Foo():
    '''
    可变类型与不可变类型：
    可变类型：list dict set
    不可变类型 ： string int tuple

    '''
    pass


def entrance():
    str_alpha = "123"
    list_alpha = [1, 2, 3]

    print(list_alpha.index(3))
    # result=0
    # for i in str_alpha:
    #     result+=int(i)*10
    # print(result)


if __name__ == "__main__":
    file_contents = entrance()
