class Human(object):
    def __init__(self, name, age, *args, **kwargs):
        print("----", *args)
        super().__init__(*args, **kwargs)
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.age)
