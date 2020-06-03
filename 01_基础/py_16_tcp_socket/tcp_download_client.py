#! /usr/bin/python3
import socket


def main():
    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.获取服务器ip port
    dest_ip = input("请输入服务器ip:")
    dest_port = int(input("请输入服务器port:"))

    # 3.链接服务器
    server_address = (dest_ip, dest_port)
    tcp_socket.connect(server_address)

    # 4.获取下载文件的文件名
    file_name = input("请输入要下载的文件名:")

    # 5.将文件名发送到服务器
    tcp_socket.send(file_name.encode("utf-8"))

    # 6.接收文件中的数据
    recv_data = tcp_socket.recv(1024)  # 1K大小

    # 7.将接收到的数据保存到文件中
    if recv_data:
        with open("download" + file_name, "wb") as f:
            f.write(recv_data)
    else:
        print("服务器无此文件")

    # 8.关闭套接字
    tcp_socket.close()


if "__main__" == __name__:
    main()
