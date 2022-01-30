# 成员运算符
list_alpha = [i for i in range(9)]
list_beta = ['one', 'two', 'three', 'four']

print(1 in list_alpha)
print('one' not in list_beta)
# 身份人算符 is 与== 之间的区别，内存地址与值之间的比较
a = 1
b = 2
c = 1
print(a is b)
print(a is c)

x = {1, 2, 3}
y = {2, 3, 1}
x is y

isinstance(a, int)
isinstance("string", (int, float, str))
import random

print(random.shuffle(list_beta))
