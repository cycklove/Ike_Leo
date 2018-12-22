# 打开文件 用写的方式
# r表示后面字符串内容不需要转义
f = open(r"d:\sql.txt","w")
# 文件打开后必须关闭
f.close()

# 此案例说明 以写方式打开文件 默认是如果没有则创建 注意 如果有会覆盖掉文件内容

# with语句案例
with open(r"d:\sql.txt","r") as f:
    pass
    # 下面语句块开始对文件f进行操作
    # 在本模块中不需要再使用close关闭文件f

# with案例
with open(r"d:\sql2.txt","r") as f:
    # 按行读取内容
    strline = f.readline()
    # 此结构保证能够完整读取文件直到结束
    while strline:
        print(strline)
        strline = f.readline()

# list能用打开的文件作为参数 把文件内每一行内容作为一个元素
with open(r"d:\sql2.txt","r") as f:
    # 以打开的文件f作为参数 创建列表
    l = list(f)
    le = 0
    for line in l:
        print(line)
        le += len(line)
    print(le)

# read是按字符读取文件内容
# 允许输入参数决定读取几个字符 如果没有指定 从当前文职读取到结尾
# 否则 从当前位置读取指定个数字符
with open(r"d:\sql2.txt", "r") as f:
    strchar = f.read()
    print(len(strchar))
    print(strchar)
    le = len(strchar)

# seek案例
# 打开文件后 从第5个字节处开始读取
# 打开读写指针在0处 即文件的开头
with open(r"d:\sql2.txt", "r") as f:
    # seek移动单位是字节
    f.seek(6,0)
    strchar = f.read()
    print(strchar)

# 关于读取文件的练习
# 打开文件 三个字符一组读取内容 然后显示在屏幕上
# 每读一次 休息一秒钟
# 让程序暂停 可以使用time下的sleep函数
import time
with open(r"d:\sql2.txt","r") as f:
    #read参数的单位是字符 可以理解成一个汉字就是一个字符
    strchar = f.read(3)
    while strchar:
        print(strchar)
        time.sleep(1)
        strchar = f.read(3)
