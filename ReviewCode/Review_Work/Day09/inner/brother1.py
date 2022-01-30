class Animal(object):
    def __init__(self, drink, sleep):
        # print("Annimal __init__ is running")
        # super(Annimal, self).__init__()
        super(Animal, self).__init__()
        self.drink = drink
        self.sleep = sleep
        # print("Annimal __init__ is end")
