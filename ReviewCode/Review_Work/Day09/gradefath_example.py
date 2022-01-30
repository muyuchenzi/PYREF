class Annimal():
    def __init__(self, drink, sleep,*args,**kwargs):
        print("Annimal __init__ is running")
        # super(Annimal, self).__init__()
        super().__init__(*args,**kwargs)
        self.drink = drink
        self.sleep = sleep
        print("Annimal __init__ is end")
