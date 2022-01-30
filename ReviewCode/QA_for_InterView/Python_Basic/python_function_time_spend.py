import time
from timeit import timeit
import cProfile


def f():
    time.sleep(1)


# print(timeit('f()', setup='from __main__ import f'))

if __name__ == '__main__':
    print(timeit(f, number=2))
    print(cProfile.run('f()'))
