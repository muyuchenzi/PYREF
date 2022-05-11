# 字符串的操作与运算
# 主要分三种。
# 字符串的拼接 + join slice
str_alpha = 'hello'
str_beta = 'world'
str_gamma = str_alpha + str_beta
print('-'.join(str_alpha))
str_test = '='.join([str_alpha, str_beta])
print()
print(str_gamma[1])
print(str_gamma[0:5])  # 前闭后开的序号取值
print(f"result---{str_gamma[1:8:2]}")
str_temp = str_gamma[4:-6]  # 取不到则为空


def print_string(str_input):
    for i in range(len(str_input)):
        print(str_input[i])


if __name__ == '__main__':
    print_string('abcdefaf')
    print_string("hellowdafd")
