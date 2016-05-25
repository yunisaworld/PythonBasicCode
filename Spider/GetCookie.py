#cookie
import urllib
import urllib2
import cookielib
import requests

def make_cookie(name, value):
    return cookielib.Cookie(
        version=0,
        name=name,
        value=value,
        port=None,
        port_specified=False,
        domain="202.114.200.86",
        domain_specified=True,
        domain_initial_dot=False,
        path="/",
        path_specified=True,
        secure=False,
        expires=None,
        discard=False,
        comment=None,
        comment_url=None,
        rest=None
    )


url='http://graduate2.cug.edu.cn/UserLogin.aspx/'
urlimage='http://graduate2.cug.edu.cn/Public/ValidateCode.aspx?image=496076078'
urlleftmenu='http://202.114.200.86/Gstudent/leftmenu.aspx?UID=1201520622'
urldefaultmenu='http://graduate2.cug.edu.cn/Gstudent/Default.aspx?UID=1201520622'
urlloginmenu='http://graduate2.cug.edu.cn/Gstudent/loging.aspx?UID=1201520622'
httpHandler=urllib2.HTTPHandler(debuglevel=1)
httpsHandler=urllib2.HTTPHandler(debuglevel=1)



cookies=cookielib.CookieJar()
opener=urllib2.build_opener(httpHandler,httpsHandler,urllib2.HTTPCookieProcessor(cookies))

request=urllib2.Request(urlimage)
#request.add_header('User-Agent','Mozillz/4.0(compatible;MSIE 6.0;Window NT 5.1)')
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
request.add_header('Connection','keep-alive')

response=opener.open(request)
outfile=open(r'code.jpg','wb')
outfile.write(response.read())
outfile.close()

#print response.geturl()
#print response.info()

authcode=raw_input('authcode:')
username='1201520622'
password='052435'

values={'UserName':username,
        'PassWord':password,
        'ScriptManger1':'UpdatePanel2|btLogin',
        'ValidateCode':authcode,
        '__ASYNCPOST':'true',
        '__EVENTTARGET':'btLogin',
        '__EVENTVALIDATION':'/wEdAAp5aNu8ZM9G0cVd2+2BHlP5QKymBEaZgVw9rfDiAaM1okdSwSl9T9cYdvdEUMk3rEUGvkTgTBH+3oFe+9r/kbESVLz6L5LCYFLkJ6flg//uC5WKhJheoUmouOqQCzlwTSNWlQTw3DcvmMLY3PAqFoA+uFSTy5ozCEG4XBxL/Ykep0cgC/Irwlr9d8VObb8MnYO0GRqRfbdgDIW2dtIsr6rbp40BXk7HVrCbnFRrrHK6QlpXR1U=',
        'drpLoginType':'1',
    }
data=urllib.urlencode(values)
#opener=urllib2.build_opener(httpHandler,httpsHandler,urllib2.HTTPCookieProcessor(cookie))
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
}


request=urllib2.Request(urldefaultmenu,data,headers)

request.add_header('Cookie',cookies)
#request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
#request.add_header('Connection','keep-alive')
response=opener.open(request)
#print response.read()

cookies.set_cookie(make_cookie('LoginType','1'))
cookiesfinal=''
for item in cookies:
    print item.name,' ',item.value
    cookiesfinal=cookiesfinal+item.name+'='+item.value+';'
cookiesfinal=cookiesfinal[:-1]

request=urllib2.Request(urlleftmenu,data,headers)
#request=urllib2.Request(urldefaultmenu)
request.add_header('Cookie',cookiesfinal)
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
response=opener.open(request)
html = response.read()

outfile=open(r'page.html','wb')
outfile.write(html)
outfile.close()





