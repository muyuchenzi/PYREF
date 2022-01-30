# yield 的作用，yield 相当于函数里的关键字return,但是只返回一个，除非进行下一次循环，利用next()进行不断迭代

# 例如斐波那契数列问题

# generator 与 iterables 生成器与可迭代对象，可迭代对象就是可以利用循环对成员进行遍历
from memory_profiler import profile
import timeit
import time

# TODO 一个简单的生成器
generator_beata = (i * i for i in range(1, 6))
print(generator_beata)

for ele in generator_beata:
    print(ele)


#  TODO 生成器函数，需要一个关键字yield--也可以理解为如果是return那么就是函数，如果是yield那么就是一个生成器函数

def produce_generator(num):
    temp = []
    for ele in range(1, num):
        s = list(range(1, ele + 1))
        temp.extend(s)
        if len(temp) >= 1:
            yield temp
            temp = []


@profile
def main_input():
    gen_gamma = produce_generator(10000)
    num = 0
    for ele in gen_gamma:
        num += 1
    print(num)


def time_spend():
    list_result = []
    for i in range(10):
        list_result.append(i)
        time.sleep(1)
    return list_result


if __name__ == '__main__':
    # main_input()
    x = time_spend()
    time_spend = timeit.timeit(time_spend, number=1)
