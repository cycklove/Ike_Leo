from urllib import request,parse

if __name__ == '__main__':
    url = "http://www.baidu.com/s?"
    wd = input("input your keyword:")
   # 要想使用data 需要使用字典结构
    qs ={
        "wd":wd
    }
    # 转换url编码
    qs = parse.urlencode(qs)

    fullurl = url + qs
    print(fullurl)
    rsp = request.urlopen(fullurl)

    html = rsp.read()

    html=html.decode()

    print(html)