import multiprocessing
import time
from datetime import datetime

def consumer(input_q):
    print("into consumer: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    while True:
        # 处理项
        item = input_q.get()
        print ("pull",item,"out if q") #此处替换为有用的工作
        input_q.task_done() # 发出信号通知任务完成
    print("out of consumer: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def producer(sequence,output_q):
    print("into producer: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    for item in sequence:
        output_q.put(item)
        print("put ",item," into q")
    print("out of producer: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    # 运行消费者进程
    cons_p = multiprocessing.Process(target=consumer,args=(q,))
    cons_p.daemon=True
    cons_p.start()
    # 生产多个项 sequence代表要发送给消费者的项序列
    # 在实践中 这可能是生成器的输出或通过一些其他方式生产出来
    sequence = [1,2,3,4]
    producer(sequence,q)
    # 等待所有项被处理
    q.join()