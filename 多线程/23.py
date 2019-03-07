import multiprocessing
from datetime import datetime
import time

def consumer(input_q):
    print("into consumer: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    while True:
        item = input_q.get()
        if item is None:
            break
        print("pull ",item," out of q")
    print("out of consumer: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def producer(sequence,output_q):
    print("into producer: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    for item in sequence:
        output_q.put(item)
        print("put ",item," into q")
    print("out of procuder: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    q = multiprocessing.Queue()
    cons_p = multiprocessing.Process(target=consumer,args=(q,))
    cons_p.start()

    sequence = [1,2,3,4]
    producer(sequence,q)

    q.put(None)
    cons_p.join()