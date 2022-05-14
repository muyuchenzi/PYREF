import random

list_alpha=[i for i  in range(20)]
random.shuffle(list_alpha)
print(list_alpha)

#针对字典的值进行排序

dict_alpha=dict(zip([i for i in "abcdefg"],list_alpha))
print(dict_alpha)
res=sorted(dict_alpha.items(),key=lambda x:x[1])
print(res)

#字典推导式
string_alpha="abcdefg"
print(string_alpha[::-1])
print(''.join(list(reversed(string_alpha))))
sts=''
for i in range(len(string_alpha)):
    ss=string_alpha[len(string_alpha)-i-1]
    sts+=ss
print(sts)

str1 = "k:1|k1:2|k2:3|k3:4"
str_list=str1.split("|")
res=dict()
for str_li in str_list:
    key_value=str_li.split(":")
    res[key_value[0]]=key_value[1]
print(type(res))

alist= [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
print(sorted(alist,key=lambda x:x["age"],reverse=True))

listb=[i for i in "abcdefg"]
print(listb[10:])