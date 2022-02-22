# REVIEW
# # 这里是一个InterViewQA的问题解答。link git@github.com:kenwoodjw/python_interview_question.git
# NOTE 51.内存泄露是什么？如何避免？
#
# **内存泄漏**指由于疏忽或错误造成程序未能释放已经不再使用的内存。内存泄漏并非指内存在物理上的消失，而是应用程序分配某段内存后，由于设计错误，导致在释放该段内存之前就失去了对该段内存的控制，从而造成了内存的浪费。

# 有`__del__()`函数的对象间的循环引用是导致内存泄露的主凶。不使用一个对象时使用: del object 来删除一个对象的引用计数就可以有效防止内存泄露问题。

# 通过Python扩展模块gc 来查看不能回收的对象的详细信息。

# 可以通过 sys.getrefcount(obj) 来获取对象的引用计数，并根据返回值是否为0来判断是否内存泄露
# NOTE 52、python 常见的列表推导
# [i for i in range(10) if i % 2 == 0]
# st = dict(zip([i for i in "abcdefgh"], [i for i in range(10)]))
# # print(st)
# ss = [{k, v} for k, v in dict(zip([i for i in "abcdefgh"], [i for i in range(10)])).items() if v > 5]
# print(ss)

# NOTE 53、简述read readline readlines
# read 读取整个文件，readline读取一行，readlines 读取整个文件到一个迭代器。

# NOTE 54、**散列函数**（英语：Hash function）又称**散列算法**、**哈希函数**，
# 是一种从任何一种数据中创建小的数字“指纹”的方法。散列函数把消息或数据压缩成摘要，使得数据量变小
# 将数据的格式固定下来。该函数将数据打乱混合，重新创建一个叫做**散列值**（hash values，hash codes，hash sums，或hashes）的指纹。
# 散列值通常用一个短的随机字母和数字组成的字符串来代表

# NOTE 55、Python函数的重载机制。可变参数类型与可变参数个数。

# NOTE 56、写一个函数找出整个数组里第二大的数，--->重复。
# import random
# list_alpha=[i for i in range(10)]
# random.shuffle(list_alpha)
# print(list_alpha)
# sorted_list_alpha=sorted(list_alpha,reverse=True)
# print(sorted_list_alpha[1])
# def find_second(list_random):
#     biggest_num=list_random[0]
#     for i in list_random:
#         if i>biggest_num:
#             biggest_num=i
#         else:
#             pass
#     second_num=list_random[0]
#     for j in list_random:
#         if j>second_num and j <biggest_num:
#             second_num=j
#         else:
#             pass
#     return second_num
# res=find_second(list_random=list_alpha)
# print(res)

# NOTE 57、手写一个判断时间的装饰器,这里改一下，改成函数运行时间的消耗。
# import time
# def time_spend(func):
#     def warpper(*args):
#         time_start=time.time()
#         func(*args)
#         time_end=time.time()
#         print(time_end-time_start)
#     return warpper


# @time_spend
# def func_cal(input_list=[i for i in range(10)]):
#     for _ in input_list:
#         time.sleep(0.2)

# func_cal()

# NOTE 58、使用python内置函数来过滤
print(list(filter(lambda x:x%2==0,[i for i in range(10)])))

#NOTE 59、编写函数的四个原则
# 1、函数设计一定要小
#2、函数声明要做到合理简单易于使用
# 3、函数要考虑向下兼容
# 4、一个函数尽量只做一个事情。

#NOTE 60、函数的参数传递

# Python 函数的参数传递,一般有值传递或者引用传递
# 值传递 一般是int bool tuple string
# 应用传递 list dict 还有后面的dataFrame Series
