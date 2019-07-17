import re
a="abbaabab"
pat = r"a.*b"
pat1 = r"a.*?b"
result = re.findall(pat,a)
result1=re.findall(pat1,a)

print(result)
print(result1)