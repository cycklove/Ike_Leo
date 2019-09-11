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
- 中文文档 http://docs.python-requests.org/zh_CN/latest/index.html
- 开源地址 https://github.com/requests/requests
- 安装 conda install requests
- get请求
    - requests.get(url)
    - requests.request("get",url)
    - 可以带有headers和parmas参数
    - 案例22
- get返回内容
    - 案例23    
    
- post
    - rsp = requests.post(url,data=data)   
    - 案例24
    - data headers要求dict类型 
- proxy
    - proxies = {
    "http":"address of proxy"
    "https":"address of proxy" }
    - rsp = requests.request("get","http:xxxxxxx",proxies=proxies)
    - 代理有可能报错 如果使用人多 考虑安全问题 可能会被强行关闭
- 用户验证
    - 代理验证
        - 可能需要使用 HTTP basic auth 可以这样
        - 格式为 用户名:密码@地址
        Proxy ={"http":"china:123456@192.168.1.123:4561"}
        rsp = request.get("http://www.baidu.com",proxies=proxy)
- web客户端验证
    - 如果遇到web客户端验证 需要添加auth=(用户名，密码)
        
          auth ={"test1","123456"} 授权信息
          rsp = requests.get("http://www.baidu.com",auth=auth)      
- cookie
    - requests可以自动处理cookie信息
    - 如果对方服务器给传送过来cookie信息 则可以通过反馈的cookie属性得到
    - 返回一个cookiejar实例
    - cookiejar = rsp.cookies
    - cookiejar转换成字典
    - cookiedict = requests.utils.dict_from_cookiejar(cookiejar) 
- session
    - 跟服务器端session不是一个东西
    - 模拟一次会话 从客户端浏览器链接服务器开始 到客户端浏览器断开
    - 能让我们跨请求时保持某些参数 比如在同一个session实例发出的所有请求之间保持cookie
            
            #创建session对象 可以保持cookie值
            ss = requests.session()
            
            headers = {"User-Agent":"xxxxxxxxxx"} 
            data = {"name":"xxxxxxxx"} 
            # 此时由创建的session管理请求 负责发出请求
            ss.post("http://www.baidu.com",data=data,headers=headers)
            
            rsp = ss.get("xxxxxxx") 
- https请求验证ssl证书
    - 参数verify负责表示是否需要验证ssl证书 默认是true
    - 如果不需要验证ssl证书 则设置成false表示关闭
    
            rsp = requests.get("https://www.baidu.com",verify=False)
            # 如果用verify=True访问12306会报错 因为他证书有问题

# 页面解析和数据提取
- 结构数据 先有的结构 再谈数据
    - JSON文件
        - JSON path
        - 转换成Python类型进行操作（json类）
    - XML文件
        - 转换成Python类型（xml to dict）
        - XPath
        - CSS选择器
        - 正则         
- 非结构化数据  先有数据 再谈结构
    - 文本
    - 电话号码
    - 邮箱地址
        - 通常处理此类数据 使用正则表达式
    - HTML文件
        - 正则
        - Xpath
        - CSS选择器 
        
# 正则表达式
- 一套规则 可以在字符串文本中进行搜查替换等
- 案例25 re的基本使用流程 match的基本使用               
- 正则常用的方法
    - match 从开始位置查找 只一次匹配
    - search 从任何位置查找 只一次匹配 案例26
    - findall 全部匹配 返回列表 案例26
    - finditer 全部匹配 返回迭代器 案例26
    - split 分割字符串 返回列表
    - sub 替换 
- 匹配中文
    - 中文Unicode范围主要在[u4e00-u9fa5]
    - 案例27
- 贪婪与非贪婪模式
    - 贪婪模式 在整个表达式匹配成功的前提下 尽可能多的匹配
    - 非贪婪模式  XXXXXXXXXXXXXXXXXXXXXXXX  尽可能少的匹配
    - Python里面数量词默认是贪婪模式
    - 例如
        - 查找文本abbbbbbbccc
        - re是 ab*
        - 贪婪模式结果是 abbbbbbb
        - 非贪婪结果是 a
        
# XML
- XML(Extensible Markup Language)
- http://www.w3school.com.cn/xml/index.asp
- 概念 父节点 子节点 先辈节点 兄弟节点 后代节点

#XPath
- XPath(XML Path Language) 是一门在XML文档中查找信息的语言
- 官方文档http://www.w3school.com.cn/xpath/index.asp
- XPath开发工具
    - 开源的XPath表达式工具 XMLQuire
    - chrome插件 XPath Helper
    - Firefox插件 XPath CHecker
- 常用路径表达式
    - nodename 选取此节点的所有子节点
    - /   从根节点开始选
    - //  选取元素 而不考虑元素的具体位置
    - .   当前节点
    - ..  父节点
    - @   选取属性
    - 案例
        - bookstore 选取bookstore下的所有子节点
        - /bookstore  选取根元素
        - bookstore/book 选取bookstore的所有为book的子元素
        - //book  选取book子元素
        - //@lang 选取名称为lang的所有属性
- 谓语(predicates)
    - 谓语用来查找某个特定的节点 并写在方括号中
    - /bookstore/book[1] 选取第一个属于bookstore下叫book的元素
    - /bookstore/book[last()] 选取最后一个属于bookstore下叫book的元素
    - /bookstore/book[last()-1] 选取倒数第二个属于bookstore下叫book的元素
    - /bookstore/book[position()<3] 选取前两个属于bookstore下叫book的元素
    - /bookstore/book[@lang] 选属于bookstore下叫book的，含有属性lang的元素
    - /bookstore/book[@lang="cn"] 选属于bookstore下叫book的 含有属性lang的值为cn的元素
    
- 通配符
    - *   任何元素节点
    - @*  匹配任何属性节点
    - node() 匹配任何类型节点
- 选取多个路径
    - //book/title  //book/author  选取book元素中的title和author元素
    - //title | //price 选取文档中所有的title和price元素          

# lxml库
- Python的HTML/XML的解析器
- 官方文档  http://lxml.de/index.html
- 案例28
- 功能
    - 解析HTML
    - 文件读取 案例29
    - etree和xpath的配合使用 案例30
    
# CSS选择器 BeautifulSoup4  
- 现在使用BeautifulSoup4
- http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/ 
- 几个常用提取工具比较
    - 正则  很快 不好用 不需安装
    - beautifulsoup 慢 使用简单 安装简单
    - lxml 比较快 使用简单 安装一般
- 案例31
- 四大对象
    - Tag
    - NavigableString
    - BeautifulSoup
    - Comment
- Tag
    - 对应html中的标签
    - 可以通过soup.tag_name
    - tag两个重要属性
        - name
        - attrs
    - 案例32
- NavigableString
    - 对应内容值
    - 案例32 
- BeautifulSoup
    - 表示的是一个文档的内容 大部分可以把他当做tag对象
    - 一般我们可以用soup表示
- Comment
    - 特殊类型的NavigableString对象
    - 对其输出 则内容不包括注释符号

- 遍历文档对象
    - contents  tag的子节点以列表的方式给出
    - children  子节点以迭代器形式返回
    - descendants  所有子孙节点
    - string  
    - 案例33    
- 搜索文档对象
    - find_all(name,attrs,recursive,text,** kwargs)
        - name 按照哪个字符串搜索 可以传入的内容为
            - 字符串
            - 正则表达式
            - 列表
        - kewwortd参数 可以用来表示属性
        - text  对应tag的文本值
        - 案例34
        
- CSS选择器
    - 使用soup.select 返回一个列表
    - 通过标签名称 soup.select("titile")
    - 通过类名 soup.select(".content")
    - 通过ID  soup.select("#name_id")
    - 组合查找 soup.select("div #input_content")
    - 属性查找 soup.select("img[class="photo"])
    - 获取tag内容  tag.get_text
    - 案例35

# 动态HTML
## 爬虫跟反爬虫
## 动态HTML介绍
- JavaScript
- jQuery
- Ajax
- DHTML
- Python采集动态数据
    - 从JavaScript代码入手采集
    - Python第三方库运行JavaScript 直接采集你在浏览器看到的页面

## selenium + phantomJS
- selenium  web自动化测试工具
    - 自动加载页面
    - 获取数据
    - 截屏
    - 官网 http://selenium-python.readthedocs.io/index.html
- phantomJS
    - 基于webkit的无界面的浏览器
    - 官网 http://phantomjs.org/download.html
- selenium 库有一个webdriver的API
- webdriver可以跟页面上的元素进行各种交互 用它可以来进行爬取
- 案例36
- chrome + chromedriver
    - 下载安装Chrome
    - 下载Chromedriver
- selenium操作主要分两大类
    - 得到UI元素
        - find_element_by_id
        - find_elements_by_name
        - find_elements_by_xpath
        - find_elements_by_link_text
        - find_elements_by_tag_name
        - find_elements_by_class_name
        - find_elements_by_css_selector
    - 基于UI元素操作的模拟
        - 单击
        - 右键
        - 拖拽
        - 输入
        - 可以通过导入ActionsChains类来做到
    - 案例37
    
# 验证码问题
- 验证码 防止机器人或爬虫
- 分类
    - 简单图片
    - 极验 官网 https://www.geetest.com
    - 12306
    - 电话
    - 谷歌
    
- 验证码破解
    - 通用方法
        - 下载网页和验证码
        - 手动输入验证号码
    - 简单图片
        - 使用图像识别软件或者文字识别软件
        - 可以使用第三方图像验证码破解网站 http://www.chaojiying.com
    - 极验 官网 https://www.geetest.com
        - 破解比较麻烦
        - 可以模拟鼠标等移动
        - 一直在进化
    - 12306
    - 电话
        - 语音识别
    - 谷歌
    
# Tesseract
- 机器视觉领域的基础软件
- OCR  OpticalChracterRecognition 光学文字识别
- Tesseract 一个ocr库 Google赞助
- 安装
    - Windows https://jingyan.baidu.com/article/6181c3e0c731ba152ef153cf.html
    - Mac brew install tesseract
    - linux apt-get install tesseract-ocr
    - 安装完后需要设置环境变量
- 安装完后还需要pytesseract
    - pip install pytesseract
- 读取案例       
    - 案例38        
                                    
                                                           
                                                       