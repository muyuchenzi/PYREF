# python 一共提供了68个内置函数
class Buildin_funcitons(object):
    def __init__(self, num_var, string_var, bool_var, dict_var, list_var, tuple_var):
        self.num_var = num_var
        self.string_var = string_var
        self.bool_var = bool_var
        self.dict_var = dict_var
        self.list_var = list_var
        self.tuple_var = tuple_var

    def build_abs(self):
        print(abs(self.num_var))

    def build_hex(self):
        print(hex(self.num_var))

    def build_oct(self):
        print(oct(self.num_var))

    def build_bin(self):
        print(bin(self.num_var))

    def build_divmode(self):
        print(divmod(self.num_var, 4))

    def build_reverse(self):
        reversed_res = reversed(self.string_var)

        # print(list(reversed(self.string_var)))
        print("".join(reversed_res))

    def build_len(self):
        print(len(self.list_var))
        print(len(self.string_var))
        print(len(self.tuple_var))
        print(len(self.dict_var))
        # print(len(self.num_var))

    @staticmethod
    def build_math():
        math_num_var = -23.343454
        print(round(math_num_var, 3))

    @staticmethod
    def build_math_pow():
        print(pow(3, 3))

    @staticmethod
    def build_math_sum():
        print(sum([1, 2, 3, 456, 45, 67]))
        print(sum({"a": 1, "b": 10, "c": 12}.values()))

    @staticmethod
    def build_min():
        print(min([12, 34, 1]))
        print(min({"a": -1, "b": 10, "c": 12}.values()))

    @staticmethod
    def build_max():
        print(max([12, 34, 1]))
        print(max({"a": -1, "b": 10, "c": 12}.values()))

    @staticmethod
    def build_repr():
        string_var = '\n第一行\t第二列 \\s第三列'
        print(repr(string_var))
        print(string_var)

    @staticmethod
    def build_sort():
        list_vars = [5, 7, 6, 12, 1, 13, 9, 18, 5]
        print(sorted(list_vars, reverse=False))
        print(sorted(list_vars, reverse=True))
        print(list_vars.reverse())
        print(list_vars.sort(reverse=True))



if __name__ == '__main__':
    build_func = Buildin_funcitons(num_var=-23, string_var="December239%$@", bool_var=False,
                                   dict_var={"a": 23, "false": False, "complex": "stringTest"},
                                   list_var=[-12, 'string', False, True, ['execute', "abc"]],
                                   tuple_var=(-12, 'string', False, True, ['FindString', "abc"]))
    build_func.build_abs()
    build_func.build_hex()
    build_func.build_oct()
    build_func.build_bin()
    build_func.build_math()
    build_func.build_divmode()
    build_func.build_math_pow()
    build_func.build_math_sum()
    build_func.build_min()
    build_func.build_max()
    print("-----------")
    build_func.build_reverse()
    build_func.build_repr()
    build_func.build_len()
    build_func.build_sort()
