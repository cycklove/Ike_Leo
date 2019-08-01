'''
使用代理访问百度网站
'''
from urllib import request,error
from chardet import detect

if __name__ == '__main__':
    url = "http://www.baidu.com"

    # 设置代理地址
    proxy = {"http":"202.112.51.51:8082"}
    # 创建proxyhandler
    proxy_handler = request.ProxyHandler(proxy)
    # 创建opener
    opener = request.build_opener(proxy_handler)
    # 安装opener
    request.install_opener(opener)

    #现在如果访问url 则使用代理服务器
    try:
        req = request.Request(url)
        print(req.headers)
        req.add_header("User_Agent","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16")
        rsp =request.urlopen(req)
        print(req.headers)
        html = rsp.read()
        cs = detect(html)
        html = html.decode(cs.get("encoding","utf-8"))
        print(html)


    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)