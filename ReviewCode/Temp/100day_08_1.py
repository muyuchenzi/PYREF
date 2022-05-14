class Student(object):
    '''
    基本类的定义与初始化
    '''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f"{self.name}正在学习{course_name}")

    def watch_movie(self):
        if self.age < 18:
            print("{0}只能动画片一类的电影".format(self.name))
        else:
            print(f"{self.name}可以任意选择电影类型")


class Test():
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print("__bar 函数被调用")






def main():
    stud1 = Student("chenzi", 12)
    stud1.study("python 程序设计")
    stud1.watch_movie()
    stud2 = Student("muyu", 22)
    stud2.study("生活经营")
    stud2.watch_movie()
    #NOTE 访问可见
    test=Test("hello")
    print(test.__dict__)
    test._Test__foo="world"
    print(test.__dict__)
    print(dir(test))
    test._Test__bar()




if __name__ == "__main__":
    main()
