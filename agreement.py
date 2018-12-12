#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name:网络编程

# 网络编程就是如何在程序中实现两台计算机的通信。
# 更确切地说，网络通信是两台计算机上的两个进程之间的通信。

# *****TCP/IP简介*****
# 互联网上每个计算机的唯一标识就是IP地址
# IP地址对应的实际上是计算机的网络接口，通常是网卡。
# IP协议负责把数据从一台计算机通过网络发送到另一台计算机
# 路由器就负责决定如何把一个IP包转发出去。
# IP包的特点是按块发送，途径多个路由，但不保证能到达，也不保证顺序到达。
# 
# TCP协议则是建立在IP协议之上的。TCP协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达。
# TCP协议会通过握手建立连接，然后，对每个IP包编号，确保对方按顺序收到，如果包丢掉了，就自动重发。
# 一个TCP报文除了包含要传输的数据外，还包含源IP地址和目标IP地址，源端口和目标端口。
# 
# 每个网络程序都向操作系统申请唯一的端口号，这样，两个进程在两台计算机之间建立网络连接就需要各自的IP地址和各自的端口号。

# *****TCP编程*****
# 是面向流连接的协议。
# Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。
# 客户端
import socket
# AF_INET指定使用IPv4协议,如果要用更先进的IPv6，就指定为AF_INET6
# SOCK_STREAM指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #创建
s.connect(('www.sina.com.cn', 80)); #建立连接
# **注意参数是一个tuple，包含地址和端口号。
# 
# **80端口是Web服务的标准端口
# 端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。
# 
# 接收数据时，调用recv(max)方法，一次最多接收指定的字节数
# 当我们接收完数据后，调用close()方法关闭Socket
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n');
buff = [];
while True:
	d = s.recv(1024)
	if d:
		buff.append(d);
	else :
		break;
data = b''.join(buff);
# s.close();
header, html = data.split(b'\r\n\r\n',1);
print(header.decode('utf-8'))
with open('sina.html', 'wb') as f:
	f.write(html);

# 服务器
# 服务器进程首先要绑定一个端口并监听来自其他客户端的连接。
# 服务器会打开固定端口（比如80）监听，每来一个客户端连接，就创建该Socket连接。
# 由于服务器会有大量来自客户端的连接，所以，服务器要能够区分一个Socket连接是和哪个客户端绑定的。
# 一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket。
# 
# 监听端口
s.bind(('127.0.0.1',9999));
# 调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量
s.listen(5) 
# accept()会等待并返回一个客户端的连接
while True:
	sock, addr = s.accept()
	t = threading.Thread(target=tcplink, args=(sock, addr)) #创建新线程来处理TCP连接
	t.start();
# 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接
def tcplink(sock, addr):
	pass

# 同一个端口，被一个Socket绑定了以后，就不能被别的Socket绑定了。


# *****UDP编程*****
# UDP则是面向无连接的协议。
# 
# 使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。
# 优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。
# 
# 服务器
# SOCK_DGRAM指定了这个Socket的类型是UDP。
# 绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据
su = socket.socket(socket.AF_INET, SOCK_DGRAM);
su.bind(('127.0.0.1',9999))
print('Bind UDP...');
while True:
	data, addr = s.recvfrom(1024);
	print('Received from %s:%s.' % addr);
	s.sendto(b'Hello, %s!' % data, addr)
# recvfrom()方法返回数据和客户端的地址与端口
# sendto()就可以把数据用UDP发给客户端
# 
# 客户端
# 客户端使用UDP时，首先仍然创建基于UDP的Socket，然后，不需要调用connect()，直接通过sendto()给服务器发数据
sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    sc.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(sc.recv(1024).decode('utf-8'))
sc.close()

# **服务器绑定UDP端口和TCP端口互不冲突