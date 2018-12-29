import threading
from datetime import  datetime
import queue
sum = 0
loopsum = 1000000

lock = threading.Lock()

def myadd():
    global sum,loopsum
    for i in range(1, loopsum):
        # 上锁 获得锁
        lock.acquire()
        sum += 1
        # 释放锁
        lock.release()

def myminu():
    global sum,loopsum
    for i in range(1,loopsum):
        lock.acquire()
        sum -= 1
        lock.release()

if __name__ == '__main__':
    print("Starting ......{0}".format(sum)," ",datetime.now())
    t1 = threading.Thread(target=myadd,args=())
    t2 = threading.Thread(target=myminu,args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done ......{0}".format(sum)," ",datetime.now())
