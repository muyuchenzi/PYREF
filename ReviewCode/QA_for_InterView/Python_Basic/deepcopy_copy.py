import copy

a = [1, 2, 3, 4, ['a', 'c']]

b = a

c = copy.copy(a)
d = copy.deepcopy(a)
print([id(i) for i in [a, b, c, d]])

a.append(5)
a[4].append(['xx'])