import re
a="hello......hello"
pat = re.compile(r"hello",re.I)
result = pat.finditer(a)
list=[]
for i in result:
    list.append(i.group())    # 这里的group函数是拿到finditer里的内容 不写这个函数的话会多输出它的位置
#finditer比findall更快，爬到一个符合的就放经list里面。而findall爬到所有符合的才统一放进list里面
print(list)