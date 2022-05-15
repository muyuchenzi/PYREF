import os
from functools import reduce
from string import ascii_lowercase
from string import digits
from collections import Counter


class Solution(object):
    # 类方法，是指一般使用@classmethod作为装饰器使用，形参为cls,一般类可以直接调用，但是实例也能调用
    # 实例方法,是类里面的常见方法，不需要装饰器，形参为self,一般用实例进行直接调用，类不能调用
    # 静态方法，这个跟平时常用的函数类似，类跟实例都能调用，采用@staticmethod，没有形式参数，作为一般函数。
    string_ss = 'abc'

    def test(self, num):
        global string_ss
        if num > 50:
            return True
        else:
            return False

    def temp(self):
        list_alpha = [i for i in range(100)]
        res = filter(self.test, list_alpha)
        # print(list(res))

    ss=globals()
    print(ss)

if __name__ == "__main__":
    s = Solution()
    s.temp()
    
