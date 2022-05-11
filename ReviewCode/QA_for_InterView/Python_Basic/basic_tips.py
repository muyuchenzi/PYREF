# REVIEW 一些python 的小tips
# 生成空白或者指定字符的二维数组dd的方法。
import numpy as np

dim=np.zeros(shape=(5,3),dtype=np.int0)
dim=dim.tolist()
print(dim)


print("--"*20)
x, y = 3, 5
two_dim_list = [[0]*x]*y
print(two_dim_list)
# NOTE 这里要注意[0]*3这里是一个浅拷贝，很容易导致修改一个就改了全部
print(two_dim_list[1][1])
two_dim_list[1][1] = "x"

print(two_dim_list)
# 但是可以使用列表推导式
print("_"*30)
two_dim_list_1 = [[0 for i in range(x)] for j in range(y)]
print(two_dim_list_1)
two_dim_list_1[1][1] = 'x'
print(two_dim_list_1)
