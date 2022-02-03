def read_jpg():
    try:
        with open(r'E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Advance\Data\img\操作符.png','rb') as f:
            jpg_data=f.read()
            print(type(jpg_data))
    except FileNotFoundError as e:
        print(e)
        print('指定的文件打不开')
    except IOError as e:
        print('读写文件的时候出现错误。')
    print('程序运行结束')

if __name__=="__main__":
    read_jpg()
