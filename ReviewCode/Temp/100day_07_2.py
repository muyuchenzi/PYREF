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
    
def get_file_end(file_path=r"E:\李震祥\PYGIT\PYref\ReviewCode\Temp\test"):
    '''
    找到文件夹下的所有文件(一级目录),首先找到该文件夹使用oswalk 进行遍历找到子文件夹，
    根据判断dirs对各个文件夹进行判断，最终找到文件夹下的文件，然后通过string.split
    找到文件名
    '''
    for root,dirs,files in os.walk(file_path):
        print(dirs)
        if dirs:
            file_list=files
        else:
            fils_noneed=files

    print(file_list)
    print("----"*10)
    print(fils_noneed)
    result=[]
    for file in file_list:
        print(file)
        file_name=file.split('.')
        result.append(file_name)
    final_res=[]
    for res in result:
        final_res.append(res[0])
    print(final_res)

def max_two():
    numb_list=[]
    for _ in range(20):
        numb_list.append(random.randint(1,100))
    print(numb_list)
    numb_list_sorted=sorted(numb_list,reverse=True)
    print(numb_list_sorted[0:2])
    '''
    设计一个函数返回传输列表最大和第二大元素的值
    '''

def number_day_of_year(year=1999,month=7,day=21):
    import datetime
    date_input=datetime.date(year=year,month=month,day=day)
    date_start=datetime.date(year=year,month=1,day=1)
    print((date_input-date_start).days+1)

    

if __name__=="__main__":
    # main()
    # generate_code()
    # ss="E:\李震祥\PYGIT\PYref\ReviewCode\Temp\test"
    # print(os.walk)
    # get_file_end()
    # max_two()
    number_day_of_year()