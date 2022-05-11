# Life is Simple ,I Use Python
# 人生苦短，我用Python
# reviewTwo
# 要用Python的语言来进行，转换
a = 1
b = 2
a, b = b, a

print(id(a))
print(id(b))
# Python 里进行数据交换是非常快速,是不需要中间值进行替代的
list_alpha=[i for i in range(10)]
list_beta=list_alpha

print(id(list_alpha))
print(id(list_beta))

#在引用类型的赋值是给了某个变量一个内存地址，然后赋值就是把内存地址给了另外一个。

# 数据结构 最重要。
