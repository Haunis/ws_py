# -*-coding:utf-8-*-
"""
非阻塞socket
http1.0使用短链接
http1.1使用长链接

短链接和长链接的区别：
短链接：浏览器每次请求成功后，关闭套接字
长链接：浏览器请求成功后不关闭套接字，再次使用该套接字请求数据，直到不再需要请求为止，此时再关闭套接字

长链接如何让浏览器知道数据已经发送完?
server在response header中的Content-Length：xxx写如body长度，这样浏览器受到后就知道要收的数据长度，就不会一直在等待
"""
import re
import socket
import time
import os

g_client_socket_list = list()

g_count = 0;


def send_msg_to_client(client_socket, receive):
    global g_count
    g_count += 1
    regex = r"[^/]+/([^\s]*)"  # 开始匹配所有非"/"字符,,匹配到非空字符结束
    file = re.match(regex, receive).group(1)  # GET /abc.html
    print("receive file====>%s<===" % file)

    if len(file) == 0 or not os.path.isfile("./html/" + file):  # 判断文件是否存在
        # response_body = "<h1>No Such File " + str(g_count) + "</h1>"
        # response_header = "HTTP/1.1 200 OK\r\n";
        # response_header += "Content-Length:%d\r\n" % len(response_body)  # 告诉客户端此body有多长
        # response_header += "\r\n"
        # response = response_header + response_body
        # client_socket.send(response.encode("utf-8"))
        # print("send ====>", response_body)

        # 也可以将body分两次发
        # 第一次发送
        response_body = "<h1>No Such File " + str(g_count) + "</h1>"
        response_header = "HTTP/1.1 200 OK\r\n";
        response_header += "Content-Length:%d\r\n" % len(response_body)  # 告诉客户端此body有多长
        response_header += "\r\n"
        response = response_header + response_body[0:3]
        client_socket.send(response.encode("utf-8"))
        print("send ====>", response_body[0:3])
        time.sleep(3)
        # 第二次发,只发body
        client_socket.send(response_body[3:].encode("utf-8"))
        print("send ====>", response_body[3:])
    else:
        with open("./html/" + file, "rb") as f:
            response_body = f.read()  # 字节类型
            response_header = "HTTP/1.1 200 OK\r\n";
            response_header += "Content-Length:%d\r\n" % len(response_body)  # 告诉客户端，此body有多长
            response_header += "\r\n"
            response = response_header.encode("utf-8") + response_body
            client_socket.send(response)
            print("send ====>%s to client" % file)


def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 设置2msl期间资源可重用
    tcp_server_socket.setblocking(False)  # 设置非阻塞
    # 2.绑定端口
    tcp_server_socket.bind(("", 8888))
    # 3.设置监听,变为被动套接字
    tcp_server_socket.listen(128)

    while True:
        try:
            # 4.链接
            new_client_socket, client_addr = tcp_server_socket.accept()
        except Exception as e:
            print("no client ... ")
        else:
            print("new client come :", client_addr)
            new_client_socket.setblocking(False)  # 与client通信的socket也设置成非阻塞
            g_client_socket_list.append(new_client_socket)

        # 5.收发数据
        for client_socket in g_client_socket_list:
            try:
                # GET /linux.html HTTP1.1/
                # 客户端发送的数据先发到server端的操作系统，recv再从操作系统取
                # 如果客户端发得太快，server取得太慢就可能导致server端卡死
                receive = client_socket.recv(1024).decode("utf-8")
            except Exception as e:
                print("no receive...", e)
            else:
                if receive:
                    send_msg_to_client(client_socket, receive)
                else:  # client调用close,导致server收到none
                    print("receive none:", receive)
                    client_socket.close()
                    g_client_socket_list.remove(client_socket)  # 使用close()的socket会抛出bad file descriptor异常

        time.sleep(3)


if __name__ == "__main__":
    main()
