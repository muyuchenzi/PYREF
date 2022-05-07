# python 分支、循环、表达式
# 表达式

user_names=['muyu','chenzi']
user_passwords=[123,456]
user_accounts=dict(zip(user_names,user_passwords))

def account_login(user_name,user_password):
    if user_name in user_names:
        if user_password== user_accounts.get(user_name):
            print("login success")
        else:
            print("your password is wrong")
    else:
        print("check your name plz")

if __name__=="__main__":
    account_login("chenz",456)