class Person():
    people_country = 'china'

    def __init__(self, name, age, *args, **kwargs):
        print("Person __init__ is running")
        super().__init__(*args, **kwargs)
        self.name = name
        self.age = age
        # super(Person, self).__init__()
        print("Person __init__ is end")

    def print_person(self):
        print(f"姓名：{self.name}；年龄：{self.age}；国籍：{Person.people_country}")


class B(object):
    class_b = "this is class_b variable"

    def __init__(self, b,*args,**kwargs):
        self.b = b

    def printer(self):
        print(self.b)
    @staticmethod
    def add(x, y):
        z = x+y
        print(f"class B printer {x}+{y}={z}")
        return z
