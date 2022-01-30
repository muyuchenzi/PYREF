# Python的基本数据类型-list str tuple

list_alpha = [i for i in range(9)]
# list_alpha = [1, 2, 56, 78, 9]
list_beta = ['1', '2', '3', 'string', 'one', 233]
list_gamma = [1, 3, 4, True, False, 'stringTest']
list_delta = [[1, 3, 4, 6], True, "string1233", (2, 3, 4)]

print(list_alpha)

# list tuple str 都能通过下标来进行取值，或者通过切片来进行。
# list的常用函数

print("one" in list_beta)
print("two" not in list_beta)
print(max(list_alpha))
print(min(list_alpha))

# ASCII码的换算
max("hello world")
min("hello world")
ord('a')
