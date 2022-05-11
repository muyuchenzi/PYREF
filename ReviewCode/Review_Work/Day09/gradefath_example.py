class Annimal():
    def __init__(self, drink, sleep, *args, **kwargs):
        print("Annimal __init__ is running")
        # super(Annimal, self).__init__()
        super().__init__(*args, **kwargs)
        self.drink = drink
        self.sleep = sleep
        print("Annimal __init__ is end")


class A(object):
    class_a = 'this is class_a variable'

    def __init__(self, a,*args,**kwargs):
        self.a = a

    def printer(self):
        print(self.a)

    @staticmethod
    def add(x, y):
        z = x+y
        print(f'class A printer function{x}+{y}={z}')
        return z
