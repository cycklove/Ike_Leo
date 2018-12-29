import threading

sum = 0
loopsum = 1000000

def myadd():
    global sum,loopsum
    for i in range(1,loopsum):
        sum = sum+1

def myminu():
    global sum,loopsum
    for i in range(1,loopsum):
        sum = sum -1

if __name__ == '__main__':
    print("Starting ......{0}".format(sum))
    t1 = threading.Thread(target=myadd,args=())
    t2 = threading.Thread(target=myminu,args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done ......{0}".format(sum))