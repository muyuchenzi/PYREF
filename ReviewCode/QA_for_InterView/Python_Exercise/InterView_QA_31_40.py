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

#NOTE 32、该函数的输入是一个仅包含数字的list,输出一个新的list，其中每一个元素要满足以下条件：
# 1、该元素是偶数
# 2、该元素在原list中是在偶数的位置(index是偶数)
list_alpha=[i for i in range(30)]
print(list_alpha)
def get_need(li):
    list_alpha_copy=list_alpha[:]
    if li%2==0 & list_alpha_copy.index(li)%2==0:
        return True

result_filter=filter(get_need,list_alpha)
result_filter_2=filter(lambda x:x%2==0 & list_alpha.index(x)%2==0,list_alpha)
print(list(result_filter_2))
print(list(result_filter))
