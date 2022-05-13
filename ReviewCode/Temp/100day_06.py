# 求阶C(M,N
import random


def add(*args):
    total = 0
    print(args)
    for val in args:
        total += val
    return total

print(add(1,2))