import urllib.request
import chardet
import  time
import datetime

'''
利用request下载页面
自动检测页面编码
'''

if __name__ == '__main__':
    url = "https://new.qq.com/omn/NEW20190/NEW2019072600579300.html"
    #url = "http://www.frxs.com/contactusxs.html"
    rsp = urllib.request.urlopen(url)
    print(type(rsp))
    print(rsp)

    print("URL : {0}".format(rsp.geturl()))
    print("Info : {0}".format(rsp.info()))
    print("Code : {0}".format(rsp.getcode()))

    html = rsp.read()
    #利用 chardet自动检测
    cs = chardet.detect(html)

    #使用get取值保证不会出错
    html = html.decode(cs.get("encoding","utf-8"))
    #print(html)

