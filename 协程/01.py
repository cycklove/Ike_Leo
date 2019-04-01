from collections import Iterable,Iterator

# 可迭代
l = [i for i in range(10)]

#l是可迭代的 但不是迭代器
for idx in l:
    print(idx)

#range是个迭代器
for i in range(5):
    print(i)

# isinstance案例
# 判断某个变量是否是一个实例

# 判断是否可迭代
ll = [1,2,3,4,5]
print(isinstance(ll,Iterable))
print(isinstance(ll,Iterator))

# iter函数
s = "i love yh"
print(isinstance(s,Iterable))
print(isinstance(s,Iterator))

s_iter = iter(s)
print(isinstance(s_iter,Iterable))
print(isinstance(s_iter,Iterator))

# 直接使用生成器
L = [x*x for x in range(5)] # 放在中括号中是列表生成器
g = (x*x for x in range(5)) # 放在小括号中就是生成器

print(type(L))
print(type(g))

# 函数案例
def odd():
    print("Step 1")
    print("Step 2")
    print("Step 3")
    return  None

odd()

# 生成器案例
# 在函数odd中 yield负责返回
def odd():
    print("Step 1")
    yield 1
    print("Step 2")
    yield 2
    print("Step 3")
    yield 3

# odd() 是调用生成器
g = odd()
one = next(g)
print(one)
two = next(g)
print(two)
three = next(g)
print(three)

# for循环调用生成器
def fib(max):
    n,a,b = 0,0,1 # 注意写法
    while n < max:
        yield  b
        print(b)
        a,b = b,a+b #注意写法
        n += 1
    # 需要注意 报出异常的返回值是return的返回值
    return "Ike_Leo"

g = fib(5)

for i in range(5):
    rst = next(g)
    print(rst)

'''for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%2d" % (i,j,i*j),end = " ")
    print(" ")'''

ge = fib(10)

for i in ge:#for循环中使用生成器
    print(i)

# 协程代码案例1
def simple_coroutine():
    print("-> start")
    x = yield
    print("-> recived",x)

#主线程
try:
    sc = simple_coroutine()
    print(1111)
    next(sc) #预激

    print(2222)
    sc.send("zhexiao")
except Exception as e:
    print("异常是：",repr(e))
finally:
    print("此次结束")

