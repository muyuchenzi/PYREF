import threading
import time

class Bank():
    '''
    不使用lock的时候，在目前版本下线程是按照顺序来进行的（以前版本是无序的
    当遇见time.sleep的时候，线程中止，展开下一个线程。
    这个时候需要lock，保证线程运行的时候整个过程是干净的。
    '''
    def __init__(self,account) -> None:
        self.account=account

    def get_money(self,number,lock_c):
        with lock_c:
            if number > self.account:
                print("取钱失败")
            else:
                time.sleep(0.1)
                print(f'取钱成功,您的余额为{self.account-number}')
                self.account-=number
        


if __name__=="__main__":
    chenzi=Bank(10000)
    l=threading.Lock()

    task_a=threading.Thread(target=chenzi.get_money,args=(8000,l),name="task_1")
    task_b=threading.Thread(target=chenzi.get_money,args=(5000,l),name='task_2')
    # chenzi.get_money(500)
    task_a.start()
    task_b.start()
    task_a.join()
    
    task_b.join()