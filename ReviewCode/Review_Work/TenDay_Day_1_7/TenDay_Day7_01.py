# 循环控制语句
# while
list_alpha = [i for i in range(20)]
list_beta = ['one', 'two', 'three', 'four']
list_gamma = ['one', [1, 3, 4], True, 3, {'a': 1, 'b': 2}]
list_delta = [i for i in "hello world python"]

condition = True
while condition:
    for i in list_alpha:
        # print(i)
        if i == 10:
            condition = False
            # continue
        else:
            # print(r"运行到了：%d,还有%d" % (i,20-i))
            print(f"运行到了：{i},还有{20 - i}")
            # print(r"运行到了：{0},还有{1}".format(i, 20 - i))

# for i in list_alpha:
#     if i == 10:
#         # continue
#         break
#     print(i)
# else:
#     print('tst')
# todo for循环里的break continue 和for else进行测试
# for ele in [list_alpha, list_beta]:
#     temp = 0
#     for item in ele:
#         if item == 10:
#             temp = 1
#             break
#         else:
#             print(item)
#     if temp == 1:
#         break
# else:
#     print("this for loop is end")
# todo 注意这两个之间的区别
for i in range(10):
    print(i, end="\t")
# list_temp = [i for i in range(10)]
print('-'.join([str(i) for i in range(10)]))
