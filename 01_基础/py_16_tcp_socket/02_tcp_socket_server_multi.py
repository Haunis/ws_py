#! /usr/bin/python3
"""
单线程，处理多个客户端.处理完当前客户端的请求，方可处理下一个客户端的请求
"""
import socket

def main():
	#1.创建监听套接字
	#监听套接字负责等待新的客户端进行链接（电话局总机）
	tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	#2.绑定端口
	local_address = ("",8888) #ip不写，表示本机任意一个ip
	tcp_server_socket.bind(local_address) 

	#3.设置监听，让监听套接字由主动变为被动	
	tcp_server_socket.listen(128)

	while True:
		"""
			循环等待多个客户端来链接；
			只要监听套接字tcp_server_socket未关闭，就可以监听多个客户端
			但由于是单线程，所以只会有一个客户端accept()成功，其余客户端等待下次accetp()
			未accept()的客户端会缓存起来，不会丢失，等待下一次accept()
		"""
		#4.等待客户端链接;accept产生的新的套接字负责为客户端服务(收发数据,理解为总机指派的具体人工服务)
		print("---------begain accept-----------")
		new_tcp_client_socket,client_address = tcp_server_socket.accept() #阻塞;client_address是元组
		print("client_address:%s"%str(client_address))
		print("---------end accept-----------")
		
		#5.收发数据;由于不知道客户端何时结束通信，所以要使用循环
		while True:
			receive_data = new_tcp_client_socket.recv(1024) #阻塞；设置接收的最大字节，receive_data是bytes类型
			print("receive_data:%s"%receive_data.decode("utf-8"))
			#recv()解堵塞有两种情况：
			#1.客户端发送数据过来，测试recevie_data不为空
			#2.客户端断开链接，此时receive_data为空
			if receive_data: #不为空
				new_tcp_client_socket.send("数据已收到".encode("utf-8"))
			else:
				break

		#6.关闭服务套接字
		new_tcp_client_socket.close() #不会再为此次链接的客户端服务
	#关闭监听套接字
	tcp_server_socket.close() #关闭监听套接字，不会再监听新的客户端的到来,即accept()会失败
	

if __name__ == "__main__":
	main()
