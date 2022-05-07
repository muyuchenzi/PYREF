# python 循环
# 是解决问题的一个思路
# while 循环特别注意不要死循环



def func_alpha():
    counter=20
    while counter:
        print(counter)
        counter-=1
    else:
        print("end")
    

if __name__ == "__main__":
    func_alpha()