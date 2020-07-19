# -*-coding:utf-8-*-
"""
http基于tcp,比udp稳定

http就是传输数据所遵循的格式:
服务器和浏览器都遵循http协议就可以保证不同的浏览器可以访问不同的服务器
都遵守相同的协议就保证了服务器可以解析浏览器发送请求,浏览器可以解析服务器发来的数据

http协议就是一种解耦,让服务器开发和浏览器开发分开来.
否则某一个服务器就需要自己开发浏览器来解析服务器发送的数据

http是无状态的,服务器可根据浏览器发来的cookie判断浏览器是否是登陆状态

浏览器请求至少包含一行:GET /a.html HTTP/1.1
server回复至少包含一行:HTTP/1.1 200 OK

浏览器的请求分header和body,服务器的response也分header和body

如果浏览器请求的是get方式,一般请求中没有body,只有request head;
如果浏览器提交表单(post请求),就有body;header告诉服务器浏览器的信息,body是用户提交的表单数据


server回复的时候,应答头和应答body在不调用close的情况下可以分两次发

在浏览器查看服务器回复的数据:f12→NetWork标签→点开具体的链接
以下内容为浏览器请求tcp_socket_server.py,tcp_socket_server.py获取到的数据
---------------即浏览器请求的数据---------------
########/a.html表示客户端请求的是哪个页面(路径)，请求时至少有这一行
GET /a.html HTTP/1.1
########服务器ip和端口
Host: 127.0.0.1:8888
########常链接
Connection: keep-alive
########浏览器自己设定的值
Upgrade-Insecure-Requests: 1
########浏览器版本
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
########浏览器可以接收何种格式
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
########浏览器可以接收的压缩格式
Accept-Encoding: gzip, deflate, br
########浏览器可以接收的语言
Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7

---------------服务器应答的部分---------------
服务器的应答分两部分:1.应答head 2.应答body
head:是告诉浏览器的东西,如告诉浏览器保存变量(Set-Cookie),按何种编码方式解析
服务器应答头如下(以www.baidu.com为例):
########http协议版本以及应答状态,200表示ok;应答header至少有这行
HTTP/1.1 200 OK
Bdpagetype: 1
Bdqid: 0xa438df010002c172
########缓存控制-私有
Cache-Control: private
Connection: keep-alive
########服务器返回的数据压缩格式,浏览器自带解压缩
Content-Encoding: gzip
########告诉浏览器按何种编码方式解析body,如utf-8
Content-Type: text/html;charset=utf-8
Date: Mon, 13 Jul 2020 06:27:16 GMT
Expires: Mon, 13 Jul 2020 06:27:00 GMT
########服务器;BWS-百度自己的服务器,一般访问得到的是apache
Server: BWS/1.1
########cookie--用户身份标识;服务器返回给浏览器,浏览器保存;浏览器在下次请求时提交cookie;
########可以没有cookie
Set-Cookie: BDSVRTM=0; path=/
Set-Cookie: BD_HOME=1; path=/
Set-Cookie: H_PS_PSSID=32190_1424_31669_32139_31253_32046_32230_32256_26350; path=/; domain=.baidu.com
Strict-Transport-Security: max-age=172800
Traceid: 1594621636060723610611833453216304120178
X-Ua-Compatible: IE=Edge,chrome=1

respose body:是浏览器要展示的内容
<h1>heolo</h1>

如何区分header和body?
header都是连续的,空一行之后都是应答body



--------------------------短链接和长链接-----------------------------
http1.0支持短链接,http1.1支持长链接

短链接：浏览器每次请求成功后，关闭套接字
长链接：浏览器请求成功后不关闭套接字，再次使用该套接字请求数据，直到不再需要请求为止，此时在关闭套接字
简单说就是短链接不复用套接字，长链接复用套接字

长链接好处：比如一个网页内容有文字和好多图片组成，长链接可以使用同一个套接字多次请求这些图片
            而短链接每次请求一个图片都要再和服务器三次握手建立新套接字，请求完之后再和服务器四次挥手关闭套接字
            每创建一个套接字服务器要使用很多资源（多进程，多线程，协程）

"""
