import threading
import time
class MyThread(threading.Thread):#继承Thread类
    def __init__(self,name):   #初始化子类自己
        threading.Thread.__init__(self)
        self.name=name

    def run(self):
        print("线程一执行——————————")
        time.sleep(1)#休眠一秒
        print("线程二执行——————————")
        time.sleep(1)
        print("线程三执行——————————")
        time.sleep(1)
        print("线程四执行——————————")
        time.sleep(1)

t1=MyThread("t1")
t2=MyThread("t2")
t3=MyThread("t3")

t1.start()
t2.start()
t3.start()
#等待子线程执行完毕再执行主线线程
t1.join()
t2.join()
t3.join()
print("主线程执行完毕")
