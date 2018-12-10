# 属性案例
# 创建Student类 描述学生类
# 学生具有Student.name属性
# 但name格式并不统一
# 可以用增加一个函数 然后自动调用的方式
class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

        self.setName(name)
        self.setAge(age)

    def intro(self):
        print("hi ,my name is {0}, is {1}".format(self.name,self.age))

    def setName(self,name):
        self.name = name.upper()

    def setAge(self, age):
        self.age = int(age)


s1 = Student("chen ban",19.8)
s2 = Student("michi stangle",24.1)

s1.intro()
s2.intro()

# property案例
# 定义一个person类 具有name age属性
# 对于任意输入姓名 我们希望都用大写方式保存
# 年龄 统一用整数保存
# X = property(fget, fset, fdel, doc)
class Person():
    '''
    这是一个人 一个高尚的人 一个脱离了低级趣味的人
    他还有属性
    '''
    # 函数名称可以任意
    def fget(self):
        return self._name
    def fset(self,name):
        # 所有输入以大写形式保存
        self._name = name.upper()
    def fdel(self):
        self._name = "noname"

    def fagee(self):
        return self._age
    def fage(self,age):
        self._age = int(age)

    name = property(fget,fset,fdel,"对name进行操作了")
    age  = property(fagee,fage,"对age进行操作了")

p1 = Person()
p1.name = "tuling"
p1.age = 18.8
print(p1.name)
print(p1.age)

# 类的内置属性举例
print("*" * 20)
# 以字典的方式显示类的成员组成
print(Person.__dict__)
# 获取类的文档信息
print(Person.__doc__)
# 获取类的名称
print(Person.__name__)
# 获取某个类的所有父类 以元祖的方式显示
print(Person.__bases__)

# __init__ 构造函数
class A():
    def __init__(self,name = 0):
        print("我被调用了")

a = A()


# __call__
class A():
    def __init__(self,name = 0):
        print("我被调用了")

    def __call__(self):
        print("我又被调用了")

a = A()
a()

# __str__
class A():
    def __init__(self,name = 0):
        print("我被调用了")

    def __call__(self):
        print("我又被调用了")

    def __str__(self):
        return "lililililililili"


a = A()
print(a)

#__getattr__
class A():
    name = "noname"
    age = 18

    def __getattr__(self,name):
        print("没找到")
        print(name)
        return  name+" 没找到" # 如果没有返回值 打印的时候回返回一个 None

a=A()
print(a.name)
print(a.addr)

# __setattr__
class Person():
    def __init__(self):
        pass
    def __setattr__(self, name, value):
        print("设置属性：{0}".format(name))
        #下面语句会导致死循环
        #self.name = value
        #此种情况 为了避免 统一调用父类魔法函数
        super().__setattr__(name,value)

p = Person()
print(p.__dict__)
p.age = 18

# __gt__
class Student():
    def __init__(self,name):
        self._name = name
    def __gt__(self, obj):
        print("哈哈 {0} 会比 {1} 大吗".format(self._name,obj._name))
        return self._name > obj._name

stu1 = Student("one")
stu2 = Student("two")
print(stu1 > stu2)

# 三种方法的案例
class Person():
    # 实例方法
    def eat(self):
        print(self)
        print("Eating......")

    #类方法 类方法的第一个参数 一般命名为cls 区别于self
    @classmethod
    def play(cls):
        print(cls)
        print("Playing......")

    # 静态方法 不需要用到第一个参数表示自身或者类
    @staticmethod
    def say():
        print("Saying......")

yueyue = Person()

# 实例方法
yueyue.eat()
# 类方法
Person.play()
yueyue.play()
# 静态方法
Person.say()
yueyue.say()

# 抽象
class Animel():
    def sayhello(self):
        pass

class Dog(Animel):
    def sayhello(self):
        print("闻下对方")

class Person(Animel):
    def sayhello(self):
        print("kiss you")

d  = Dog()
d.sayhello()

p = Person()
p.sayhello()

# 抽象类的实现
import  abc
# 声明一个类并且指定当前类的元类为抽象类提供的元类
class Human(metaclass=abc.ABCMeta):
    # 定义一个抽象的方法
    @abc.abstractmethod
    def smoking(self):
        pass

    # 定义类抽象方法
    @abc.abstractclassmethod
    def drink():
        pass
    #定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass

    def sleep(self):
        print("{0} sleep".format(self))

Human.sleep("Leo")

# 自己组装一个类  函数名可以当变量使用
class A():
    pass

def say(self):
    print("saying......")

say(9)

A.say = say

a= A()
a.say()

from types import MethodType

class B():
    pass

def say(self):
    print("saying......")

b = B()
b.say = MethodType(say,B)
b.say()

# 利用type造一个类
# 先定义类应该具有的成员函数
def say(self):
    print("saying....")

def talk(self):
    print("Talking......")

# 用type来创建一个类
A = type("Aname",(object,),{"class_say":say,"class_talk":talk})
# 然后可以像正常访问一样使用类
a = A()
a.class_say()
a.class_talk()

# 元类
# 元类写法是固定的 它必须继承自type
# 元类一般命名以MetaClass结尾
class  leoMetaClass(type):
    # 注意以下写法
    def __new__(cls, name, bases, attrs):
        #自己的业务处理
        print("我是元类")
        attrs['id'] = '000000'
        attrs['addr'] = '湖南长沙市长沙县泉塘街道'
        return type.__new__(cls, name, bases, attrs)
#元类定义完就可以使用 使用注意写法
class Teacher(object,metaclass=leoMetaClass):
    pass

t = Teacher()
