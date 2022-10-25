import time
from timeit import timeit
import cProfile


def f(a, b):
    c = a + b
    time.sleep(1)
    print("end")


# print(timeit('f(1,2)', setup="from __main__ import f", number=5))

if __name__ == '__main__':
    print(timeit("f(1,2)", setup="from __main__ import f", number=2))
    # print(cProfile.run('f()'))
