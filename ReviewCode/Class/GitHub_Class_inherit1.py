class Father(object):
    father_lever = [0]

    def __init__(self, uid, num):
        self.uid = uid
        self.__num = num

    def get_num(self):
        return self.__num

    def modify_private_data(self, new_num):
        if new_num < 0:
            raise RuntimeError("new_num is letter than zero")
        else:
            self.__num = new_num
            print('this is modify private data called')

    def __private_object_method(self):
        self.uid = "init"

    @property
    def get_id(self):
        return self.uid

    @staticmethod
    def get_full_string():
        print("this is static method")

    @classmethod
    def get_father_lever(cls):
        return cls.father_lever

