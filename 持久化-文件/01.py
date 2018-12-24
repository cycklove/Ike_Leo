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
    strchar = f.read(3)
    # tell函数  用来显示文件读写指针的当前位置
    pos = f.tell()
    while strchar:
        print(strchar.replace("\r","").replace("\n","").strip())
        print(pos)
        time.sleep(0.1)
        strchar = f.read(3)
        pos = f.tell()

# 结果说明
# tell的返回数字的单位是byte
# read是以字符为单位

# write 案例
# 向文件追加一句诗
# a代表追加方式打开
with open(r"d:\sql2.txt",mode="r") as f:
    if "生活不止眼前的苟且" in f.read():
        print("字符串已经存在，不追加写入")
    else:
        with open(r"d:\sql2.txt", mode="a") as g:
            str = g.write("\n生活不止眼前的苟且 \n还有诗和远方")
            # 可以直接写入行 用writelines 参数可以是list格式
            # l = ["i","love","yh"]
            # g.用writelines(l)
            print("追加写入成功")
    with open(r"d:\sql2.txt", mode="r") as h:
        nr = h.read()
        print(nr)

# 序列化案例
import pickle
age = 19
name = "Ike_Leo"
with open(r"d:\sql3.txt", "wb") as f:
    pickle.dump(age,f)
with open(r"d:\sql3.txt", "ab") as f:
    pickle.dump(name,f)
# 反序列化案例
with open(r"d:\sql3.txt", "rb") as f:
    age = pickle.load(f)
    name = pickle.load(f)
    print(age,name)

a = [19,"lke","ike leo yh",[172,62]]
with open(r"d:\sql3.txt", "wb") as f:
    pickle.dump(a,f)
with open(r"d:\sql3.txt", "rb") as f:
    a = pickle.load(f)
    print(a)

# shelve创建文件并使用
import shelve
# 打开文件
# shv相当于一个字典
shv = shelve.open(r"d:\sql4.txt")
shv['one'] = 1
shv['two'] = 2
shv['three'] = 3
shv['four'] = {"one":1,"two":2,"three":3}

shv.close()
# 通过以上案例发现 shelve自动创建的不仅仅是一个sql4.txt 还包括其他格式文件

# shelve读取案例
shv = shelve.open(r"d:\sql4.txt")
try:
    print(shv['one'])
    print(shv['three'])
except Exception as e:
    print(repr(e))
finally:
    shv.close()

# shelve忘记写回 需要使用强制写回
shv = shelve.open(r"d:\sql4.txt",writeback=True)
try:
    k1 = shv["four"]
    print(k1)
    #此时 一旦shelve关闭 则内容还是存在于内存中 没有写回数据库
    k1["one"] = 100
except Exception as e:
    print(repr(e))
finally:
    shv.close()

shv = shelve.open(r"d:\sql4.txt")
try:
   k1 = shv["four"]
   print(k1)
finally:
    shv.close()

# shelve 使用with管理上下文环境
with shelve.open(r"d:\sql4.txt",writeback=True) as shv:
    k1 = shv["four"]
    print(k1)
    k1["one"] = 1000

with shelve.open(r"d:\sql4.txt") as shv:
    print(shv["four"])