import threading
import time
import  datetime

class Mythread(threading.Thread):
    def __init__(self,arg):
        super(Mythread,self).__init__()
        self.arg = arg

    def run(self):
        time.sleep(2)
        print("the args for this class is {0} ".format(self.arg))

for i in range(5):
    t = Mythread(i)
    t.start()
    t.join()

print("Main thread is done !!!")