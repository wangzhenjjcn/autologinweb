#coding=utf-8
import sys,time,datetime,os,requests

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
    pageData=responseRes.text
    proxyLink=pageData[pageData.index("<div class='b_line'></div>"):] 
    proxyLink=proxyLink[:proxyLink.index("</ul>")]    
    proxyLink=proxyLink[proxyLink.index("线路3"):proxyLink.index("线路4")] 
    proxyLink=proxyLink[proxyLink.index("</li><li><a href=\"")+18:proxyLink.index("target=")]  
    proxyLink=proxyLink[:proxyLink.index("\"")]                     
    print(proxyLink)
    return proxyLink

def getLoginAuthPage(proxyLink):
    openSecPageUrl = proxyLink
    getLoginAuthPageHeaders = {
        'upgrade-insecure-requests': "1",
        'dnt': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'referer': "http://vst520.net/",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
        'cache-control': "no-cache"
        }
    responseRes = mafengwoSession.get(openSecPageUrl, headers = getLoginAuthPageHeaders, allow_redirects = True)
    print(f"statusCode = {responseRes.status_code}")
    print(f"text = {responseRes.text}")
    mafengwoSession.cookies.save()
    postLoginAuthPage()




def postLoginAuthPage():
    print("") 
    # print("") var ajax = new current_page.Ajax();
    #         ajax.get("/getCodeInfo/.auth?u=" + Math.random() + '&systemversion=' + systemversion + '&.auth', function(xmlhttp) {
    #             if (xmlhttp) {
    #                 var t = xmlhttp.responseText.split("_");
    #                 document.getElementById("img").innerHTML = "<img alt='請刷新' onerror='current_page.flag = false' title='如看不清，點擊刷新' onload='current_page.flag = false;current_page.getbk()' src='/getVcode/.auth?t=" + t[0] + '&systemversion=' + systemversion + "&.auth' />";
    #                 document.getElementsByName("__VerifyValue")[0].value = t[1];
    #                 var objx = document.getElementById("textActive");
    #                 if(objx){
    #                     current_page.time = (t[t.length-1]+"").replace(/\s+/g,"");
    #                     objx.Time = current_page.time;
    #                 }
    #                 return;

def openProxyPage(proxyLink):
    getLoginAuthPage(proxyLink)
    
    print("")

 
    
def doLogin(account, password):
    openMainPage()
    openSecPage()
    proxyLink=openSearchPage()
    openProxyPage(proxyLink)



    
    
    
    

if __name__ == "__main__":
    doLogin(" ", " ")


 
 