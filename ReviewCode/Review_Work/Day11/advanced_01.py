# 闭包 函数与环境变量 不返回函数与不使用外部变量不是闭包

# def curve_pre():
#     a = 25
#
#     def curve(x):
#         return a * x * x
#
#     return curve
#
#
# y = curve_pre()
# y(3)


# 闭包的应用

def travel(postion):
    def go(step):
        # todo 声明非本地局部变量
        nonlocal postion
        new_pos = postion + step
        postion = new_pos
        return new_pos

    return go


alpha = travel(0)
beta = alpha(3)
gamma = alpha(5)
#
# origin = 0
#
#
# def go(step):
#     global origin
#     origin += step
#
#     return origin
#
#
# go(2)
# go(3)
# go(4)
origin = 0


# def go(step):
#     global origin
#     new_ops = origin+step
#     origin = new_ops
#     return new_ops

# print(go(2))
# print(go(3))
# print(go(6))


def travel(pos):
    def day(step):
        nonlocal pos
        new_ops = pos+step
        pos = new_ops
        return new_ops
    return day


monday = travel(0)
print(monday(4))
print(monday(4))
print(monday(4))

wenday=travel(100)
print(wenday(100))
print(wenday(100))
print(wenday(100))