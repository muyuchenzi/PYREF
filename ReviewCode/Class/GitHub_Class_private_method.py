class Father(object):
    father_lever = []

    # def __new__(cls, *args, **kwargs):
    #     print("this is new happened")

    def __init__(self, id, num):
        '''初始化实例'''
        print("this is init happened")
        self.id = id
        self.num = num
        self.father_lever.append((self.id, self.num))

    def get_num(self):
        return self.num

    @property
    def get_id(self):
        return self.id

    @staticmethod
    def get_full_string():
        print("this is static method")

    @classmethod
    def get_father_lever(cls):
        return cls.father_lever

    # def __dict__(self):
    #     return {self.id: self.num}
    def __repr__(self):
        return f"this is about repr function {self.id}:{self.num}"

    def __str__(self):
        return f"this is about str function {self.id}:{self.num}"


if __name__ == '__main__':
    father_001 = Father("001", 100)
    father_002 = Father("002", 200)
    '''
    father_001.__dict__
    Father.__dict__
    实例和类的__dict__，用来拿到实例和类的变量 用dict来进行表述
    '''
    """
    temp = Father.__call__("003", 300)
    temp.get_full_string()
    __call__()就是类的初始化调用等同于Father("id","num")
    """
    father_001.__class__
    father_001.__dir__()
    father_001.__repr__()
    father_001.__str__()
    print(father_001)


