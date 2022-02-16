import os
import pandas as pd

output_path = r'E:\李震祥\temp\pandas\Result'
name = 'fadf'
file_path = r'E:\李震祥\temp\pandas\Data'


def result_output(path, name):
    if os.path.exists(path):
        os.mkdir(path)
    file_path = path + "\\" + name
    return file_path


xxxxxx = [i for i in range(20)]


def file_path_read(file_path):
    for (dir_path, _, file_name) in os.walk(file_path):
        file_name = ['contain_na_data.xlsx', 'dataframe_add.py', '各省市订单数据.csv', '各省市订单数据.xlsx']
        xlsx_file_name = filter(lambda x: x.endswith('.xlsx'), file_name)
        xlsx_file_full_path = [file_path + file for file in xlsx_file_name]
        return xlsx_file_full_path


def file_result():
    pass


os.path.exists(output_path)
