import  time,os,sys
from datetime import  datetime
import _thread as thread
def loop1(in1):
    # ctime 得到当前时间
    print("start loop 1 at: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("我是参数 ",in1)
    time.sleep(4)
    print("end loop 1 at: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def loop2(in1,in2):
    # ctime 得到当前时间
    print("start loop 2 at: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("我是参数 ",in1 ,"和参数 ",in2)
    time.sleep(2)
    print("end loop 2 at: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def main():
    print("starting at: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程函数为start_new_thread
    # 参数两个 一个是需要运行的函数名 第二是函数的参数作为元祖使用 为空则使用空元祖
    # 注意 如果函数只有一个参数 需要参数后有一个逗号
    thread.start_new_thread(loop1,("刘华强",))
    thread.start_new_thread(loop2,("王大鹏","韩跃平"))
    print("all done at: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    main()
    while True:
        time.sleep(5)
        exit()