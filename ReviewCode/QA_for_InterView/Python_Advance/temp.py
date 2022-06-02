import random
import numpy as np
from numpy.random import randint
from operator import add, sub
import json


def temp():
    file_path = r'e:\李震祥\pygit\pyref\reviewcode\qa_for_interview\python_advance\data\file_example.json'
    with open(file_path, 'r', encoding='utf-8') as f:
        result = json.load(f)
    # print(result)
    dict_alpha = {}

    key_list = list(result[0].keys())
    print(key_list)
    for key in key_list:
        dict_alpha[key] = []
    for item in result:
        for key,val in item.items():
            dict_alpha[key].append(val)

if __name__ == "__main__":
    temp()
