import re

# findall 找到所有的符合的字符串并以list返回
# sub 找到符合字符串，用字符串进行替换
# replace 替换
lanuage = "pythonC#JavaPHPpythonpythonpythonpython"
lanuage_result = re.sub('python', 'rube', lanuage, count=2)
result = lanuage_result.replace('C#', "GO")

xx = None


def covert_func(list):
    global xx  # 通过声明为全局变量，将变量打印出来查看
    xx = list
    print(list.group(0))
    return "end"


# re sub可以使用函数
lanuage_sub_result = re.sub('python', covert_func, lanuage)
xx.group()  # 查看匹配结果
xx.span()  # 查看匹配的开始与结束tuple

str_alpha = 'A8C3721D86'  # 找出所有数字，如果数字大于6替换成9,如果小于等于6替换成0


def num_covert(str_input):
    str_num = int(str_input.group())
    if str_num > 6:
        return "9"
    else:
        return "0"


result_number = re.sub(r'\d', num_covert, str_alpha)

# match
# match 从首字符开始 找不到就None
# search 找到第一个就返回 找不到返回None
str_beta = "pythoC#JAVAPHP python"
beta_result = re.match(r'python', str_beta)
beta_result2 = re.search(r'python', str_beta).group()
