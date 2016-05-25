#request-cug
import requests


url='http://graduate2.cug.edu.cn/UserLogin.aspx/'
urlimage='http://graduate2.cug.edu.cn/Public/ValidateCode.aspx?image=496076078'
urlleftmenu='http://graduate2.cug.edu.cn/Gstudent/leftmenu.aspx?UID=1201520622'
urldefaultmenu='http://graduate2.cug.edu.cn/Gstudent/Default.aspx?UID=1201520622'
urlloginmenu='http://graduate2.cug.edu.cn/Gstudent/loging.aspx?UID=1201520622'
urllogin='http://graduate2.cug.edu.cn/gstudent/ReLogin.aspx?ReturnUrl=/Gstudent/loging.aspx?UID=1201520622'


s=requests.session()
r=s.get(urlimage,timeout=60*4)

outfile=open(r'code.jpg','wb')
outfile.write(r.content)
outfile.close()

print r.cookies


authcode=raw_input('authcode:')

username='1201520622'
password='052435'

values={'UserName':username,
        'PassWord':password,
        'ValidateCode':authcode,
        'drpLoginType':'1',
    }

hds = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
    }


r=s.post(urllogin,data=values,headers=hds)

print r.url

r=s.get(urlleftmenu)
#print r.content
