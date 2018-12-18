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