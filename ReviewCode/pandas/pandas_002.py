import numpy as np

# numpy 的基本算书运算  矩阵的运算
a = np.array([i*10 for i in range(1, 5)])
print(a)
b = np.arange(1, 5)
print(b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(b**2)

# max min sum 计算
c = np.random.random((2, 5))
print(c)
print(np.max(c))
print(np.sum(c, axis=1))
print(np.min(c))
print(np.max(c, axis=0))

# 均值 中位数 累加值 累差 非零
d = np.arange(2, 14).reshape(3, 4)
print(d)
print(np.mean(d))
print(np.average(d))
print(np.median(d))
print(np.cumsum(d))
print(np.diff(d))
print(np.nonzero(d))
np.random.shuffle(d)
print("-"*20)
print(d)
e = np.sort(d, axis=1)
print(e)
# axis 轴 axis=0 是针对index (也就是行之间计算，得到的是列的值)
# 同理 axis=1是针对columns计算(也就是列之间计算，得到的是行的值)

matrix = np.arange(0, 12).reshape(3, 4)
print(matrix)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(np.sum(matrix, axis=0))
# [12 15 18 21]
print(np.sum(matrix, axis=1))
# [ 6 22 38]
