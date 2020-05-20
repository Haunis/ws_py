#! /usr/bin/python3
import socket


def main():
    # 1.创建socket
    receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定端口：使用哪个端口接受数据
    local_address = ("", 7788)  # ip地址和端口；ip一般不写，表示任意一个ip
    receive_socket.bind(local_address)  # 申请绑定接口

    # 3.接受数据
    while True:
        receive_data = receive_socket.recvfrom(1024)  # 本次接收的最大字节，一般为1024
        # print("origin:%s" % str(receive_data))  # (b'dfsdf', ('192.168.1.11', 43325))

        print("msg:%s  , from:%s" % (receive_data[0].decode("utf-8"), str(receive_data[1])))
    # 4.关闭socket
    receive_socket.close()


if "__main__" == __name__:
    main()
