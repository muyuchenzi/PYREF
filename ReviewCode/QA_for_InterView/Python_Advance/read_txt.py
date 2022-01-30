import os


def read_txt_file(file_path):
    # todo read()全部读取
    with open(file_path, 'rb') as f:
        f_read_res = f.read()
    # print(f_read_res)
    # todo readline
    with open(file_path, 'rb') as f:
        f_readline_res = f.readline(3)
    print(f_readline_res)

    #     todo readlines
    with open(file_path, 'rb') as f:
        f_readlines_res = f.readlines()
    print(f_readlines_res)


# todo 使用生成器读取 大文件
def reader_text_file(file_path):
    with open(file_path, 'rb') as f:
        while True:
            text_line = f.readline()
            if not text_line:
                break
            yield text_line


def txt_file_read_generator(file_path):
    file_generator = reader_text_file(file_path)
    count = 0
    for line in file_generator:
        print(line)
        count += 1
    print(count)


def txt_file_write(file_path):
    file = r'E:\李震祥\temp\QA_for_InterView\Python_Advance\Data'
    file_temp_name = 'result.txt'
    file_full_path = file + '\\' + file_temp_name
    if os.listdir(file):
        file_reader_res = reader_text_file(file_path)
        with open(file_full_path, 'wb') as f:
            for line in file_reader_res:
                f.write(line)


if __name__ == '__main__':
    file_path = r'E:\李震祥\temp\QA_for_InterView\Python_Advance\Data\readfile_example.txt'
    read_txt_file(file_path)
    txt_file_read_generator(file_path)
    txt_file_write(file_path)
    print('end')
