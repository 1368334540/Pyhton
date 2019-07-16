import  requests
url="http://www.baidu.com"
req = requests.get(url).content.decode() # content返回的是bytes，二级制型的数据  但是如果你想要提取图片、文件，就要用到content
print(req)
req1=requests.get(url)
req1.encoding="utf-8"
print(req1.text)   #获取文本用text 返回的是unicode 型的数据，一般是在网页的header中定义的编码形式。