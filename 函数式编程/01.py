import os,sys
print(os.getcwd())
print(os.path.basename(sys.argv[0]))
# lambda 表达式
# “小”函数举例
def AAA():
    print("AAAAAAAAAA")

AAA()

# lambda表达式的用法
# 以 lambda开头
# 紧跟一定的参数（如果有的话）
# 参数后用冒号和表达式主体隔开
# 只是一个表达式 所有 没有return

# 计算一个数字的100倍数
stm = lambda x: 100 * x
print(stm(89))

stm2 = lambda x,y,z: x+y*10 + z*100
print(stm2(4,5,6))

# 函数名称就是一个变量
# 既然函数名称是变量 则应该可以被当做参数传入另一个函数
def funa():
    print("funa")

funb = funa
funb()

# 高阶函数举例
# funa是普通函数 返回一个传入数字的100倍
def funa(n):
    return n*100

# 再写一个函数 把传入参数乘以300倍 利用高阶函数
def funb(n):
    return funa(n) * 3

print(funb(9))

# 写一个高阶函数
def func(n,f):
    # 假定函数是把n扩大100倍
    return  f(n) * 3
print(func(9,funa))

# 比较func和funb 显然func的写法要优于funb
#例如：
def fund(n):
    return n*10

# 需求变更 需要把放大30倍 此时funb则无法实现
print(func(9,fund))

# 系统高阶函数 - map
# map举例
# 有一个列表 想对列表里的每一个元素乘以10 并得到新的列表
l1 = [i for i in range(10)]
print(l1)
l2 = []
for i in l1:
    l2.append(i*10)
print(l2)

# 利用map实现
def multen(n):
    return n * 10

#map()和filter()等一些高阶函数在Python3中的返回值类型变成了Iteraotr（迭代器）对象（在Python2中的返回值类型为list）
#所以结果想打印出列表形式的话，list定义一下
l3 = list(map(multen,l1))
# map类型是一个可迭代的结构 所以可以使用for遍历
for i in l3:
    print(i)

#所以结果想打印出列表形式的话，list定义一下
l4 = [i for i in l3]
print(l4)

# reduce
# 愿意是归并 缩减
# 把一个可迭代对象最后归并成一个结果
# 对于作为参数的函数要求 必须有两个参数 必须有返回结果
from functools import  reduce
# 定义一个操作函数
# 加入操作函数只是相加
def myadd(x,y):
    return  x + y

rst = reduce(myadd,[1,2,3,4,5,6,7,8,9])
print(rst)

# filter案例
# 需要定义过滤函数
# 过滤函数要求有输入 返回布尔值
# 对于一个列表 对其进行过滤 偶数组成一个新列表
def iseven(a):
    return  a % 2 == 0

l = [ i for i in range(20)]

rst = filter(iseven,l)
# 返回的filter内容的一个可迭代对象
print(rst)
print(list(rst))

# 排序的案例
a = [12,56,456,9,456,3,4,6,1899,5]
al = sorted(a,reverse=True) # 不加reverse=True为升序  加reverse=True为降序
print(al)

# 排序的案例2
a = [-12,123,121,4,6,489,-123,99,-322]
al = sorted(a,key=abs)  # key=abs按绝对值排序
print(al)

# 排序案例3 sorted
astr = ['ddd','www','leo','LL','jingjing','owner']

str1 = sorted(astr)
print(str1)
str2 = sorted(astr,key=str.lower) #转化为小写再排序
print(str2)

# 返回函数
# 定义一个普通函数
def myf(a):
    print('in myf')
    return None
a = myf(9)
print(a)

# 函数作为返回值返回 被返回的函数在函数体内定义
def myf2():
    def myf3():
        print("in myf3")
        return 3
    return myf3

# 使用上面定义
# 调用myf2 返回一个函数myf3 赋值给f3
f3 = myf2()
print(type(f3))
print(f3)

print(f3())

# 复杂一点的返回函数的例子
# args 参数列表
# myf3定义函数 返回内部定义的函数myf5
# myf5使用了外部变量 这个变量是myf4的参数
def myf4( *args):
    def myf5():
        rst = 0
        for n in args:
            rst += n
        return  rst
    return myf5

f5 = myf4(1,2,5,6,8,9,7,1,3)
# f5的调用
print(f5())

# 闭包常见坑
def count():
    # 定义列表 列表里存放的是定义的函数
    fs = []
    for i in range(1,4):
        # 定义一个函数f f是一个闭包结构
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())
# 出现的问题：
# 造成上述状况的原因是 返回函数引用了变量i i并非立即执行 而是等到三个函数都返回了的时候才统一使用 此时i已经变成了3
#最终调用的时候 都返回的是3*3
# 此问题描述成 返回闭包时 返回函数不能引用任何循环变量
# 解决方案 再创建一个函数 用该函数的参数绑定循环变量的当前值 无论该循环变量以后如何改变 已经绑定的函数参数值不在改变
def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3 = count1()
print(f1())
print(f2())
print(f3())

# 装饰器
def hello():
    print("hello world")
hello()

f = hello
f()

# f和hello是一个函数
print(id(f))
print(id(hello))

print(f.__name__)
print(hello.__name__)

# 现在有新的需求
# 对hello功能进行扩展 每次打印hello之前打印当前系统时间
# 而实现这个功能又不能改动现有代码
# ==>使用装饰器

#任务
#对hello函数进行功能扩展 每次执行hello打印当前时间
import time,datetime
# 高阶函数 以函数作为参数

def ptime(f):
    def wapper(*args,**kwargs):
        print("Time: ", time.strftime('%Y{0}%m{1}%d{2} %H:%M:%S').format('年','月','日'))
        return f(*args,**kwargs)
    return wapper
# 上面定义了装饰器 使用的时候需要用到@ 此符号是Python的语法糖
@ptime
def hello():
    print("hello world")

hello()

print("------分隔符-------")
@ptime
def hello2():
    print("今天很郁闷 那些人都是傻逼")
    print("滚")

hello2()
print("------分隔符-------")
# 上面对函数的装饰使用了系统定义的语法糖
# 下面开始手动执行下装饰器
# 先定义函数
def hello3():
    print("我是手动执行的")

hello3()

hello3 = ptime(hello3)
hello3()

f = ptime(hello3)
f()

# 偏函数
# 把字符串转化成十进制数字
i1 = int("12345")
print(i1)
# 求八进制的字符串12345 表示成十进制的数字是多少
i2 = int("12345",base=8)
print(i2)

# 新建一个函数 此函数是默认输入的字符串是16进制的数字
# 把此字符串返回十进制的数字
def int16(x,base=16):
    return int(x,base)

print(int16("12345"))

import functools
# 实现上面int16的功能
int16 = functools.partial(int,base=16)

i16 = int16("12345")
print(i16)

# zip 案例
l1 = [1,2,3,4,5]
l2 = [11,22,33,44,55]

z = zip(l1,l2)
print(type(z))
print(z)
l3 = []
for i in z:
    l3.append(i)
print(l3)

l1 = ["wangwang","mingyue","yyt"]
l2 = [89,60,78]

z = zip(l1,l2)

for i in z:
    print(i)

l3 = [i for i in z]
print(l3)
print(type(l3))

# enumerate
l1 = [11,22,33,44,55]

em =enumerate(l1)

l2 = [i for i in em]
print(l2)

em = enumerate(l1,start=1) # start 从多少开始
l2 = [i for i in em]
print(l2)

# namedtuple
import  collections
Point = collections.namedtuple("point",['x','y'])
p = Point(11,22)
print(p.x)
print(p[0])

circle = collections.namedtuple("circle",['x','y','r'])
c = circle(100,150,50)
print(c)
print(type(c))
# 检测到底是属于谁的子类
isinstance(c,tuple)

#deque
from collections import deque
q = deque(['a','b','c'])
print(q)

q.append('d')
print(q)

q.appendleft('x')
print(q)

# defaultdict
from collections import defaultdict
d1 = {"one":1,"two":2,"three":3}
# lambda表达式 直接返回字符串
func = lambda : "陈大拿"
d2 = defaultdict(func)
d2["one"] = 1
d2["two"] = 2
print(d2['one'])
print(d2['ten'])

# counter
from collections import Counter
c = Counter("fasjifjqiojfkdsnklgnioneqwionfknsglnklnklsdngkl") #统计每个字符出现的次数
print(c)
ct = c.elements()
j = 0
for i in ct:
    j+=1
print(j)

s = ["leo","love","love","love"]
c = Counter(s)
c2 = s.count("love")
print(c)
print(c2)
obj =c.elements()
j = 0
for i in obj:
    j +=1
print(j)




