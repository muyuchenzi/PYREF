# 表达式，分支、循环
from random import randint
from random import randrange
from random import uniform
from random import choice
import random

a = random.choice([1, 2, 'x', 'y'])
result = []
for i in range(1, 20):
    result.append(random.choice([1, 2, 'x', 'y']))

list_alpha = [i for i in range(9)]
list_beta = ['one', 'two', 'three', 'four']
list_gamma = ['one', [1, 3, 4], True, 3, {'a': 1, 'b': 2}]
list_delta = [i for i in "hello world python"]

if len(list_alpha) > 50:
    print("list_alpha length more than 5")
else:
    print("ddddd")

user_name = ['muyu', 'chenzi']
user_password = ["1111", "233"]
user_account = dict(zip(user_name, user_password))
print(list(user_account.keys()))
user_account.get('chenzi')


def account_login(user_name, user_password):
    if user_name in list(user_account.keys()):
        if user_password == user_account.get(user_name):
            print("成功了")
        else:
            print('您的密码错误')
    else:
        print("您的账号有问题")


# def account_login(user_name, user_password):
#     if user_name in list(user_account.keys()) and user_password == user_account.get(user_name):
#         if user_password == user_account.get(user_name):
#             print("成功了")
#         else:
#             print('您的密码错误')
#     else:
#         print("您的账号有问题")
if __name__ == '__main__':
    print("please input name")
    name_input = input()
    print("please input password")
    password = input()
    account_login(user_name=name_input, user_password=password)
