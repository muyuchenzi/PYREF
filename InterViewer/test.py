from itertools import permutations
from itertools import combinations

import sys
import psycopg2
import copy


def single_class(cls):
    cls_dict = {}

    def wrapper(*args, **kwargs):
        if cls not in cls_dict:
            cls_dict[cls] = cls(*args, **kwargs)
        else:
            return cls_dict[cls]

    return wrapper


@single_class
class Phd:
    ...


def solution():
    alpha = [i for i in range(10, 100)]
    alpha.index(10)
    alpha.remove(10)
    alpha.insert(1, 0)


if __name__ == '__main__':
    solution()
