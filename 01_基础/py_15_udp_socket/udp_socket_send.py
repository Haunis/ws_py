"""
可以使用同一个套接字收发数据

单工：只能收，或者只能发，只能指向一个方向（收音机，只能收）
半双工：收的时候不能发，发的时候不能发（对讲机）
双工：同一时刻可收可发，如：socket（打电话，互相说话）

"""
import socket


def main():
    # 1.创建socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # ipv4,udp

    # 如果未绑定端口,操作系统会自动分配一个端口;对于发送方,可以不绑定端口,但是接收方必须绑定
    # 同一个端口,同一时刻不可以被多个程序使用
    # local_address = ("", 7788)  # ip地址和端口；ip一般不写，表示任意一个ip
    # udp_socket.bind(local_address)  # 申请绑定接口

    # 2.发送数据
    while True:
        input_str = input("请输入要发送的数据：")
        if "exit" == input_str:
            print("退出程序")
            break;
        # udp_socket.sendto(b"hhaha", ("192.168.1.11", 8080)) #第一个参数为字节，第二个参数为目标的ip和端口
        # 每次都要写ip和port
        # TCP使用的是send()
        udp_socket.sendto(input_str.encode("utf-8"), ("192.168.1.12", 7788))
        # print("send: %s" % input_str)

    # 3.关闭socket
    udp_socket.close()


if __name__ == "__main__":
    main()
