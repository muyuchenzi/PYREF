class Annimal(object):
    annimal_class_name='Annimal'
    def __init__(self,drink,sleep,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.drink=drink
        self.sleep=sleep
    
    def print_annimal(self):
        print(f"动物类的变量为{self.drink}、{self.sleep}.")