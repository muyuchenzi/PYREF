from Class_Human import Human
from Class_Work import Work


class Student(Human, Work):
    sum_number = 0

    # def __init__(self, name, age, work_class,school):
    def __init__(self, name, age, work_class, school):
        # super(Student, self).__init__(*args, **kwargs)
        # super(Student, self).__init__()
        # super(Student, self).__init__(work_class)
        # super(Student, self).__init__(age, name)
        # Human.__init__(self, name, age)
        # Work.__init__(self, work_class)
        super(Student, self).__init__(name, age, work_class)
        self.school = school

        # self.__score = 0
        # self.__class__.sum_number += 1

    def modify_score(self):
        pass

    @classmethod
    def cal_num(cls):
        print(cls.sum_number)

    @staticmethod
    def my_static():
        print("this is staticmethod")


if __name__ == '__main__':
    st1 = Student(name='chenzi', age=12, work_class='lalala', school='code')
