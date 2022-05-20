import numpy as np

a = np.arange(2, 14).reshape(3, 4)
print(a)
print(a[2])
print(a[2][1])
print(a[2, 1])
print(a[:, 1])

print('-'*15+"遍历行"+"-"*15)
for row in a:
    print(row)

print('-'*15+"遍历列"+"-"*15)
for col in a.T:
    print(col)

print('-'*15+"遍历所有"+"-"*15)
for row in a:
    for col in row:
        print(col)

#  numpy 的合并
A=np.array([1,1,1])
B=np.array([2,2,2])
print(np.stack((A,B)))

print(np.vstack((A,B)))
print(np.hstack((A,B)))
#转变成竖 然后合并
C=A[:,np.newaxis]
D=B[:,np.newaxis]
print(C)
print(D)
print("_"*30)
print(np.hstack((C,D)))
#
E=np.concatenate((A,B,B,A),axis=0)
print(E)