import  requests
header =  {"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
           }
#创建session对象 每次登录session把最新的cookie传上服务器,其实就是用cookie登录，用session带cookie 登录 好比船和人，人是主体，船是运输工具
ses= requests.session()
data={"email":"15892095320","password":"lovebbaa"}
#sesstion通过post方式传递用户名和密码拿到cookie信息，放到session中
ses.post("http://www.renren.com/PLogin.do",data=data)
#session带着刚刚Post得到的cookies请求登录需要的页面
response=ses.get("http://www.renren.com/880151247/profile")
print(response.text)