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
    
    '''
    pass


def entrance():
    str_alpha="A quick brown for jumps over the lazy dog"
    res=str.lower(str_alpha)
    res=set(res)
    print(res)
    str_set_all=set(ascii_lowercase)
    result=str_set_all-res
    print(result)

if __name__ == "__main__":
    file_contents = entrance()
