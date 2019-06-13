import re

# 查找数字
# r表示字符串不转义
p = re.compile(r'\d+')
# 在字符串one1two2three3four4five5six6中进行查找 按照规则P制定的正则进行查找
# 返回结果是None表示没有找到 否则返回match对象
m = p.match("one1two2three3four4five5six6")
print(m)

p1= re.compile(r'\d+')
# 在字符串one1two2three3four4five5six6中进行查找 按照规则P制定的正则进行查找
# 返回结果是None表示没有找到 否则返回match对象
m1 = p.match("one168two2three3four4five5six6",3,10)
print(m1)
print(m1[0],m1.start(0),m1.end(0))
# 上述说明的问题
# match可以输入参数表示起始位置
# 查找的结果只包含一个 表示第一次进行匹配成功的内容

# I 表示忽略大小写
p2 = re.compile(r'([a-z]+) ([a-z]+)', re.I)
str = "i am really love yanghan"
m2 = p2.match(str)
print(m2)
print(m2.groups())

# search findall
p3 = re.compile(r'\d+')
m3 = p3.search("one1two2three3four4five5six6")
print(m3.group())

rst = p.findall("one1two2three3four4five5six6")
print(type(rst))
print(rst)

# sub替换案例
p4 = re.compile(r'(\w+) (\w+)')
s = "hello 123 yang 456 han, i love you"
rst2 = p4.sub(r'hello world',s)
print(rst2)

# 匹配中文案例
title = u'世界 你好， hello moto'
p5 = re.compile(r'[\u4e00-\u9fa5]+')
rst3 = p5.findall(title)
rst4 = p5.match(title)
rst5 = p5.search(title)
print(rst3)
print(rst4)
print(rst5)

# 贪婪和非贪婪案例
print("-------------------------------")
title2 = u'<div>name</div><div>age</div><div>sex</div>'

p6 = re.compile(r"<div>.*</div>")
p7 = re.compile(r"<div>.*?</div>")

m5 = p6.search(title2)
print(m5.group())


m6 = p7.search(title2)
print(m6.group())