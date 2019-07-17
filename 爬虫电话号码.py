import requests
import re
header =  {"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
           }
url="https://changyongdianhuahaoma.51240.com/"
response = requests.get(url,headers=header).text
# <tr bgcolor="#EFF7F0">
#
#
#           <td>索爱</td>
#
#
#           <td>400-810-0000</td>
#
#
#         </tr>
pat=re.compile(r'<tr bgcolor="#EFF7F0">[\s]*?<td>(.*?)</td>[\s]*?<td>.*?</td>[\s]*?</tr>')
pat1=re.compile(r'<tr bgcolor="#EFF7F0">[\s]*?<td>.*?</td>[\s]*?<td>(.*?)</td>[\s]*?</tr>')
result = pat.findall(response)
result1 = pat1.findall(response)
resultlist = []
for i in range(0,len(result)):
    resultlist.append(result[i]+result1[i])
print(resultlist)