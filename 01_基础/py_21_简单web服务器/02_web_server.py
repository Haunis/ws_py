"""
最简单的服务器
    使用浏览器访问： 192.168.xx.xx:8888 本机访问的话：127.0.0.1
    http协议基于tcp协议
"""
import socket
import gevent
from gevent import monkey

monkey.patch_all()
g_count = 0;


def handle_msg(client_socket):
    global g_count
    g_count += 1
    # while True:
    try:
        print("--------waiting recv-----------")
        receive_data = client_socket.recv(1024)  # 阻塞
        print("type(receive_data):", type(receive_data))
        print("receive_data:\n%s" % receive_data.decode("utf-8"))
        # 应答头和应答体之间空一行
        client_socket.send(("HTTP/1.1 200 OK\n\n<h1>hello" + str(g_count) + "</h1>").encode("utf-8"))
    except Exception as e:
        print("end<====================== ")
            # break
    # client_socket.close()


def main():
    # 1.创建socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定ip和端口
    tcp_server_socket.bind(("", 8888))  # 参数传元组，ip为空表示绑定本机任意一个ip

    # 3.设置套接字为被动套接字
    tcp_server_socket.listen(128)

    # 4.等待客户端链接
    while True:
        print("------waiting accept--------")
        new_client_socket, client_address = tcp_server_socket.accept()  # accept()返回元组，且client_address也是元组
        print("------finish accept--------", client_address)

        # 5.通信
        gevent.joinall([gevent.spawn(handle_msg, new_client_socket)])

    # 6.关闭
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
