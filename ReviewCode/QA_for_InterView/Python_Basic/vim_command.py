from itertools import cycle, islice
from timeit import timeit
import pandas as pd
assert 1 in [1, 2, 3]
# assert 1 not in [1, 2, 3]
d = {1: 'foo', 2: 'bar', 3: 'qux'}
assert 1 in d
# fix: 设置
# TODO:
# FIXME
# DEBGU
# REVIEW
# NOTE
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


def gene_test():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


my_test = gene_test()

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
    for j in xx:
        list_xx.append(j)


time_spend = timeit(lambda: noral_list("string is input"), number=20000)

# 1、python 的参数传递 分为两种 i、值类型ii、应用类型，python常见的数据结构中，number string tuple 是值类型
# list dict set DataFrame Series是引用类型 值类型是copy一个副本，引用类型是copy了一个引用，


def get_kinds_var():
    num_var = 12
    str_var = "stringTest124@gmail.com"
    tuple_var = (1, 3, 'str', False)
    list_var = [1, 3, 'str', False]
    dict_var = {
        "one": 'one_value',
        "two": "two_value"
    }
    set_var = set([1, 2, 3, 4, 'str', 2, 3, False, True, False])
    DataFrame_var = pd.DataFrame(dict_var, index=[0])
    return num_var, str_var, tuple_var, list_var, dict_var, set_var, DataFrame_var


def function_var(num_var, str_var, tuple_var, list_var, dict_var, set_var, DataFrame_var):
    num_res = num_var - 5
    str_res = str_var + "_changed"
    tuple_res = tuple_var + (3, 2, 1, 0)
    list_res = list_var
    list_res.extend([3, 2, 1, 0])
    dict_res = dict_var
    dict_res["one"] = "one_value_changed"
    set_var.add("addValeu")
    DataFrame_res = DataFrame_var
    DataFrame_res.loc[0, 'one'] = "oneValueChanged"
    print(num_res, str_res, tuple_res, list_res,
          dict_res, set_var, DataFrame_res)
    return num_res, str_res, tuple_res, list_res, dict_res, set_var, DataFrame_res


if __name__ == '__main__':
    """值类型和引用类型进行验证，"""
    num_var, str_var, tuple_var, list_var, dict_var, set_var, DataFrame_var = get_kinds_var()
    print(num_var, str_var, tuple_var, list_var,
          dict_var, set_var, DataFrame_var)
    num_res, str_res, tuple_res, list_res, dict_res, set_res, DataFrame_res = \
        function_var(num_var=num_var, str_var=str_var, tuple_var=tuple_var, list_var=list_var,
                     dict_var=dict_var,
                     set_var=set_var,
                     DataFrame_var=DataFrame_var)
    assert num_res == num_var
    assert str_var == str_res
    assert tuple_var == tuple_res
    assert list_res == list_var
    assert dict_var == dict_res
    assert set_var == set_res
    # assert tuple_var == tuple_res
    assert DataFrame_res.equals(DataFrame_var)
    print("this is vim cw key  exercise!!")
    print("this is vim i  key  exercise!!")
    print("this is vim i  key  exercise!!")
    print("this is vim i  key  exercise!!")
    print("this is vim i  key  exercise!!")
    print("this is vim i  key  exercise!!")
    print("this is ci  i  key  exercise!!")
    print("this is vim i ")

    for i in range(100):
        print(i)

    string_alha = "<ttdfatdfadfa>lsit"
