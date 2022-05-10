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