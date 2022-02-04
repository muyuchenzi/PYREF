import multiprocessing as mp
import threading
from queue import Queue
import time
'''
对于多线程多进程与常规办法的运算速度进行对比，线程共享内存，进程需要对共享
内存进行设置
'''


def cal_time(func):
    def wrapper():
        time_start = time.time()
        func()
        time_end = time.time()
        print(f"运算时间为:{time_end-time_start}")
    return wrapper


def job(q):
    res = 0
    for i in range(1000000):
        res += i+i**2+i**3
    q.put(res)


@cal_time
def sample_multi_peocessing():
    '''多线程与多进程十分的相似，类似代码不再赘述'''
    q = mp.Queue()
    p_alhpa = mp.Process(target=job, args=(q,), name="p_alhpa")
    p_beta = mp.Process(target=job, args=(q,), name="p_beta")
    p_alhpa.start()
    p_beta.start()
    p_alhpa.join()
    p_beta.join()
    alhpa_res = q.get()
    beta_res = q.get()

    print(f'多进程的计算结果:{alhpa_res+beta_res}')


@cal_time
def sample_mulit_thread():
    '''使用多线程来进行解决问题'''
    # q=mp.Queue()# 多进程与多线程非常的相似，线程都可以直接用进程类的Queue，而不用自己重新创建
    q = Queue()
    t_alhpa = threading.Thread(target=job, args=(q,), name="t_alhpa")
    t_beta = threading.Thread(target=job, args=(q,), name="t_beta")
    t_alhpa.start()
    t_beta.start()
    t_alhpa.join()
    t_beta.join()
    alhpa_res = q.get()
    beta_res = q.get()
    print(f'多线程的计算结果:{alhpa_res+beta_res}')


@cal_time
def normal_cal():
    res = 0
    for i in range(1000000):
        res += i+i**2+i**3
    res2 = 0
    for i in range(1000000):
        res2 += i+i**2+i**3
    print(f"正常运算结果:{res+res2}")


if __name__ == "__main__":
    # sample_multi_peocessing()
    # sample_mulit_thread()
    # normal_cal()
    pass
