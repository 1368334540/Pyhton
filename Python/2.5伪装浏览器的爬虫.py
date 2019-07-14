from urllib import request
import  re
url=r"http://www.baidu.com"
header={"User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
        }

res = request.Request(url,headers=header)
response= request.urlopen(res).read().decode()
pat = r"<title>(.*?)</title>"
data = re.findall(pat,response)
print(data)