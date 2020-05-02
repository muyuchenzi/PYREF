class Father(object):
    father_lever = []

    # def __new__(cls, *args, **kwargs):
    #     print("this is new happened")

    def __init__(self, id, num):
        self.id = id
        self.__num = num

    def get_num(self):
        return self.num

    def modify_private_data(self, new_num):
        if new_num < 0:
            raise RuntimeError("new_num is letter than zero")
        else:
            self.__num = new_num
            print('this is modify private data called')

    def __private_object_method(self):
        self.id = "init"

    @property
    def get_id(self):
        return self.id

    @staticmethod
    def get_full_string():
        print("this is static method")

    @classmethod
    def get_father_lever(cls):
        return cls.father_lever


if __name__ == '__main__':
    father_001 = Father('001', 100)
    # father_001.__private_object_method()#私有化方法
    father_001.__num = 200  # 这个是给father_001添加了个__num副本，并没有改变私有变量
    father_001.__num  # 这个是读取了上面重新赋值的__num
    father_001.__dict__  # 从这个可以看到私有变量并乜有什么改变
