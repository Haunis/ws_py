"""
短链接
根据浏览器的请求回复对应的html文件
使用多进程或进程池

主进程在创建子进程时,子进程会拷贝父进程的所有资源(全局变量,局部变量,代码等)
所以new_client_socket主进程和子进程都有一份,但是这两份socket指向同一个文件描述符
必须这两个socket都调用close之后,才会有tcp的四次挥手,否则浏览器会一直在等待

在Linux中一切设备皆文件
fd:标记文件;就是一个数字,对应一个特殊的文件,如网络接口等等
标记和浏览器通信的套接字socket也是文件

任何一个进程在新起时都会打开三个文件:键盘,显示器,错误输出
函数里调用print(),实际上是向显示器文件write
"""
import socket
import os
import re
import multiprocessing
from multiprocessing import Pool
import time

g_count = 0;


def handle_msg(client_socket):
    global g_count
    g_count += 1
    print("pid:%d recv ...... " % os.getpid())
    receive_data = client_socket.recv(1024)  # 阻塞;收到的是bytes类型
    # print("type(receive_data):", type(receive_data))
    # print("receive_data:\n%s" % receive_data.decode("utf-8"))
    result_str = receive_data.decode("utf-8")  # 转成string

    if result_str:  # 客户端有发来非空数据
        # 第一行一般是:GET /a.html HTTP/1.1
        # regex = r".*/(.*)\sHTTP/" #任意字符开头,匹配到/,再匹配到 HTTP/结束
        # regex = r"[^/]+.*\s" #开始匹配所有非"/"字符,匹配到有空格结束
        regex = r"[^/]+/([^\s]*)"  # 开始匹配所有非"/"字符,,匹配到非空字符结束
        file = re.match(regex, result_str)  # GET /abc.html
        if file:
            file = file.group(1)  # 取出文件名
            print("receive file====>%s<===浏览器请求" % file)
        else:
            print("receive ====>%s<===非浏览器请求" % file)
            file = ""

        response = "HTTP/1.1 200 OK\r\n\r\n"  # 应答头和应答体之间空一行;为了兼容windows换行用\r\n表示
        client_socket.send(response.encode("utf-8"))  # 可以先回复头,在socket.close()之前再回复body
        if len(file) == 0 or not os.path.isfile("./html/" + file):
            body = "<h1>No Such File " + str(g_count) + "</h1>"
            client_socket.send(body.encode("utf-8"))  # 回复body
            print("send ====>", body)
        else:
            with open("./html/" + file, "rb") as f:
                content = f.read()
                client_socket.send(content)  # 回复body
            print("send ====>%s to client" % file)
    else:  # client套接字调用close()，开始四次挥手
        print("client 调用close")
    # time.sleep(10)
    client_socket.close()  # 短链接，每次发送完数据服务器主动断开


def main():
    pool = Pool(3)
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
        print("accept......")
        new_client_socket, client_address = tcp_server_socket.accept()  # 阻塞;accept()返回元组，且client_address也是元组
        print("new client come: ", client_address)

        # 5.通信
        # 使用进程池;使用进程池不用关闭主进程new_client_socket..
        # pool.apply_async(handle_msg, (new_client_socket,))

        p = multiprocessing.Process(target=handle_msg, args=(new_client_socket,))
        p.start()
        # # 主进程和子进程的new_client_socket指向同一个fd
        # # 先将主进程的new_client_socket关了,子进程关闭new_client_socket后,fd才会关闭;否则四次挥手失败,浏览器会一直在等
        new_client_socket.close()
    # 6.关闭
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
