# REVIEW
# # 这里是一个InterViewQA的问题解答。link git@github.com:kenwoodjw/python_interview_question.git
# NOTE 31、统计一个文本中单词频次最高的10个单词?
# import re
# from collections import Counter


# def file_reader(file_path):
#     with open(file_path, 'r', encoding='utf-8') as f:
#         while True:
#             txt_line = f.readline()
#             if not txt_line:
#                 break
#             else:
#                 yield txt_line


# def file_word_counter():
#     txt_file_path = 'E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Exercise\data\stone.txt'
#     #第一种方法，使用生成器对文本进行操作
#     file_reader_ge = file_reader(file_path=txt_file_path)
#     counter_num = {}
#     for line in file_reader_ge:
#         li = re.findall(pattern='\w', string=line)
#         for i in li:
#             if not counter_num.get(i):
#                 counter_num[i] = 1
#             else:
#                 counter_num[i] += 1
#     num_ten = sorted(counter_num.items(),
#                      key=lambda x: x[1], reverse=True)[:10]
#     print(num_ten)
#     # 第二种方法
#     with open(txt_file_path, 'r', encoding='utf-8') as f:
#         file_content = f.read()
#         word_counter = Counter(re.findall(pattern='\w', string=file_content))
#         ten_word = word_counter.most_common(10)
#         print(ten_word)

# if __name__ == "__main__":
#     file_word_counter()

# NOTE 32、该函数的输入是一个仅包含数字的list,输出一个新的list，其中每一个元素要满足以下条件：
# 1、该元素是偶数
# 2、该元素在原list中是在偶数的位置(index是偶数)
# list_alpha=[i for i in range(30)]
# print(list_alpha)
# def get_need(li):
#     list_alpha_copy=list_alpha[:]
#     if li%2==0 & list_alpha_copy.index(li)%2==0:
#         return True

# result_filter=filter(get_need,list_alpha)
# result_filter_2=filter(lambda x:x%2==0 & list_alpha.index(x)%2==0,list_alpha)
# print(list(result_filter_2))
# print(list(result_filter))

# NOTE 33.使用单一的列表生成式来产生一个新的列表
# list_alpha = [i for i in range(100)]
# res = [i for i in list_alpha[::2] if i % 2 == 0]
# print(res)

# NOTE 34.用一行代码生成[1,4,9,16,25,36,49,64,81,100]
# print([i**2 for i in range(1, 11)])

# NOTE 35.输入某年某月某日，判断这一天是这一年的第几天？

# import datetime
# input_year,inpu_month,input_day=1993,4,15

# input_date=datetime.datetime(year=input_year,month=inpu_month,day=input_day)
# start_date=datetime.datetime(year=input_year,month=1,day=1)
# result=input_date-start_date
# print(result.days)

# NOTE 36.两个有序列表，l1,l2，对这两个列表进行合并不可使用extend
# l1=[i for i in range(1,20,2)]
# l2=[i for i in range(0,20,2)]
# # l1.extend(l2)
# print(l1)
# res=[]
# for i in l1:
#     res.append(i)
# for i in l2:
#     res.append(i)
# print(res)
# res=[]
# while True:
#     if len(l1)>0:
#         res.append(l1[0])
#         del l1[0]
#     else:
#         continue
#     if len(l2)>0:
#         res.append(l2[0])
#         del l2[0]
#     if len(l1)==0 and len(l2)==0:
#         break
# print(res)

# NOTE 37、让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序，
# 如字符串'1982376455',变成'1355798642'
# import random
# l1 = [i for i in range(1, 20, 2)]
# l2 = [i for i in range(0, 20, 2)]
# random.shuffle(l1)
# random.shuffle(l2)
# l1.extend(l2)
# print(l1)
# # l1.sort()
# # 案例
# def func1(l):
#     l.sort(reverse=True)
#     for i in range(len(l)):
#         if l[i] % 2 > 0:
#             l.insert(0, l.pop(i))
#     print(''.join(str(e) for e in l))
# func1(l=l1)
# # 方法二
# def func2(l):
#     print("".join(sorted(l, key=lambda x: int(x) % 2 == 0 and 20 - int(x) or int(x))))

#NOTE 38、写一个函数找出一个整数数组中，第二大的数
# 这个直接使用sorted即可。
# import random
# list_beta=[i for i in range(20)]
# random.shuffle(list_beta)
# sorted_res=sorted(list_beta,key=lambda x:x,reverse=True)[1]
# print(sorted_res)
# def find_second_num(list_beta):
#     biggest_num=0
#     second_num=0
#     for i in list_beta:
#         if i>biggest_num:
#             biggest_num=i
#     for i in list_beta:
#         if i>second_num and i< biggest_num:
#             second_num=i
#     return second_num
# print(find_second_num(list_beta=list_beta))

#NOTE 39、阅读一下代码他们的输出结果是什么？
def multi():
    return [lambda x : i*x for i in range(4)]
print([m(3) for m in multi()])

#NOTE 40、又是一个词频统计的问题，跟上面的很像，这里不再赘述