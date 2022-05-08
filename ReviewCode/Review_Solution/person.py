from human import Human
from annimal import Annimal

class Person(Annimal,Human):
    class_person_name="Person"
    def __init__(self,drink,sleep,name,age,score) -> None:
        super(Person,self).__init__(drink,sleep,name,age)
        self.score=score
        
    def print_person(self):
        print(f"Person 的变量为{self.score}")
        print(f"Human 的变量为{self.name},{self.age}")
        print(f"Annimal 的变量为{self.drink},{self.sleep}")
        

class Father():
    def __init__(self,father) -> None:
        self.father=father

class Son(Father):
    def __init__(self, father,son) -> None:
        super().__init__(father)
        self.son=son
    
    def print_son(self):
        print(self.father,self.son)


if __name__=="__main__":
    chenzi=Person("water",'12hours','chenzi','23',100)
    chenzi.print_person()
    #
    muyu=Son("fat-her","s--on")
    muyu.print_son()