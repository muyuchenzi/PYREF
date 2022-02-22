# REVIEW
# # 这里是一个InterViewQA的问题解答。link git@github.com:kenwoodjw/python_interview_question.git
#NOTE 61.如何在function里面设置一个全局变量
# list_alpha=[i for i in range(10)]

# def print_result():
#     # global list_alpha
#     list_beta=[i for i in "abcd"]
#     for i in list_beta:
#         list_alpha.append(i)
#     print(list_alpha)

# def print_second():
#     print(list_alpha)
# print_second()
# print_result()

#NOTE62、缺省参数

# def func_alpha(a,b=1,c=[1,3,4],*args,**kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#     print(kwargs)
# func_alpha("a",'b',['1','2','3'],'c','d',e='e',f='f')

#NOTE 64、带参数装饰器
# def add_func(func):
#     def wrapper(username,password):
#         print("通过验证")
#         print("开始执行功能")
#         result=func(username,password)
#         return result
#     return wrapper
# @add_func
# def log_in(username,password):
#     # username="chenzi"
#     # password=123
#     if username=='chenzi' and password==123:
#         return "right"
# print(log_in("chenzi",123)) 

#NOTE ### 65.为什么函数名字可以当做参数用?

# Python中一切皆对象，函数名是函数在内存中的空间，也是一个对象

#NOTE ### 66.Python中pass语句的作用是什么？

# 在编写代码时只写框架思路，具体实现还未编写就可以用pass进行占位，是程序不报错，不会进行任何操作。

#NOTE  67、c的结果
# a = 10
# b = 20
# c = [a]
# a = 15
# print(c)
# 68、交换两个变量的值
# a,b=1,2
# a,b=b,a
# print(a,b)
# #NOTE 69、map 函数和reduce函数
# from functools import reduce
# print(list(map(lambda x:x**2,[i for i in range(5)])))
# print(reduce(lambda x,y:x+y,[i for i in range(10)]))

#NOTE ### 70.回调函数，如何通信的?

# 回调函数是把函数的指针(地址)作为参数传递给另一个函数，将整个函数当作一个对象，赋值给调用的函数。