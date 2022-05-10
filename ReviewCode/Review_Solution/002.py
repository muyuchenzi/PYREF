from enum import Enum

yellow = 1
green = 2


color = {"yellow": 1, "green": 2}


class Color(object):
    yellow = 1
    green = 2

class VIP(Enum):
    '''
    枚举类：不重复，不能修改
    '''
    YELLOW=1
    GREEN=2


if __name__=="__main__":
    #使用常用的类变量
    color_alpha=Color()
    print(color_alpha.green)
    color_alpha.green=3
    print(color_alpha.green)
    print("-"*30)
    print(VIP.GREEN.value)
    # VIP.GREEN.value=10
    result=VIP.GREEN==VIP.YELLOW
    print(result)
    print(VIP.__members__)
    print(VIP.__members__.items())
    print("-"*30)
    for vip in VIP.__members__.items():
        print(vip)
