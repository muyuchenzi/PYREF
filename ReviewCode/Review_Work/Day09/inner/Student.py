class Student():
    name = 'muyuchenzi'
    age = 20

    def __init__(self, store):
        self.store = store

    def print_file(self):
        print(f"学生name：{self.name};学生age:{self.age};学生成绩:{self.store}")

    @staticmethod
    def static_print_file():
        print("this is 静态方法")

    @classmethod
    def class_print_file(cls):
        print("this is 类函数")


if __name__ == '__main__':
    stu1 = Student('76')
    stu1.print_file()
    stu1.static_print_file()
    stu1.class_print_file()
    Student.class_print_file()
    Student.static_print_file()
