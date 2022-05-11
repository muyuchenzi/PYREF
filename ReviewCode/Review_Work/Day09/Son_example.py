from Parent_example import Person
from gradefath_example import Annimal
from gradefath_example import A
from Parent_example import B

# 利用super 进行多重继承的时候容易引起钻石问题，为了保险起见用下面的方法，对父类进行逐个初始化。利用MRO进行查找
# 进行搜索，下面就是成功例子


class Student(Person, Annimal):
    def __init__(self, name, age, score, drink, sleep):
        print(f"{Student.mro()}")
        # todo 非常重要。。
        #  非常重要
        #  非常重要
        super(Student, self).__init__(name, age, drink,
                                      sleep)  # 是错的，因为super Student已经在Person---
        # 了，drink 与sleep在Person类查找不到，而需要在Annimal查找，
        # todo 还可以通过 设置*args **kwargs 来进行。总共三种方法，
        #  1、是对父类逐个进行初始化。
        #  2、通过mro进行查找进行初始化--->非常不推荐
        #  3、通过对父类初始化函数补充 未知参数 *args *kwargs

        # super(Student, self).__init__(name, age)
        # super(Person, self).__init__(drink, sleep)
        print("Student __init__ is running")
        # Person.__init__(self, name, age)#这个是另外一种方法
        # Annimal.__init__(self, drink, sleep)
        self.score = score
        print("Student __init__ is end")

    def print_file(self):
        print(self.name, self.age, self.score,
              self.people_country, self.drink, self.sleep)


class C(A, B):
    class_c = "this is class_c variable"

    def __init__(self, a, b, c):
        super(C,self).__init__(a, b)
        self.c = c
    def printer(self):
        print(self.class_c)

if __name__ == '__main__':
    # s1 = Student('chenzi', 14, 77, True, False)
    # print("-"*30)
    # s1.print_file()
    # print("-"*30)
    # print(Student.mro())

    print("----"*10)
    print(C.mro())
    chenzi=C("a","b","c")
    chenzi.printer()
    reuslt=chenzi.add(1,3)
