tcp和udp的区别：
    tcp稍复杂稳定，严格区分客户端和服务器；客户端连接服务器时，必须调用connect()链接,所以tcp是面向链接的通信，udp是面向无链接的通信
    udp简单不稳定，不区分客户端和服务器

单工：只能收，或者只能发，只能指向一个方向（收音机，只能收）
半双工：收的时候不能发，发的时候不能发（对讲机）
双工：同一时刻可收可发，如：socket（打电话，互相说话）

现在的网络通信99%都是tcp或者udp


qq通信原理：
    udp和tcp都采用,客户端都不绑定端口,都不绑定就可以多开qq客户端；绑定了端口不一定能够运行起来，如果其他程序占用了此端口，该程序就启动失败
    client1和client2通信过程：
        1.client1链接服务器，告知本机ip和port
        2.client1将消息发于服务器
        3.服务器找到client2的ip和port(通过qq号)
        4.服务器将消息转发给client2


tcp建立链接时三次握手:
客户端和服务器都要知道彼此已准备好资源,为此client和server分别做了以下工作:
1.client发送发送一个包,询问server是否已经准备好,syn = 1
2.server收到该包,将syn的值+1,回复client ack=2,告知client已准备好;
    同时为了知道client是否已准备好,发送syn=1;就是发送的两个包放在一次发(所以是三次握手,挥手是四次)
3.client收到server的包,将ack解析出来,ack的值是其请求时syn的值+1,说明server已准备好
    同时收到server的syn=1,将syn的值+1,回复ack=2告知server自己已准备好

syn的值等于1只是举例,具体是多少,我也不知道..
|↘            |
|   ↘         |
|     ↘ syn=1 |
|       ↘     |
|         ↘   |
|          ↙  |
|        ↙    |
|      ↙      |
|    ↙ ack=2  |
|  ↙   syn=1  |
|↘            |
|   ↘         |
|     ↘ ack=2 |
|       ↘     |
|         ↘   |

tcp断开链接时四次挥手:
tcp是全双工的,具有收发两个通道.四次挥手就是关闭收发通道,释放资源的过程,一般是客户端先请求close:
1.client先调用close关闭发送通道,发送数据给server告知自己不会再发送数据(应用程序不会再发数据,不会再调用send)
2.server收到(new_client_socket.recv()收到None),recv解阻塞,收通道关闭;发送包给client告知已收到
3.server调用close关闭发送通道,发送数据给client告知server关闭发送通道(延时关闭,如果没收到ack包就重发)
4.client收到数据,recv解阻塞,关闭收通道(等待2msl时间关闭,以确保server没收到再重发的包client可以收到)
    2msl--Maximum Segment Lifetime,数据包在网络中最大存活时间
    无论server有没有收到ack2包,client都要等待2msl,期间资源不可重用(当然,设置socket.SO_REUSEADDR就可用了)

client        server
调用close
|↘            |
|   ↘         |
|syn1=1↘      |
|       ↘     |
|         ↘   |
|          ↙  |
|        ↙  ↙ |server调用close时发,不调close就不发syn2
|ack1=2 ↙  ↙  |
|    ↙  ↙     |
|  ↙  ↙syn2=1 |
|   ↙         |
| ↙           |
|↘            |
|   ↘         |
|ack2=2↘      |
|       ↘     |
|         ↘   |
为什么挥手要四次,而不是三次?
建立链接时,server将回复包ack和请求包syn在一起发
关闭链接时,server可以不调用close从而不关闭发通道,从而不必发syn包;所以回复包ack和调用close时的syn包不能在一起发

四次挥手时,为何client收到syn后要等待2msl?
syn2是server关闭发送通道的消息,client收到后,要发送确认包ack2;万一ack包到达不了server,server会重发syn2包
所以client要等待两个msl,即自己发送的ack2包msl和server重发的syn2 msl
一般2msl是2min,这段时间不能重复使用资源;即使程序关了也要等待2msl

为什么一般要客户端发起关闭?
按上述分析,四次挥手client先发起关闭,最后要等待2msl(通俗地说,谁先调用close谁最后就要等待2msl)
如果server先发起关闭,server就要等待2msl,这段时间资源不能重用.表现形式就是这段时间重启server会报端口被占用的错
(当然可以调用socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)重用资源)

为何client先发起关闭tcp,client可以成功重启,server先发起关闭就不行?
client一般不绑定端口,这个端口不可用就换下一个;而server是必须要绑定端口的