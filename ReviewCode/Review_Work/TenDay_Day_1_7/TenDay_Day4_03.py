# Python的基本数据类型---Set&dict

set_alpha = {1, 3, 45, 6, 6}

set_beta = {1, 3, 'one', 'two', True}
set_gamma = {1, 3}
# 集合的差,交集，并集

set_test = set_alpha - set_gamma
set_temp = set_alpha & set_gamma
set_delta = set_alpha | set_beta

# 集合的定义
set_a = set()
set_b = {}  # wrong 这是一个字典定义。。。

# 字典的使用 必须能够哈希,key可能被覆盖

dict_alpha = {"a": 1, "b": 3}
print(dict_alpha['a'])
a = {}

dict_alpha_key = [i for i in range(10)]
dict_alpha_value = [i for i in 'abckefghai']
dict_alpha = dict(zip(dict_alpha_key, dict_alpha_value))
for key, value in dict_alpha.items():
    print(key, value)
keys = list(dict_alpha.keys())
if __name__ == '__main__':
    # dict_for_loop()
    pass
