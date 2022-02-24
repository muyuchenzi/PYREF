# REVIEW
# # 这里是一个InterViewQA的问题解答。link git@github.com:kenwoodjw/python_interview_question.git
# NOTE 这里着重的谈一下多线程的问题。
# #Q&A 1.simple thread
# import threading
# import multiprocessing as mp
# import queue
# import time
# from functools import wraps
# # NOTE 一个简单的多线程跟多进程 Multi_process_threading的整理。


# def time_spend(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         time_start = time.time()
#         result = func(*args, **kwargs)
#         time_end = time.time()
#         print(f"{func} function time spend:{time_end-time_start} .")
#         return result
#     return wrapper


# @time_spend
# def job(n):
#     res = 0
#     for i in range(n):
#         res += i+i**2+i**3
#     time.sleep(2)
#     print(res)


# def sample_thread():
#     '''一个简单的thread'''
#     thread_alpha = threading.Thread(
#         target=job, args=(1000000,), name="thread_alpha")
#     thread_beta = threading.Thread(
#         target=job, args=(2000000,), name="thread_beta")
#     thread_alpha.start()
#     thread_beta.start()
#     thread_alpha.join()
#     thread_beta.join()
#     print("multi thread end")


# def sample_process():
#     '''一个简单的multiprocess
#     FIXME这里使用装饰器会出现
#     ：File "C:\ProgramData\Anaconda3\lib\multiprocessing\spawn.py",
#     line 102, in spawn_main source_process = _winapi.OpenProcess(OSError: [WinError 87] 参数错误。
#     这里根据 NOTE https://blog.csdn.net/S_o_l_o_n/article/details/106129004进行修改，添加一个wraps保证程序
#     在多进程的时候引用函数式一致的。'''
#     process_list = []
#     # process_alpha = mp.Process(target=job, args=(1000000,), name="process_alpha")
#     # process_beta = mp.Process(target=job, args=(2000000,), name="process_beta")
#     # process_alpha.start()
#     # process_beta.start()
#     # process_alpha.join()
#     # process_beta.join()
#     # print("multi process end!")
#     for i in range(2):
#         p = mp.Process(target=job, args=(1000000,), name=f"process{i}")
#         p.start()
#         process_list.append(p)
#     for p in process_list:
#         p.join()
#     print("end")


# if __name__ == "__main__":
#     sample_thread()
#     sample_process()

# Q&A 2.线程锁，线程queue
import time
import queue
import threading
import multiprocessing as mp
import queue



def wakeup(lock):
    lock.acquire()
    print("I'am wake up")

    def wash(action):
        print(action)
        time.sleep(1)
    wash("wash face")
    print("wake up end")
    lock.release()

def work(n,lock):
    lock.acquire()
    print("start work")
    res = 0
    for i in range(n):
        res += i+i**2+i**3
    time.sleep(1)
    print("end work")
    lock.release()
    return res


def sleep(lock):
    lock.acquire()
    print("prepare for sheep")

    def takeof(action):
        print(action)
        time.sleep(1)
    takeof("take off cloth")

    print("I'am sleeping")
    lock.release()


def day(n,lock):
    lock.acquire()
    print('start a day')
    lock.release()
    wakeup(lock)
    work(n,lock)
    sleep(lock)
    lock.acquire()
    print("end a day")
    lock.release()


def multi_thread():
    '''代码冗余度太高了，非常非常不建议这样写'''
    lock=threading.Lock()
    thread_list=[]
    for i in range(7):
        td=threading.Thread(target=day,args=(1000000,lock),name=f"thread{i}")
        td.start()
        thread_list.append(td)
    for td in thread_list:
        td.join()

if __name__=="__main__":
    multi_thread()

