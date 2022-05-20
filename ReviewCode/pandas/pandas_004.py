import numpy as np
import copy
A=np.arange(12).reshape(3,4)
print(A)
print(np.split(A,2,axis=1))
print(np.split(A,3,axis=0))

print(np.hsplit(A,2))
print(np.vsplit(A,3))

# numpy的copy 与deepcopy

a=np.arange(4)
b=a
c=a
d=b

e=copy.copy(a)
print(a,b,c,d)
a[0]=11
print(a,b,c,d,e)
