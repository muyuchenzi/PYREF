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


def day_week_up(parameter=None, lock_current=None):
    lock_current.acquire()
    print('-------week up start---------\n')
    print(parameter)
    week_up_list = [_ for _ in 'weekup']
    for i in week_up_list:
        time.sleep(0.5)
        print(i)
    print('----------week up end--------\n')
    lock_current.release()


def day_code(parameter=None, lock_current=None):
    lock_current.acquire()
    print('----------code start---------\n')
    print(parameter)
    code_list = [i for i in 'iscode']
    result = []
    for i in code_list:
        result.append(i)
        time.sleep(0.5)
        print(i)
    print('----------code end-----------\n')
    lock_current.release()


def day_sleep(parameter=None, lock_current=None):
    lock_current.acquire()
    print('----------sleep start--------\n')
    print(parameter)
    sleep_list = [i for i in 'asleep']
    for _ in sleep_list:
        time.sleep(0.5)
        print(_)
    print('----------sleep end----------\n')
    lock_current.release()


@time_spend
def answer_normal():
    '''
    三个任务，简单的来说就是起床，写代码，睡觉
    第一个就是按照顺序来执行。
    每个函数就是3秒,按照顺序进行执行，总共时间也就是9秒多
    '''
    day_week_up()
    day_code()
    day_sleep()


@time_spend
def answer_thread():
    '''
    第二个任务：使用多线程来处理
    每个函数3秒，按照多线程来处理，由于是三个函数是同步进行，所以总共也就3秒多，
    但是由于多线程是分别执行，所以执行的顺序可能没有按照顺序，
    这个可以用来处理多个任务，且多个任务之间没有联系。    
    使用lock来进行处理，那就是跟不用多线程的感觉差不多。
    NOTE 
    这里不用multiprocess的Process 来重写一遍了，因为其使用方法是与Thread的thread 是一致的
    甚至连lock都能通用。
    '''
    l = Lock()
    t1 = Thread(target=day_week_up, args=('weekup', l), name='week_uping')
    t2 = Thread(target=day_code, args=('day_code', l), name='coding')
    t3 = Thread(target=day_sleep, args=('sleep', l), name='sleeping')
    thread_list = [t1, t2, t3]
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()


if __name__ == "__main__":
    # answer_thread()
    answer_thread()


