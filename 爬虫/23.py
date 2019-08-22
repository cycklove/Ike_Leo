'''
使用参数headers和params
研究返回结果
'''

import requests
# 完整访问URL是下面URL加上参数构成
url = "http://www.baidu.com/s?"

kw = {
    "wd":"王八蛋"
}

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
rsp = requests.get(url,params=kw,headers=headers)
print(rsp.text)
print(rsp.content)
print(rsp.url.encode().decode())
print(rsp.encoding)
print(rsp.status_code) # 请求返回码