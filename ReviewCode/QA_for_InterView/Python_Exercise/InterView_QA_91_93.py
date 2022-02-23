# REVIEW
# # 这里是一个InterViewQA的问题解答。link git@github.com:kenwoodjw/python_interview_question.git
# NOTE 91.Python的魔法方法
# 魔法方法就是可以给你的类增加魔力的特殊方法，如果你的对象实现（重载）了这些方法中的某一个，那么这个方
# 法就会在特殊的情况下被Python所调用，你可以定义自己想要的行为，而这一切都是自动发生的，它们经常是两个下
# 划线包围来命名的（比如`__init___`,`__len__`),Python的魔法方法是非常强大的所以了解其使用方法也变得尤为重要!

# `__init__`构造器，当一个实例被创建的时候初始化的方法，但是它并不是实例化调用的第一个方法。

# `__new__`才是实例化对象调用的第一个方法，它只取下cls参数，并把其他参数传给`__init___`.

# `___new__`很少使用，但是也有它适合的场景，尤其是当类继承自一个像元祖或者字符串这样不经常改变的类型的时候。

# `__call__`让一个类的实例像函数一样被调用

# `__getitem__`定义获取容器中指定元素的行为，相当于self[key]

# `__getattr__`定义当用户试图访问一个不存在属性的时候的行为。

# `__setattr__`定义当一个属性被设置的时候的行为

# `__getattribute___`定义当一个属性被访问的时候的行为

# NOTE 92.面向对象的只读属性

# class Person():
#     def __init__(self, name):
#         self.__name = name

#     def name_print(self):
#         print(self.__name)
#     #最好的属性设定方法
#     @property
#     def name_set(self,new_name):
#         self.__name=new_name

# chenzi = Person("chenzi")
# print(chenzi.__dict__)
# chenzi._Person__name = "muyu"  # 其实还是可以访问的只不过是经过隐藏了,不过还是遵守这个约定。
# chenzi.name_print()

# setattr(chenzi,'_Person__name',"chenzi")# 也可使用装饰器来改回来。
# chenzi.name_print()

# NOTE  93.谈谈你对面向对象的理解？
# 面向对象是相当于面向过程而言的，面向过程语言是一种基于功能分析的，以算法为中心的程序设计方法，
# 而面向对象是一种基于结构分析的，以数据为中心的程序设计思想。在面向对象语言中有一个很重要的东西，叫做类。
# 面向对象有三大特性：封装、继承、多态。
#
#NOTE 94.请写出一段代码用正则匹配出ip？
# import re
# string_alpha="23reafdjafwqerfafj123.255.255.192euiriafjafajf"
# resutl=re.findall('\d+\.\d+\.\d+\.\d{0,3}',string_alpha)
# print(resutl)

#NOTE 95.a="abbbccc"请用正则匹配abccc不管有多少b，就出现一次

# import re

# string_alpha='abbbccc'
# print(re.sub('b+','b',string_alpha))
