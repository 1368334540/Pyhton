import re
a="asadadPYthon"
pat=re.compile("python",re.I) #re.I忽略大小写  compile函数提高爬虫效率
result = pat.findall(a)
print(result)