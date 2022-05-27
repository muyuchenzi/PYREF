from string import ascii_lowercase

'''
多重继承的问题，这个是一个模板例子
'''


class A():
    class_a = [i for i in range(100)]

    def __init__(self, a, *args, **kwargs):
        '''
        获取class_a的前多个元素的和
        :param a:
        '''
        super(A, self).__init__(*args, **kwargs)
        # super().__init__(*args,**kwargs) 这个也可以
        self.a = a

    def print_a(self):
        '''
        显示a的数字
        :return:
        '''
        print(self.a)

    def show_sum(self, number):
        result = sum(self.class_a[0:number])
        return result


class B():
    class_b = ascii_lowercase

    def __init__(self, b, *args, **kwargs):
        '''
        获取calss_b前多个元素
        '''
        super(B, self).__init__(*args, **kwargs)
        # super().__init__(*args,**kwargs) 这个也可以的
        self.b = b

    def print_b(self):
        print(self.b)

    def show_str(self, number):
        result = self.class_b[0:number]
        return result


class C(A, B):
    list_alpha = [_ for _ in range(10)]
    list_beta = [_ for _ in ascii_lowercase]
    class_c = dict(zip(list_beta, list_alpha))

    def __init__(self, a, b, c):
        super(C, self).__init__(a, b)
        # super().__init__(a,b)这个可以的，在多父类进行初始化的时候直接用super 就好，
        self.c = c

    def print_c(self):
        print(self.c)

    def show_dict(self, key):
        result = self.class_c[key]
        return result


def answer():
    ...


if __name__ == "__main__":
    chenzi = C(5, 4, 5)
    chenzi.print_a()
    chenzi.print_b()
    chenzi.print_c()

    class_a_vari = chenzi.class_a
    class_b_vari = chenzi.class_b
    class_c_vari = chenzi.class_c
    print(f"class_a_vari:{class_a_vari},\nclass_b_vari:{class_b_vari},\nclass_c_vari:{class_c_vari}")

    res_sum = chenzi.show_sum(4)
    res_str = chenzi.show_str(4)
    res_dic = chenzi.show_dict('e')
    print(f"class_a sum :{res_sum},\nclass_b str{res_str},\n class_c dict {res_dic}")
