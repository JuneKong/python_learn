#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name:模块
# 最大的好处是大大提高了代码的可维护性。其次，编写代码不必从零开始。
# 使用模块还可以避免函数名和变量名冲突。
# 注意:自己创建模块时要注意命名，不能和Python自带的模块名称冲突。
# 
# 导入模块：import 模块名
# 导入第三方模块


#***********************模块了解************************
#
# asyncio模块：支持TCP,子进程
# 作用：1.异步网络操作
# 		2.并发
# 		 3.协程 => 通过async关键字定义一个协程（coroutine）,当然协程不能直接运行，需要将协程加入到事件循环loop中
# 		 		=> 协程的目的也是让这些IO操作异步化。
# 关于asyncio的一些关键字的说明：
# event_loop 事件循环：程序开启一个无限循环，把一些函数注册到事件循环上，当满足事件发生的时候，调用相应的协程函数
# coroutine 协程：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用。
# 		=> 协程对象不能直接运行，在注册事件循环的时候，其实是run_until_complete方法将协程包装成为了一个任务（task）对象. 
# 		=> task对象是Future类的子类，保存了协程运行后的状态，用于未来获取协程的结果
# 
# task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含了任务的各种状态
# future: 代表将来执行或没有执行的任务的结果。它和task上没有本质上的区别
# 		=> 创建task后，在task加入事件循环之前为pending状态，当完成后，状态为finished
# 		=> 通过loop.create_task(coroutine)创建task,同样的可以通过 asyncio.ensure_future(coroutine)创建task		
# 		=> 绑定回调，在task执行完成的时候可以获取执行的结果，回调的最后一个参数是future对象，通过该对象可以获取协程返回值。
# 		=> 通过add_done_callback方法给task任务添加回调函数，当task（也可以说是coroutine）执行完成的时候,就会调用回调函数。并通过参数future获取协程执行的结果。
# async/await 关键字：python3.5用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。
# 	=> 使用async可以定义协程对象，使用await可以针对耗时的操作进行挂起，就像生成器里的yield一样，函数让出控制权。
#  	=> 并发和并行：
#  		1.并发指的是同时具有多个活动的系统
# 		2.并行是用并发来使一个系统运行的更快。并行可以在操作系统的多个抽象层次进行运用
# 		3.所以并发通常是指有多个任务需要同时进行，并行则是同一个时刻有多个任务执行
# 		asyncio.wait(tasks) ：接受一个task列表， *列表不能为空，返回(done, pending)
# 		== asyncio.gather(*tasks) ：接收一堆task。返回task所有结果(按加入的task排)
# 
# 协程嵌套：即一个协程中await了另外一个协程
# 
# 协程的调用和组合非常灵活，主要体现在对于结果的处理：如何返回，如何挂起
# asyncio.as_completed(): 返回future对象的迭代器
# 
# future对象有几个状态：
# 			Pending => 创建future的时候
# 			Running => 事件循环调用执行的时候
# 			Done => 调用完毕, 如果需要停止事件循环，就需要先把task取消。
# 					可以使用asyncio.Task获取事件循环的task
# 					**loop stop之后还需要再次开启事件循环，最后在close，不然还会抛出异常
# 			Cacelled
# 
# 不同线程的事件循环：
# 当前线程创建一个事件循环，然后在新建一个线程，在新线程中启动事件循环。当前线程不会被block。
# 
# 
# os模块：用来处理文件和目录。