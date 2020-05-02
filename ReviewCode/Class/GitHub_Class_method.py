'''

'''

class TemplateClass(object):
    class_vars = [1, 2, 3]

    def __init__(self, obj_var):
        self.obj_var = obj_var

    def object_method(self):
        print(self.obj_var)
        print(self.class_vars)
        return "object" + self.obj_var

    @classmethod
    def class_method(cls):
        cls.class_vars = [0]
        print("this is class method")
        print("class_var" + str(cls.class_vars))

    @staticmethod
    def static_method():
        '''static_method 可以当做一般的方法'''
        print("this is staticmethod")

    def obj_modify_class_var(self):
        '''object 可以修改类变量，但是修改的是自身的类变量'''
        self.class_vars = ['temp']


if __name__ == '__main__':
    temp = TemplateClass('my_object_vars')
    TemplateClass.class_method()
    temp.object_method()
    temp.obj_modify_class_var()
    temp.static_method()
    temp.static_method()
    temp.class_method()