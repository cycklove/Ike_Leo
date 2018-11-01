'''
定义一个学生类 用来形容学生
'''
#定义一个空的类
class Student():
    pass  #代表直接跳过

# 定义一个对象
mingyue = Student()

class PythonStudent():
    name = None
    age = 18
    course = "Python"

    def dohomework(self):
        print("I 在做作业")

        return  None

#实例化
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)

yueyue.dohomework()
# print(PythonStudent.__dict__)

#yueyue.name = str(yueyue.name)
yueyue.name = "cb"
yueyue.age = 28

print(yueyue.name)
print(yueyue.age)