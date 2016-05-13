#coding:utf8

import urllib
import urllib2
import cookielib




url='http://202.114.200.86'
urllog='http://202.114.200.86/UserLogin.aspx'
urlleftmenu='http://202.114.200.86/Gstudent/leftmenu.aspx?UID=1201520622'

def CugMasterLogin(username,password):
    cookiejar=cookielib.CookieJar()
    urlopener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    urllib2.install_opener(urlopener)
    imgurl=url+'/Public/ValidateCode.aspx?image=2019208853'
    print 'imageurl:',imgurl
    urlopener.addheaders.append(('User-Agent', 'Mozilla/5.0 (compatible; MISE 9.0; Windows NT 6.1); Trident/5.0'))

    DownloadFile(imgurl,urlopener)

    authcode=raw_input('authcode:')

    values={'login_id':username,
            'opl':'op_login',
            'login_passwd':password,
            'login_check':authcode}
    data=urllib.urlencode(values)
    #urlDefault=urlopener.open(urllib2.Request('http://202.114.200.86/Gstudent/Default.aspx?UID=1201520622', data))
    req=urllib2.Request(urllog,data)
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


print CugMasterLogin('1201520622','052435')
