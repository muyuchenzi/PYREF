a = 1.2345
print(round(a, 3))
import itertools


# 函数的定义def 关键字，参数的设置，返回值
def add_function(input_list_1, input_list_2):
    '''
    将两个list合并然后返回内容的字符串
    :param input_list_1:第一个list
    :param input_list_2: 第二个list
    :return: 返回合并list的字符串
    '''
    add_result = ''.join([str(i) for i in input_list_1]) + ''.join(input_list_2)
    return add_result


list_input = [i for i in range(20)]


def recursion_function(list_input):
    '''
    计算数值list的值，采用递归的方法
    :param list_input:
    :return: 返回总和
    '''
    # if list_input_len == len(list_input):
    #     return
    # list_sum += recursion_function(list_input)
    print(list_input)
    if len(list_input) == 0:
        return 0
    else:
        print(list_input[1:])
        return list_input[0] + recursion_function(list_input[1:])

    sum_result = recursion_function(list_input)


def temp(input_string='abcdefghig'):
    if len(input_string) == 0:
        return ''
    else:
        result = input_string[0] + '-' + temp(input_string[1:])
        return result


# xx = temp()
a, b = (1, 2)


def function_mulit_result(list_input1=[1, 2, 34], list_input_2=['x', 'y', 'z'], *args, **kwargs):
    print(args)
    print(kwargs)
    return list_input1[1], list_input_2[1]


xx = function_mulit_result([1, 23], ['x', 'x'], 3, a=1, b=3)

if __name__ == '__main__':
    # print(add_function(input_list_1=[1, 2, 3, 4], input_list_2=['x', 'y', 'z']))
    sum_result = recursion_function(list_input)
