#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name:异步IO

# 在异步IO模型下，一个线程就可以同时处理多个IO请求，并且没有切换线程的操作。
# 对于大多数IO密集型的应用程序，使用异步IO将大大提升系统的多任务处理能力。

# **这就是异步编程的一个原则：一旦决定使用异步，则系统每一层都必须是异步，“开弓没有回头箭”。

# *****协程*****
# 协程，又称微线程，纤程。英文名Coroutine。
# 
# 子程序，或者称为函数，在所有语言中都是层级调用
# 子程序调用是通过栈实现的，一个线程就是执行一个子程序。
# 子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。
# 
# **注意，在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断。
# 
# 协程的特点在于是一个线程执行
# 1、最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，
# 因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
# 2、第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，
# 在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
# 
# 因为协程是一个线程执行，那怎么利用多核CPU呢？
# 最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。

# *****asyncio*****
# asyncio的编程模型就是一个消息循环。
# 我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
# 
# @asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。
# yield from语法可以让我们方便地调用另一个generator
import asyncio


# *****async/await*****
# **请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
# **1、把@asyncio.coroutine替换为async；（async写于函数前）
# **2、把yield from替换为await

async def wget(host):
	print('wget %s...' % host);
	connect = asyncio.open_connection(host, 80);
	reader, writer = await connect;
	header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
	writer.write(header.encode('utf-8'))
	await writer.drain();
	while True:
		line = await reader.readline();
		if line == b'\r\n':
			break;
		print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
	writer.close();

# loop = asyncio.get_event_loop();
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']];
# loop.run_until_complete(asyncio.wait(tasks));
# loop.close();


# *****aiohttp*****
# asyncio可以实现单线程并发IO操作
# asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架。

# 编写一个HTTP服务器，分别处理以下URL：
# / - 首页返回b'<h1>Index</h1>'；
# /hello/{name} - 根据URL参数返回文本hello, %s!。

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    # content_type指定返回的类型
    return web.Response(body=b'<h1>Index</h1>',content_type='text/html')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
# **注意aiohttp的初始化函数init()也是一个coroutine，loop.create_server()则利用asyncio创建TCP服务。