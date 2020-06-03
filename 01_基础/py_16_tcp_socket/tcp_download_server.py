#! /usr/bin/python3
import socket


def main():
    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定端口
    tcp_socket.bind(("", 8888))

    # 3.设置监听，让监听套接字由主动变为被动
    tcp_socket.listen(128)

    while True:
        # 4.等待客户端连接；客户端连接成功会产生一个新的套接字为客户端服务
        new_tcp_client_socket, client_address = tcp_socket.accept()  # 阻塞

        # 5.接收客户端请求下载的文件名
        file_name = new_tcp_client_socket.recv(1024).decode("utf-8")  # 一次接收的最大字节数
        print("file_name: %s" % file_name)

        # 6.打开文件并发送文件内容
        file_content = None
        try:
            f = open(file_name, "rb")
            file_content = f.read()
            f.close()
        except Exception as e:
            print("无下载文件:%s" % str(e))
        if file_content:
            new_tcp_client_socket.send(file_content)

        # 关闭套接字
        new_tcp_client_socket.close()
    tcp_socket.close()


if __name__ == "__main__":
    main()
