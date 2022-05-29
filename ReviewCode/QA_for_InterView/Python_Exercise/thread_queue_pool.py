import pandas as pd
import time
import os
import datetime
import random
from string import ascii_uppercase, ascii_lowercase, digits
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
        print(f"-----------> 总共消耗时间:{time_end - time_start} <-----------\n")

    return wrapper


def product_fun(product, customer):
    print('---------code start---------\n')

    temp_result = []
    while True:
        if not product.empty():
            temp = product.get()  # 挨个取
            res = str.upper(temp)
            temp_result.append(res)
            customer.put(res)
        else:
            break
    print(temp_result)
    print('------code end--------\n')


def customer_fun(customer):
    lowercase = [_ for _ in ascii_uppercase]
    digital = [_ for _ in range(1, 27)]
    dict_alpha = dict(zip(lowercase, digital))
    result = []
    while True:
        if not customer.empty():
            temp = customer.get()
            result.append(dict_alpha.get(temp))
        else:
            break
    print(result)


def answer_queue():
    '''
    1、关于queue队列的问题
    2、关于使用进程池的方法
    '''
    product = Queue()
    customer = Queue()
    lowercase = [_ for _ in ascii_lowercase]
    for i in lowercase:
        product.put(i)
    product_list = []
    for i in range(4):  # 创建四个生产函数的线程
        t1 = Thread(target=product_fun, args=(product, customer))
        t1.start()
        product_list.append(t1)
    [t.join() for t in product_list]
    customer_list = []
    for i in range(3):  # 使用3个消费者线程来处理
        t2 = Thread(target=customer_fun, args=(customer,))
        t2.start()
        customer_list.append(t2)
    [t.join() for t in customer_list]
    print('end')
    # final_result = customer.result()


@time_spend
def str_upper(string):
    time.sleep(1)
    return str.upper(string)


@time_spend
def str_change(string):
    temp = []
    for i in string:
        temp.append(i)
        time.sleep(0.1)
    res = [str.upper(i) for i in temp]
    return ''.join(res)


def answer_pool():
    '''
    使用thread pool来处理
    分别使用map 与 submit
    '''
    lowcase = [_ for _ in ascii_lowercase]
    # 第一种办法是使用map，来对每一个元素进行处理
    with ThreadPoolExecutor(max_workers=2) as future:
        result = future.map(str_upper, lowcase)

    for res in result:
        print(res)
    # 第二种办法是使用submit，对输入元素进行处理，
    with ThreadPoolExecutor() as future:
        res = future.submit(str_change, lowcase)
    print(res.result())


if __name__ == "__main__":
    # answer_queue()
    answer_pool()
