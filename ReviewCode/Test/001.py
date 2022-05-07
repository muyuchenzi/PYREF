# python 分支、循环、表达式
# 表达式
from random import randint
from random import choice
from random import randrange
from random import uniform
import random

print(randint(1,10))# 查找一个整数范围内的整数
print(choice([i for i in range(10)]))
print(randrange(1,100,3))
print(round(uniform(1,10),3))
print("-"*30)

re_alpha=random.choices([i for i in range(10)],weights=None,k=2)
print(re_alpha)

list_alpha = [i for i in range(9)]
list_beta = ['one', 'two', 'three', 'four']
list_gamma = ['one', [1, 3, 4], True, 3, {'a': 1, 'b': 2}]
list_delta = [i for i in "hello world python"]

dict_res=dict(zip(list_beta,list_alpha))
print(dict_res)
print(dict_res.get('ones','sss'))# python dict获取字典默认值
