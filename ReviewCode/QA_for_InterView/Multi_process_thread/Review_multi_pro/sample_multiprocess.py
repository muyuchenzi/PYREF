import random
import time
from multiprocessing import Process
from threading import Thread
from os import getpid


def down_task(file_name):
    print(f"开始下载{file_name}")
    time_to_download=random.randint(1,6)
    time.sleep(time_to_download)
    print(f"{file_name}下载完成！耗时{time_to_download}!")


def main():
    start_time=time.time()
    down_task("Python进阶")
    down_task("Pandas进阶")
    end_time=time.time()
    print(f"总共耗时{end_time-start_time}")

def process_main():
    start_time=time.time()
    p_alpha=Process(target=down_task,args=('Python进阶.pdf',))
    p_alpha.start()
    p_beta=Process(target=down_task,args=('Pandas进阶进程.wps',))
    p_beta.start()
    p_alpha.join()
    p_beta.join()
    end_time=time.time()
    print("总共消耗了%.2f"%(end_time-start_time))


from multiprocessing import Process
from time import sleep

counter = 0


def sub_task(string):
    global counter
    while counter < 10:
        print(string, end=' ', flush=True)
        counter += 1
        sleep(0.01)

        
def t_main():
    Process(target=sub_task, args=('Ping', )).start()
    Process(target=sub_task, args=('Pong', )).start()


if __name__ =="__main__":
    # main()
    # process_main()
    t_main()
