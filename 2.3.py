from urllib import request
import  re
url=r"http://www.baidu.com"
res = request.Request(url)
response= request.urlopen(res).read().decode()
pat = r"<title>(.*?)</title>"
data = re.findall(pat,response)
print(data)...