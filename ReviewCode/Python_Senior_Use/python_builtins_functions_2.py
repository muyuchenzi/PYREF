class Buildin_functions(object):
    def __init__(self, num_var, string_var, bool_var, dict_var, list_var, tuple_var):
        self.num_var = num_var
        self.string_var = string_var
        self.bool_var = bool_var
        self.dict_var = dict_var
        self.list_var = list_var
        self.tuple_var = tuple_var

    def build_all(self):
        print(all(self.list_var))

    def build_any(self):
        print(any(self.list_var))

    def build_zip(self):
        print(zip(self.list_var, self.tuple_var))
        print(list(zip(self.list_var, self.tuple_var)))

    def build_filter(self):
        filter_res = filter(lambda x: len(str(x)) > 3, self.list_var)
        print(list(filter_res))

    def build_map(self):
        map_result = map(lambda x: str(x) + "map_functions", self.list_var)
        print(list(map_result))

    def build_range(self):
        range_res = range(len(self.list_var))
        print(range_res)

    def build_iter(self):
        iter_res = iter(self.list_var)
        print(next(iter_res))
        print(next(iter_res))
        print(next(iter_res))
        print(next(iter_res))
        print(next(iter_res))

    def build_eval(self):
        eval("print(f'this is heppened {self.num_var}')")
        print("Done")

    def build_exec(self):
        exec("for i in range(10):"
             "print(i)"
             )


global_string_vars = "string_var"
global_num_vars = 23


def func():
    a = 10
    print(locals())
    # print(globals())


if __name__ == '__main__':
    build_func = Buildin_functions(num_var=-23, string_var="December239%$@", bool_var=False,
                                   dict_var={"a": 23, "false": False, "complex": "stringTest"},
                                   list_var=[-12, 'string', False, True, ['execute', "abc"]],
                                   tuple_var=(-122, False, "temp_string", "String", ['FindString', "abc"]))
    build_func.build_all()
    build_func.build_any()
    build_func.build_zip()
    build_func.build_filter()
    build_func.build_map()
    func()
    print("-" * 20)
    build_func.build_range()
    build_func.build_iter()
    build_func.build_eval()
    build_func.build_exec()
    print(callable(func))
    print(callable(global_num_vars))
