class Student:
    #类的私有变量和实例的私有变量(其实还是可以通过其他办法来进行访问)
    sum_num = 0
    __number = 100

    def __init__(self, name, age, score, res):
        self.name = name
        self.age = age
        self.score = score
        self.__pri_num = res
        self.__class__.sum_num += 0

    def marking(self, get_score):
        if get_score < 0:
            print("成绩不能为负")
        else:
            self.score = get_score

    def get_number(self):
        print(self.__number)


if __name__ == '__main__':
    # pass
    chenzi = Student('chenzi', 14, 34,1)
    chenzi.get_number()
    # print(Student.__dict__)
    #类变量__number虽然是私有变量但是仍然可以通过一定的手段来进行访问
    Student._Student__number=99
    print(Student.__dict__)
    #实例变量__pri__num虽然是私有变量但是跟类变量一样也可以通过一定手段进行访问。
    print(chenzi.__dict__)
    chenzi._Student__pri_num=11
    print(chenzi.__dict__)
