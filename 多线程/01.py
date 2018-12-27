# 利用time函数 生成两个函数
# 顺序调用 计算总的运行时间

import  time,os,sys
from datetime import  datetime

def loop1():
    # ctime 得到当前时间
    print("start loop 1 at: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(4)
    print("end loop 1 at: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def loop2():
    # ctime 得到当前时间
    print("start loop 2 at: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(2)
    print("end loop 2 at: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def main():
    print("starting at: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    loop1()
    loop2()
    print("all done at: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    main()
    print(os.getcwd()+"\\"+os.path.basename(sys.argv[0]))