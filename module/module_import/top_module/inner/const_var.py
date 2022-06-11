from string import ascii_lowercase, digits

list_alpha = [int(i) for i in digits]
list_beta = [i for i in ascii_lowercase]
list_gamma = [[1, 2, 3], [100, 200, 300], True, False, 'string']

tuple_alpha = tuple(list_alpha)
tuple_beta = tuple(list_beta)
tuple_gamma = tuple(list_gamma)

dict_alpha = {k: v for k, v in zip(list_beta, list_alpha)}

set_alpha = set(digits)
set_beta = set(list_beta)
