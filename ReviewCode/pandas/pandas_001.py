import numpy as np


# numpy的array里最简单的创建案例
array_alpha = np.array([[1, 2, 3],
                       [4, 5, 6]])
print(array_alpha)
print(f"number of dim :{array_alpha.ndim}")
print(f"shape:{array_alpha.shape}")
print(f"size:{array_alpha.size}")

array_alpha_1=np.array([[[1,2,4],[2,3,4]],[[1,2,3],[8,0,9]]])
print(array_alpha_1.ndim)
print(array_alpha_1)

array_beta=np.array([2,3,4],dtype=np.int64)
print(array_beta)

#zeros ones eye arrange 的例子
array_a=np.zeros(5,dtype=np.int64)
print(array_a)
arra_a_1=np.ones(12,dtype=np.int64).reshape(3,4)
print(arra_a_1)
arra_a_2=np.eye(5,dtype=np.int64)
print(arra_a_2)
array_b=np.arange(12).reshape(3,4)
print(array_b)

# numpy 的基本运算


