import re

string_alpha = 'life is short,i use python'
string_res = re.search(r'life(.*)python$', string_alpha)
string_res.group(0, 1)
string_res.groups()
