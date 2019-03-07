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
        print(b)
        a,b = b,a+b #注意写法
        n += 1

    return "Done"
