# 正则表达式与字符串

# . \w \d \s 单个字符 \W \D \S 与前面相反
# [a-z] (abc) 一定范围内，和整个字符
# ^ 开始 $ 以结束
# ? + * {m,n}数量
# findall search match sub
# RE.I 忽略大小写，RE.S 忽略
# 贪婪模式与非贪婪模式

import re

def qq_number():
    user_name=input("请输入用户名:")
    user_numb=input("请输入QQ号:")
    m1=re.match(r'^[0-9a-zA-Z]{6,20}',user_name)
    if not m1:
        print('请输入有效的用户名')
    m2=re.match(r'^[1-9]\d{4,11}$',user_numb)
    if not m2:
        print('请输入有效的QQ号')
    if m1 and m2:
        print("您的信息输入是有效的")

def bad_voice():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.I)
                    
    print(purified)  # 你丫是*吗? 我*你大爷的. * you.

def main():
    # 验证QQ号码
    # qq_number()
    bad_voice()



if __name__=="__main__":
    main()