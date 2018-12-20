# OS 模块
# getcwd()  获取当前的工作目录
# 格式  os.getcwd()
# 返回值 当前工作目录的字符串
# 当前工作目录就是程序进行文件相关操作 默认查找文件的目录
import os
import sys
import time

mydir = os.getcwd()
print(mydir)
print (sys.argv[0])

# chdir() 改变当前的工作目录
# 格式 os.chdir（路径）
# 返回值 无

os.chdir('D:\PycharmProjects\Ike_Leo\常用模块')
mydir = os.getcwd()
print(mydir)

# listdir() 获取一个目录中所有子目录和文件的名称列表
# 格式 os.listdir(路径)
# 返回值 所有子目录和文件名称的列表
ld = os.listdir()
for i in ld:
    print(i)

# makedirs()  递归创建文件夹
# 格式 os.makedirs(递归路径)
# 返回值  无
# 多个文件夹层层包含的路径就是递归路径  例如A/B/C
rst = os.makedirs("leo")
print(rst)

os.removedirs("leo")

# system() 运行系统命令
# 格式 os.system(系统命令)
# 返回值 打开一个shell或者终端界面
# 一般推荐使用subprocess代替

'''rst = os.system("services.msc")
print(rst)'''

# getenv() 获取指定的系统环境变量值
# 相应的还有putenv()
# 格式 os.getenv（'环境变量名'）
# 返回值 指定环境变量名对应的值
ret = os.getenv("path")
print(ret)

# exit() 退出当前程序
# 格式 exit()
# 返回值 无

# 值部分
# os.curdir  curretn dir 当前目录
# os.pardir  parent dir 父目录
# os.sep   当前系统的路径分隔符
# os.linesep 当前系统的换行符号
# os.name 当前系统名称
print(os.curdir)
print(os.pardir)
print(os.sep)
print(os.linesep)

# 当前系统名称
# windows:  nt       mac unix linux: posix
print(os.name)

# abspath（） 将路径转化为绝对路径
# 格式 os.path.abspath('路径')
# 返回值 路径的绝对路径形式

# linux中
# . 点号 代表当前目录
# .. 双点 代表父目录
absp = os.path.abspath('')
print(absp)

# basename() 获取路径中的文件名部分
# 格式 os.path.basename（'路径'）
# 返回值 文件名字符串

bn = os.path.basename(sys.argv[0])
print(bn)

# join() 将多个路径拼成一个路径
# 格式 os.path.join（路径1，路径2.....）
h1 = "d:\\leo"
h2 = "ike.doc"
pj = os.path.join(h1,h2)
print(pj)

# split() 将路径切割为文件夹部分和当前文件部分
# 格式 os.path.split (路径)
# 返回值： 路径和文件名组成的元组
print(os.path.split(os.getcwd()+os.path.basename(sys.argv[0])))

# isdir() 检测是否是目录
# 格式 os.path.isdir(路径)
# 返回值 布尔值
rst = os.path.isdir(os.getcwd())
print(rst)
print(os.path.isdir(sys.argv[0]))

# exists() 检测文件或者目录是否存在
# 格式 os.path.exists（路径）
# 返回值 布尔值
e = os.path.exists(os.getcwd())
print(e)
print(os.path.exists("F:\\"))

# shutil 模块
# 格式 shutil.copy(来源路径，目标路径)
# 返回值 返回目标路径
# 拷贝的同时 可以给文件重命名
import shutil
'''rst = shutil.copy("e:\\pycharm.txt","d:\\pycharmmmm.txt")
print(rst)'''

#copy2() 复制文件 保留原数据（文件信息）
# 格式 shutil.copy2（来源路径，目标路径）
# 返回值： 返回目标路径
# 注意 copy和copy2的唯一区别在于copy2复制文件时尽量保留原数据

# copyfile() 将一个文件中的内容复制到另外一个文件当中
# 格式 shutil.copyfile（源路径，目标路径）
# 返回值  无
'''rst = shutil.copyfile("e:\\工作\SQL.txt","d:\\pycharmmmm.txt")
print(rst)'''

# move 移动文件/文件夹
# 格式 shutil.move(源路径，目标路径)
# 返回值 目标路径
'''rst = shutil.move("e:\\pycharm.txt","d:\\")
print(rst)'''

# 归档和压缩
# make_archive() 归档操作
# 格式shutil.make_archive('归档后的目录和文件名','后缀','需要归档的文件夹')
# 返回值 归档之后的地址

# 是想得到一个叫做leo.zip 的归档文件
'''rst = shutil.make_archive("d:\leo","zip","d:\按键精灵9")
print(rst)'''

# unpack_archive() 解包
# 格式 shutil.unpack_archive("归档文件地址","解包之后的地址")
# 返回值 解包后的地址
import  zipfile

# 创建一个zipfile对象 表示一个zip文件 参数file表示文件的路径或者类文件对象
zf = zipfile.ZipFile("d:\leo.zip")

# ZipFile.getinfo(name)
# 获取zip文档内指定文件的信息 返回一个zipfile.zipinfo对象 它包括文件的详细信息
rst = zf.getinfo("qmacro.ini") #不可以是zip里子文件夹里的 要在根目录
print(rst)

# zipfile.namelist()
# 获取zip文档内所有文件的名称列表
nl = zf.namelist()
for i in nl:
    if '.bak' in i:
        print(i)

# zipfile.extractall([path[,members[,pwd]]])
# 解压zip文档中的所有文件到当前目录 参数members的默认值为zip文档内的所有文件名称

''' rst = zf.extractall("e:\\ajjl9") '''

# random
# 格式 random.random()
# 返回值 随机0-1之间的小数
import random
rm = random.random()
print(rm)
print(int(rm*100))

#random.randrange
#参数：
     #start -- 指定范围内的开始值，包含在范围内
     #stop -- 指定范围内的结束值，不包含在范围内。
     #step -- 指定递增基数
rm1 = random.randrange(1,101)
print(rm1)

# random.randint
#参数：
     #x -- 指定范围内的开始值，包含在范围内
     #y -- 指定范围内的结束值，包含在范围内。
rm2 = random.randint(1,100)
print(rm2)

# choice() 随机返回序列中的某个值
# 格式 random.choice(序列)
# 返回值 序列中的某个值
l = [str(i)+" leo" for i in range(100,200)]
rst = random.choice(l)
print(rst)

# shuffle()  随机打乱列表
# 格式 random.shuffle(列表)
# 返回值 打乱顺序之后的列表
l1 = [i for i in range(10)]
print(l1)

random.shuffle(l1)
print(l1)

