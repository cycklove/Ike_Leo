# 利用time函数 生成两个函数
# 顺序调用 计算总的运行时间

import  time,os,sys
from datetime import  datetime
import _thread as thread
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
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程函数为start_new_thread
    # 参数两个 一个是需要运行的函数名 第二是函数的参数作为元祖使用 为空则使用空元祖
    # 注意 如果函数只有一个参数 需要参数后有一个逗号
    thread.start_new_thread(loop1,())
    thread.start_new_thread(loop2,())
    print("all done at: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    main()
    while True:
        time.sleep(4)
        exit()
    # print(os.getcwd()+"\\"+os.path.basename(sys.argv[0]))