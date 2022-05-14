import os
import time
import string
import random
def main():
    '''
    生成一个跑动的文字效果'''
    content='北京欢迎你为你开天辟地。。。'
    count=20
    while count:
        os.system("cls")
        print(content)
        time.sleep(0.5)
        content=content[1:]+content[0]# 生成一个新的字符串
        count-=1

def generate_code(code_length=4):
    '''
    生成指定长度的验证码

    '''
    all_chars=string.ascii_letters
    all_dig=string.digits
    all_members=all_chars+all_dig
    code_fours=''
    for _ in range(code_length):
        code_fours+=random.choice(all_members)
    



if __name__=="__main__":
    # main()
    generate_code()