from itertools import islice
from itertools import cycle
from timeit import timeit

assert 1 in [1, 2, 3]
# assert 1 not in [1, 2, 3]
d = {1: 'foo', 2: 'bar', 3: 'qux'}
assert 1 in d

list_alpha = [1, 2, 3, 4, 5]
generator_alpha = iter(list_alpha)
generator_alpha.__next__()
generator_beta = iter(list_alpha)
generator_beta.__next__()

colors = cycle(['red', 'black', 'white', 'yellow'])
colors_res = []
for i in range(40):
    colors_res.append(next(colors))

colors_x = islice(colors_res, 0, 20)
colors_x_res = []
for col in colors_x:
    colors_x_res.append(col)


def my_gene():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


my_test = my_gene()

for i in my_test:
    print(i)


# 生成一个斐波那契数列


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = a + b, a
        yield a


xx = fib(10)
list_xx = []
for i in xx:
    list_xx.append(i)
print(list_xx)


def noral_list(input_string):
    print(input_string)
    list_xx = []
    for i in xx:
        list_xx.append(i)


time_spend = timeit(lambda: noral_list("string is input"), number=20000)

pass
