from urllib import request
urllist=["http://www.baidu.com"
     ,"http://www.baidu.com"
     ,"http://www.ewewaftegcdsdfaa.com",
     "http://www.baidu.com"]
i=0

for url in urllist:
    i = i + 1
    req = request.Request(url)
    try:
        resp = request.urlopen(req).read().decode()
        print("第" + str(i) + "个成功")
    except Exception as f:
        print("第"+str(i)+"个失败"+str(f))
print("结束")