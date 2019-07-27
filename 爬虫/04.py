import urllib.request
import re
url='http://www.frxs.com/contactusxs.html'
response=urllib.request.urlopen(url,timeout=10)
html=response.read()  # 获取到页面的源代码
p=html.decode('utf-8')
m=re.findall('[\u4e00-\u9fa5]',p)
for zw in m:
    print(zw)