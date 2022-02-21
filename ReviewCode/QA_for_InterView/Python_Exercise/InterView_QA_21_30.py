# REVIEW
# # 这里是一个InterViewQA的问题解答。link git@github.com:kenwoodjw/python_interview_question.git
# 21、NOTE Python-遍历列表时删除元素的正确做法


# def wrong_answer():
#     '''
#     这里进行删除是对list进行删除，这个会导致list_alpha进行重新整理，可以debug调试查看一下。会得到错误的答案，
#     需要遍历一个副本来操作。
#     '''
#     for i in list_alpha:
#         if i > 5:
#             list_alpha.remove(i)
#         else:
#             pass
#     return list_alpha


# for i in list_alpha[:]:
#     if i > 5:
#         pass
#     else:
#         list_alpha.remove(i)

# print(list_alpha)
# print(list(filter(lambda x:x>5,list_alpha))
# print([i for i in list_alpha if i>5])

# NOTE 22、字符串的操作题目 查找字符串里没有的字符
# from string import ascii_lowercase
# print(ascii_lowercase)
# string_list=["A quick brown for jumps over the lazy dog","A slow yellow fox crawls under the proactive dog",
#             "Lions, and tigers, and bears, oh my",""]
# letters_set=set(ascii_lowercase)
# def get_missing_letter(string_list):
#     missing_result=[]
#     for str_li in string_list:
#         str_li_set=set(str_li.lower())
#         result=letters_set-str_li_set
#         result="".join(list(result))
#         missing_result.append(result)
#     return missing_result
# print(get_missing_letter(string_list))
# NOTE 23、可变类型与不可变类型
# 在Python的类型中，可变的类型有dict list ,number、string、tuple、bool是不可变类型，同时在函数参数的传递中一定要切记
# 这个。可变类型就是在赋值的时候是给了一块内存，修改的时候只是改内存里的内容，不可变类型如果修改则重新分配内存
# NOTE 24、is == 区别
# is是内存比较，知否指向同一块内存地址，==是值的比较。

# NOTE 25、求出list的所有奇数并创造新的列表
# print([i for i in range(20) if i%2==1])

# NOTE 26、利用Python写出一个1+2+3+10248
# from functools import reduce

# print(sum([1,2,3,10248]))

# print(reduce(lambda x,y: x+y,[1,2,3,10248]))
# NOTE 27、Python中变量的作用域，
# LEGB
# L local 本地 当前函数体内，for循环找，
# E enclose函数内部与内嵌函数之间
# G global 全局作用域
# B build-in Python内置
# NOTE 28、字符串"123"转换为123，不可使用int等内置函数
# def exchange_string2num(string_in="123"):
#     num=0
#     for s in string_in:
#         for i in range(len(s))

# NOTE 29、给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。你可以假设每个输入只对应一种答案，且同样元
# 素不能被重复利用。示例:给定nums = [2,7,11,15],target=9 因为 nums[0]+nums[1] = 2+7 =9,所以返回[0,1]
# import copy


# def twoSum(nums, target):
#     for num in nums:
#         nums_ori = copy.deepcopy(nums)
#         # 如果target-num在nums中返回这两个index
#         print(target - num)
#         nums.remove(num)
#         if target - num in nums:
#             return nums_ori.index(num), nums_ori.index(target - num)
#         else:
#             return 0, 0


# print(twoSum(nums=[2, 7, 11, 15], target=9))
# sr = [2, 3, 4, 2];
# sr.remove((2))
# NOTE30、删除重复元素，这个题目跟上面的很相似
import random
list_alpha = [random.randint(1, 10) for _ in range(20)]
print(set(list_alpha))
res_alpha=[]
for li in list_alpha:
    if li not in res_alpha:
        res_alpha.append(li)
print(res_alpha)