import  time,os,sys
from datetime import  datetime
import _thread as thread
import  threading
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
    # 生成threading.Thread实例
    t1 = threading.Thread(target=loop1,args=("刘华强",))
    t1.start()
    t2 = threading.Thread(target=loop2,args=("韩跃平","王大鹏"))
    t2.start()
    print("all done at: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    main()
    while True:
        time.sleep(5)
        exit()