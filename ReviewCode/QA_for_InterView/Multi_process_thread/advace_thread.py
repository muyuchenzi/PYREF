import data.blog_spider as blog_data
import threading
import queue
import time
import random

'''
#NOTE使用queue来进行使用多线程，多进程
'''


@blog_data.time_spend
def multi_thread_craw():
    threads = []
    for url in blog_data.urls:
        url_t = threading.Thread(target=blog_data.craw, args=(url,), name=url)
        threads.append(url_t)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def multi_thread_queue_craw(url_queue, html_queue):
    while True:
        url = url_queue.get()
        # url = url_queue.get(blog_data.urls)
        html = blog_data.craw_data(url)
        html_queue.put(html)
        print(threading.current_thread().name,
              f"craw:{url}", f"url_queue.size:", url_queue.qsize())
        time.sleep(random.randint(1, 2))


def multi_thread_queue_prase(html_queue, file_save):
    while True:
        html = html_queue.get()
        results = blog_data.parse_data(html)
        print(threading.current_thread().name,
              f"parse:{len(results)}", f"html_queue.size:", html_queue.qsize())
        # print(results)
        for result in results:
            file_save.write(str(result) + '\n')
        time.sleep(random.randint(1, 2))


def run():
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    for url in blog_data.urls:
        url_queue.put(url)
    # craw_threads = []
    for i in range(3):
        t = threading.Thread(target=multi_thread_queue_craw, args=(url_queue, html_queue),
                             name=f"craw{i}")
        # craw_threads.append(t)
        t.start()
    # parse_threads = []
    file_save = open(
        r"E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Multi_process_thread\craw_data2.txt", "w")
    for i in range(5):
        t = threading.Thread(target=multi_thread_queue_prase, args=(html_queue, file_save),
                             name=f"parese{i}")
        # parse_threads.append(t)
        t.start()
    # for thread in craw_threads:
    #     thread.start()
    # for thread in parse_threads:
    #     thread.start()
    #
    # for thread in craw_threads:
    #     thread.join()
    # for thread in parse_threads:
    #     thread.join()


if __name__ == "__main__":
    # multi_thread_craw()
    run()
