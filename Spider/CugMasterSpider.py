#coding:utf8

import urllib
import urllib2
import cookielib




url='http://202.114.200.86'
urllog='http://202.114.200.86/UserLogin.aspx'
urlleftmenu='http://202.114.200.86/Gstudent/leftmenu.aspx?UID=1201520622'


def Getcookie():
    #cookie=cookielib.CookieJar()
    #handler=urllib2.HTTPCookieProcessor(cookie)
    #opener=urllib2.build_opener(handler)
    
    #response=opener.open('http://202.114.200.86/UserLogin.aspx')
    #for item in cookie:
     #   print 'Name='+item.name
      #  print 'Value='+item.value

    postdata=''
    header={}
    req=urllib2.Request(urllog,postdata,header)
    req.add_header('POST','/UserLogin.aspx HTTP/1.1')
    req.add_header('Host','202.114.200.86')
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
    req.add_header('Connection','keep-alive')
    req.add_header('Cache-Control','no-cache')
    req.add_header('X-Requested-With','XMLHttpRequest')
    req.add_header('X-MicrosoftAjax','Delta=true')
    req.add_header('Referer','http://202.114.200.86/UserLogin.aspx')
    req.add_header('Accept-Encoding','gzip,deflate')
    req.add_header('Content-Length','842')
    req.add_header('Content-Type','application/x-www-form-urlencoded; charset=UTF-8')
    req.add_header('Accept-Language','zh-CN,zh;q=0.8')
    req.add_header('Cookie','ASP.NET_SessionId=q1eaxjc3gzgta3gw5aw0efr5; CNZZDATA1256760907=1621146004-1463220868-%7C1463220868; LoginType=LoginType=1')
    ckjar=cookielib.MozillaCookieJar('cookie.txt')
    ckproc=urllib2.HTTPCookieProcessor(ckjar)

    opener=urllib2.build_opener(ckproc)
    f=opener.open(req)
    htm=f.read()
    f.close()

    ckjar.save(ignore_discard=True,ignore_expires=True)

    


def CugMasterLogin(username,password):
    cookiejar=cookielib.CookieJar()
    urlopener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    urllib2.install_opener(urlopener)
    imgurl=url+'/Public/ValidateCode.aspx?image=2019208853'
    print 'imageurl:',imgurl
    urlopener.addheaders.append(('User-Agent', 'Mozilla/5.0 (compatible; MISE 9.0; Windows NT 6.1); Trident/5.0'))

    DownloadFile(imgurl,urlopener)

    authcode=raw_input('authcode:')

    values={'UserName':username,
            'PassWord':password,
            'ValidateCode':authcode,
	    'ScriptManger1':'UpdatePanel2|btLogin',
	    'drpLoginType':'1'}
    data=urllib.urlencode(values)
    #urlDefault=urlopener.open(urllib2.Request('http://202.114.200.86/Gstudent/Default.aspx?UID=1201520622', data))
    req=urllib2.Request(urlleftmenu,data)
    urlleft=urlopener.open(req)
    #print urlleft



    if not 'id' in [cookie.name for cookie in cookiejar]:
        print "Login failed with login=%s, password=%s, authcode=%s" % (username, password, authcode)
    print 'We are logged in!'
 
    page=urlleft.read()

    print len(page)
    
    return page

def DownloadFile(fileUrl, urlopener):
    isDownOk=False
 
    try:
        if fileUrl:
            outfile=open(r'code.jpg', 'wb')
            outfile.write(urlopener.open(urllib2.Request(fileUrl)).read())
            outfile.close()
 
            isDownOK=True
        else:
            print 'ERROR: fileUrl is NULL!'
    except:
        isDownOK=False
 
    return isDownOK


#Getcookie()
print CugMasterLogin('1201520622','052435')
