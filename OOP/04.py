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
print(Person.__dict__)
print(Person.__doc__)