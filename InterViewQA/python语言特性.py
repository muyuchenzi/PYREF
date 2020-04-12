# qa_link https://github.com/taizilongxu/
# interview_python#1-python%E7%9A%84%E5%87%BD%E6%95%B0%E5%8F%82%E6%95%B0%E4%BC%A0%E9%80%92
# 1、python 参数传递

a = 1


def value_fun(a):
    a = 2
    print(a)


value_fun(a)
print(a)

variable_a = []


def vari_fun(a):
    variable_a.append(1)
    print(variable_a)


vari_fun(variable_a)
print(variable_a)


# solution: python所有的数据类型都是对象，但是对象分为两种可更改的和不可更改对象。
# string numbers tuples 是不可更改对象，list、dict、set是 可以修改的对象
# 函数进行参数传递的时候，如果是值类型的话，那么就是传递一个复制，如果是引用类型的话那么传递的是指针
# 这个跟JavaScript是一样的
# 2、python中的元类

def class_foo(x):
    print(f"execting class_foo{x}")


class Class_A(object):

    def class_foo(self, x):
        print(f"executing{self, x}")

    @classmethod
    def classmethod_foo(cls, x):
        print(f"executing classmethod{cls, x}")

    @staticmethod
    def staticmthod_foo(x):
        print(f"executing staticmethod{x}")
a_2=Class_A()