class Student:
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
    chenzi = Student('chenzi', 14, 34)
    chenzi.get_number()
