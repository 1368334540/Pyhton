import requests
proxy = {"http":"http://61.128.208.94:3128"}
response = requests.get("http://www.baidu.com",proxies=proxy)
print(response.content.decode())