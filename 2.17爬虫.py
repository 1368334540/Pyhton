import re
import urllib
from urllib import request
url ="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

header =  {"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
           }
key="pattern"
fordata={
"i":key,
"from":"AUTO",
"to":"AUTO",
"smartresult":"dict",
"client":"fanyideskweb",
"salt":"15632032415002",
"salt":"b2b5a87fab2617c8cff248c1719d0a24",
"ts":"1563203241500",
"bv":"65db4e7e1a2a0ee160ea1e66436196cd",
"doctype":"json",
"version":"2.1",
"keyfrom":"fanyi.web",
"action":"FY_BY_CLICKBUTTION"
}
data = urllib.parse.urlencode(fordata).encode("utf-8") #这里特殊问题 要byte of type ，encode转utf-8
req= request.Request(url,data=data,headers=header)
resp=request.urlopen(req).read().decode() #读取加解码，把二进制的html解为utf-8 文字就能显示了 而不是二进制
pat=r'"tgt":"(.*?)"}]]}'  #r表示不转义
result = re.findall(pat,resp)
print("{0:}:".format(key)+result[0])