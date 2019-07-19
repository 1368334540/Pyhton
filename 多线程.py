import  threading
import time
def run(name):
    print(name,"线程执行了")
    time.sleep(5)
#创建两个线程对象

t1=threading.Thread(target=run,args=("t1"))

# t2=threading.Thread(target=run,args=("t2"))
t1.start()
# t2.start()
#等待子线程执行完，再解析下面的主线程
# t1.join()
# t2.join()


print("执行完毕！")
