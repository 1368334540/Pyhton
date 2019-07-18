import urllib
from urllib import  request
from lxml import  etree
# http://tieba.baidu.com/f?kw=java&ie=utf-8&pn=0
# http://tieba.baidu.com/f?kw=java&ie=utf-8&pn=50

class Spider(object):
    def __init__(self):
        self.tiebaName="java"
        self.beginPage=1
        self.endPage=3
        self.url="http://tieba.baidu.com/f?"
        self.filename=1
  #       self.ua_header  =   { "User-Agent":
  # "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3"\
  # "282.140 Safari/537.36 Edge/17.17134"}#请求头都不行！！
    #构建url
    # http://tieba.baidu.com/f?kw=java&ie=utf-8&pn=100
    def tiebaSpider(self):
        for page in range(self.beginPage,self.endPage+1):
            pn=(page-1)*50
            wo={"pn":pn,"kw":self.tiebaName,"ie":"utf-8"}
            word=urllib.parse.urlencode(wo)#解析字典成urlencode 使之变为url的参数
            url=self.url+word
            self.loadPage(url)


#
#     < div class ="threadlist_lz clearfix" >
#     < div class ="threadlist_title pull_left j_th_tit " >
#     < a rel = "noreferrer"
# href = "/p/6197887795"
# title = "编程零基础想做一名程序员，该怎么学习？首先要学习什么？"
# target = "_blank"
# class ="j_th_tit " > 编程零基础想做一名程序员，该怎么学习？首先要学习什么？ < / a >

    #爬取页面内容
    def loadPage(self,url):
        req=request.Request(url)
        data=urllib.request.urlopen(req).read()   #加decode()会查不到 ，没反应 不要用decode解析，用etree的xpath解析etree封装到好html
        html=etree.HTML(data)
        links=html.xpath('//div[@class ="threadlist_lz clearfix"]/div[@class ="threadlist_title pull_left j_th_tit "]/a/@href')

        for link in links :
            link="http://tieba.baidu.com"+link
            self.loadImages(link)
    #爬取帖子详细页，获取图片的链接
    def loadImages(self,link):
        req=request.Request(link)
        data=request.urlopen(req).read()
        html = etree.HTML(data)
        links = html.xpath('//img[@class="BDE_Image"]/@src')
        for imageslink in links:
            self.writeImages(imageslink)
    #通过图片所在链接，爬取图片并保存图片到本地
    #<img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=e93c5d88d433c895a67e9873e1137397/65b3c5fc1e178a825f1955bffb03738da977e81a.jpg" size="42012" changedsize="true" width="560" height="371" style="cursor: url(&quot;http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur&quot;), pointer;">
    def writeImages(self,imagesLink):
        print("正在存储图片:",self.filename,"...")
        image = request.urlopen(imagesLink).read()
        file = open(r"C:\\Users\\mi\\Desktop\\img\\"+str(self.filename)+".jpg","wb")
        file.write(image)
        file.close()
        self.filename=self.filename+1
if __name__ == "__main__":

    mySpider=Spider()
    mySpider.tiebaSpider()