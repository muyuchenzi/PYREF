import threading
import time
from queue import Queue
import copy


def eat():
    print(f"eat is runing")
    for i in range(10):
        time.sleep(0.1)
        print('eating')
    print('eat is end')


def multi_thread():
    my_thread = threading.Thread(target=eat())
    my_thread.start()
    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())
    print('eat_thread is running')
    # todo 你这里可以看到 my_thread 还没开始执行，multi——thread 的打印已经结束。所以这里需要
    # 一个序列，特别是一个thread 需要另外一个thread运行的结果的时候
    #


def wake_up(arg):
    print('now you is wake up')
    print(arg)
    # 懒床一秒钟
    for i in range(2):
        time.sleep(1)
    print('wake up end')


def code(arg):
    print('it\'s time to coding')
    print(arg)
    for i in range(5):
        time.sleep(1)
    print('code is end')


def mulit_thread_join():
    print('day is start')
    my_day_wake_thread = threading.Thread(
        target=wake_up, name="wake", args=('hello today',))
    my_day_code_thread = threading.Thread(
        target=code, name="code", args=("best wish",))  # 参数传递

    my_day_wake_thread.start()
    my_day_wake_thread.join()
    my_day_code_thread.start()
    my_day_code_thread.join()
    print('day is over')


def job(list_alpha, q):
    q.put([i**2 for i in list_alpha])


def mulit_thread_queue():
    '''把线程放到一个Queue的对象q(q.put),然后把这个线程队列放到主线程，最后把主线程运行的结果
    利用q.get()取出来'''
    q = Queue()
    threads = []
    data = [[i for i in range(10)], [j for j in range(10, 20)], [
        k for k in range(100, 110)]]
    for i in range(3):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    result = []
    for _ in range(3):
        result.append(q.get())
    print('计算结束')
    print(result)

# --------------------多线程与常规方法对比---------------------------------------------


def thread_job(list_alhpa, q):
    res = sum(list_alhpa)
    q.put(res)


def multithreading(list_input):
    '''这种方法如果是用来处理数据的话，可能效果不是很好，因为归根到底多线程还是在一个处理器上工作
    除非两件完全不同的任务，而且任务中间处理器有空闲，否则的话由于GIL global interpreter lock的缘故
    还是在一个线程上工作，这可能就要引入多进程的处理方法，即：使用CPU的多个核心来处理数据，这样虽然有
    GIL但是核心之间是单独存在的。'''
    cal_queue = Queue()
    cal_thread = []
    for i in range(4):
        t = threading.Thread(target=thread_job, args=(
            copy.copy(list_input), cal_queue), name=f"cal_{i}")
        t.start()
        cal_thread.append(t)
    [cal_t.join() for cal_t in cal_thread]
    total_result = 0
    for _ in range(4):
        total_result += cal_queue.get()
    print(total_result)


def normal_cal(list_input):
    total_result = sum(list_input*4)
    print(total_result)
    return total_result


A = 0
lock = threading.Lock()


def job_gil_1():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 1
    lock.release()
    print('job_gil_1', A)


def job_gil_2():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 10
    lock.release()
    print('job_gil_2', A)


def gil_entry():
    '''我这里是正常的，不用lock也是可以的，可能IDE进行了整理，'''
    t1 = threading.Thread(target=job_gil_1)
    t2 = threading.Thread(target=job_gil_2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('GIL test is end')


if __name__ == "__main__":
    print(f'------------simple-----------------d')
    multi_thread()
    print('--------------join-----------------')
    mulit_thread_join()
    print('------------queue---------------')
    mulit_thread_queue()
    print('------------gil---------------')
    list_input = list(range(1000000))
    time_start = time.time()
    normal_cal(list_input)
    print(f"常规计算方法消耗的时间：{time.time()-time_start}")
    time_start = time.time()
    multithreading(list_input=list_input)
    print(f"多线程计算方法消耗时间：{time.time()-time_start}")
    gil_entry()
