import math
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from data.blog_spider import time_spend
'''
# NOTE 通过使用ThreadPoolExecuteor、ProcessPoolExceutor使用多进程，相对于Thread、Process
中的Queue模块来说简便了不少,
'''
def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):  # 这里 +1是将开方后的结果包含在内
            if n % i == 0:
                return False
        return True

prime_list=[112272535095293]*10
@time_spend
def single_thread():
    result=[]
    for i in prime_list:
        result.append(is_prime(i))
    
@time_spend
def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime,prime_list)

@time_spend
def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime,prime_list)

if __name__=="__main__":
    single_thread()
    multi_thread()
    multi_process()