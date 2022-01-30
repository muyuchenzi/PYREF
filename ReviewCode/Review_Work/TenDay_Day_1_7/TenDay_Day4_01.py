# Python的基本数据类型
list_alpha = [1, 2, 3, 4, 5]
list_beta = [1, '3', True, [12]]
list_gamma = [1, 3, 4, True, False, 'stringTest']
list_delta = [[1, 3, 4, 6], True, "string1233", (2, 3, 4)]
print([list_alpha[2]])
dict_alpha = {'1': 1, 'x': 2}
print(list(dict_alpha.keys()))
dict_value = dict_alpha.values()
dict_my = dict(zip([1, 2, 3], ['1', 'a']))

tuple_alpha = (1, 3, 4)
# tuple_alpha+(4,)
list_alpha.append(23)

a = 1 not in list_alpha


def print_element(list_input):
    for i in range(len(list_input)):
        print(list_input[i])


if __name__ == '__main__':
    print_element(list_input=list_alpha)
    print_element(list_beta)
