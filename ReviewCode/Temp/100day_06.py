# 求阶C(M,N
import random
from functools import reduce

def add(*args):
    total = 0
    print(args)
    for val in args:
        total += val
    return total

print(add(1,2))


def temp(m,n):
    res_m=reduce(lambda x,y:x*y,m)
    res_n=reduce(lambda x,y:x+y,n)
    print(res_m)
    print(res_n)

temp([i for i in range(10)],[i for i in range(20)])