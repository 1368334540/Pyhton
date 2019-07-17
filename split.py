import  re
a= "小明,,,,大明,,,,大华,,,小红,小白"
pat = re.compile(r",+")
result = pat.split(a)  #匹配到的内容，用于分割字符串的标识，将其他分割出来的字符串输出
print(result)