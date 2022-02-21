# REVIEW
# # 这里是一个InterViewQA的问题11-20的解答。link git@github.com:kenwoodjw/python_interview_question.git
# NOTE 11、 写一个列表生成式，产生一个公差为11的等差数列
# list_alpha = [i for i in range(1, 100, 11)]
# list_beta = [i*11 for i in range(10)]
# print(list_beta)
# print(list_alpha)

# NOTE 12、给定两个列表，找到里面相同的元素

# list_alpha=[2,3,4,34,456,24,9,24]
# list_beta=[i for i in range(30)]
# def find_same(li_alpha,li_beta):
#     same_list=[]
#     for i in li_alpha:
#         if i in li_beta:
#             same_list.append(i)
#         else:
#             pass
#     return same_list

# print(find_same(list_alpha,list_beta))
# set_alpha=set(list_alpha)
# set_beta=set(list_beta)
# print(set_alpha&set_beta)
# #NOTE 13、删除重复的list元素。

# print(list(set(list_alpha)))
# #保留原有顺序
# print(list_alpha.index)
# list_gamma=list(set_alpha)
# list_gamma.sort(key=list_alpha.index)
# print(list_gamma)

# #NOTE 14、找出不同的元素 ^&-|
# list_in_A_not_B=set(list_alpha)+set(list_beta)#A中有B中没有的
# list_not_same=set(list_alpha)^set(list_beta)
# list_all_items=set(list_alpha)|set(list_beta)

# NOTE 15、Python新式类与经典类的区别。
# python里凡是继承了基类object的就是新式类，class class_name(object);经典类的就是class class_name:
# python3里全是新式类，Python2是经典类
# 经典类是深度优先的搜索，继承类是广度优先的继承。
# 新式类使用a.class 与type(a)的结果是一样的，但是经典类是不一样的

# NOTE 16、Python的内置数据类型  数字、字符串、list、tuple、bool、dict、set
# NOTE 17、Python单例模式的实现方式：两种
# 第一种使用装饰器 建议使用这种方法。

# def singleton(cls):
#     instance={}
#     def wrapper(*args,**kwargs):
#         if cls not in instance:
#             instance[cls]=cls(*args,**kwargs)
#         return instance[cls]
#     return wrapper
# @singleton
# class Foo(object):
#     def __init__(self,x):
#         self.x=x
#     def print_item(self):
#         print(self.x)

# foo1=Foo("string")
# foo1.print_item()
# foo2=Foo(4)
# foo2.print_item()
# print(foo1 is foo2)

# 第二种 使用基类
# class Singleton(object):
#     def __new__(cls,*arg,**kwargs):
#         if not hasattr(cls,"_instance"):
#             cls._instance=super(Singleton,cls).__new__(cls,*arg,**kwargs)
#         return cls._instance

# class Coo(Singleton):
#     pass

# coo1=Coo()
# coo2=Coo()
# print(coo1 is coo2)

# NOTE 翻转一个整数 可能为整数213，也可能是-355.23一类的。
# from string import digits

# def rever_number(num):
#     ele = list(str(num))
#     if ele[0] in digits:
#         result = str(num)[::-1]
#         return int(result)
#     else:
#         result = str(num)[:0:-1]
#         return int(ele[0]+result)


# print(rever_number(-231))

# NOTE19、 查找指定文件夹下的指定格式的文件
# import os
# dir_path = "E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView"
# file_extend = 'txt'


# def find_filename(path, file_extend):
#     file_list = []
#     txt_file_list = []
#     for _, _, file in os.walk(path):
#         file_list.append(file)
#     # print(file_list)
#     file_list = [sub for i in file_list for sub in i]
#     for file in file_list:
#         extend = file.split(".")
#         if extend[1] == "txt":
#             txt_file_list.append(file)

#     print(txt_file_list)


# find_filename(dir_path, file_extend)
#NOTE 20、一句话实现1-100的和

print(sum([i for i in range(0,101)]))