"""
做一个简易的半双工聊天程序
半双工：就像对讲机一样，接收和发送不能同时进行。注意：socket是全双工的

运行：
    1.使用控制台运行本文件
    2.绑定一个接收端口，如：8888
    3.选择功能发送，ip:127.0.0.1, port:9999(发送给本机9999端口)

    1.再开一个控制台运行此文件：
    2.绑定接收端口，9999，接收第一个控制台发送的数据



"""
import socket

str_fun_remind = """
    请输入功能：
    1-发送数据
    2-接收数据
    0-退出
"""


def send_msg(my_socket):
    ip = input("请输入目标ip:")  # 输入127.0.0.1可发送给本机程序
    port = input("请输入目标端口：")
    msg = input("请输入消息：")
    my_socket.sendto(msg.encode("utf-8"), (ip, int(port)))


def receive_msg(my_socket):
    msg = my_socket.recvfrom(1024)
    print("msg: %s" % str(msg))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = int(input("请输入本程序申请绑定的端口："))  # 如8888
    local_address = ("", port)
    udp_socket.bind(local_address)  # 接收数据时候需要申请绑定接口

    while True:
        op = input(str_fun_remind + "\n:")
        if op == "1":
            send_msg(udp_socket)
        elif op == "2":
            receive_msg(udp_socket)
        elif op == "0":
            break
        else:
            print("请输入正确的功能")


if "__main__" == __name__:
    main()
