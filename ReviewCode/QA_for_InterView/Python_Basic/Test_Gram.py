# 1、python 的参数传递 分为两种 i、值类型ii、应用类型，python常见的数据结构中，number string tuple 是值类型
# list dict set DataFrame Series是引用类型 值类型是copy一个副本，引用类型是copy了一个引用，
import pandas as pd


def get_kinds_var():
    num_var = 12
    str_var = "stringTest124@gmail.com"
    tuple_var = (1, 3, 'str', False)
    list_var = [1, 3, 'str', False]
    dict_var = {
        "one": 'one_value',
        "two": "two_value"
    }
    set_var = set([1, 2, 3, 4, 'str', 2, 3, False, True, False])
    DataFrame_var = pd.DataFrame(dict_var, index=[0])
    return num_var, str_var, tuple_var, list_var, dict_var, set_var, DataFrame_var


def function_var(num_var, str_var, tuple_var, list_var, dict_var, set_var, DataFrame_var):
    num_res = num_var - 5
    str_res = str_var + "_changed"
    tuple_res = tuple_var + (3, 2, 1, 0)
    list_res = list_var
    list_res.extend([3, 2, 1, 0])
    dict_res = dict_var
    dict_res["one"] = "one_value_changed"
    set_var.add("addValeu")
    DataFrame_res = DataFrame_var
    DataFrame_res.loc[0, 'one'] = "oneValueChanged"
    print(num_res, str_res, tuple_res, list_res,
          dict_res, set_var, DataFrame_res)
    return num_res, str_res, tuple_res, list_res, dict_res, set_var, DataFrame_res
