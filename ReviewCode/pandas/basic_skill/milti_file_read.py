import os
import pandas as pd

output_path = r'E:\李震祥\PYGIT\PYref\ReviewCode\pandas\Result'
name = 'fadf'
file_path = r'E:\李震祥\PYGIT\PYref\ReviewCode\pandas\Data\各省市订单数据.csv'


def result_output(path, name):
    if not os.path.exists(path):
        os.mkdir(path)
    file_path = path + "\\" + name
    return file_path


xxxxxx = [i for i in range(20)]
result = result_output(output_path, name)
print(result)


def file_path_read(file_path):
    x = 0
    for (dir_path, _, file_name) in os.walk(file_path):
        file_name = ['contain_na_data.xlsx', 'dataframe_add.py', '各省市订单数据.csv', '各省市订单数据.xlsx']
        xlsx_file_name = filter(lambda x: x.endswith('.xlsx'), file_name)
        xlsx_file_full_path = [file_path + file for file in xlsx_file_name]

        return xlsx_file_full_path


file_path_read(file_path)

for dir_path, _, files_name in os.walk(r'E:\李震祥\PYGIT\PYref\ReviewCode\pandas\Data'):
    print(dir_path, files_name)
