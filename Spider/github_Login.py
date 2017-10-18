#coding=utf-8
import requests
import re

url = 'https://github.com/login'   # 登录一般是 login 接口
user = input('请输入账号：')
psw = input('请输入密码：')

# 此例中， login 接口只是为 session 接口提供表单数据 authenticity_token 值
# 要重定向的 session 接口才是关键
sss = requests.Session()
r = sss.get(url)
reg = r'<input name="authenticity_token" type="hidden" value="(.*)" />'
pattern = re.compile(reg)
result = pattern.findall(r.text)
token = result[0]
print "token: ", token

# 构造 From Data 表单数据
my_data = {
    'commit': 'Sign in',
    'utf8': '%E2%9C%93',   # view source 可查看
    'authenticity_token': token,
    'login': user,
    'password': psw
}

# 填写错误账号或密码登录，通过 Network 查看 From Data 在哪个接口
redirect_url = 'https://github.com/session'
r = sss.post(redirect_url, data=my_data)
if r.url == 'https://github.com/':
    print "登录成功."
else:
    print "登录失败"
print(r.url, r.history)    # 重定向的 GitHub 首页，则登陆成功；仍停留在 session 接口，则登陆失败