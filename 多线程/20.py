import  multiprocessing
import time
from datetime import datetime
import sys

class clockprocess(multiprocessing.Process):

     #两个函数比较重要
     #1 init构造函数
     #2 run

    def __init__(self,interval):
        super().__init__()
        self.interval = interval

    def run(self):
        while True:
            print("the time is " ,datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            time.sleep(self.interval)
            exit()

if __name__ == '__main__':
    p = clockprocess(3)
    p.start()


    while True:
        for i in range(1,4):
            time.sleep(1)
            print("int:",i)
        exit()
