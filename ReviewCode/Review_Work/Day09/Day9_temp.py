class Person:
    __grade = '人民路'
    __school = '复兴中学'

    def __init__(self, name, age, gender, score, high):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score
        self.high = high

    def print_file(self):
        print(f'这个学生的档案为：学校：{self.__school};年级：{self.__grade};名称：{self.name};性别：{self.gender};'
              f'年龄：{self.age};身高:{self.high};成绩：{self.score}')

    def change_class_var(self):
        self.__school = '中兴学校'

    @classmethod
    def print_class_var(cls):
        print(f"Person grade变量为：{cls.__grade}")
        print(f"Person school变量为：{cls.__school}")


if __name__ == '__main__':
    chenzi = Person('chenzi', 12, '男', score=78, high='178cm')
    muyu = Person('muyu', 12, '女', score=68, high='168cm')
    chenzi.change_class_var()
    chenzi.print_file()
    # muyu.print_file()
    # Person.print_class_var()
