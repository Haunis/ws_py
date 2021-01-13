"""
短链接
使用多线程回复浏览器
"""
import socket
import os
import re
import threading

g_count = 0;


def handle_msg(client_socket):
    global g_count
    g_count += 1
    print("recv......")
    receive_data = client_socket.recv(1024)  # 阻塞;收到的是bytes类型
    # print("type(receive_data):", type(receive_data))
    # print("receive_data:\n%s" % receive_data.decode("utf-8"))
    result_str = receive_data.decode("utf-8")  # 转成string

    if result_str:
        # 第一行一般是:GET /a.html HTTP/1.1
        # regex = r".*/(.*)\sHTTP/" #任意字符开头,匹配到/,再匹配到 HTTP/结束
        # regex = r"[^/]+.*\s" #开始匹配所有非"/"字符,匹配到有空格结束
        regex = r"[^/]+/([^\s]*)"  # 开始匹配所有非"/"字符,,匹配到非空字符结束
        file = re.match(regex, result_str)  # GET /abc.html
        if file:
            file = file.group(1)
            print("receive file====>%s<===" % file)
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
    else:  # 客户端套接字调用close(),所有服务端受到为空
        print("client 调用 close:")
    client_socket.close()  # 服务完一次就关闭，短链接


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
        print("accept ......")
        new_client_socket, client_address = tcp_server_socket.accept()  # 阻塞;accept()返回元组，且client_address也是元组
        print("new client come: ", client_address)
        # 5.通信
        t = threading.Thread(target=handle_msg, args=(new_client_socket,))
        t.start()
    # 6.关闭
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
