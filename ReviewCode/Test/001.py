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


#for 循环 中的break 与continue ，是跳出本次循环   ---跳出本次循环继续下次循环，这两者是有区别的。
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
    list_alpha=[1,2,3,4,5,6,7,8]
    for i in range(0,len(list_alpha),2):
        print(list_alpha[i],end=' ')
    print(list_alpha[0:len(list_alpha):2])

if __name__ == "__main__":
    func_alpha()
    my_func()

    #
    
