class Father(object):
    father_class_var = "father"

    def __init__(self, father_var):
        self.father_var = father_var

    def modify_object_var(self):
        self.father_var = "modify father"
        print("modify object var father")

    @staticmethod
    def father_static_method():
        print("this is father static meth od")

    @classmethod
    def father_class_method(cls):
        print("this is father class method")

    def father_object_method(self):
        print("this is father object method")


class Mother(object):
    mother_class_var = "mother"

    def __init__(self, mother_var):
        self.mother_var = mother_var

    def modify_object_var(self):
        self.mother_var = "modify mother" 
        print("modify object var mother")


class Son(Father, Mother):
    son_class_var = "son"

    def __init__(self, father_var, mother_var, son_var):
        # super().__init__(father_var=father_var, mother_var=mother_var)
        super().__init__(father_var=father_var)
        super().__init__(mother_var=mother_var)

        # Father.__init__(self, father_var=father_var)
        # Mother.__init__(self, mother_var=mother_var)
        self.son_var = son_var

    def modify_object_var(self):
        self.son_var = "modify by father object"
        self.father_var = "modify by son object"
        print("modify object var son")

    @staticmethod
    def father_static_method():
        print("this is happened in son class and call by son object")


if __name__ == '__main__':
    father = Father("father init")
    son = Son("son father init", "son mather init", "son son init")
    son.modify_object_var()
