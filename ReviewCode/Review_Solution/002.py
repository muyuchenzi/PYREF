# 装饰器
import time


def decorator(func):
    def wrapper(number):
        time_start = time.time()
        reuslt=func(number)
        time_end = time.time()
        print(f"函数运行消耗了{time_end-time_start}s！,总数为：{reuslt}")

    return wrapper



def isprime(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
@decorator
def prime_nums(number):
    # time_start=time.time()
    count=0
    for i in range(2,number):
        if isprime(i):
            count+=1
            # time.sleep(1)
            print(i)
    return count
    # time_end=time.time()
    # print(f"总共花费了{time_end-time_start}s!")

if __name__ == "__main__":
    prime_nums(10000)
    # print(isprime(34))
