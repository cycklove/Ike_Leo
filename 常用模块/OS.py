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