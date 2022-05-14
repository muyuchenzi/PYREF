import random
import time
from time import sleep
from threading import Thread,Lock


def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = random.randint(1, 5)
    time.sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main_thread():
    time_start = time.time()
    t1 = Thread(target=download, args=('python进阶',))
    t1.start()
    t2 = Thread(target=download, args=("pandas进阶",))
    t2.start()
    t1.join()
    t2.join()
    time_end = time.time()
    print(f'总共耗时{time_end-time_start}')

class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁才能执行后续的代码
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__=="__main__":
    main_thread()