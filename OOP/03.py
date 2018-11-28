# 多继承的例子
# 子类可以直接拥有父类的属性和方法 私有属性和方法除外
class Fish():
    def __init__(self,name):
        self.name = name
    def swim(self):
        print("i amd swimming......")

class Bird():
    def __init__(self,name):
        self.name = name
    def fly(self):
        print("i am flying......")

class Person():
    def __init__(self,name):
        self.name=name
    def work(self):
        print("Working......")

class SuperMan(Person,Bird,Fish):
    def __init__(self,name):
        pass

s = SuperMan("leo")
s.fly()
s.swim()


# 多继承的例子
class Student(Person):
    def __init__(self,name):
        self.name = name

stu = Student("leo")
stu.work()

# 菱形继承问题
class A():
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass

class Person2():
    # 对Person2类进行实例化的时候
    # 姓名要确定
    # 年龄要确定
    # 地址肯定有
    def __init__(self):
        self.name = "noname"
        self.age = 18
        self.address = "house"
        print("in init func")

p = Person2()

# 如果子类没写构造函数 则自动向上查找 直到找到位置
class A():
    pass
class B(A):
    def __init__(self,name):
        print("B")
class C(B):
    def __init__(self,name):
        B.__init__(self,name)
        print("这是C中附加的功能")

#首先查找C的构造函数 如果没有 则向上按照MRO顺序查找父类的构造函数 直到找到为止
c = C("我是C")