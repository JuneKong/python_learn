#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name:常用第三方模块

# 可用pip安装。

# *****Pillow*****
from PIL import Image
# img = Image.open() => 打开图片文件
# img.size => 获得图片尺寸（宽、高）
# img.thumbnail() => 缩放
# img.save() => 保存图片
from PIL import ImageFilter
# 模糊效果
# img.filter() => 模糊滤镜
from PIL import ImageDraw
# 绘制图形

# *****requests*****
# 处理URL资源特别方便。
import requests
# r = requests.get('https://www.doban.com/') #豆瓣首页
# # 对于带参数的URL，传入一个dict作为params参数：
# re = requests.get('https://www.douban.com/search', params={'q': 'python'});
# # 对于特定类型的响应，例如JSON，可以直接获取：
# # re.json();
# # 需要传入HTTP Header时，我们传入一个dict作为headers参数
# # 
# # 要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
# p = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})

# # requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数

# # 上传文件需要更复杂的编码格式，但是requests把它简化成files参数
# upload_files = {'file': open('report.xls', 'rb')}
# f = requests.post(url, files=upload_files);
# 在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。
# put()，delete()等，就可以以PUT或DELETE方式请求资源。


# *****chardet*****
# 用它来检测编码，简单易用。
import chardet
s = chardet.detect(b'Hello world');
print(s);

# *****psutil*****
# 获取系统信息
# 用Python来编写脚本简化日常的运维工作是Python的一个重要用途
# 它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。
import psutil
# 获取CPU信息
print(psutil.cpu_count());
print(psutil.cpu_count(logical=False));

# 获取内存信息
# 使用psutil获取物理内存和交换内存信息
psutil.virtual_memory()
psutil.swap_memory()

# 获取磁盘信息
# 获取磁盘分区、磁盘使用率和磁盘IO信息
psutil.disk_partitions()
psutil.disk_usage('/')
psutil.disk_io_counters()

# 获取网络信息
# 可以获取网络接口和网络连接信息
psutil.net_io_counters()  #获取网络读写字节/包的个数
psutil.net_if_addrs()  #获取网络接口信息
psutil.net_if_stats()  #获取网络接口状态
# 要获取当前网络连接信息，使用net_connections()

# 获取进程信息
# 可以获取到所有进程的详细信息
psutil.pids() # 所有进程ID
pr = psutil.Process(3376) # 获取指定进程id=3376
pr.name()
pr.exe() #进程exe路径
pr.cwd() #进程工作目录
pr.cmdline() #进程启动的命令行
pr.ppid() #父进程ID
pr.parent() #父进程
pr.children() # 子进程列表
pr.status() #进程状态
pr.username() #进程用户名
pr.create_time() # 进程创建时
pr.terminal() # 进程终端
pr.cpu_times() # 进程使用的CPU时间
pr.memory_info() # 进程使用的内存
pr.open_files() # 进程打开的文件
pr.connections() # 进程相关网络连接
pr.num_threads() # 进程的线程数量
pr.threads() # 所有线程信息
pr.environ() # 进程环境变量
pr.terminate() # 结束进程
# psutil还提供了一个test()函数，可以模拟出ps命令的效果