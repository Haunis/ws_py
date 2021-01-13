#! /usr/bin/python3
"""
本demo以多进程服务器为基础进行修改,在其基础上增加了动态解析的功能

所谓的支持动态解析就是client请求同一个特殊文件,如xx.py,server要实时更新内容进行回复

支持WSGI协议:向应用程序框架mini_frame传入一个函数,mini_frame通过该函数回调传回http协议的header
mini_frame的application返回body

该文件作为web服务器

"""
import socket
import os
import re
import multiprocessing
from multiprocessing import Pool
import sys

sys.path.append("../")  # 将当前目录的上级目录添加到系统目录，否则无法导入LogUtils

import time
import dynamic.mini_frame as mini_frame  # 需要指定一个变量mini_frame来接受不能直接使用
import LogUtils
import re


class WSGIServer(object):
    def __init__(self, port, app, static_path):
        self.pool = Pool(3)
        # 1.创建socket
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 可重用端口;防止server先关闭后,再重启无法重用端口(如果server先调用close就要等2ms--大概2~5min)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 2.绑定ip和端口
        self.tcp_server_socket.bind(("", port))  # 参数传元组，ip为空表示绑定本机任意一个ip
        # 3.设置套接字为被动套接字
        self.tcp_server_socket.listen(128)

        self.application = app  # 要调用指定的框架
        self.static_path = static_path  # 静态资源所在路径

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
            file = re.match(regex, result_str)  # GET /abc.html 返回Match
            if file:
                file = file.group(1)  # 取出文件名
                LogUtils.i("receive file====>%s<===浏览器请求" % file)
            else:
                file = ""  # 为空，默认请求主页
                LogUtils.w("receive ====>%s<===非浏览器请求" % file)  # 比如socket直接链接

            if file.endswith(".py") or len(file) == 0:  # 回复动态请求
                self.response_dynamic(file, client_socket)
            else:
                self.response_static(file, client_socket)
        else:  # client套接字调用close()，开始四次挥手
            print("client 调用close")
        # time.sleep(10)
        client_socket.close()  # 短链接，每次发送完数据服务器主动断开

    def response_static(self, file, client_socket):  # file 以html结尾
        response = "HTTP/1.1 200 OK\r\n\r\n"  # 应答头和应答体之间空一行;为了兼容windows换行用\r\n表示
        client_socket.send(response.encode("utf-8"))  # 可以先回复头,在socket.close()之前再回复body
        try:
            with open(self.static_path + "/" + file, "rb") as f:
                body = f.read()
                LogUtils.d("send ====>%s to client" % file)
        except FileNotFoundError as e:
            body = "<h1>No Such File: " + file + "</h1>"
            body = body.encode("utf-8")  # 要转换为二进制才可发出去
            LogUtils.e("无此文件%s, send ====>%s" % (file, body))
        client_socket.send(body)  # 回复body

    def response_dynamic(self, file, client_socket):
        temp_dict = dict()
        temp_dict['FILE_PATH'] = file
        # body = mini_frame.application(temp_dict, self.start_response)  # 向应用框架mimi_frame传入函数start_response
        body = self.application(temp_dict, self.start_response)  # 向应用框架mimi_frame传入函数start_response

        res_header = "HTTP/1.1 %s\r\n" % self.status
        for line in self.header_line:  # 每一个line都是元组
            res_header += '%s:%s\r\n' % (line[0], line[1])
        res_header += '\r\n'
        print("res_header:")
        print(res_header)

        client_socket.send(res_header.encode("utf-8"))  # 可以先回复头,在socket.close()之前再回复body
        client_socket.send(body.encode("utf-8"))

    def start_response(self, status, header_line):  # mini_frame应用框架通过该方法回传header
        self.status = status
        self.header_line = [('server', 'mini web 1.0')]
        self.header_line = self.header_line + header_line

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
    li = sys.argv
    LogUtils.d(li)
    if len(li) < 3:
        LogUtils.e("请指定端口和框架，按该方式运行：python3 server_返回模板数据.py 8888 mini_frame:application")
        return
    try:
        port = int(li[1])
        frame_app = re.match(r"([^:]+):(.*)", li[2])
        frame = frame_app.group(1)
        app = frame_app.group(2)
        LogUtils.d("port:%s, frame:%s, app:%s" % (port, frame, app))
    except Exception as e:
        LogUtils.e(e)
        LogUtils.e("请指定端口和框架，按该方式运行： python3 server_返回模板数据.py 8888 mini_frame:application")
        return

    with open("server.conf") as f:
        di = eval(f.read())  # 将字符串转化为表达式
        static_path = di['static_path']
        dynamic_path = di['dynamic_path']
        sys.path.append(dynamic_path)  # 加入到搜索路径方可导入框架模块
    # import frame #会导入frame模块
    frame = __import__(frame)
    app = getattr(frame, app)
    server = WSGIServer(port, app, static_path)
    server.run()


if __name__ == "__main__":
    main()
