class First():
    def __init__(self, name, *args, **kwargs):
        # super(First, self).__init__()
        self.name = name
        super().__init__(*args, **kwargs)
        print("first")


class Second():
    def __init__(self, age, *args, **kwargs):
        self.age = age
        super().__init__(*args, **kwargs)
        print("second")


class Third(First, Second):
    def __init__(self, name, age, score):
        self.score = score
        super(Third, self).__init__(name, age)
        Second.__init__(self, age)
        print("third")

    def get_value(self):
        print(self.name, self.age, self.score)


print(Third.mro())
xx = Third('chenzi', 12, 44)
# xx.get_value()
if __name__ == '__main__':
    xx = Third('chenzi', 12, 34)
