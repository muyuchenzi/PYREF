#python的生成式
import random
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
print(prices)
prices_bigthan_100={key:value for key,value in prices.items() if value>100}
# print(prices_bigthan_100)

names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
scores=[[None]*len(courses) for _ in range(len(names))]#这里有一个坑
# scores = [[None] * len(courses)] * len(names)#这里有一个浅拷贝会造成结果不如预期
for row,name in enumerate(names):
    for col,course in enumerate(courses):
        scores[row][col]=random.randint(50,100)
print(scores)

#NOTE heapq模块 

import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# print(heapq.nlargest(4,list1))
# print(heapq.nlargest(4,list2,key=lambda x:x['price']))


#NOTE itertools模块

import itertools

iter_res=itertools.permutations("abcd")
print(list(iter_res))

from collections import Counter
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))
