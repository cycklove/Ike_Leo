import threading
import time
from datetime import  datetime
loop = [4,2]

class ThreadFunc:
    def __init__(self,name):
        self.name = name

    def loop(self,nloop,nsec):
        print("Start loop", nloop," at ",datetime.now())
        time.sleep(nsec)
        print("Done loop", nloop, " at ", datetime.now())

def main():
    print("Start at: ",datetime.now())

    t = ThreadFunc("loop")
    t1 = threading.Thread(target=t.loop,args=("LOOP1",4))
    t2 = threading.Thread(target= ThreadFunc("loop").loop,args=("LOOP2",2))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("ALL done at: ",datetime.now())

if __name__ == '__main__':
    main()