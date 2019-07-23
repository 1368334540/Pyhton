import requests
import re
import pymysql
db = pymysql.Connect(host="localhost",user="root",db="spider",port=3306,passwd="123",charset="utf8")
cursor = db.cursor()

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

delete = "delete from phone"
cursor.execute(delete)

for i in range(0,len(result)):
    resultlist.append(result[i]+result1[i])    #  ’ ‘ 要加 ，不然数据会出CC
    sql = "insert into phone(id,phone,name) values ('"+str(i)+"','"+result1[i]+"','"+result[i]+"')"
    cursor.execute(sql)
db.commit()
db.close()
print(resultlist)
