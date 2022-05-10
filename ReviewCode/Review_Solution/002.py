import copy
from functools import reduce
import string



def add(x):
    return x[0]+x[1]


list_alpha = [[1, 2], [3, 4], [10, 11]]
list_beta = copy.deepcopy(list_alpha)
print(list_beta)

result = map(lambda x: x[0]+x[1], list_alpha)
print(list(result))

print("---"*10)
res = map(lambda x, y: [x[0]+y[0], x[1]+y[1]], list_alpha, list_beta)
print(list(res))


list_gamma = [i for i in range(20)]

res_alpha = filter(lambda x: x > 10, list_gamma)
print(list(res_alpha))
print("*-"*20)
print(reduce(lambda x, y: x+y, list_gamma,100))

# 三元表达式

num_alpha = 0 if 3 < 2 else 1
print(num_alpha)

list_x = [i for i in range(10)]

print(list(map(lambda x: x*x, list_x)))

ss=["x","Y","a"]
res=filter(lambda x:x.islower(),ss)
print(list(res))
