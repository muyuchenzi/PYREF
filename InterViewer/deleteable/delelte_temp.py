import bisect
import random
import string
from itertools import zip_longest

list_alhpa = [random.randint(1, 100) for _ in range(20)]
# NOTE
# FIXME
# REVIEW
# TODO
list_beta = [_ for _ in string.ascii_letters]

dict_temp = dict(zip_longest(list_beta, list_alhpa, fillvalue=0))
temp = "string"
dict_temp_sorted = sorted(dict_temp.items(), key=lambda x: x[1], reverse=True)
