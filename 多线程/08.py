import  time,os,sys
from datetime import  datetime
import _thread as thread
import  threading
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

def loop3():
    # ctime 得到当前时间
    print("start loop 3 at: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(5)
    print("end loop 3 at: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def main():
    print("Start at: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    t1 = threading.Thread(target=loop1,args=())
    t1.setName("THR 1")
    t1.start()

    print("Start at: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    t2 = threading.Thread(target=loop2, args=())
    t2.setName("THR 2")
    t2.start()

    print("Start at: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    t3 = threading.Thread(target=loop3, args=())
    t3.setName("THR 3")
    t3.start()

    time.sleep(3)

    for thr in threading.enumerate():
        print("正在运行的线程名字是：{0}".format(thr.getName()))

    print("正在运行的子线程数量为：{0}".format(threading.activeCount()))

    print("ALL done at: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)
        exit()