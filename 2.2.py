from urllib import request
import  re
url=r"http://www.baidu.com"
response= request.urlopen(url).read().decode()
pat = r"<title>(.*?)</title>"
data = re.findall(pat,response)
print(data)