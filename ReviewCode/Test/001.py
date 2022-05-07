# python 循环
# 是解决问题的一个思路
# while 循环特别注意不要死循环

def func_alpha():
    counter = 20
    while counter:
        print(counter, end=" ")
        counter -= 1
    else:
        print("end")


def my_func():
    a = [1, 2, 3]
    for i in a:
        if i == 2:
            break
        print(i)
    for i in a:
        if i == 2:
            continue
        print(i)


if __name__ == "__main__":
    func_alpha()
    my_func()

    #
