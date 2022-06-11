import sys

sys.path.append(r'E:\李震祥\PYGIT\Temp\Review')

from ten_module.inner.const_var import list_alpha


#
def temp():
    print(list_alpha)
    print("src_func module")


if __name__ == '__main__':
    print(__package__)
    temp()
    # temp(list_alpha)
