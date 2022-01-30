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
