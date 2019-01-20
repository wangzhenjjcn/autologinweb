#coding=utf-8
import sys,time,datetime,os,requests

import pytesseract
from PIL import Image
from random import random
 
try:
 
    import cookielib
    print(f"python2.")
except:
 
    import http.cookiejar as cookielib
    print(f"python3.")

 
mafengwoSession = requests.session()
mafengwoSession.cookies = cookielib.LWPCookieJar(filename = "mafengwoCookies.txt")



url = "http://vst520.net/"

headers = {
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    'dnt': "1",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
    'cache-control': "no-cache"
    }

# response = requests.request("GET", url, headers=headers)
# print(f"statusCode = {response.status_code}")
# print(f"text = {response.text}")
# print(response.text)

 

def openMainPage():
    mainPageurl = "http://vst520.net/"
    print("openMainPage:"+mainPageurl)
    mainPageheaders = {
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'dnt': "1",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
        'cache-control': "no-cache"
        }
    responseRes = mafengwoSession.get(mainPageurl,  headers = mainPageheaders)
    print(f"statusCode = {responseRes.status_code}")
    print(f"text = {responseRes.text}")
    mafengwoSession.cookies.save()
    return responseRes.text

def openSecPage():
     
    openSecPageUrl = "http://vb66.auu97.com/"
    print("openSecPage:"+openSecPageUrl)
    openSecPageHeaders = {
        'upgrade-insecure-requests': "1",
        'dnt': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'referer': "http://vst520.net/",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
        'cache-control': "no-cache"
        }
    responseRes = mafengwoSession.get(openSecPageUrl, headers = openSecPageHeaders, allow_redirects = False)
    print(f"statusCode = {responseRes.status_code}")
    print(f"text = {responseRes.text}")
    mafengwoSession.cookies.save()
    return responseRes.text
 
def openSearchPage():
 
    openSearchPageUrl = "http://vb66.auu97.com/"
    print("openSearchPage:"+openSearchPageUrl)
    openSearchPageheaders = {
        'origin': "http://vb66.auu97.com",
        'upgrade-insecure-requests': "1",
        'dnt': "1",
        'content-type': "application/x-www-form-urlencoded",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'referer': "http://vb66.auu97.com/",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
        'cache-control': "no-cache"
        }
    postData = { 
        "code": "0z29w",
        "submit_bt": "搜索",
    }
    responseRes = mafengwoSession.post(openSearchPageUrl, data = postData, headers = openSearchPageheaders)
    mafengwoSession.cookies.save()
    print(f"statusCode = {responseRes.status_code}")
    print(f"text = {responseRes.text}")
    return responseRes.text
  

def getLinkBySearchPage(pageData,line):
    line1=""
    line2="线路"
    if line==1:
        line1="<div class='b_line'></div>"
        line2=line2+str(line)
    else:
        line1=line2+str(line-1)
        line2=line2+str(line)
    print("getLinkBySearchPage:")
    proxyLink=pageData[pageData.index("<div class='b_line'></div>"):] 
    proxyLink=proxyLink[:proxyLink.index("</ul>")]    
    proxyLink=proxyLink[proxyLink.index(line1):proxyLink.index(line2)] 
    print(proxyLink)
    proxyLink=proxyLink[proxyLink.index("<li><a href=\"")+13:proxyLink.index("target=")]  
    proxyLink=proxyLink[:proxyLink.index("\"")]                     
    print(proxyLink)
    return proxyLink



def getLoginAuthPage(proxyLink):
    print("getLoginAuthPage"+proxyLink)
    print("YouAreFindding This:>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    getLoginAuthPageUrl = proxyLink
    getLoginAuthPageHeaders = {
        'upgrade-insecure-requests': "1",
        'dnt': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'referer': "http://vb66.auu97.com/",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
        'cache-control': "no-cache"
        }
    responseRes = mafengwoSession.get(getLoginAuthPageUrl, headers = getLoginAuthPageHeaders, allow_redirects = True)
    print(f"statusCode = {responseRes.status_code}")
    print(f"text = {responseRes.text}")
    mafengwoSession.cookies.save()
    return responseRes.text
  
def downloadLoginAuthPageImage(loginAuthPageImageUrl,fileName):
    print("downloadLoginAuthPageImage:loginAuthPageImageUrl---"+loginAuthPageImageUrl+" ////fileName:"+fileName)
    r = requests.get(loginAuthPageImageUrl)
    with open(fileName, 'wb') as f:
        f.write(r.content) 
  
def transImage(FileName,gFilename,bFilename,path):   
    print("transImage:"+FileName+"   "+gFilename+"   "+bFilename+"   "+path) 
    threshold = 140  
    table = []  
    for i in range(256):  
        if i < threshold:  
            table.append(0)  
        else:  
            table.append(1)  
    gryFilename=gFilename
    blackFilename=bFilename
    im = Image.open(FileName)  
    imgry = im.convert('L')
    imgry.save(gryFilename)  
    out = imgry.point(table,'1')  
    out.save(blackFilename)  



def decodeImage(FileName,path):
    print("decodeImage:"+path+FileName+"  ") 
    transImage(FileName,"g_"+FileName,"b_"+FileName,path)
    text=decodeLoginAuthPageImage(path+"b_"+FileName)
    return text


def fixNumResault(Resault):
    print("fixNumResault"+Resault)
    rep={'O':'0',  
        'I':'1','L':'1',  
        'Z':'2',  
        'S':'8'  
        }
    text = Resault.strip()  
    text = Resault.upper()
    for r in rep:  
        text = text.replace(r,rep[r])  
    return text


def decodeLoginAuthPageImage(loginAuthPageImageName):
    print("decodeLoginAuthPageImage:"+loginAuthPageImageName) 
    image = Image.open(loginAuthPageImageName)
    text = pytesseract.image_to_string(image, lang='eng',config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789').strip()
    print("text:"+text)
    return text


def getLoginAuthPageImageAuthCode(proxyLinkURI):
    print("getLoginAuthPageImageAuthCode:"+proxyLinkURI) 
    getLoginAuthPageXMLUrl =proxyLinkURI+ "/getCodeInfo/.auth?u=" + str(random()) + '&systemversion=' + "4_6_sp9" + "&.auth"
    print(getLoginAuthPageXMLUrl)
    getLoginAuthPageXMLHeaders = {
        'upgrade-insecure-requests': "1",
        'dnt': "1",
        'accept': "*/*",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'referer': "http://pc5.g.nmnmnn.ninja/ssczx74883a/account/login.html.auth",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
        'cache-control': "no-cache"
        }
    responseRes = mafengwoSession.get(getLoginAuthPageXMLUrl, headers = getLoginAuthPageXMLHeaders, allow_redirects = True)
    mafengwoSession.cookies.save()
    print(f"statusCode = {responseRes.status_code}")
    print(f"text = {responseRes.text}")
    print("") 
    return responseRes.text


def getLoginAuthPageImageAddrByAuthCode(authCode):
    print("getLoginAuthPageImageAddrByAuthCode:"+authCode) 
    t = authCode.split("_")
    loginAuthPageImageUrl= "/getVcode/.auth?t=" + t[0] + "&systemversion=" + "4_6_sp9" + "&.auth"
    print(loginAuthPageImageUrl)
    return loginAuthPageImageUrl

def getVerifyValueByAuthCode(authCode):
    print("getVerifyValueByAuthCode:"+authCode) 
    t = authCode.split("_")
    verifyValue= t[1]  
    print(verifyValue)
    return verifyValue
    
def getLoginAuthPageTimeByAuthCode(authCode):  
    print("getLoginAuthPageTimeByAuthCode:"+authCode) 
    t = authCode.split("_")
    current_page_time = (t[len(t)-1]+"").replace(" ","")
    print(current_page_time)
    return current_page_time

def getLoginAuthVerifyValueByAuthCode(authCode):  
    print("getLoginAuthVerifyValueByAuthCode:"+authCode) 
    t = authCode.split("_")
    current_page_time = (t[len(t)-2]+"").replace(" ","")
    print(current_page_time)
    return current_page_time


def getValueByLoginAuthPage(loginAuthPage,value):
    data=""
    if value in loginAuthPage:
        data=loginAuthPage[loginAuthPage.index("name=\""+value):]
        data=data[data.index("value=\"")+7:]
        data=data[:data.index("\"")]
        print(data)
        return data
    else:
        return data
    print("getLoginAuthPageData:"+value+"   is   "+ data) 
    return data


def getSystemVersionByLoginAuthPage(loginAuthPage):
    data=""
    if "var systemversion" in loginAuthPage:
        data=loginAuthPage[loginAuthPage.index("var systemversion"):]
        data=data[data.index("\"")+1:]
        data=data[:data.index("\"")]
        return data
    else:
        return data
    print(  data) 
    return data




def encodePassword(password):
    print("encodePassword:"+password)
    symbolMappingList = {'`' : '!V$', '-' : '!m$', '=' : '!k$', '[' : '!O$', ']' : '!K$', ';' : '!I$', '\'' : '!S$', '\\' : '!T$', '/' : '!r$', '.' : '!Z$', ',' : '!a$', '~' : '!i$', '!' : '!p$', '@' : '!f$', '#' : '!7$', '$' : '!D$', '%' : '!l$', '^' : '!9$', "&" : '!q$', '*' : '!t$', '(' : '!6$', ')' : '!g$', '_' : '!v$', '+' : '!J$', '{' : '!L$', '}' : '!d$', '|' : '!W$', '"' : '!E$', ':' : '!0$', '?' : '!H$', '>' : '!y$', '<' : '!b$' }
    original_pwd = password
    replace_pwd  = '' 
    for   c in original_pwd :
            if(c in symbolMappingList.keys()   ) :
                print(symbolMappingList[c])
                replace_pwd += symbolMappingList[c]
            else :
                replace_pwd += c
    print(replace_pwd)
    return replace_pwd
            




def postLogin(proxyLink,username,pwd,line):
    print("postLogin:"+proxyLink) 
    print("username:"+username) 
    print("pwd:"+pwd) 
    proxyLinkURI=proxyLink[proxyLink.index("//")+2:]
    proxyLinkURI="http://"+proxyLinkURI[:proxyLinkURI.index("/")]
    print("proxyLinkURI:"+proxyLinkURI) 
    loginAuthPage=getLoginAuthPage(proxyLink)
    
    
    authCode=getLoginAuthPageImageAuthCode(proxyLinkURI)
    imageAddr=proxyLinkURI+getLoginAuthPageImageAddrByAuthCode(authCode)
    downloadLoginAuthPageImage(imageAddr,"./auth.jpg")
    imageCode=fixNumResault(decodeImage("auth.jpg","./"))
    print("ImageCode:"+imageCode)

    for c in imageCode:
        if c.isdigit():
            continue
        else:
            print("ERR  NOT NUM PIC  ERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
            time.sleep(5)
            return doLogin(username,pwd,line)
    verifyCode =imageCode
    verifyValue =getVerifyValueByAuthCode(authCode)
    cid =getValueByLoginAuthPage(loginAuthPage,"cid")
    cname =getValueByLoginAuthPage(loginAuthPage,"cname")
    print(cname)
    systemversion = getSystemVersionByLoginAuthPage(loginAuthPage)
    password=encodePassword(pwd)
    loginURL = proxyLinkURI+"/loginVerify/.auth"
    loginURLheaders = {
        'origin': "http://pc5.g.nmnmnn.ninja",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'dnt': "1",
        'content-type': "application/x-www-form-urlencoded;",
        'accept': "*/*",
        'referer': "http://pc5.g.nmnmnn.ninja/ssczx74883a/account/login.html.auth",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
        'cache-control': "no-cache"
        }

    postStr = ""
    postStr += "VerifyCode=" + verifyCode + "&"
    postStr += "__VerifyValue=" + verifyValue + "&"
    postStr += "__name=" + username + "&"
    postStr += "password=" + password  + "&"
    postStr += "isSec=0&"
    postStr += "cid=" + cid + "&"
    postStr += "cname="+cname +"&"
    postStr += "systemversion=" + systemversion + "&"
    postStr=postStr.strip()
    print(loginURL)
    print(postStr)
    responseRes = mafengwoSession.post(loginURL, data = postStr.encode('UTF-8'), headers = loginURLheaders, 
    verify=False )  
    mafengwoSession.cookies.save()
    print(f"statusCode = {responseRes.status_code}")
    print(f"text = {responseRes.text}")
    # 验证码已过期,请重新刷新。
    return responseRes.text
   
def testLogin(proxyLink):
    testLogin("testLogin:"+proxyLink) 
    proxyLinkURI=proxyLink[proxyLink.index("//")+2:]
    proxyLinkURI="http://"+proxyLinkURI[:proxyLinkURI.index("/")]
    testURL="http://pc5.g.nmnmnn.ninja/ssczx74883a/login/87c5896663_rdsess/k"



    
def doLogin(account, password,line):
    print("doLogin:"+account+"  "+password) 
    mainPage=openMainPage()
    secPage=openSecPage()
    searchPage=openSearchPage()
    proxyLink=getLinkBySearchPage(searchPage,line)
    proxyPage=postLogin(proxyLink,account,password,line)
    print(proxyPage)
    # testLogin(proxyLink)

if __name__ == "__main__":
    doLogin("", "",4)

