class Student():
    # name=""
    # password="abc123"
    sum = 0
    __number=1
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.sum += 1

    def frofile_print(self):
        print(self.name)
        # print(self.password)
        print(self.age)
        # print(f"创建了{sum}个对象！")

    @classmethod
    def class_print(cls):
        print(cls.sum)
        print(f"类的私有变量{cls.__number}.")

    @staticmethod
    def static_print():
        print("this is staticmethod")
# 方法跟函数，方法其实是在设计方面，而是一种面向对象的结果，而函数就是一个解决问题的途径
# 面向对象方法就是把数据和对数据的操作封装在一起，这个就是很容易理解


if __name__ == '__main__':
    chenzi = Student("chenzi", 12)
    chenzi.frofile_print()
    chenzi.class_print()
    muyu = Student("muyu", 13)
    muyu.frofile_print()
    muyu.class_print()
    print("-"*30)
    # print(Student.__number)
