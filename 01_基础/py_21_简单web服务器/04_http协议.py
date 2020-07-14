#-*-coding:utf-8-*-
"""
http基于tcp,比udp稳定

以下内容为浏览器请求tcp_socket_server.py,tcp_socket_server.py获取到的数据
即浏览器请求的数据:
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


在浏览器查看服务器回复的数据:f12→NetWork标签→点开具体的链接
服务器的应答分两部分:1.应答header 2.应答body
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

应答body:是浏览器要展示的内容
如何区分header和body:header都是连续的,空一行之后都是应答body


"""