
# REVIEW
# # 这里是一个InterViewQA的问题解答。link git@github.com:kenwoodjw/python_interview_question.git
# NOTE https://regex101.com/ 是一个非常好用的在线匹配测试，很直观。
#NOTE 94.请写出一段代码用正则匹配出ip？
# import re
# string_alpha="23reafdjafwqerfafj123.255.255.192euiriafjafajf"
# resutl=re.findall('(\d+\.\d+\.\d+\.\d{0,3})',string_alpha)
# result2=re.search('(\d+\.\d+\.\d+\.\d{0,3})',string_alpha).group()
# print(resutl)
# print(result2)

#NOTE 95.a="abbbccc"请用正则匹配abccc不管有多少b，就出现一次

# import re

# string_alpha='abbbccc'
# print(re.sub('b+','b',string_alpha))

#NOTE 96.字符串的操作
# Q&A str.find(substring,start,end)：正序字符串查找函数
# 函数原型：
# str.find(substr [,pos_start [,pos_end ] ] )
# 返回str中第一次出现的substr的第一个字母的标号，如果str中没有substr则返回-1，
# 也就是说从左边算起的第一次出现的substr的首字母标号。

# 参数说明：
# str：代表原字符串
# substr：代表要查找的字符串
# pos_start：代表查找的开始位置，默认是从下标0开始查找
# pos_end：代表查找的结束位置
# string_alpha="23reafdjafwqerfafj123.255.255.192euiriafjafajf"
# # str.find 查找子字符串在父字符串的位置
# res=string_alpha.find('123',0,25)#
# print(res)
#Q&A str.index(substr,start,end)
# 与find很类似，差别在于找不到的时候find返回-1，index抛出异常ValueError
# result=string_alpha.index('123',0,25)
# print(result)
# Q&A str.rfind(substr,start,end)与find一样，这个是倒叙查找。
# Q&A str.rindex(substr,start,end)也是倒序。
# Q&A str.replace 对字符串进行替换。
# re的主要就是
import re
# re.findall(pattern,string,flags) 找到并以list的形式返回，如果查找失败返回空list
# re.match(pattern,string,flags) 从字符串开始的地方进行匹配，找到了就返回matchobject，匹配不到返回None
# re.search(pattern,string,flags) 匹配整个字符串，找到了返回matchobject，匹配不到返回None
# re.sub(pattern,repl,string，count,flags) 匹配整个字符串，对匹配到的进行替换,count 替换多少个。

# print(string_alpha.replace(".",'-'))

#98.用Python匹配HTML tag的时候，<.*> 和 <.*?> 有什么区别
# Q&A 贪婪模式跟非贪婪模式，re模块默认的是贪婪模式，尽可能的匹配到，而非贪婪模式就是尽可能少的匹配
#贪婪模式：
# 定义：正则表达式去匹配时，会尽量多的匹配符合条件的内容
# 标识符：+，?，*，{n}，{n,}，{n,m}
# 匹配时，如果遇到上述标识符，代表是贪婪匹配，会尽可能多的去匹配内容

# 非贪婪模式：
# 定义：正则表达式去匹配时，会尽量少的匹配符合条件的内容 也就是说，
# 一旦发现匹配符合要求，立马就匹配成功，而不会继续匹配下去(除非有g，开启下一组匹配)
# 标识符：+?，??，*?，{n}?，{n,}?，{n,m}?
# 可以看到，非贪婪模式的标识符很有规律，就是贪婪模式的标识符后面加上一个?
#
# string_beta="<h1>this is h1 title <h2> this is h2 tile</h2> </h1>"

# result_more=re.findall('<.*>',string_beta)
# result_less=re.findall("<.*?>",string_beta)
# print(result_more)
# print(result_less)
#99.写出开头匹配字母和下划线，末尾是数字的正则表达式？
# s1='_aai0efe00'
# res=re.findall('^[a-zA-Z_]+[a-zA-Z0-9]+\d$',s1)
# print(res)

#NOTE 100.正则表达式操作 四大操作：匹配，切割，替换，获取
#NOTE 103.简述Python里面search和match的区别
#NOTE 104.请写出匹配ip的Python正则表达式
#NOTE 105.Python里match与search的区别？
# 这些答案如上不再赘述。