#
# NOTE 猜数字游戏
# import random


# answer = random.randint(0, 100)

# round = 20
# count = 0
# print(answer)
# while True > 0:
#     input_answer = int(input("请输入0-100以内的数字(包括)："))
#     if input_answer > answer:
#         print("小一点")
#     elif input_answer < answer:
#         print("大一点")
#     else:
#         print("恭喜你猜对了")
#         break
#     round -= 1
#     count += 1
# print(f'你总共猜了{count}')

# 输入两个正整数，计算他们的最大公约数与最小公倍数


def input_func():
    x, y = input("请输入两个正整数:x, y:").split(",")

    x = int(x)
    y = int(y)
    return x, y


def get_max(x, y):
    '''
    求最大公约数与最小公倍数
    '''
    max_list = []
    if x > y:
        x, y = y, x
    for i in range(2, y):
        if x % i == 0 and y % i == 0:
            max_list.append(i)

    print(max_list)
    if max_list:
        print(f"最大公约数{max_list[len(max_list)-1]}")
        print(f"最小公倍数{x*y/max_list[len(max_list)-1]}")

def my_func():
    for i in  range(100,1000):
        low=i%10 #个位数
        mid=i//10%10
        high=i//100
        if i == low**3+mid**3+high**3:
            print(i)
    

def fun_c():
    for x in range(0,20):
        for y in range(0,34):
            z=100-x-y
            if 5*x+y*3+z/3==100:
                print(x,y,z)


if __name__ == "__main__":
    # x, y = input_func()
    # get_max(x, y)
    my_func()
    fun_c()