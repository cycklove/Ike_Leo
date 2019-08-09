from urllib import  request
import  ssl
from chardet import detect

# 利用非认证上下文环境替换认证的上下文环境
#ssl._create_default_https_context = ssl._create_unverified_context()

url = "https://www.12306.cn/mormhweb"

rep = request.Request(url)

rsp = request.urlopen(rep)

html = rsp.read()

cs = detect(html)

html = html.decode(cs.get("encoding","utf-8"))

print(html)