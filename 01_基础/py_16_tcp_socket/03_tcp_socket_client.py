#! /usr/bin/python3

import socket


def main():
    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.链接服务器
    server_ip = input("please input server ip:")
    server_port = int(input("please input server port:"))
    server_address = (server_ip, server_port)
    tcp_socket.connect(server_address)
    # 3.发送数据
    while True:
        send_data = input("请输入要发送的数据(0-exit):")
        if send_data == "exit":
            break
        else:
            # TCP使用send()，而UDP使用sendto()
            tcp_socket.send(send_data.encode("utf-8"))

            recv_data = tcp_socket.recv(1024)
            print(type(recv_data))
            print("recv_data:%s" % recv_data.decode("utf-8"))
    # 4.关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()
