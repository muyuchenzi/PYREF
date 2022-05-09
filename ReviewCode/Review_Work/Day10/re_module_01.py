import re

# 元字符，字符集，数量词，边界词，字符组
# . \d \w \s
#  [daf] [a-z]
# {} ? + *
# ^ $
# ()


str_alpha = "C|C++|Java|Python|JavaScript"
# 1、查找字符串
print('python' in str_alpha.lower())
print(str_alpha.index('Python'))
pattern_result = re.findall('Python', str_alpha)
print(pattern_result)
if len(pattern_result) > 0:
    print('发现')
# todo 元字符
# .除了换行符\n以外的所有字符
# 数字元字符
str_beta = 'C8|67C+34+|3Ja#xva6Python4Java868Script'
result_number = re.findall(r'\d\d', str_beta)
result_no_number = re.findall(r'\D', str_beta)

# Todo 字符集
str_gamma = 'abc,acc,adc,afc,ahc'
result = re.findall(r'a[cf]c', str_gamma)  # []内是或的关系
result1 = re.findall(r'a[^cf]c', str_gamma)  # []内取反
result2 = re.findall(r'a[c-f]c', str_gamma)  # []范围
str_delta = 'python1111java 678&$_php'
result3 = re.findall(r'[\d]', str_delta)  # \d digit简称
result4 = re.findall(r'\w', str_delta)  # \w word 简称
str_delta_a = 'pyt\rhon\n1111\t java 678&$_php'
result5 = re.findall(r'\s', str_delta_a)  # \s space 简称
