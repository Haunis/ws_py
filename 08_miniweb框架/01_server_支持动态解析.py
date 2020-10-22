"""
本demo以多进程服务器为基础进行修改,在其基础上增加了动态解析的功能

所谓的支持动态解析就是client请求同一个特殊文件,如xx.py,server要实时更新内容进行回复
"""
import socket
import os
import re
import multiprocessing
from multiprocessing import Pool
import time
import mini_frame


class WSGIServer(object):
    def __init__(self):
        self.pool = Pool(3)
        # 1.创建socket
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 可重用端口;防止server先关闭后,再重启无法重用端口(如果server先调用close就要等2ms--大概2~5min)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 2.绑定ip和端口
        self.tcp_server_socket.bind(("", 8888))  # 参数传元组，ip为空表示绑定本机任意一个ip
        # 3.设置套接字为被动套接字
        self.tcp_server_socket.listen(128)

    def handle_msg(self, client_socket):
        print("handle_msg: pid=%d recv ...... " % os.getpid())
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

            if file.endswith(".py"):  # 回复动态请求
                self.response_dynamic(file, client_socket)
            else:
                self.response_static(file, client_socket)
        else:  # client套接字调用close()，开始四次挥手
            print("client 调用close")
        # time.sleep(10)
        client_socket.close()  # 短链接，每次发送完数据服务器主动断开

    def response_static(self, file, client_socket):
        response = "HTTP/1.1 200 OK\r\n\r\n"  # 应答头和应答体之间空一行;为了兼容windows换行用\r\n表示
        client_socket.send(response.encode("utf-8"))  # 可以先回复头,在socket.close()之前再回复body
        if len(file) == 0 or not os.path.isfile("./html/" + file):
            body = "<h1>No Such File: " + file + "</h1>"
            client_socket.send(body.encode("utf-8"))  # 回复body
            print("send ====>", body)
        else:
            with open("./html/" + file, "rb") as f:
                content = f.read()
                client_socket.send(content)  # 回复body
            print("send ====>%s to client" % file)

    def response_dynamic(self, file, client_socket):
        res_header = "HTTP/1.1 200 OK\r\n\r\n"  # 应答头和应答体之间空一行;为了兼容windows换行用\r\n表示
        client_socket.send(res_header.encode("utf-8"))  # 可以先回复头,在socket.close()之前再回复body

        body = mini_frame.main(file)
        client_socket.send(body.encode("utf-8"))

    def run(self):
        while True:
            print("accept......")
            new_client_socket, client_address = self.tcp_server_socket.accept()  # 阻塞;accept()返回元组，且client_address也是元组
            print("new client come: ", client_address)

            # 5.通信
            # 使用进程池;使用进程池不用关闭主进程new_client_socket..
            # pool.apply_async(handle_msg, (new_client_socket,))

            p = multiprocessing.Process(target=self.handle_msg, args=(new_client_socket,))
            p.start()
            # # 主进程和子进程的new_client_socket指向同一个fd
            # # 先将主进程的new_client_socket关了,子进程关闭new_client_socket后,fd才会关闭;否则四次挥手失败,浏览器会一直在等
            new_client_socket.close()
        # 6.关闭
        self.tcp_server_socket.close()


def main():
    server = WSGIServer()
    server.run()


if __name__ == "__main__":
    main()
