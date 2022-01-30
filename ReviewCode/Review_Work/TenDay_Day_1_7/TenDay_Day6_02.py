# 循环控制语句

# while
list_alpha = [i for i in range(20)]
list_beta = ['one', 'two', 'three', 'four']
list_gamma = ['one', [1, 3, 4], True, 3, {'a': 1, 'b': 2}]
list_delta = [i for i in "hello world python"]

while_num = 100
#
# while while_num > 0:
#     '''
#     while里面必须对条件进行操作，否则很容易进行死循环，会导致很多bug
#     '''
#     print(list_alpha[while_num])
#     while_num -= 1

a, b, c, d = 1, 2, 3, []
account = ['muyu', 'chenzi']
password = ['lizhenxiang', 'liyijin']
#
# user = dict(zip(account, password))
#
#
# def account_password_correct(account_input, password_input):
#     if account_input in account:
#         if password_input == user[account_input]:
#             print("success")
#         else:
#             print('your password is wrong!!')
#     else:
#         print('please check your account!!')
#
#
# def Test():
#     account = ['muyu', 'chenzi']
#     password = ['lizhenxiang', 'liyijin']
#
#
# #
# # def continue_test():
# #     for i in list_alpha:
# #         while i < 10:
# #             print(i)
# #             i += 1
# #         else:
# #             continue
# #         print(i)

if __name__ == '__main__':
    print('please input your acount')
    account_input = input('please input  account:')
    account_password = input('please input password')
    # account_password_correct(account_input=account_input, password_input=account_password)
