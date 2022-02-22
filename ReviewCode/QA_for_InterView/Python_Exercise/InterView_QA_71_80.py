# REVIEW
# # 这里是一个InterViewQA的问题解答。link git@github.com:kenwoodjw/python_interview_question.git

# NOTE 71.Python主要的内置数据类型都有哪些？ print dir( ‘a ’) 的输出？
# int string bool list tuple dict set

# NOTE 72.map(lambda x:x*x,[y for y in range(3)])
# list_alpha=map(lambda x:x*x,[y for y in range(3)])
# print(list(list_alpha))

# NOTE 73.hasattr(),setattr(),getattr()

# class Student():
#     student_num=0
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def name_print(self):
#         print(self.name)
#     def age_print(self):
#         print(self.age)
#     #测试
#     @property
#     def name_get(self):
#         return self.name

#     @property
#     def age_get(self):
#         return self.age

#     @property
#     def name_set(self,new_name):
#         self.name=new_name
#     @property
#     def age_set(self,new_age):
#         self.age=new_age

# chenzi=Student("chenzi",11)
# #hasattr
# print(hasattr(chenzi,'name'))
# print(hasattr(chenzi,'name_print'))
# print(hasattr(chenzi,'age_get'))
# #setattr
# setattr(chenzi,"name","muyu")
# print(chenzi.name)
# setattr(chenzi,"age",14)
# print(chenzi.age)
# #getattr
# print(getattr(chenzi,'name'))

# NOTE 74.一句话解决阶乘问题，采用reduce

# from functools import reduce
# result=reduce(lambda x,y:x*y ,[i for i in range(1,10)])
# print(result)

# NOTE 75.什么是lambda函数？ 有什么好处？

# 匿名函数，简单实用，不必为了一些很小的功能来进行函数定义等一系列复杂的操作。

# NOTE 76.递归函数停止的条件？
# 递归的终止条件一般定义在递归函数内部，在递归调用前需要进行判断，根据判断结果选择继续调用还是停止

# def recursive(n=10):
#     if n==0:
#         return 1
#     return n*recursive(n-1)
# print(recursive())

# 77.下面这段代码的输出结果将是什么？请解释。
# def mulit():
#     return [lambda x:i*x for i in range(4)]
# print(list([m(2)] for m in mulit()))#[[6], [6], [6], [6]]

# def multi_modify():
#     for i in range(4):
#         yield lambda x:i*x

# print(list([m(2) for m in multi_modify()]))

# 78.也是一个lambda的问题，求一个两个数的和
#
# 79.对设计模式的理解，简述你了解的设计模式？
# 设计模式是经过总结，优化的，对我们经常会碰到的一些编程问题的可重用解决方案。一个设
# 计模式并不像一个类或一个库那样能够直接作用于我们的代码，反之，设计模式更为高级，它
# 是一种必须在特定情形下实现的一种方法模板。
# 常见的是工厂模式和单例模式
#
# 80.一个单例模式

# def singleton(class_name):
#     single_class = {}

#     def wrapper(*args, **kwargs):
#         if class_name not in single_class:
#             single_class[class_name] = class_name(*args, **kwargs)
#             return single_class[class_name]
#         else:
#             pass
#     return wrapper


# @singleton
# class Stud():
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def age_print(self):
#         print(self.name)

# chenzi=Stud("chenzi",11)
# print(chenzi.age)
# muyu=Stud("muyu",12)
# print(muyu.age)