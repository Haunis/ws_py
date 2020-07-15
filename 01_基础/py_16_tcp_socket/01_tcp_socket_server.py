#! /usr/bin/python3
"""
处理一次客户端交互就关闭
也可以接收浏览器的请求,http协议是基于tcp协议的
"""
import socket


def main():
    # 1.创建监听套接字
    # 监听套接字负责等待新的客户端进行链接（电话局总机）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # 2.绑定端口；服务器需要绑定端口
    local_address = ("", 8888)  # ip不写，表示本机任意一个ip
    tcp_server_socket.bind(local_address)

    # 3.设置监听，让监听套接字由主动变为被动;如果不做，只能链接别人，不能让别人链接你;
    # 参数128可简单理解为并发数，但是分操作系统，写成256，写成10...没啥区别，这个值的大小几乎不会影响同一时刻客户端的多少，最终由操作系统决定
    tcp_server_socket.listen(128)

    # 4.等待客户端链接;accept产生的新的套接字负责为客户端服务(收发数据,理解为具体的人工服务),这个套接字标记客户端
    print("---------begain accept-----------")
    new_tcp_client_socket, client_address = tcp_server_socket.accept()  # <<<<<阻塞>>>>>;client_address是元组;客户端调用connect(）会解阻塞

    print("client_address:%s" % str(client_address))
    print("---------end accept-----------")

    # 5.收发数据
    # 阻塞:设置接收的最大字节，receive_data是bytes类型;
    # 何时解阻塞：1.收到消息 2.客户端调用close
    receive_data = new_tcp_client_socket.recv(1024)
    print(type(receive_data))
    print("receive_data:%s" % receive_data.decode("utf-8"))
    #new_tcp_client_socket.send("数据已收到".encode("utf-8"))
    #第一行是应答头，空一行，后面是应答body;使用浏览器可以直接访问：127.0.0.1:8888/a/b/c.html
    new_tcp_client_socket.send("HTTP/1.1 200 OK\n\n<h1>hhhahh</h1>".encode("utf-8"))

    # 6.关闭套接字
    new_tcp_client_socket.close()  # 不会在为此次链接的客户端服务;发送syn数据包给client,关闭发送通道
    tcp_server_socket.close()  # 关闭监听套接字，不会再监听新的客户端的到来,即accept()会失败


if __name__ == "__main__":
    main()
