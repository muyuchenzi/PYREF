# REVIEW
# # 这里是一个InterViewQA的问题解答。link git@github.com:kenwoodjw/python_interview_question.git
# #NOTE 41.super函数的具体用法和场景
# class A():
#     def __init__(self, a, *args, **kwargs) -> None:
#         super().__init__(*args,**kwargs)
#         self.a = a
#         # print(args)

#     def a_print(self):
#         print(self.a)


# class B():
#     def __init__(self, b, *args, **kwargs) -> None:
#         super().__init__(*args,**kwargs)
#         self.b = b

#     def b_print(self):
#         print(self.b)
#     def temp(self):
#         print("test")

# class C(A, B):
#     def __init__(self, a, b, c, * args, **kwargs) -> None:
#         super().__init__(a, b, *args, **kwargs)
#         self.c = c

#     def c_print(self):
#         print(self.c)


# c = C(1, 2, 3)
# c.a_print()
# c.b_print()
# c.c_print()
# c.temp()

#NOTE python 类方法、类实例方法、静态方法有何区别？
# Python 类方法可以被类调用，也可以被实例调用
# 实例方法可以被实例调用，
# 静态方法可以呗类调用，也可以被实例调用，因为这基本上是一个平常函数。

