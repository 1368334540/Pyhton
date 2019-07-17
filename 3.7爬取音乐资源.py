import re

import requests
# http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20 #第一页
# http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20 #第二页
# http://www.htqyy.com/top/musicList/hot?pageIndex=2&pageSize=20 #第三页
#歌曲url http://www.htqyy.com/play/33
songID=[]
songName=[]
page=eval(input("请输入要爬的页数"))
for i in range(0,page):
    url="http://www.htqyy.com/top/musicList/hot?pageIndex="+str(i)+"&pageSize=20"
    html=requests.get(url)
    strr= html.text
    pat1=r'title="(.*?)" sid'
    pat2=r'sid="(.*?)"'
    titilelist=re.findall(pat1,strr)
    idlist=re.findall(pat2,strr)

    songID.extend(idlist)
    songName.extend(titilelist)
    print(strr)
print(songName)
print(songID)

