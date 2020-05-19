import socket


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #ipv4,udp

    udp_socket.sendto(b"hhaha",("192.168.1.11",8080))
    print("run")
    udp_socket.close()


if __name__ == "__main__":
    main()
