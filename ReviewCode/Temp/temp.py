from functools import reduce

# 人生苦短，我用Python
a, b, *c, d = [1, 2, 3, 4, 5, 6]
a = (i for i in range(10))


def call_back(n):
    if n > 1:
        return n * call_back(n - 1)
    if n == 1:
        return 1


list_alpha = [i for i in range(1, 6)]
res = reduce(lambda x, y: x * y, list_alpha)
