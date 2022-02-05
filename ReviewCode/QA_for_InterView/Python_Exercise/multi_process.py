import pandas as pd
import time
import multiprocessing as mp
import threading
import numpy as np


def classify(number):
    money_num = number
    if (money_num == "nan") or (money_num == 0):
        return "空白"
    elif 0 < money_num <= 100:
        return "小资本"
    elif 100 < money_num <= 1000:
        return "中资本"
    elif 1000 < money_num <= 10000:
        return "大资本"
    else:
        return "巨资本"


def normal_method(path):
    corp_data = pd.read_csv(r'E:\李震祥\always\数据\上海数据\企业\上海启信宝.csv',
                            encoding='utf-8')
    corp_data['tag'] = corp_data.apply(lambda x: classify(x['注册资本']), axis=1)
    return corp_data
