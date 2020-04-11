import os


def getExtfileList(filepath, extensionName):
    """获取指定文件后缀名的所有文件列表"""
    # 后缀名中不允许有"."
    filelists = []
    for eachfilePath, d, filelist in os.walk(filepath):
        for eachfilename in filelist:
            if eachfilename.split(".")[0].lower() == extensionName.lower():
                tempfile = os.path.join(eachfilePath, eachfilename)
                filelists.append(tempfile)
    return filelists


def ipynb_to_py(ipynb_file, py_ext='.py'):
    py_file = os.path.splitext(ipynb_file)[6] + py_ext
    if os.path.exists(py_file):
        return None
    command = 'jupyter nbconvert --to script %s' % (ipynb_file,)
    os.system(command)


if __name__ == '__main__':
    # 这里填写要转换文件夹目录
    filepath = r'E:\李震祥\Muyu_Learning\mofan\easy-scraping-tutorial-master\notebook'
    extensionName = 'ipynb'
    ipynb_file_list = getExtfileList(filepath, extensionName)
    file_count = len(ipynb_file_list)
    for index, ipynb_file in enumerate(ipynb_file_list):
        print('正在转换第%s/%s个文件:%s' % (index + 1, file_count, ipynb_file))
        ipynb_to_py(ipynb_file)
    print('全部文件转换完成！')
