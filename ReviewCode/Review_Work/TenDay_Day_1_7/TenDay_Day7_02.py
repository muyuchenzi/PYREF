# 循环

# while循环
list_alpha = [i for i in range(10)]

condition = 1
while condition < 30:
    if condition:
        print(condition)
        condition += 1
else:
    print("end")
# for loop
for i in range(len(list_alpha)):
    if i == 5:
        print("到5了")
        # break
        continue
    else:
        print(list_alpha[i])
else:
    print("end")

for i in range(0, len(list_alpha), 2):
    print(list_alpha[i])
xx = list_alpha[::2]
xx = list_alpha[0:len(list_alpha):2]
