class Student():
    name=""
    password="abc123"
    

    def __init__(self,age):
        self.age=age

    def frofile_print(self):
        print(self.name)
        print(self.password)
        print(self.age)
    
    @classmethod
    def class_print(cls):
        print(cls.name)

    
    @staticmethod
    def static_print():
        print("this is staticmethod")


if __name__=='__main__':
    chenzi=Student(12)
    chenzi.frofile_print()