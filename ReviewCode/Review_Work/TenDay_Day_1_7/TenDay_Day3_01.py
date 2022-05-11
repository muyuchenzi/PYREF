# Python 数据类型--------数字

# Python 的类型总共有两种：值类型和引用类型

# 值类型：int string tuple 
# 引用类型：dict list set 

# 整数的切
# 进制的表示 0110表示二进制。12表示十进制，
#0b是二进制，0o是八进制 0x十六进制
# 进制的切换bin，oct，hex,int


# TODO int str list tuple dict set bool
#  bin hex int oct
#  0b 0x oo

# # 整数 int
# # 浮点数 float
# # Python 数据中基本上只有这两种，而不像其他的有double,long等类型
#
# # 0b是二进制的前两个
# # 0b01后面两个是进制数
print(0b10)
# 0o是八进制的前两个
print(0o11)
# # 0x表示十六进制
print(0x1f)
#
# # 进制的转换

# 十进制转换成二进制 bin方法转换成二进制
print(bin(10))

# 转换成十进制
print(int(0b111))
# 转换成八进制
oct()
# 转换成十六进制
hex()

# # bool类型 空字符串，空tuple,空列表,空字典,None值
# bool 类型中False 中常见的状况：数字里的0,string里的'',list中的[],dict中的{},tuple里的(),还有一个None
bool(0)
bool("")
bool(())
bool([])
bool({})
bool(None)
# 数据类型-- 数字
print(type(1))
# 多种数据类型的合并
print(type(1.0 + 1))
# 取正，取余
print(2 // 2)
print(1 // 2)
print(3 % 2)

result=divmod(10,3)
# python 进制  二进制 十进制 八进制


# bool 类型
bool("")
bool('abc')
bool(0)
bool('')
bool([])
complex(1, 3)
complex(0, 3)

str_alpha = '''
alpha\n
beta\t
gamma 
delta'''
str_beta = 'alpha\n' \
           'beta\r' \
           'gamma' \
           'delta'
