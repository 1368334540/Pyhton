import urllib
from urllib import request
import  time
header =  {"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
           }
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0  #第一页 (1-1)*50
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50 #第二页 (2-1)*50
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100#第三页 (3-1)*50
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=150#第四页 (4-1)*50
for i in range (1,4):
    print("http://tieba.baidu.com/f?kw=python&ie=utf-8&pn="+str((i-1)*50))


def loadpage(fullurl, filename):
    print("正在下载:",filename)
    req=request.Request(fullurl,headers=header)
    resp=request.urlopen(req).read()
    return  resp


def writepage(html, filename):
    print("正在保存本地:",filename)
    with open(filename,"wb") as f:
        f.write(html)
    print("----------------------")


#构造url
def tiebaSpider(url,begin,end):
    for page in range(begin,end+1):
        pn = (page-1)*50
        fullurl=url+"&pn="+str(pn)
        filename="c:/第"+str(page)+"页.html"
        html = loadpage(fullurl,filename) #调用爬虫，抓取网页
        writepage(html,filename) #把获取的html写入文件
kw = input("请输入贴吧名:")
begin = eval(input("请输入起始页:"))
end=eval(input("请输入结束页:"))
url="http://tieba.baidu.com/f?"
key = urllib.parse.urlencode({"kw":kw})
url = url+key
tiebaSpider(url,begin,end)








