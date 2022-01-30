import package_function
import package_data
# from inner_function import data_covert
from inner_function.data_covert import *
# import inner_function
xx = package_data.list_alpha

temp = inner_list_alpha
test = data_covert_a
print(temp)
print(test)


def print_func():
    package_function.print_list_funciton()
    print(xx)


if __name__ == '__main__':
    print_func()
