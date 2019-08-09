from urllib import request,parse
from http import cookiejar
from chardet import detect

#创建FileCookieJar的实例
filename = "filecookie.txt"
cookie = cookiejar.MozillaCookieJar(filename)
# 生成 cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()
# 生成HTTPS管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def login():
    '''
    负责初次登录
    需要输入用户名密码 用来获取登录cookie凭证
    :return:
    '''
    # url需要从登录form的action属性中提取 右键查看网页源代码找
    url = "http://www.renren.com/PLogin.do"
    # 此键值需要从form的两个对应input中提取name属性
    data = {
        "email":"saiyuyu3@163.com",
        "password":"caokai3220251"
    }
    # 把数据进行编码
    data = parse.urlencode(data)
    # 创建一个请求对象
    req = request.Request(url,data=data.encode())
    # 使用opener发起请求
    rsp = opener.open(req)

    #保存cookie到文件
    # ignore_discard 表示即使cookie将要丢弃也要保存下来
    # ignore_expires 表示如果文件中cookie即使已经过期也保存
    cookie.save(ignore_discard=True,ignore_expires=True)

if __name__ == '__main__':
    login()