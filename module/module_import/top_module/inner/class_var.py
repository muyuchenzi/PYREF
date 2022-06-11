from const_var import list_alpha


class Person:
    def __init__(self, name, age, *args, **kwargs):
        super(Person, self).__init__(*args, **kwargs)
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} age is {self.age}"


class Stu(Person):
    def __init__(self, name, age, score):
        super(Stu, self).__init__(name, age)
        self.score = score


class Tools:
    def __init__(self, tool, space, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tool = tool
        self.space = space


class Worker(Person, Tools):
    def __init__(self, name, age, tool, space, money):
        super().__init__(name, age, tool, space)
        self.money = money

    def work_profile(self):
        return f"name:{self.name},age:{self.age},tool:{self.tool}" \
               f"space:{self.space},money:{self.money}"


if __name__ == '__main__':
    chenzi = Stu("chenzi", 12, 99)
    muyu = Worker("muyu", 23, 'code', 'desktop', 15000)
    print(list_alpha)
