import random
from urllib import request
import  re
url=r"http://www.baidu.com"
agent1="Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"
agent2="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
agent3="Mozilla/5.0 (Linux; Android 8.1.0; ALP-AL00 Build/HUAWEIALP-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.1.0)"
List = [agent1,agent2,agent3]
agent= random.choice(List)
print(agent)
header={"User-agent":agent}
res = request.Request(url,headers=header)
response= request.urlopen(res).read().decode()
pat = r"<title>(.*?)</title>"
data = re.findall(pat,response)
print(data)