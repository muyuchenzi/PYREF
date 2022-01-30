# python 变量与运算符

from copy import deepcopy

# 变量就是一个变量，变量的定义，变量的命名是非常重要
# 变量的命名，避开系统保留关键字，另外要简单易懂，可读性要好。
# 变量不需要进行定义，而是可以进行赋值，是动态语言。
list_alpha = [i for i in range(5)]
list_beta = [i for i in 'list_test']
list_test = list_alpha * 3 + list_beta
list_alpha = ['a', 'b'] +[1, 2]

# 值类型与引用类型
a = 1
b = a
a = 3

a_alpha = [1, 2, 3]
b_alpha = a_alpha
a_alpha[1] = [1, 3]


# Todo 变量的值类型和引用类型的区别
# Todo int,str,tuple是值类型，list set dict 是引用类型
# todo 值类型不可改，直接绑定内存地址，而引用类型是给了一块地址，


def func_alpha(list_input):
    for alpha in list_input:
        print(alpha)


if __name__ == '__main__':
    list_input = [i for i in range(16)]
    func_alpha(list_input=list_input)
