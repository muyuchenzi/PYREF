# REVIEW
# # 这里是一个InterViewQA的问题解答。link git@github.com:kenwoodjw/python_interview_question.git
# NOTE 81.单例模式的应用场景有那些？
# 资源共享的情况下，避免由于资源操作时导致的性能或损耗等，如日志文件，应用配置
# 1,网站的计数器 2,应用配置 3.多线程池 4数据库配置 数据库连接池 5.应用程序的日志应用

# NOTE 82.用一行代码生成[1,4,9,16,25,36,49,64,81,100]
# print([i**2 for i in range(1,10)])

# NOTE 83.装饰器的理解。还是装饰器的例子，这里加了一个返回值。
# import time
# def time_spend(func):
#     def warpper(*args):
#         time_start=time.time()
#         func(*args)
#         time_end=time.time()
#         print(time_end-time_start)
#         return time_end-time_start
#     return warpper


# @time_spend
# def func_cal(input_list=[i for i in range(10)]):
#     for _ in input_list:
#         time.sleep(0.2)

# result=func_cal()
# print(result)
# 84.闭包
# NOTE 84.闭包就是函数内部有一个函数，且内部函数使用了外部函数的参数

# def out_func():
#     name="string"
#     def in_func():
#         for i in name:
#             print(i)
#     in_func()

# out_func()

# 85.函数装饰器有什么作用？
# 它可以在让其他函数在不需要做任何代码的变动的前提下增加额外的功能。
# 装饰器的返回值也是一个函数的对象，它经常用于有切面需求的场景。
# 比如：插入日志，性能测试，事务处理，缓存


# 86.生成器，迭代器的区别？
# https://docs.python.org/zh-cn/3/tutorial/classes.html#iterators
# 生成器会有yield关键字，迭代器是指遵循迭代协议的对象，比如list dict tuple string set
# def iteror():
#     list_res=[]
#     for i in range(10):
#         list_res.append(i)
#     return list_res
# res_1=iteror()
# print(res_1)
# def genertor():
#     for i in range(10):
#         yield i

# result=genertor()
# for res in result:
#     print(res)

# 87.X是什么类型?
# x=(i for i in range(10))
# x是生成器。
# print ([[x for x in range(1,100)] [i:i+3] for i in range(0,100,3)])

# 89. Python中yield的用法。
# 基本上就是generator的使用.


### 90.Python中的可变对象和不可变对象？

# 不可变对象，该对象所指向的内存中的值不能被改变。当改变某个变量时候，由于其所指的值不能被改变，相当于把原来的值
# 复制一份后再改变，这会开辟一个新的地址，变量再指向这个新的地址。

# 可变对象，该对象所指向的内存中的值可以被改变。变量（准确的说是引用）改变后，实际上其所指的值直接发生改变，
# 并没有发生复制行为，也没有开辟出新的地址，通俗点说就是原地改变。

# Pyhton中，数值类型(int 和float)，字符串str、元祖tuple都是不可变类型。而列表list、字典dict、集合set是可变类型