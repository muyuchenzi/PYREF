assert 1 in [1, 2, 3]
assert 1 not in [1, 2, 3]
d = {1: 'foo', 2: 'bar', 3: 'qux'}
assert 1 in d

list_alpha = [1, 2, 3, 4, 5]
generator_alpha = iter(list_alpha)
generator_alpha.__next__()
generator_beta = iter(list_alpha)
generator_beta.__next__()

from itertools import cycle

colors = cycle(['red', 'black', 'white', 'yellow'])
colors_res = []
for i in range(40):
    colors_res.append(next(colors))

from itertools import islice

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
