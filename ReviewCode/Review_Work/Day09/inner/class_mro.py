class A():
    pass


class B():
    pass


class C():
    pass


class D(A, B):
    pass


class E(B, C):
    pass


class F(D, E):
    pass


# 继承的规范，如果左侧优先 与 是否有父类
print(F.mro())
