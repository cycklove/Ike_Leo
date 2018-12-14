import calendar
import  time
import datetime

# calendar 获取一年的日历字符串
# 参数
# w = 每个日历之间的间隔字符数
# l = 每周所占用的行数
# c = 每个月之间的间隔字符数
cal = calendar.calendar(2018)
print(cal)
print(type(cal))

cal2 = calendar.calendar(2018,l=0,c=5)
print(cal2)

# isleap  判断某一年是否闰年
print(calendar.isleap(2018))

# leapdays 获取指定年份之间的闰年的个数
print(calendar.leapdays(1998,2018))

help(calendar.leapdays)

# month () 获取某个月的日历字符串
# 格式 calendar.month(年,月)
# 回值 月日历的字符串
print(calendar.month(2018,6))

# monthrange() 获取一个月的周几开始和天数
# 格式 calendar.monthrange(年,月)
# 回值 元组（周几开始 总天数）
# 注意 周默认0-6 表示周一到周日
help(calendar.monthrange)
print(calendar.monthrange(2018,6))

# monthcalendar() 返回一个月每天的矩阵列表
# 格式 calendar.monthcalendar（年,月）
# 回值 二级列表
# 注意 矩阵中没有天数用0表示
print(calendar.monthcalendar(2018,6))

for i in (calendar.monthcalendar(2018,6)):
    for j in i:
        print(j)
        #time.sleep(0.1)

# prcal print calendar 直接打印日历
# calendar.prcal(2018)
calendar.prcal(2018)

# prmonth() 直接打印整个月的日历
# 格式 calendar.prmonth(年,月)
# 返回值 无
calendar.prmonth(2018,6)

# weekday() 获取周几
# 格式 calendar.weekday(年,月,日)
# 返回值 周几对应的数字
wk =calendar.weekday(2018,12,12)
print(wk+1)

# 时间模块的属性
# timezone   当前时区和UTC时间相差的秒数 在没有夏令时的情况下的间隔 东八区
# altzone   获取当前时区与UTC相差的秒数 在有夏令时的情况下
# daylight 测当前是否是夏令时状态

tz = time.timezone
print(tz)
altz = time.altzone
print(altz)
dl = time.daylight
print(dl)

# 得到时间戳 time.time()
print(time.time())
# 得到当前时间 time.localtime()
# 可以通过点号操作符得到相应的属性元素内容
localtm = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(localtm)
ltm = time.localtime()
print(ltm.tm_hour)

# asctime() 返回时间元组的正常字符串化后的时间格式
# 格式 time.asctime(时间元组)
t = time.localtime()
print(time.asctime(t))

# ctime 获取字符串化的当前时间
clt = time.ctime()
print(clt)

# mktime() 使用时间元组获取对应的时间戳
# 格式 time.mktime(时间元组)
# 返回值 浮点数时间戳
lt = time.localtime()
ts = time.mktime(lt)
print(ts)

# clock 获取CPU时间  3.0-3.3版本直接使用  3.6调用有问题
def p():
    time.sleep(1)

t0 = time.clock()
p()
t1 = time.clock()
print(t1 - t0)

# sleep 使程序进入睡眠 n秒后继续
for i in range(10):
    print(i)
    #time.sleep(0.1)

# strftime 将时间元组转化为自定义的字符串格式
# 把时间表示成 2018年12月26日 15:58
t = time.localtime()
ft = time.strftime('%Y{0}%m{1}%d{2} %H:%M').format('年','月','日')
print(ft)

#datetime.date 提供 year month day属性
dt = (datetime.date(2018,12,12))
print(dt)
#datetime.time 提供hour minute sec microsec等
#datetime.datetime  日期跟时间的组合
from datetime import datetime,timedelta
# today:
# now:
# utcnow
# fromtimestamp
dt = datetime(2018,12,12)
print(dt.today())
print(dt.now())

print(dt.fromtimestamp(time.time()))

#datetime.timedelta  时间差 时间长度
t1 =datetime.now()
print(t1.strftime("%Y-%m-%d %H:%M:%S"))
#td表示一小时的时间长度
td = timedelta(hours=1)
#当前时间加上时间间隔后 把得到的一个小时后的时间格式化输出
print((t1+td).strftime("%Y-%m-%d %H:%M:%S"))

# timeit 时间测量工具
# 测量程序时间间隔实验
def pp():
    time.sleep(1.6)

t1 =time.time()
p()
print(time.time() - t1)

# 生成列表两种方法
# 如果单纯比较生成一个列表的时间 可能很难实现
import  timeit
c = '''
sum = []
for i in range(1000):
    sum.append(i)'''

# 利用欧timeit调用代码 执行100000次 查看运行时间
t1 = timeit.timeit(stmt = "[i for i in range(1000)]",number=100000)
# 测量代码c执行100000次运行结果
t2 = timeit.timeit(stmt = c,number=100000)
print(t1)
print(t2)
# help(timeit.timeit)

# timeit 可以执行一个函数 来测量一个函数的执行时间
def doit():
    num = 3
    for i in range(num):
        print("repeat for {0}".format(i))

# 执行函数 重复10次 打印出时间
t = timeit.timeit(stmt=doit,number=10)
print(t)

s= '''
def doit(num):
    for i in range(num):
        print("repeat for {0}".format(i))
'''
# 执行doit(num)
# setup负责把环境变量准备好
# 实际相当于给timeit创造了一个小环境

t = timeit.timeit("doit(num)",setup=s+"num=3",number=10)
print(t)

