tcp/ip协议是一组协议簇,分四层,事实上的标准,实际开发都是这么做的
osi分七层,只是理论标准,实际上没多少人这么做
tcp/ip先出,osi后出

tcp/ip协议四层:
    应用层:http协议(应用程序也可以自己规定协议) <------>对应osi 会话层,表示层,应用层
    传输层:tcp udp                         <------>对应osi不变,还是传输层
    网际层(网络层):ip icmp arp igmp rarp 等等<------>对应osi不变,还是网络层
        ip有两个概念:1.ip地址 2.ip协议
    网络接口层(链路层):网卡驱动             <------>对应osi:物理层,数据链路层

一般应用程序和服务器通信所要使用的协议链路:
    http -> tcp/udp -> ip
特殊的应用程序通信所经过的协议链路:
    1.如ping:应用层 -> icmp -> ip
    2.如特殊的外挂:原始套接字->ip(直接跳过tcp/udp)
               原始套接字可以做到以非本机ip发送数据(伪造ip),tcp套接字和udp套接字做不到

一个数据在从客户端到服务器经过各个协议时,各个协议所做的动作(发送方是个组包的过程):
1.http协议 加上请求头
2.tcp/ip协议 加上源端口和目的端口
3.ip协议 加上源ip和目标ip
4.链路层 加上mac地址
接收方服务器在接收数据后是个解包的过程:
去mac地址->去源ip和目标ip->去源端口和目的端口->去http协议头,最终获取想要的数据

windows抓包工具:wireshark,安装时注意勾选"install winpcaoxxx"
    应用:网络开发中,确定发送的数据已经发出去
    原理:使用原始套接字直接到操作系统取数据包
    常用筛选条件:1.tcp
               2.udp
               3.ip.dst == 192.168.x.x and udp
               4.udp.port = 2222 (使用udp协议,并且端口是2222的包)