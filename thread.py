#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name:进程和线程

# 对于操作系统来说，一个任务就是一个进程（Process）
# 把进程内的这些“子任务”称为线程（Thread）。

import os, time, random
# *****多进程*****
# 
# multiprocessing
# 多进程模块，提供了一个Process类来代表一个进程对象
from multiprocessing import Process
# 子进程要执行的代码
def run(name):
	print('run child %s (%s)...' % (name, os.getpid()));
if __name__ == '__name__':
	print('parent %s' % os.getpid());
	p = Process(target=run, args=('test',));
	print('child will start');
	p.start();
	p.join();
	print('child end');
# 创建Process类时要传入一个执行函数和函数参数
# 用start()方法启动
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步

# Pool
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程
from multiprocessing import Pool
# join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，
# 调用close()之后就不能继续添加新的Process了
po = Pool(4); #表示最多可以同时执行4个进程

# 子进程
# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
import subprocess
# communicate()方法 => 输入

# 进程间通讯
# multiprocessing模块中Queue、Pipes等多种方式来交换数据。
# 父进程所有Python对象都必须通过pickle序列化再传到子进程去

# *****多线程*****
# threading是高级模块，对_thread进行了封装
import threading
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
# current_thread()函数，它永远返回当前线程的实例

# Lock
# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
# 而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改
# 线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
# 
# 由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。
# 创建一个锁就是通过threading.Lock()来实现
lock = threading.Lock();
lock.acquire(); # 获得锁
lock.release(); # 释放锁 => 修改完一定要释放
# 锁的好坏：
# 好处： 就是确保了某段关键代码只能由一个线程从头到尾完整地执行
# 坏处： 首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。
# 		 其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，
# 		 导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。

# 多核CPU

# *****ThreadLocal*****
# ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。


# *****进程 vs. 线程*****
# 优缺点：
# 多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程。
# 多进程模式的缺点是创建进程的代价大
# 
# 多线程模式通常比多进程快一点，但是也快不到哪去，
# 多线程模式致命的缺点就是任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存。
