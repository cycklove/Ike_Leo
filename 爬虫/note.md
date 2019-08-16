# 爬虫准备工作
- 参考资料
    - Python网络数据采集 图灵工业出版
    - 精通Python爬虫框架scrapy  人民邮电出版社
    - [Python3网络爬虫](http://blog.csdn.net/c406495762/article/details/72858983)
    - [scrapy](http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.heml)
- 前提知识
    - url
    - http协议
    - web前端 html css js 
    - ajax
    - re xpath
    - xml

# 爬虫简介
- 爬虫定义：网络爬虫（又被称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常的称为网页追逐者），是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。另外一些不常使用的名字还有蚂蚁、自动索引、模拟程序或者蠕虫。
- 两大特征
    - 能按作者要求下载数据或内容
    - 能自动在网络上流窜
- 三大步骤
    - 下载信息
    - 提取正确的信息
    - 根据一定规则自动跳到另外的网页上执行上两步内容
- 爬虫分类
    - 通用爬虫
    - 专用爬虫（聚焦爬虫）

- Python网络包简介
    - Python2.X  urllib urllib2 urllib3 httplib httplib2 requests
    - Python3.X  urllib urllib3 httplib2 requests
    - Python2.X  urllib和urllib2配合使用 或者requests
    - Python3.X  urllib requests

# urllib
- 包含模块
    - urllib.request  打开和读取urls
    - urllib.error 包含urllib.request产生的常见的错误 使用try捕捉
    - urllib.parse 包含解析url的方法
    - urllib.robotparse  解析robots.txt文件
    - 案例01
- 网页编码问题解决
    - chardet 可以自动检测页面文件的编码格式 但是可能有误
    - 需要安装 conda install chardet
    - 02
- urlopen的返回对象
    - 案例03
    - geturl 返回请求对象的url
    - info 请求反馈对象的meta信息
    - getcode 返回的http code 比如404 200 500
- request.data 的使用
    - 访问网络的两种方法
        - get  
            - 利用参数给服务器传递信息
            - 参数为dict 然后用parse编码
        - post
            - 一般向服务器传递参数使用
            - post是把信息自动加密处理
            - 我们如果想使用post信息 需要用到data参数               
            - 使用post 意味着HTTP的请求头可能需要更改
            - 简而言之 一旦更改请求方法 请注意其他请求头部信息相适应
        - urilib.parse.urlencode可以将字符串自动装换成上面的
        - 06
        - 简易的英汉译词典 07
        - 为了更多的设置请求信息 单纯的通过urlopen函数已经不太好用可
        - 需要利用request.Request 类
        - 案例08
- urllib.error
    - URLerror产生的原因
        - 没网
        - 服务器链接失败
        - 找不到指定服务器
    - 是OSerror的子类
    - 案例09
    - HTTPerror  是URLerror的一个子类
        - 案例10
        
    - 两者区别
        - HTTPerror是对应的HTTP请求的返回码错误 如果返回错误码是400以上的 则引发HTTPerror
        - URLerror对应的一般是网络出现问题 包括URL问题
        - 关系区别 OSerror-URLerror-HTTPerror    
        
- UserAgent
    - UserAgent 用户代理 简称UA 属于heads的一部分 服务器通过UA来判断访问者的身份
    - 常见的UA值 使用的时候可以直接复制粘贴 也可以用浏览器访问的时候抓包
     ```chrome 
        Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 
        Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11 
        Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16
        
        Firefox 
        Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0 
        Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10
        
        Opera 
        Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60 
        Opera/8.0 (Windows NT 5.1; U; en) 
        Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50 
        Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50
        
        Safari 
        Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2
        
        360 
        Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36 
        Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
        
        QQ浏览器 
        Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400) 
        Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)
        
        sogou浏览器 
        Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0 
        Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)
        
        UC浏览器 
        Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36
        
        ======移动端=======
        IPhone 
        Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5
        
        IPAD 
        Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5 
        Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5
        
        Android 
        Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
        Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
        
        QQ浏览器 Android版本 
        MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
        
        Android Opera Mobile 
        Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10
        
        Android Pad Moto Xoom 
        Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13 ```
        
- 设置UA可以通过两种方式
    - heads
    - add_header
    - 案例11
    
- proxyhandler处理（代理服务器）
    - 使用代理IP 是爬虫的常用手段
    - 获取代理服务器地址
        - www.xicidaili.com
        - www.goubanjia.com
    - 代理用来隐藏真实访问中 代理也不允许频繁访问某一个固定网站 所以代理一定要很多很多
    - 基本使用步骤
        - 设置代理地址
        - 创建proxyhandler
        - 创建opener
        - 安装opener
    - 案例12
    
- cookie & session
    - 由于HTTP协议的无记忆性 人们为了弥补这个缺憾 所采用的一个补充协议
    - cookie是发给用户（即HTTP浏览器）的一段信息 session是保存在服务器上的对应的另一办信息 用来记录用户信息
    
- cookie和session的区别
    - 存放位置不用
    - cookie并不安全
    - session会保存在服务器上一定时间 会过期
    - 单个cookie保存数据不超过4K 很多浏览器限制一个站点最多保存20个
- session的存放位置
    - 存在服务器端
    - 一般情况 session是存在内存中或者数据库中
    - 没有cookie登录 案例13  可以看到(本来已经登录的个人中心网页) 没有使用cookie则反馈的网页为未登录的状态
    
- 使用cookie登录
    - 直接把cookie复制下来 然后手动放入请求头 案例14
    - http模块包含一些关于cookie的模块 通过他们我们可以自动使用cookie
        - CookieJar
            - 管理存储cookie 向传出的HTTP请求添加cookie
            - cookie存储在内存中 CookieJar实例回收后cookie将消失
        - FileCookieJar(filename,delayload=None,policy=None)
            - 使用文件管理cookie
            - filename是保存cookie的文件
        - MozillaCookieJar(filename,delayload=None,policy=None)
            - 创建与Mozilla浏览器cookie.txt兼容的FileCookieJar实例
        - LwpCookieJar
            - 创建与libwww-perl标准兼容的Set-Cookie3格式的FileCookieJar实例
        - 他们的关系 CookieJar-->FileCookieJar-->MozillaCookieJar & LwpCookieJar
    - 利用CookieJar访问人人网 案例15
        - 自动使用cookie登录 大致流程是
        - 打开登录页面后自动通过用户名密码登录
        - 自动提取反馈回来的cookie
        - 利用提取的cookie登录隐私页面
    - handler是Handler的实例 常用的有
        - request.HTTPCookieProcessor(cookie)
        - request.HTTPHandler()
        - request.HTTPSHandler()
    - 创建handler后 使用opener打开 打开后相应的业务由相应的handler处理
    - cookie作为一个变量 打印出来 案例 16
        - name  名称
        - value 值
        - domain 可以访问此cookie的域名
        - path 可以访问此cookie的页面路径
        - expire 过期时间
        - size 大小
        - HTTP字段                              
    - cookie的保存 - FileCookieJar  案例17
    - cookie的读取 案例18
    
- SSL
    - SSL证书是指遵守SSL安全套阶层协议的服务器数字证书（SecureSocketLayer）
    - 美国网景公司开发
    - CA（certificateauthority）是数字证书认证中心 是发放管理废除数字证书的收信人第三方机构 
    - 遇到不信任的SSL证书 需要单独处理 案例19
- js加密
    - 有的反爬虫策略采用js对需要传输的数据进行加密处理（通常是取md5值）
    - 经过加密 传输的就是密文
    - 加密函数或者过程一定是在浏览器完成 也就是一定会把代码（js代码）暴露给使用者
    - 通过阅读加密算法 就可以模拟出加密过程 从而达到破解
    - 过程参看案例20
    
- ajax          
    - 异步请求
    - 一定会有URL 请求方法 可能有数据
    - 一般使用json格式
    - 案例 爬豆瓣电影 案例21
             
- Requests-献给人类
- HTTP for Humans 更简洁更友好
- 继承了urllib的所有特征
- 底层使用的是urllib3
                                                                                              