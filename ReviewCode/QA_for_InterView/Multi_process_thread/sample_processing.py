import multiprocessing as mp
import time

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def job(x):
    return x**x


def multi_core():
    '''利用pool更方便的来拿各个进程计算的结果'''
    time_start = time.time()
    # REVIEW
    # pool = mp.Pool(processes=4)
    # res = pool.map(job, range(200))
    # NOTE 其中multiprocess下的Pool也可以使用上下文管理器的with
    with mp.Pool(processes=4) as pool:
        res=pool.map(job,range(10000))
    time_end = time.time()
    print(f"使用mp pool 消耗的时间为：{time_end-time_start},result:res")

    # NOTE另外通过ProcessExccutor来进行解决
    time_start=time.time()
    with ProcessPoolExecutor(max_workers=4) as p:
        results = p.map(job, range(10000))
    time_end=time.time() 
    print(f"使用ProcessPool 消耗的时间为：{time_end-time_start},result:{results}")

    
    
    # for result in results:
    #     print(result)
    # 另外的取值办法
    # res_t = pool.apply_async(job, (2,))
    # print(res_t.get())  # 这样就跟thread的办法很相似
    # res_l = [pool.apply_async(job, (i,)) for i in range(10)]
    # result_v = [l.get() for l in res_l]
    # print(result_v)


def job_lock(v, num, lock_v):
    lock_v.acquire()
    for _ in range(10):
        v.value += num
        print(v.value)
    lock_v.release()


def multi_core_share_memory():
    '''这里要注意，各个进程运算的开始，因为很多时候系统安排进程的时候不一定是alhpa 
    写的靠前就首先运行
    '''
    lock_v = mp.Lock()
    value = mp.Value('i', 0)
    process_alhpa = mp.Process(target=job_lock, args=(value, 1, lock_v))
    process_beta = mp.Process(target=job_lock, args=(value, 3, lock_v))
    # process_alhpa.start()
    # process_alhpa.join()
    # process_beta.start()
    # process_beta.join()
    process_alhpa.start()
    process_beta.start()
    process_alhpa.join()
    process_beta.join()


if __name__ == "__main__":
    multi_core()
    # multi_core_share_memory()
