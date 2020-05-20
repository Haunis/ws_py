import socket


def main():
    # 1.创建socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # ipv4,udp

    # 2.发送数据
    while True:
        input_str = input("请输入要发送的数据：")
        if "exit" == input_str:
            print("退出程序")
            break;
        # udp_socket.sendto(b"hhaha", ("192.168.1.11", 8080)) #第一个参数为字节，第二个参数为目标的ip和端口
        udp_socket.sendto(input_str.encode("utf-8"), ("192.168.1.12", 7788))
        # print("send: %s" % input_str)

    # 3.关闭socket
    udp_socket.close()


if __name__ == "__main__":
    main()
