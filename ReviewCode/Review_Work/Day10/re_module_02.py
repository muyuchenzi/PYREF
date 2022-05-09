import re

# 数量词* + ? {}
str_alpha = 'python 23 javaScript rube89php'
alpha_result = re.findall('[a-zA-Z]+', str_alpha)  # +符号-->1到无穷
alpha_result2 = re.findall('[a-zA-Z]{3,10}', str_alpha)  # {}符号 -->3次-10次 默认贪婪模式
alpha_result3 = re.findall('[a-zA-Z]{3,10}?', str_alpha)  # {}符号 -->3次-10次 ？非贪婪模式

str_beta = "pytho0python1pythonn2pythonnnn3"
beta_result = re.findall(r'python*', str_beta)  # *前面这个字符0次或者无数次
beta_result1 = re.findall(r'python+', str_beta)  # *前面这个字符0次或者无数次
beta_result2 = re.findall(r'python?', str_beta)  # ?前面这个字符0次或者1次--->切记中英文
# ?如果前面是范围的话是贪婪模式与非贪婪模式，如果是字符的话则是0次与1次
beta_result3 = re.findall(r'python{1,2}?', str_beta)

qq_number = '1234566787'
qq_result = re.findall(r'\d{4,11}', qq_number)
qq_result1 = re.findall(r'\d{4,5}7$', qq_number)  # 边界匹配，以^开头 $结束
qq_result2 = re.findall(r'^1\d{4,9}$', qq_number)  # 边界匹配，以^开头 $结束

str_gamma = 'pythonpythonpythonpythonpythonpython'
gamma_result = re.findall('(python){2}', str_gamma)  # pythonpython字符 可以多测试这个

str_delta = 'python\nC#Java'
str_result = re.findall(r'PYTHON', str_delta, re.I)  # re.I 忽略大小写
str_result2 = re.findall(r'PYTHON.{1}', str_delta, re.I | re.S)  # re.S忽略换行符
