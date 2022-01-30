import random

list_keys = [i for i in 'abcdefghijk']
list_value = [i for i in range(11)]
random.shuffle(list_value)
sort_dict = dict(zip(list_keys, list_value))
sort_values = {k: v for k, v in sorted(sort_dict.items(), key=lambda item: item[1])}
sort_other = sorted(sort_dict.items(), key=lambda item: item[1])
