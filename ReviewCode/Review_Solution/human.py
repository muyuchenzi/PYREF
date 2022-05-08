class Human(object):
    class_person_name = "Person"

    def __init__(self, name, age, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.name = name
        self.age = age

    def print_human(self):
        print(f"human 的变量为{self.name},{self.age}")
