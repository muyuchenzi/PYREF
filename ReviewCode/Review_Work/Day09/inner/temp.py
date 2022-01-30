from brother1 import Animal
from brother2 import Person


class Student(Person, Animal):
    def __init__(self, name, age, score, drink, sleep):
        # Person.__init__(self, name, age)
        # Animal.__init__(self, drink, sleep)
        super().__init__()
        self.score = score

    def print_file(self):
        print(self.name, self.age, self.score, self.people_country, self.drink, self.sleep)


if __name__ == '__main__':
    s1 = Student('chenzi', 14, 77, True, True)
    s1.print_file()
