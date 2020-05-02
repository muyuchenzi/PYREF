from enum import Enum


class EnumColor(Enum):
    Red = 2
    Yellow = 1
    Blue = 0
    Green = -1
    Black = 0


if __name__ == '__main__':
    print(EnumColor.Red.value)
    print(EnumColor.Red.name)
    print("----值不能相等----")
    # EnumColor.Red = 10
    for color in EnumColor:
        print(color.name)

    print('------')
    for color in EnumColor.__members__:
        print(color)
    print('---------')
    assert EnumColor.Red.value == 2
