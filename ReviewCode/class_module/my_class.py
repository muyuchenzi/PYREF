class Student():
    name = 'xx'
    age = 0

    def __init__(self, name, age):
        print(name)
        self.name = name
        self.age = age
        self.test = 'test'
        print("-----")
        print(self.__class__.name)
        print("-----")

    def printer(self):
        print(self.name)
        print(self.age)
        print(self.test)


if __name__ == '__main__':
    x = Student.name
    chenzi = Student('chenzi', 12)
    chenzi.printer()
