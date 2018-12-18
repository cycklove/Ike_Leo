# 常用模块
- calendar
- time
- datetime
- timeit
- os
- shutil
- zip
- math
- string
- 上述所有模块使用都应该先导入 string是特例
- calendar time datetime的区别参考中文意思

# calendar
- 跟日历相关的模块

# time模块
- 时间戳
    - 一个时间表示 根据不同语言 可以是整数或者浮点数
    - 是从1970年1月1日0时0分0秒到现在经历的秒数
    - 如果表示的时间是1970年以前或者太遥远的未来 可能出现异常
    - 32位操作系统能够支持到2038年
    
- UTC时间
    - 世界协调时间 以英国的格林尼治天文所在地区的时间作为参考时间 也叫世界标准时间
    - 中国时间 UTC+8 东八区
    
- 夏令时
    - 夏令时就是在夏天的时候将时间调快一小时 本意是督促大家早睡早起 每天变成25小时 本质没变还是24小时
    
- 时间元组
    - 一个包含时间内容的普通元组
#    
    索引             内容          属性            值
    0                 年           tm_year         2015
    1                 月           tm_mon          1~12
    2                 日           tm_day          1~31
    3                 时           tm_hour         0~23
    4                 分           tm_min          0~59
    5                 秒           tm_sec          0~61   60表示闰秒 61保留值
    6                 周几         tm_wday         0~6
    7                 第几天       tm_yday         1~366
    8                 夏令时       tm_isdst        0，1，-1（表示夏令时）
     
# strftime 将时间元组转化为自定义的字符串格式                    
    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12） 
    %M 分钟数（00=59）
    %S 秒（00-59）
    
    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称
    %% %号本身
    
# datatime模块
- datetime提供日期和时间的运算和表示

# datetime.datetime模块
- 提供比较好用的时间而已
# 类定义
    class datetime(date)
    datetime(year, month, day[, hour
    [, minute
    [, second
    [, microsecond
    [,tzinfo]]]]])
    #The year, month and day arguments are required.
    MINYEAR <= year <= MAXYEAR
    1 <= month <= 12
    1 <= day <= n
    0 <= hour < 24
    0 <= minute < 60
    0 <= second < 60
    0 <= microsecond < 10**6 
    
# OS - 操作系统相关
- 跟操作系统相关 主要是文件操作
- 与系统相关的操作 主要包含在三个模块里
    - os 操作系统相关模块相关
    - os.path 系统路径相关操作
    - shutil  高级文件操作 目录树的操作 文件赋值 删除 移动
- 路径：
    - 绝对路径 总是从根目录上开始
    - 相对路径 基本以当前环境为开始的一个相对的地方
    
# OS 模块
# getcwd()  获取当前的工作目录
# 格式  os.getcwd()
# 返回值 当前工作目录的字符串
# 当前工作目录就是程序进行文件相关操作 默认查找文件的目录
             
# 值部分
- os.curdir  curretn dir 当前目录
- os.pardir  parent dir 父目录
- os.sep   当前系统的路径分隔符
- os.linesep 当前系统的换行符号
- os.name 当前系统名称 

# os.path 模块 跟路径相关的模块

# shutil 模块          

# 归档和压缩
- 归档 把多个文件或者文件夹合并到一个文件中
- 压缩 用算法把多个文件或者文件夹无损或者有损合并到一个文件当中

# zip 压缩包
- 模块名称叫  zipfile

# random
- 随机数
- 所有的随机模块都是伪随机  