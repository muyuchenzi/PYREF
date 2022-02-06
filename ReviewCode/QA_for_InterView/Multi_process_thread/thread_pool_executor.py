import data.blog_spider as blog_data
import threading
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
def pool_run():
    '''使用线程池来解决，相对于queue，代码更加简洁和容易阅读'''
    #NOTE 使用map来运行
    # with ThreadPoolExecutor() as pool:
    #     
    #     results=pool.map(blog_data.parse_data,htmls)
    #     for result in results:
    #         print(result)
    #NOTE 这里使用submit来进行
    with ThreadPoolExecutor() as pool:

        futures={}
        htmls=pool.map(blog_data.craw_data,blog_data.urls)
        htmls=list(zip(blog_data.urls,htmls))
        for url,html in htmls:
            future=pool.submit(blog_data.parse_data,html)
            futures[future]=url
        
        with open(r"E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Multi_process_thread\craw_data_2.txt","w") as f:
            for future,url in futures.items():
                f.write(str(url)+"\n")
        #
            
pool_run()