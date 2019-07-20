from   aip import  AipOcr



import re
APP_ID =  "16849502"  #全部大写
API_KEY= "2p1dxw29kqPbewp3kjSPSsug"
SECRET_KEY = "MEXoizBlDf4DfySIU8sTVMMZvMZx2rOQ"
client = AipOcr(APP_ID,API_KEY,SECRET_KEY)
with open(r"C://Users/mi/Desktop/1.png","rb") as filename:
    image=filename.read()
data = str(client.basicGeneral(image))   #这里要string 字符串， 因为re.findall要字符串的data
pat = re.compile(r"{'words': '(.*?)'}")
results=re.findall(pat,data)
print(data)
for data in results:

    print(data)
    