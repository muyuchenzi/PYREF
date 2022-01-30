# if __name__ == '__main__' 检查当前文件是否为程序入口
# python解析器在读取一个文件的时，会执行里面的所有代码，但是在它执行之前会定义一些特殊的变量
# 例如会把一个module(the source File)当成主程序来执行的话，会把__name__的变量定义为__main__,
# 如果这个文件被其他module引入的，那么__name__的名字会被设定其他module

import time, _thread


def myfunction(string, sleeptime, lock, *args):
    while True:
        lock.acquire()
        time.sleep(sleeptime)
        lock.release()
        time.sleep(sleeptime)


if __name__ == "__main__":
    lock = _thread.allocate_lock()
    _thread.start_new_thread(myfunction, ("Thread #: 1", 2, lock))
    _thread.start_new_thread(myfunction, ("Thread #: 2", 2, lock))
else:
    print('你在别的模块引入的该模块')
