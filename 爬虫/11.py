'''
访问一个网址
更改自己的UserAgent进行伪装
'''
from urllib import request,error
import chardet

if __name__ == '__main__':
    url = "http://www.baidu.com"

    try:
        #使用head方法伪装UA
        # headers = {}
        # headers["User-Agent"]="Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5"
        # req = request.Request(url,headers=headers)

        # 使用add_header方法
        req = request.Request(url)
        req.add_header("User-Agent","Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
        print(req.headers)
        #正常访问
        rsq = request.urlopen(req)

        html = rsq.read()
        cs = chardet.detect(html)
        html = html.decode(cs.get("encoding", "utf-8"))

        print(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
