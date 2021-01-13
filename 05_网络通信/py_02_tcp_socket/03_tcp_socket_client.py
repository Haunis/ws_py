#! /usr/bin/python3

"""
全双工客户端：主线程发送，子线程接受
客户端可以不绑定端口
"""

import socket
import threading
import signal
import os


# ctrl+c时，改变loop为False
def handler(signum, frame):
    print("接受到了 ctrl c:", signum, frame)
    exit(0)


def recv_msg(tcp_socket):
    global g_exit
    while True:
        recv_data = tcp_socket.recv(1024)  # 阻塞
        if recv_data:  # 服务器有回数据
            print("type(recv_data): ", type(recv_data))
            print("recv_data: \n%s" % recv_data.decode("utf-8"))
        else:  # 服务器套接字调用close主动断开链接
            print("服务器调用close")
            tcp_socket.close()
            os.system("kill %d" % os.getpid())
            break


def main():
    signal.signal(signal.SIGINT, handler)  # 注册ctrl+c按键监听。。。本demo每用到该功能
    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.链接服务器
    server_ip = input("please input server ip:")
    server_port = int(input("please input server port:"))
    server_address = (server_ip, server_port)

    tcp_socket.connect(server_address)  # 面向链接的通信

    # 3.用自线程接受数据
    t = threading.Thread(target=recv_msg, args=(tcp_socket,))
    t.start()
    # 4.发送数据
    while True:
        send_data = input("请输入要发送的数据(exit--退出):")
        if send_data == "exit":
            tcp_socket.close()
            os.system("kill %d" % os.getpid())
            break
        else:
            tcp_socket.send(send_data.encode("utf-8"))
    # 4.关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()
