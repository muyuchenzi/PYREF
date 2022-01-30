from enum import Enum

# enumerate的用法 ，我想错了
enum_alpha = enumerate(['1', "2", "xyz"])
xx = {index: value for index, value in enum_alpha}


# 枚举类，前后都不能有相同值，如果相同关键字的话raise ERROR 如果值相同的话，则第二个是第一个的别名。
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLUE = 3
    RED = 4
    BLACK = 5


for vip in VIP:
    print(vip)
    print([vip.name, vip.value])
for vip in VIP.__members__:
    print(vip)
for vip in VIP.__members__.items():
    print(vip)
print(VIP(4).name)