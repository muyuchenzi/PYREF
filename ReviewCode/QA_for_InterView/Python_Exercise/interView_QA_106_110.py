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
# import time
# import queue
# import threading
# import multiprocessing as mp
# import queue
# from functools import wraps


# def wakeup(lock):
#     # global lock=threading.lock()
#     lock.acquire()
#     print("2、I'am wake up")

#     def wash(action):
#         print(action)
#         time.sleep(1)
#     wash("3、wash face")
#     print("4、wake up end")
#     lock.release()

# def work(n,lock):
#     lock.acquire()
#     print("5、start work")
#     res = 0
#     for i in range(n):
#         res += i+i**2+i**3
#     time.sleep(1)
#     print("6、end work")

#     lock.release()
#     return res


# def sleep(lock):
#     lock.acquire()
#     print("7、prepare for sheep")

#     def takeof(action):
#         print(action)
#         time.sleep(1)
#     takeof("8、take off cloth")

#     print("9、I'am sleeping")
#     lock.release()


# def day(n,lock):
#     # lock.acquire()
#     '''多个函数不建议这样写，尽量多线程进行进行单个函数体进行操作，否则太容易出现
#     锁出现错误'''
#     print('1、start a day')

#     wakeup(lock)
#     work(n,lock)
#     sleep(lock)

#     print("10、end a day")
#     # lock.release()

# def multi_thread():
#     '''代码冗余度太高了，非常非常不建议这样写'''
#     lock=threading.Lock()

#     thread_list=[]
#     for i in range(5):
#         td=threading.Thread(target=day,args=(1000000,lock),name=f"thread{i}")
#         td.start()
#         thread_list.append(td)
#     for td in thread_list:
#         td.join()
#     # print("multi process start")
#     # lock=mp.Lock()
#     # process_list=[]
#     # for i in range(2):
#     #     p=mp.Process(target=day,args=(100000,lock),name=f"process:{i}")
#     #     p.start()
#     #     process_list.append(p)
#     # for p in process_list:
#     #     p.join()


# if __name__=="__main__":
#     multi_thread()

# Q&A queue使用 生产者消费者模型
# FIXME 这里queue 数据list 一定要跟 线程数一样才行。
# 这里是由于没有把queue全部取出来，而是建了一个线程才存放一次，这样
#就是导致最开始出错的原因，

import time
import threading
import multiprocessing as mp
import queue


def producer(pro_line, cust_line):
    while True:
        if not pro_line.empty():
            pro_get = pro_line.get()
            produce_list = [i for i in range(pro_get)]
            time.sleep(1)
            cust_line.put(produce_list)
        else:
            break


def customer(cust_line):
    while True:
        if not cust_line.empty():
            cust_get = cust_line.get()
            result = [str(i) for i in cust_get]
            time.sleep(0.2)
            print(result)
        # return result
        else:
            break


def func_entry():
    produce_line = queue.Queue()
    custome_line = queue.Queue()
#   NOTE 入口数据
    list_alpha = [i for i in range(10, 25)]
    # 将数据放到生产者队列
    for p_line in list_alpha:
        produce_line.put(p_line)
    # 使用生产者对数据进行加工
    produce_thread_list = []
    for _ in range(6):
        pro_td = threading.Thread(target=producer, args=(produce_line, custome_line))
        pro_td.start()
        produce_thread_list.append(pro_td)
    [pro_thread.join() for pro_thread in produce_thread_list]
    # 消费者对数据进行处理
    custome_thread_list = []
    for _ in range(4):
        cus_td = threading.Thread(target=customer, args=(custome_line,))
        cus_td.start()
        custome_thread_list.append(cus_td)
    print("----")
    # print("__end__")
    [cus_thread.join() for cus_thread in custome_thread_list]


    # 对结果进行读取
    # final_res=[]
    # for _ in range(4):
    #     final_res.append(custome_line.get())
    # print("end")
    # print(final_res)
    print("end")
if __name__ == "__main__":
    func_entry()
