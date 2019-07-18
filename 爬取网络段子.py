import requests
from lxml import etree
header =  {"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
           }
url="http://www.qiushibaike.com"
#<div class="recmd-right">
# <a class="recmd-content" href="/article/121130446" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">
# 都说这女人胆子有点儿肥，都是老虎谁怕谁？</a>
response=requests.get(url,headers=header,).content
html=etree.HTML(response)
result=html.xpath('//div//a[@class="recmd-content"]/@href')
for site in result:
    xurl="http://www.qiushibaike.com"+site
    response2 = requests.get(xurl).text
    html=etree.HTML(response2)
    result1=html.xpath('//div[@class="content"]')

    for i in range(0,len(result1)):
        print(result1[i].text)