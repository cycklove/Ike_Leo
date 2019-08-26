'''
利用parse模块模拟post请求
分析百度词典
分析步骤
1. 打开F12
2. 尝试输入单词girl 发现没敲一个字母后都有请求
3. 请求地址是 http://fanyi.baidu.com/sug
4. 利用F12后里的 NERWORK ALL Hearders 查看 发现fordata的值是 kw:girl
5. 检查返回内容格式 发现返回的是json格式内容   需要用到json包
'''

import requests
from urllib import parse
import json

'''
大致流程是
1.利用data构造内容 然后urlopen打开
2.返回一个json格式的结果
3.结果就应该是girl的释义
'''
baseurl = "https://fanyi.baidu.com/sug"
# 存放用来模拟from的数据 一定是dict格式
kw = input("请输入：")
data = {
    'kw':kw
}

# 需要构造一个请求头 应该至少包含传入的数据的长度
# request要求传入的请求头是一个dict格式

headers = {
    # 因为使用post 至少包含content-length 字段
    "Content-Length":str(len(data))
}

rsp = requests.post(baseurl,data=data,headers=headers)

#print(rsp.text)
print(rsp.json())


