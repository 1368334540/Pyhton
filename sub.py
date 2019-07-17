import re
a="111 hello bbb"
pat = re.compile(r"\d{2}")
result = pat.sub("我替换进来了",a)  #sub函数用于替换
print(result)