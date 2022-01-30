import time


def display_time(func):
    def wrapper(end_number):
        time_start = time.time()
        prime_count, prime_list = func(end_number)
        time_end = time.time()
        print(f"总共运行时间{time_end - time_start}")
        return prime_count, prime_list

    return wrapper


# todo 装饰器的参数
# def display_time(func):
#     def wrapper(*args):
#         time_start = time.time()
#         prime_count = func(end_number)
#         time_end = time.time()
#         print(f"总共运行时间{time_end - time_start}")
#         return prime_count
#
#     return wrapper
#


def is_prim(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


@display_time
def prim_nums(end_number):
    count = 0
    prim_list = []
    for i in range(2, end_number):
        if is_prim(i):
            count += 1
            prim_list.append(i)
            # print(i)
    return count, prim_list


if __name__ == '__main__':
    prim_count, prim_list = prim_nums(10000)
