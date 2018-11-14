# 任何类都有一个共同的父类object
class Person():
    name = "noname"
    age = 0
    __score = 0    #private私有
    _petname = "sec" #protected 受保护
    def sleep(self):
        self.name = "Leo"
        print("sleeping ... ...{0}".format(self.name))
    def work(self):
        print("make some money")

#父类写在括号内
class Teacher(Person):
    teacher_id = "9527"
    name = "Leo"  # 跟父类定义相同名称变量  优先使用子类
    def make_test(self):
        print("attention")
        pass
    def work(self):
        #Person.work(self)
        super().work
        self.make_test()

t = Teacher()
print(t.name)
print(t._petname)
print(t.teacher_id)

p = Person()
p.sleep()

t = Teacher()
t.work()

class Animel():
    pass

class PaxinAni(Animel):
    pass

class Dog(PaxinAni):
    # __init__就是构造函数 每次实例化的时候第一个被调用 因为主要工作是进行初始化
    def __init__(self):
        print("i am init in dog")

# 实例化的时候 括号内的参数需要跟构造函数参数匹配
kaka = Dog()
