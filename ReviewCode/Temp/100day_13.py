# python 里的多线程与多进程
import random
import time

def down_task(file_name):
    print(f"开始下载{file_name}")
    time_to_download=random.randint(5,10)
    time.sleep(time_to_download)
    print(f"{file_name}下载完成！耗时{time_to_download}!")


def main():
    start_time=time.time()
    down_task("Python进阶")
    down_task("Pandas进阶")
    end_time=time.time()
    print(f"总共耗时{end_time-start_time}")

if __name__ =="__main__":
    main()
