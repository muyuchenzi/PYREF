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


if __name__ == '__main__':
    build_func = Buildin_functions(num_var=-23, string_var="December239%$@", bool_var=False,
                                   dict_var={"a": 23, "false": False, "complex": "stringTest"},
                                   list_var=[-12, 'string', False, True, ['execute', "abc"]],
                                   tuple_var=(-122, False, "temp_string", "String", ['FindString', "abc"]))
    build_func.build_all()
    build_func.build_any()
    build_func.build_zip()
    build_func.build_filter()
