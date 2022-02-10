"""
- 直接在控制台使用命令行运行
- 程序运行之后倒计时1分钟之后结束
- 随机出100以内的2个整数加减乘除运算题目（除法确保能够除尽，但除数不能为0）
- 每出一道题目，由玩家给出答案，然后程序判断对错，接着出下一题，并且显示剩余时间
- 1分钟时间结束，显示总题数和正确率（正确率精确到小数点后2位），并将之前的题目和答案显示出来
"""


import time
import random


def get_divisor(n):
    '''
    出题：加减乘除运算，拿到除数的分母，
    '''
    res = []
    for i in range(1, n+1):
        if n % i == 0:
            res.append(i)
    result=random.choice(res)
    return result


def get_varies(operator):
    a = random.randint(1, 101)
    if operator == "÷":
        b = get_divisor(a)
    else:
        b = random.randint(1, 101)
    return a, b


def get_answer(a, b, operator):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "x":
        return a*b
    elif operator =="÷":
        return a/b


def func_main():
    time_start = time.time()
    operators = ["+", "-", "x", "÷"]
    questions=[]
    answers=[]
    input_answers=[]
    correct=0
    while time.time()-time_start < 60:
        operator = random.choice(operators)
        # operator="÷"
        x, y = get_varies(operator)
        answer = get_answer(x, y, operator=operator)
        questions.append(f"Question: {x} {operator} {y},请输入结果：")
        answers.append(answer)
        print(f"Question: {x} {operator} {y},请输入结果：")
        input_answer = input()
        input_answers.append(int(input_answer))
        if int(input_answer)==answer:
            print("回答正确，请继续...")
            correct+=1
        else:
            print("回答错误，请继续...")
     
    print("总共{}道题目，回答正确为{}，准确率为{:.2f}%".format(len(questions),correct,
    correct/len(questions)*100))
    print(questions)


if __name__=="__main__":
    func_main()