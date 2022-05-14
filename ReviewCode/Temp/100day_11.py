# 文件和异常

# NOTE
# 'r'读取
# w 写
# x 写入，如果文件存在会产生异常
# a 追加，将内容写入现有文件的尾部
# b 二进制模式
# + 更新
import time
import math
import json
file_path = 'E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Exercise\data\stone.txt'


def file_reader():
    '''
    读取文件
    '''
    global file_path
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # file_content_read=f.read()
            file_readline = f.readline()
            # file_readlines=f.readlines()
    except FileNotFoundError:
        print('无法打开指定文件')
    except LookupError:
        print('指定了未知编码')
    except UnicodeDecodeError:
        print('读取文件发生错误')
    finally:
        print(file_readline)
        print("end")

def line_by_line():
    with open(file_path,'r',encoding='utf-8') as f:
        for line in f:
            print(line,end='')
            time.sleep(2)

def is_prime(n):
    assert n>2
    for factor in range(2,n):
        if n%factor==0:
            return False
    return True

def prime_main():
    '''
    写入文件
    '''
    filenames=[i+'.txt' for i in [i for i in "abc"]]
    file_path=r'E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Exercise\data'
    file_full_path = [file_path+'\\'+i for i in filenames]
    fs_list=[]
    try:
        for filename in file_full_path:
            fs_list.append(open(filename,'w',encoding='utf-8'))
        for number in range(3,10000):
            if is_prime(number):
                if number<100:
                    fs_list[0].write(str(number)+'\n')
                elif number<1000:
                    fs_list[1].write(str(number)+'\n')
                else:
                    fs_list[2].write(str(number)+'\n')
    except IOError as ex:
        print(ex)
        print("写入文件出错")
    finally:
        for fs in fs_list:
            fs.close


def json_main():

    ''' 
    注意这里的load,loads,dump,dumps
    与文件结合的是load ,dump
    '''
    my_dict={
        'name':34,
        'age':23,
        'qq':324546,
        'friend':['wang','li'],
        'cars':[
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        print(type(my_dict))
        res=json.dumps(my_dict)
        print(res)
        loads_res=json.loads(res)
        print(loads_res)
        with open('E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Exercise\data\e.txt','w+',
                    encoding='utf-8') as f:
            json.dump(my_dict,f)
    except Exception as e:
        print(e)
    finally:
        print('end')


if __name__ == "__main__":
    # file_reader()
    # line_by_line()
    # prime_main()
    json_main()