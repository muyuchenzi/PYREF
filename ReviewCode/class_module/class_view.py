class Student():
    student_sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__score = 0
        self.__class__.student_sum += 1

    def cal_num_self(self):
        print(self.__class__.student_sum)

    def modify_score(self, score=0):
        self.__score = score

    @classmethod
    def cal_num(cls):
        print(cls.student_sum)

    @staticmethod
    def my_static():
        print("this is staticmethod")


if __name__ == '__main__':
    student1 = Student('chenzi', 11)
    # student1.__score
    student1.modify_score(59)
    student1.__score = 1
    print(student1.__score)
    # student1.cal_num_self()
    # student2 = Student("muyu", 12)
    # student2.cal_num_self()
    # student3 = Student("xiao", 22)
    # student3.cal_num_self()
    # Student.cal_num()
