'''
 - server端流程
        1.建立socket socket是负责具体通信的一个实例
        2.绑定 为创建的socket指派固定的端口和IP地址
        3.接受对方发送内容
        4.给对方发送反馈 此步骤为非必须步骤
'''
import socket

def serverfunc():
    # 1.建立socket
    # socket.AF_INET使用IPC4协议族  socket.SOCK_DGRAM使用UDP通信
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 2.绑定 为创建的socket指派固定的端口和IP地址
    # 127.0.0.1 本机
    # 7852 随便指定的端口号
    # 地址是一个tuple类型（ip,port）
    addr = ("127.0.0.1",7582)
    sock.bind(addr)
    # 3.接受对方发送内容
    # recvfrom
    data,addr = sock.recvfrom(500)

    print(data)
    print(type(data))
    # 发送过来的数据是bytes格式 必须通过解码才能得到str格式内容
    text = data.decode()
    print(type(text))
    print(text)

    # 给对方返回的消息
    rsp = "wo bu e"

    # 发送的数据需要编码成bytes格式
    data = rsp.encode()
    sock.sendto(data,addr)

if __name__ == '__main__':
    print("starting server ......")
    serverfunc()
    print("ending server ......")