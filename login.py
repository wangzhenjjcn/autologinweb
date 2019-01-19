#coding=utf-8
import sys,time,datetime,os,requests
import urllib.request
 
from pytesseract import *
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
    print("开始打开http://vst520.net/")
    responseRes = mafengwoSession.get(url,  headers = headers)
    print(f"statusCode = {responseRes.status_code}")
    print(f"text = {responseRes.text}")
    mafengwoSession.cookies.save()
    return responseRes.text

def openSecPage():
    openSecPageUrl = "http://vb66.auu97.com/"
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
  

def getLinkBySearchPage(pageData):
    proxyLink=pageData[pageData.index("<div class='b_line'></div>"):] 
    proxyLink=proxyLink[:proxyLink.index("</ul>")]    
    proxyLink=proxyLink[proxyLink.index("线路3"):proxyLink.index("线路4")] 
    proxyLink=proxyLink[proxyLink.index("</li><li><a href=\"")+18:proxyLink.index("target=")]  
    proxyLink=proxyLink[:proxyLink.index("\"")]                     
    print(proxyLink)
    return proxyLink



def getLoginAuthPage(proxyLink):
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
    r = requests.get(loginAuthPageImageUrl)
    with open(fileName, 'wb') as f:
        f.write(r.content) 
  
def transImage(FileName,gFilename,bFilename,path):    
    threshold = 140  
    table = []  
    for i in range(256):  
        if i < threshold:  
            table.append(0)  
        else:  
            table.append(1)  
    gryFilename=gFilename
    blackFilename=bFilename
    
    if os.path.exists(gFilename):
        gryFilename="new_"+gryFilename
    if os.path.exists(blackFilename):
        blackFilename="new_"+blackFilename
    im = Image.open(FileName)  
    imgry = im.convert('L')
    imgry.save(gryFilename)  
    out = imgry.point(table,'1')  
    out.save(blackFilename)  



def decodeImage(FileName,path):
    transImage(FileName,"g_"+FileName,"b_"+FileName,path)
    text=decodeLoginAuthPageImage(path+"b_"+FileName)
    return text


def fixNumResault(Resault):
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
    image = Image.open(loginAuthPageImageName)
    text = pytesseract.image_to_string(image, lang='eng',config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789').strip()
    print("text:"+text)
    return text


def getLoginAuthPageImageAuthCode(proxyLinkURI):
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
    t = authCode.text.split("_")
    loginAuthPageImageUrl= "/getVcode/.auth?t=" + t[0] + "&systemversion=" + "4_6_sp9" + "&.auth"
    print(loginAuthPageImageUrl)
    return loginAuthPageImageUrl
    
    
def getLoginAuthPageTimeByAuthCode(authCode):  
    t = authCode.text.split("_")
    current_page_time = (t[len(t)-1]+"").replace(" ","")
    print(current_page_time)
    return current_page_time

def getLoginAuthVerifyValueByAuthCode(authCode):  
    t = authCode.text.split("_")
    current_page_time = (t[len(t)-2]+"").replace(" ","")
    print(current_page_time)
    return current_page_time


def getVerifyCodeByLoginAuthPage(loginAuthPage):
    return ""
 
def postLogin(proxyLink):
    proxyLinkURI=proxyLink[proxyLink.index("//")+2:]
    proxyLinkURI="http://"+proxyLinkURI[:proxyLinkURI.index("/")]
    loginAuthPage=getLoginAuthPage(proxyLinkURI)
    verifyCode=getVerifyCodeByLoginAuthPage(loginAuthPage)
    authCode=getLoginAuthPageImageAuthCode(proxyLinkURI)
    imageAddr=getLoginAuthPageImageAddrByAuthCode(authCode)
    downloadLoginAuthPageImage(imageAddr,"./auth.jpg")
    imageCode=fixNumResault(decodeImage("auth.jpg","./"))


    #  <form id="login_form" action="http://54.64.37.20:5201/loginVerify/.auth" style="display: none" method="post" target="_blank">
    #     <input type="hidden" name="VerifyCode" value="1111">
    #     <input type="hidden" name="__name" value="1111" id="user_name">
    #     <input type="hidden" name="__VerifyValue" value="1">
    #     <input type="hidden" name="systemversion" value="1_0">
    #     <input type="hidden" name="banbeng" value="1">
    #     <input type="hidden" name="cname" value="tc">
    #     <input type="hidden" name="password" value="000000">
    #     <input type="hidden" name="cid" value="65">
    #     <input type="hidden" name="loginType" value="1">
    # </form>


    # function loginForm (argument) {
    #         var userName = document.getElementById("user_name"),tN;
    #         while( !tN || tN > 900){
    #             tN = tN = parseInt((+(new Date())-(Math.random())*10).toFixed(3).slice(-3).replace('.',''),10);
    #         }
    #         userName.value = 't' + parseInt(tN,10);
    #         document.getElementById("login_form").submit();
    #     }












    loginURL = "http://pc5.g.nmnmnn.ninja/loginVerify/.auth"
    loginURLheaders = {
        'origin': "http://pc5.g.nmnmnn.ninja",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'dnt': "1",
        'content-type': "application/x-www-form-urlencoded;",
        'accept': "*/*",
        'referer': "http://pc5.g.nmnmnn.ninja/ssczx74883a/.auth",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
        'cache-control': "no-cache"
        }

    payload = "VerifyCode="+verifyCode+"&__VerifyValue="+VerifyValue+"&__name="+username+"&password=Aa1471471!Z$&isSec=0&cid=1050033&cname=èé&systemversion=4_6_sp9&"
 
    responseRes = mafengwoSession.post(loginURL, data = payload, headers = loginURLheaders)
    mafengwoSession.cookies.save()
    print(f"statusCode = {responseRes.status_code}")
    print(f"text = {responseRes.text}")
    # 验证码已过期,请重新刷新。
    return responseRes.text
    


def openProxyPage(proxyLink):
    proxyLinkURI=proxyLink[proxyLink.index("//")+2:]
    proxyLinkURI="http://"+proxyLinkURI[:proxyLinkURI.index("/")]
    loginAuthPage=getLoginAuthPage(proxyLinkURI)
    authCode=getLoginAuthPageImageAuthCode(proxyLinkURI)
    imageAddr=getLoginAuthPageImageAddrByAuthCode(authCode)
    downloadLoginAuthPageImage(imageAddr,"./auth.jpg")
    imageCode=fixNumResault(decodeImage("auth.jpg","./"))
    print(imageCode)
    return loginAuthPage


# VerifyCode=46123
# &__VerifyValue=e5698f2685ed8b3152e68ae04e52d53357b4Mzc2OTo1OTk5Mn5efn5efnY0NjEyMw
# &__name=admina88
# &password=Aa1471471!Z$
# &isSec=0
# &cid=1050033
# &cname=联通
# &systemversion=4_6_sp9&





    
    
def doLogin(account, password):
    mainPage=openMainPage()
    secPage=openSecPage()
    searchPage=openSearchPage()
    proxyLink=getLinkBySearchPage(searchPage)
    proxyPage=openProxyPage(proxyLink)


    

if __name__ == "__main__":
    doLogin(" ", " ")

