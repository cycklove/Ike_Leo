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
