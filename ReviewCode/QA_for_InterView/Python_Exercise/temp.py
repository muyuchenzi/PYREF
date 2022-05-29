import pandas as pd
import time
import os
import datetime
import random
from string import ascii_lowercase
from functools import reduce
import re
from threading import Thread
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from queue import Queue
from threading import Lock


def time_spend(func):
    def wrapper(*args, **kwargs):
        time_start = time.perf_counter()
        func(*args, **kwargs)
        time_end = time.perf_counter()
        print(f"-----------> 总共消耗时间:{time_end - time_start} <-----------")

    return wrapper


def day_week_up(parameter=None):
    print('-------week up start---------\n')
    print(parameter)

    week_up_list = [_ for _ in 'weekup']
    for i in week_up_list:
        time.sleep(0.5)
        print(i)
    print('----------week up end--------\n')


def day_code(parameter=None):
    print('----------code start---------\n')
    print(parameter)
    code_list = [i for i in 'iscode']
    result = []
    for i in code_list:
        result.append(i)
        time.sleep(0.5)
        print(i)
    print('----------code end-----------\n')


def day_sleep(parameter=None):
    print('----------sleep start--------\n')
    print(parameter)
    sleep_list = [i for i in 'asleep']
    for _ in sleep_list:
        time.sleep(0.5)
        print(_)
    print('----------sleep end----------\n')


def day_think(para, q):
    print('----------think start----------\n')
    print(para)
    temp_res = []
    while True:
        if not q.empty():
            temp_res.append(q.get())
        else:
            break
    result = '-'.join(temp_res)
    print(result)
    print('----------think end----------\n')


@time_spend
def answer_thread_queue():
    '''
    '''
    q = Queue()
    for i in 'muyuchenzi':
        q.put(i)
    t = Thread(target=day_think, args=('xx', q), name='week_up')
    t.start()
    t.join()


if __name__ == "__main__":
    # answer_thread()
    answer_thread_queue()
