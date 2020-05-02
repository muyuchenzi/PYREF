from GitHub_Class_inherit1 import Father


class Son(Father):
    def __init__(self, uid, num, old):
        self.old = old
        # super().__init__(uid, num)
        super(Son,self).__init__(uid, num)

    def modify_son_uid(self, new_uid):
        self.uid =new_uid


if __name__ == '__main__':
    son = Son("0001", 100, 23)
    father_num = son.get_num()
    father_id = son.get_full_string()
    print(son.father_lever)
    son.modify_son_uid('temp')