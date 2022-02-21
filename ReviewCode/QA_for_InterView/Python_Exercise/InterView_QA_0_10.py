# #REVIEW
# # 这里是一个InterViewQA的问题解答。link git@github.com:kenwoodjw/python_interview_question.git
# #Q&A 1、有一个jsonline格式的文件file.txt大小约为10K
# def read_text_file():
#     with open("E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Exercise\data\stone.txt","r",
#                 encoding="utf-8") as f:
#         result=f.readlines()
#         return result
# # print(read_text_file())
# # 当文件很小，可以直接用全部读取,但是当文件很大的时候需要使用生成器
# file_path='E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Exercise\data\stone.txt'
# def read_text_file_generator(file_path):
#     with open(file_path,"r",encoding='utf-8') as f:
#             while True:
#                 line=f.readline()
#                 if not line:
#                     break
#                 else:
#                     yield line
# #NOTE 一定要注意使用循环来进行进行反复读取。
# for line in read_text_file_generator(file_path=file_path):
#     print(line)
# print("---"*16)

# Q&A 2、显示文件夹路径下的文件os.walk 这里省略
# Q&A 3、输入日期，打印日期是某一年的第多少天。
# import datetime
# def print_number_days(year,month,day):

#     start_time=datetime.date(year,month=1,day=1)
#     end_date=datetime.date(year,month,day)
#     print((end_date-start_time).days)

# print_number_days(1993,4,21)
# Q&A 4，打乱一个排序好的list对象。

# import random

# list_alpha=[i for i in range(10)]
# random.shuffle(list_alpha)
# print(list_alpha)
# #Q&A 5、对字典进行排序
# import random
# list_value=[i for i in range(2,9)]
# random.shuffle(list_value)
# list_key=[i for i in "abcdefg"]
# dict_alpha=dict(zip(list_key,list_value))
# for k,v in dict_alpha.items():
#     print(k,v)
# print(dict_alpha)
# dict_alpha_res=sorted(dict_alpha.items(),key=lambda x:x[1])
# print(dict(dict_alpha_res))

# Q&A 6、字典推导式
# list_value=[i for i in range(5)]
# list_key=[i for i in "abcde"]
# dict_beta={k:v for k,v in zip(list_key,list_value)}
# print(dict_beta)
# Q&A 7、翻转字符串
# string_alpha='abedefg'
# string_reverse=string_alpha[::-1]
# string_rev_a=reversed(string_alpha)
# string_rev_b=''
# for i in range(len(string_alpha)):
#     string_rev_b+=string_alpha[len(string_alpha)-i-1]
# print(string_rev_b)
# Q&A 8、k:1 |k1:2|k2:3|k3:4"处理成dict
# string_in = "k:1 |k1:2|k2:3|k3:4"
# dict_rs = {}
# for i in string_in.split('|'):
#     items = i.split(":")
#     dict_rs[items[0]] = items[1]
# print(dict_rs)
# Q&A 9、alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}] age排序
# alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
# sorted_alist=sorted(alist,key=lambda x:x['age'],reverse=False)
# print(sorted_alist)
#Q&A 10、这个是一个小的bug 如果使用切片切不到不会产生indexError会产生一个空白list,很容易产生BUG找不到。
list = ['a','b','c','d','e']
print(list[10:])