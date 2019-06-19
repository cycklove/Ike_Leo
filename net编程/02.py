'''
  1.建立通信的socket
  2.发送内容到指定服务器
3.接受服务器给定的反馈内容
'''


import socket

def clentFunc():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    text = "i love yh"

    # 发送数据必须bytes格式
    data = text.encode()
    # 发送
    sock.sendto(data,("127.0.0.1",7852))

    data,addr = sock.recvfrom(200)

    data = data.decode()

    print(data)

if __name__ == '__main__':
    clentFunc()
