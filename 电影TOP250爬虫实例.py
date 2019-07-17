from urllib import request
import re
# https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20
# https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20
# https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20
header =  {"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
           }
url="https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20"
#  "rating":["9.6","50"]    #"title":"肖申克的救赎"
data=request.Request(url,headers=header)
response = request.urlopen(data).read().decode()
pat=re.compile(r'"rating":\["(.*?)","\d+"\]')
pat2=re.compile(r'"title":"(.*?")')
result=re.findall(pat,response)
result2=re.findall(pat2,response)
for i in range(0,len(result)):
    print("豆瓣排名："+str(i+1)+"\t电影名："+result2[i]+"\t豆瓣评分："+result[i])
