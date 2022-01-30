# yield 就是一个生成器，就是返回一个生成的方法。

# yield 定义的函数就是一个生成器，生成器的使用就是不断调用next()，所以需要for循环进行使用
# 就是返回一个生成器对象，这个生成器对象有一个__next__()方法，每次调用时候就是调用__next__()
# 调用结束会有一个StopIterator Error，然后就能够停止，所以一般采用for循环的方式，这样就能自动捕捉Error
# 需要注意的一个地方就是这个是一次性的。
import time


def read_txt_function(file_path):
    with open(file_path, 'rb') as f:
        while True:
            txt_content = f.readlines(3)  # readlines
            if not txt_content:
                break
            yield txt_content


# use of with read_file
def read_file_with_chunk(file_path):
    with open(file_path, 'rb') as file_obj:
        for line in file_obj:
            print(line)


def yield_fun():
    list_var = [i for i in range(20)]
    for li in list_var:
        time.sleep(1)
        yield li
        print(li)


def Generator_test():
    yield 1
    yield 2
    yield 3
    yield 4


if __name__ == '__main__':
    file_path = r'E:\李震祥\temp\QA_for_InterView\Python_Advance\Data\readfile_example.txt'
    # 1、使用yield 方法
    read_file_with_chunk(file_path=file_path)
    print('----')
    for _chunk in read_txt_function(file_path=file_path):
        print(_chunk)
    yield_res = yield_fun()
    for i in yield_res:
        print(i)

    #    测试
    genTest = Generator_test()
    # for i in range(10):
    #     try:
    #         temp = genTest.__next__()
    #         print(temp)
    #     except Exception:
    #         print("this genTest is end")

    try:
        for i in range(10):
            temp = genTest.__next__()
            print(temp)
    except Exception:
        print("this geTest is end")
