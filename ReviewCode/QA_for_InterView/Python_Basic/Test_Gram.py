from timeit import timeit


def normal_gene_list():
    normal_list = []
    for i in range(1000):
        normal_list.append(i)
    return normal_list


def generator_list(num):
    for i in range(num):
        yield i


def get_gener_list(num):
    # num = int(num)
    generator_list_x = []
    for x in generator_list(num):
        generator_list_x.append(x)
    return generator_list_x


print(timeit(normal_gene_list, number=3))
res = timeit(lambda: get_gener_list(1000), number=1000)
print(res)
