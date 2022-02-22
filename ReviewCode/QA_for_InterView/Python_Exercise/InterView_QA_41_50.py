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
# class Student():
#     student_sum=0
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         self.__score=0
#         self.__class__.student_sum+=1
#     def cal_num_self(self):
#         print(self.__class__.student_sum)
#     def modify_socre(self,score):
#         self.__score=score
    
#     @classmethod
#     def cal_num(cls):
#         print(f"类方法：{cls.student_sum}")
#     @staticmethod
#     def my_static():
#         print("this is a static method!!")

# if __name__=="__main__":
#     std_alpha=Student("chenzi",12)
#     std_beta=Student("muyu",23)
#     std_gamma=Student("gogo",24)
#     #NOTE 实例可以调用 类方法，静态方法，实例方法
#     std_alpha.cal_num()
#     std_alpha.my_static()
#     std_alpha.cal_num_self()
#     #NOTE 类可以调用类方法，静态方法
#     Student.cal_num()
#     Student.my_static()
#     #NOTE 静态方法可以被类或者实例调用。就是一个常规函数。

#NOTE 43、 遍历一个object的所有属性，
class Car():
    def __init__(self,name,loss):# loss [价格，油耗，公里数]
        self.name=name
        self.loss=loss
        self._obj_num=0
    def getName(self):
        return self.name
    def getPrice(self):
        return self.loss[0]
    def getLoss(self):
        return self.loss[1]*self.loss[2]
    @property
    def getSpend(self):
        return self._obj_num
    @property
    def set_obj(self,num):
        self._obj_num=num
BMW=Car("宝马",[50,9,500])
print(getattr(BMW,'name'))
print(BMW.getSpend)
setattr(BMW,"name","bm")
print(getattr(BMW,"name"))
print(hasattr(BMW,"name"))
#NOTE 44
# class Array:
#     __list = []
    
#     def __init__(self):
#         print ("constructor")
    
#     def __del__(self):
#         print ("destruct")
    
#     def __str__(self):
#         return "this self-defined array class"

#     def __getitem__(self,key):
#         return self.__list[key]
    
#     def __len__(self):
#         return len(self.__list)

#     def Add(self,value):
#         self.__list.append(value)
    
#     def Remove(self,index):
#         del self.__list[index]
    
#     def DisplayItems(self):
#         print ("show all items---")
#         for item in self.__list:
#             print(item)

#NOTE 46.请描述抽象类和接口类的区别和联系
# 1.抽象类： 规定了一系列的方法，并规定了必须由继承类实现的方法。由于有抽象方法的存在，所以抽象类不能实例化。
# 可以将抽象类理解为毛坯房，门窗，墙面的样式由你自己来定，所以抽象类与作为基类的普通类的区别在于约束性更强

#2.接口类：与抽象类很相似，表现在接口中定义的方法，必须由引用类实现，但他与抽象类的根本区别在于用途：与不同
# 个体间沟通的规则，你要进宿舍需要有钥匙，这个钥匙就是你与宿舍的接口，你的舍友也有这个接口，所以他也能进入
# 宿舍，你用手机通话，那么手机就是你与他人交流的接口

#NOTE47、 setatrr,getattr.hasattr
#NOTE48、哪些操作会导致Python内存溢出，怎么处理？
# 1、内存加载的数据过大或者从数据库里一次性提取的数据过多，比如4g内存，读取8g的数据的时候就会导致这样的问题
# 2、集合类中有对对象的引用，引用没有消除，产生堆积，没有释放
# 3、代码中死循环for while等
# 4、启动参数内存过小，或者使用的第三方bug

#NOTE49、内存的管理
# 变量不需要声明
#变量无需指定类型
# 不用担心内存的管理，采用引用计数的办法如果没有引用会被回收
# del能直接释放资源。
