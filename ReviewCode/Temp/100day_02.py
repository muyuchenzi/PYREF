# 猜数字游戏
import random


answer = random.randint(0, 100)

round = 20
count = 0
print(answer)
while True > 0:
    input_answer = int(input("请输入0-100以内的数字(包括)："))
    if input_answer > answer:
        print("小一点")
    elif input_answer < answer:
        print("大一点")
    else:
        print("恭喜你猜对了")
        break
    round -= 1
    count += 1
print(f'你总共猜了{count}')
