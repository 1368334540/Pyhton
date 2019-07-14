from urllib import  request
#创建HTTTP请求处理器对象
http_handler= request.HTTPHandler()
opener = request.build_opener(http_handler)
url = r"http://www.baidu.com"
req = request.Request(url)
response = opener.open(req).read().decode()
print(response)