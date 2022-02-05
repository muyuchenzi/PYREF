import requests
import time
from bs4 import BeautifulSoup

urls = [f"https://www.cnblogs.com/#p{i}" for i in range(1, 51)]


def time_spend(func):
    def wrapper(*args):
        time_start = time.time()
        func()
        time_end = time.time()
        print(f"{func}运行时间为:{time_end - time_start}")

    return wrapper


def craw_data(url):
    html = requests.get(url)
    return html.text


def parse_data(html):
    html_soup = BeautifulSoup(html, "html.parser")
    links = html_soup.find_all('a', class_="post-item-title")
    result = [(link['href'], link.get_text()) for link in links]  # 拿到链接跟标题
    return result


# def test():
#     '''测试一下是否可行'''
#     html = craw_data(urls[3])
#     res = parse_data(html)
#     print(res)


def craw(url):
    html = requests.get(url)
    print(url, len(html.text))


@time_spend
def spider():
    for url in urls:
        time.sleep(0.5)
        craw(url=url)

# if __name__ == "__main__":
#     # spider()
#     test()
