import random
print([i*11 for i in range(10)])
list_alpha=[1,2,3,4,5]
list_beta=[3,4,5,6,7,3,4,5]
set_alpha=set(list_alpha)
set_beta=set(list_beta)

list_gamma=['b','c','a','d','c','a']
list_delta=list_gamma.copy()

xx=list(set(list_beta))
xx.sort(key=xx.index)
