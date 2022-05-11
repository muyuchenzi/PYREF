import time


def time_spend(func):
    def warpper():
        time_start = time.time()
        func()
        time_end = time.time()
        print(f"{func}运行的时间为:{time_end - time_start}")

    return warpper


def get_want(num):
    # num=2224
    str_num = list(str(num))
    flag = list(filter(lambda x: not int(x) % 2, str_num))
    if len(flag) == 4:
        return True
    else:
        return False


@time_spend
def normal():
    ''''
    查找一个数字范围内所有数字都是偶数的数值
    '''
    values = []
    for i in range(1000, 3000):
        s = str(i)
        if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
            values.append(s)
    print(f"normal is end result->{values};数量为{len(values)}")
    # return values


@time_spend
def test_fun():
    '''
    跟normal 一样查找一定范围内的数字都是偶数的数值。normal写的太刻意，只能表示四位数。这个需要改正
    '''
    num_range = list(range(1000, 3000))
    result = filter(get_want, num_range)
    values = list(result)
    print(f"test is end {values} ;数量为{len(values)}")
    return values


if __name__ == "__main__":
    # test_fun_res = test_fun()
    normal_fun_res = normal()
    # normal()
    print('end')
