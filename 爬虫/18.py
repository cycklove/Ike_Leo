from urllib import request,parse
from http import cookiejar
from chardet import detect

cookie = cookiejar.MozillaCookieJar()
cookie.load("filecookie.txt")
# 生成 cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()
# 生成HTTPS管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def gethomepage():
    url = "http://www.renren.com/256297970/profile"

    rsp = opener.open(url)

    html = rsp.read()
    cs = detect(html)
    html = html.decode(cs.get("encoding", "utf-8"))

    with open("rsp4.html", "w", encoding="utf-8") as f:
        f.write(html)
        f.close()

if __name__ == '__main__':
    gethomepage()