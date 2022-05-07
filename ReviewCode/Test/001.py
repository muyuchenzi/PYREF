# python 里的值类型与引用类型
# 值类型 string int tuple 
# 引用类型 list  dict set
# 字符串的比较是ASCII码的比较

# 成员运算符
list_alpha=[i for  i in range(10)]
list_beta=[i for i in 'abcdefg']

dict_alpha=set(list_beta)
print(dict_alpha)
print(3 in list_alpha)
print('a' in dict_alpha)

# 身份运算符
list_alpha=[1,2,3]
list_beta= [1,2,3]
print(list_alpha is list_beta)
print(list_alpha == list_beta)
import random
print(random.shuffle(list_alpha))
print(list_alpha)
# 类型判断

print(isinstance([1,2],list))
