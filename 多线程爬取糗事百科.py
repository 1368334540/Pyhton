#使用线程库
import threading
#队列
import queue
import requests
import time
from lxml import  etree
#https://www.qiushibaike.com/8hr/page/1/
#https://www.qiushibaike.com/8hr/page/2/
#https://www.qiushibaike.com/8hr/page/3/
#爬取网页线程--爬取段子所在的网页，放进队列
class Thread1(threading.Thread):
    def __init__(self, threadName, pageQueue, dataQueue):
        threading.Thread.__init__(self)

        self.pageQueue=pageQueue
        self.dataQueue=dataQueue
        self.headers = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

        self.threadName = threadName

    def run(self):
        print("启动线程"+self.threadName)
        while not flag1:  #判断队列是否还有东西
            try:
                page =self.pageQueue.get()  #拿完第一个必须再拿，所以做while循环 但是什么时候结束while，就是队列没东西get了，
                                            #就可以结束while循环了！
                url  = "https://www.qiushibaike.com/8hr/page/"+str(page)+"/"
                content=requests.get(url,headers=self.headers).text
                time.sleep(0.1)#免得数据还没有拿到就放进去
                self.dataQueue.put(content) #将数据放在数据队列中
            except :
                pass
        print("结束线程"+self.threadName)

#解析网页线程，从队列中拿到列表页面，进行解析，并把段子内容放到本地
class Thread2(threading.Thread):
    def __init__(self,threadName,dataQueue,filename):
        threading.Thread.__init__(self)

        self.threadName = threadName
        self.dataQueue = dataQueue
        self.filename = filename
    def run(self):
        print("启动线程"+self.threadName)
        while not flag2:
            try:
                time.sleep(0.1) #等待0.1秒，确保dataQueue已经放有内容，等一等采集线程的加载网页和抓取网页的时间
                data1 = self.dataQueue.get()
                html=etree.HTML(data1)
                urllist=html.xpath('//div/a[@class="recmd-content"]')
                for url in urllist:
                    data=url.text #拿到标题信息
                    self.filename.write(data+"\n")
            except:
                pass
        print("结束线程"+self.threadName)
flag1 =False #判断页码队列中是否为空
flag2 =False #判断数据队列中是否为空
def main():
    #页码队列
    pageQueue = queue.Queue(maxsize=10)
    for i in range(1,11):
        pageQueue.put(i)
    #解析页面的队列,存放采集好的数据队列
    dataQueue = queue.Queue()

    filename = open(r"C://Users//mi/Desktop/糗事百科1-10页段子标题.txt","w")#写text不能用二进制，写不进的 直接a或w
                                                                            #写text用字节码，写文件或图片用二进制 所以urllib.request.urlopen(url).read()也不用解析decode()函数 默认读read()就是二进制

    t1 = Thread1("采集线程",pageQueue,dataQueue)
    t1.start()
    t2 = Thread2("解析线程",dataQueue,filename)
    t2.start()
    #当pageQueue为空时，结束采集线程
    while not pageQueue.empty():
        pass
    global flag1
    flag1 =True
    #当dataQueue为空时，结束解析线程
    while not dataQueue.empty():
        pass
    global flag2
    flag2 =True
    #等待线程完毕再关闭文件
    t1.join()
    t2.join()
    filename.close()
if __name__ == '__main__':

    main()