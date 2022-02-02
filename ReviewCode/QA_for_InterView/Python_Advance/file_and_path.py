import os

file_path = r'E:\李震祥\temp\QA_for_InterView\Python_Advance\Data'

dir_name_list = []
sub_dir_list = []
file_name_list = []
for dir_path, sub_dir, file_name in os.walk(file_path):
    dir_name_list.append(dir_path)
    sub_dir_list.append(sub_dir)
    file_name_list.append(file_name)

os.listdir(file_path)  # 查看当前文件夹下文件目录
os.mkdir(file_path + '\\' + 'test')  # 新建文件夹
os.path.isdir(r'E:\李震祥\temp\QA_for_InterView\Python_Advance\Data\temp')
os.path.isfile(r'E:\李震祥\temp\QA_for_InterView\Python_Advance\file_and_path.py')  # 检查是文
# 件夹还是文件
os.rename(r'E:\李震祥\temp\QA_for_InterView\Python_Advance\Data\test',  # 重命名文件或者文件夹
          r'E:\李震祥\temp\QA_for_InterView\Python_Advance\Data\test2')
os.rename(r'E:\李震祥\temp\QA_for_InterView\Python_Advance\Data\result.txt',
          r'E:\李震祥\temp\QA_for_InterView\Python_Advance\Data\result2.txt')
os.remove(r'E:\李震祥\temp\QA_for_InterView\Python_Advance\Data\result2.txt')  # 删除文件
os.rmdir(r'E:\李震祥\temp\QA_for_InterView\Python_Advance\Data\test2')  # 删除文件夹
