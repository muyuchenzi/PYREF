import queue
import threading
import time


def producer(pro_queue, cus_queue):
    # NOTE 查看当前的pro
    while True:
        if not pro_queue.empty():
            data = pro_queue.get()
            mid_res = int(str(data) + "0")
            cus_queue.put(mid_res)
        else:
            break


def customer(cus_queue):
    while True:
        if not cus_queue.empty():
            data = cus_queue.get()
            fin_res = data * 10
            print(fin_res)
            # cus_queue.put(fin_res)
        else:
            break


def entry():
    print("start")
    produce_queue = queue.Queue()
    custome_queue = queue.Queue()
    # produce_queue.empty()
    origin_data = [i for i in range(1, 11)]
    for ori in origin_data:
        produce_queue.put(ori)
    produce_thread_list = []
    for i in range(4):
        td_al = threading.Thread(target=producer, args=(produce_queue, custome_queue))
        td_al.start()
        produce_thread_list.append(td_al)
    [pro_td.join() for pro_td in produce_thread_list]
    custome_thread_list = []
    for j in range(6):
        td_beta = threading.Thread(target=customer, args=(custome_queue,))
        td_beta.start()
        custome_thread_list.append(td_beta)
    [cus_td.join() for cus_td in custome_thread_list]
    # time.sleep(4)
    print("end")


if __name__ == "__main__":
    entry()
