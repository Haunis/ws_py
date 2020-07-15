"""
根据浏览器的请求回复对应的html文件
"""
import socket
import gevent
import os
from gevent import monkey
import re

monkey.patch_all()
g_count = 0;


def handle_msg(client_socket):
    global g_count
    g_count += 1
    # while True:
    try:
        print("********waiting recv************")
        receive_data = client_socket.recv(1024)  # 阻塞;收到的是bytes类型
        # print("type(receive_data):", type(receive_data))
        # print("receive_data:\n%s" % receive_data.decode("utf-8"))
        result_str = receive_data.decode("utf-8")  # 转成string
        print("********finish recv************")

        file = re.match(r".*/(.*)\sHTTP/", result_str).group(1)

        response = "HTTP/1.1 200 OK\r\n\r\n"  # 应答头和应答体之间空一行;为了兼容windows换行用\r\n表示
        client_socket.send(response.encode("utf-8"))  # 可以先回复头
        if len(file) == 0 or not os.path.isfile("./html/" + file):
            print("file is empty")
            body = "<h1>No Such File " + str(g_count) + "</h1>"
            client_socket.send(body.encode("utf-8"))  # 可以先回复头
        else:
            print("file====>", file)
            with open("./html/" + file, "rb") as f:
                content = f.read()
                client_socket.send(content)

    except Exception as e:
        print("==========handle_msg end============ ")
        # break
    client_socket.close()


def main():
    # 1.创建socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 可重用端口;防止server先关闭后,再重启无法重用端口
    # server先调用close就要等2ms--大概2~5min
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2.绑定ip和端口
    tcp_server_socket.bind(("", 8888))  # 参数传元组，ip为空表示绑定本机任意一个ip

    # 3.设置套接字为被动套接字
    tcp_server_socket.listen(128)

    # 4.等待客户端链接
    while True:
        print("------waiting accept--------")
        new_client_socket, client_address = tcp_server_socket.accept()  # 阻塞;accept()返回元组，且client_address也是元组
        print("------finish accept---------", client_address)

        # 5.通信
        gevent.joinall([gevent.spawn(handle_msg, new_client_socket)])

    # 6.关闭
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
