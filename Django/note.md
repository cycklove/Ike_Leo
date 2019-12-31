# Django系统
- 环境
    - Python3.6
    - Django1.8
- 参考资料
    - [django中文教程](https://yiyibooks.cn/xx/django_182/index.html)  
    - Django架站的16堂课
# 环境搭建
- anaconda+pycharm
- anaconda使用
    - conda list 显示当前环境安装的包
    - conda env list 显示安装的虚拟环境列表
    - conda create -n env_name python=3.6
    - 激活conda的虚拟环境
        - Linux source activate env_name
        - win activate env_name
    - pip install django=1.8
    
# 创建第一个Django程序
- django-admin startproject
- 命令行启动 
    - cd 到 manage.py的目录  python manage.py runserver
    
- pycharm启动
    - 需要配置 parameters: runserver
                               
# 路由系统-urls
- 创建APP
    - APP：负责一个具体业务或者一类具体业务的模块
    - python manage.py startapp teacher
- 路由
    - 按照具体的请求url 导入到相应的业务处理模块的一个功能模块
    - django的信息控制中枢
    - 本质上是接受的URL和相应的处理模块的一个映射
    - 在接受URL请求的匹配上使用了RE
    - URL的具体格式如urls.py所示
- 需要关注的两点：
    - 接受的url是什么 即如何用RE对传入URL进行匹配
    - 已知URL匹配到哪个处理模块
- URL匹配规则
    - 从上往下一个一个比对
    - URL格式是分级格式 则按照级别一级一级往下比对 主要对应URL包含子URL的情况
    - 子URL一旦被调用则不会返回到主URL
        - `/one/two/three/`
    - 正则以r开头表示不要转义 注意尖号(^)和美元符号($)
        -  `/one/two/three/` 配对 r'^one/'
        -  `/oo/one/two/three/` 不配对 '^one/'
        -  `/one/two/three/` 配对 r'three/$'
        -  `/oo/one/two/three/oo/`  不配对 r'three/$'
        - 开头不需要有反斜杠
    - 如果从上向下都没有找到合适的匹配内容 则报错                                             
    
# 正常映射
- 把某一个符合RE的URL映射到事务处理函数中去
    - 举例如下：
        ```
        from showeast import view as sv
        
        urlpatterns = [ 
            url(r'^admin/',admin.site.urls),
            url(r'^normalmap/',sv.normalmap),
        ]  
        ```
 # URL中带参数映射
 - 在事件处理代码中需要由URL传入参数 形如 /myurl/param中的param
 - 参数都是字符串形式 如果需要整数形式需要自行转换
 - 通常的形式如下
    ```
      /search/page/432 中的432需要经常性变换
    ```        
    
# URL在app中处理
- 如果所有应用URL都集中在chenban/urls.py中 可能导致文件的臃肿
- 可以把urls具体功能逐渐分散到每个app中
    - 从django.conf.urls 导入 include
    - 注意此时RE部分的写法
    - 添加include导入
- 使用方法
    - 确保include被导入
    - 写主路由的开头url
    - 写子路由
    - 编写views函数        
- 同样可以使用参数
    - 捕获某个参数的一部分
    ```
    url(r'^book/(?:page-(?P<pn>\d+)/)$', tv.do_param2),
    ```
- 传递额外参数
- 参数不仅仅来自以URL 还可能是我们自己定义的内容
    '''
    url(r'extrem/$',sv.extremParam,{'name':"chenban"}),
    '''        
- 附加参数同样适用于include语句 此时对include内所有都添加    
                                          