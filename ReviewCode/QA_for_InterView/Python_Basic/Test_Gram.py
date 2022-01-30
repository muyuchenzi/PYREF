import random

list_key = [i for i in 'abcdefag4eggds']
list_values = [random.randint(1, 100) for _ in range(10)]
dict_alpha = dict(zip(list_key, list_values))
del dict_alpha['a']
dict_alpha.pop('b')

list_key.reverse()
lsi = list_key[::-1]
