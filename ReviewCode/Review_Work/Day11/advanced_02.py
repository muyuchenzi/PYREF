from functools import reduce

# python里的三元表达式


def three_x(x): return True if x > 3 else False


list_alpha = [i for i in range(10)]
# 对可迭代对象里的每一个元素进行计算
# list(map(lambda x, y: x + y + 1, list_alpha))
list(map(lambda x: x + 1, list_alpha))

# reduce() 的意义就是((((1+2)+3)+4) 将运算结果作为参数传进去进行下一波计算（所以后面的一定是可迭代对象）
reduce(lambda x, y: x + y + 10, list_alpha)
list_x = [i for i in 'abcdefg']
list_x_res = reduce(lambda x, y: x + y, list_x, '---')

# filter对可迭代对象进行过滤
list_y = [i for i in range(10)]
list_y_res = list(filter(lambda x: x > 4, list_y))
list_y_sss = list(filter(three_x, list_y))  # 利用三元表达式
