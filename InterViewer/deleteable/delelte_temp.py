import re


def solution(x):
    if x >= 0:
        return int(str(x)[::-1])
    else:
        return -int(str(x)[1:][::-1])


res = solution(-123)
