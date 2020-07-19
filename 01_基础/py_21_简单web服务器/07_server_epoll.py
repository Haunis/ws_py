"""
长链接

epoll:
    1.采用内存映射技术，应用程序和内和共享一块内存空间，省去操作系统内核态和用户态的字切换
        （像05，06例子里的应用程序轮询非阻塞socket recv是否有数据时，是向内核复制一份内存进行询问）
    2.当共享内存里的套接字变化时，内核直接通知应用程序，不用去轮询内存里的所有套接字

内存映射技术(mmap):应用程序和内核共用同一块内存

"""
import select
import socket
import time
import re
import os

fd_event_dict = dict()
g_count = 0


def send_msg_to_client(client_socket, receive):
    global g_count
    g_count += 1
    regex = r"[^/]+/([^\s]*)"  # 开始匹配所有非"/"字符,,匹配到非空字符结束
    file = re.match(regex, receive)  # GET /abc.html
    if file:  # 能匹配就匹配出文件
        file = file.group(1)
    else:
        file = ""
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
    epl = select.epoll()  # 获取epoll对象
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 设置2msl期间资源可重用
    tcp_server_socket.bind(("", 8888))  # 绑定和端口;ip为空表示本机任意一个ip(本机可能不止一个网卡)
    tcp_server_socket.listen(128)  # 设置监听，变为被动套接字
    tcp_server_socket.setblocking(False)  # 设置非阻塞

    tcp_socket_fd = tcp_server_socket.fileno()  # 获取套接字的文件描述符
    epl.register(tcp_socket_fd, select.EPOLLIN)  # 注册套接字的事件

    while True:
        print("start poll...")
        fd_event_list = epl.poll()  # 阻塞；如果epl注册的事件select.EPOLLIN有新事件就解诸塞
        for fd, event in fd_event_list:
            if fd == tcp_server_socket.fileno():  # 监听的tcp_server_socket有事件变动
                new_client_socket, client_addr = tcp_server_socket.accept()
                print("new client come:", client_addr)
                new_client_socket.setblocking(False)
                fd_event_dict[new_client_socket.fileno()] = new_client_socket  # 向字典存client套接字
                epl.register(new_client_socket.fileno(), select.EPOLLIN)  # 给客户端服务的套接字也注册
            elif event == select.EPOLLIN:  # 给客户端服务的套接字有变动
                client_socket = fd_event_dict[fd]  # 取出套接字
                receive = client_socket.recv(1024).decode("utf-8")
                if receive:
                    send_msg_to_client(client_socket, receive)
                else:  # 浏览器socket调用close()导致服务端socket收到为空
                    client_socket.close()
                    epl.unregister(fd)  # 取消注册
                    del client_socket  # 自字典删除


if __name__ == "__main__":
    main()
