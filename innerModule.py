#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name:内建模块

# *****datetime*****
# 处理日期和时间的标准库。

# 获取当前日期和时间
# 第一个datetime是模块，第二个datetime是datetime模块中的类
from datetime import datetime
# now()返回当前日期和时间，其类型是datetime
now = datetime.now();
print(now);

# 获取指定日期和时间
dt = datetime(2018,2,2);
print(dt);

# datetime转换为timestamp（时间戳）
ts = datetime.timestamp(dt);
# **注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。

# timestamp转换为datetime
datetime.fromtimestamp(ts);
# **注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。
# 上述转换是在timestamp和本地时间做转换
datetime.utcfromtimestamp(ts) # UTC标准时间

# str转换为datetime
# strptime()实现，需要一个日期和时间的格式化字符串
st = datetime.strptime("2018-2-15", '%Y-%m-%d');
print(st);
# **注意转换后的datetime是没有时区信息的。

# datetime转换为str
# strftime(),同样需要一个日期和时间的格式化字符串
strNow = now.strftime('%a, %b %d %H:%M');
print(strNow);

# datetime加减
# 加减可以直接用+和-运算符，需要导入timedelta这个类
from datetime import timedelta
tomorrow = now + timedelta(hours = 8);
print(tomorrow);

# 本地时间转换为UTC时间
# 本地时间是指系统设定时区的时间
# UTC时间指UTC+0:00时区的时间
# 
# datetime类型有一个时区属性tzinfo，但是默认为None
# 
from datetime import timezone
utc = timezone(timedelta(hours=8)); # 创建时区UTC+8:00
now.replace(tzinfo = utc)  # 强制转换成UTC+8:00
# 如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区

# 时区转换
# utcnow() => 当前的UTC时间
# astimezone()方法，可以转换到任意时区
# **注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换
# **如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。

# 练习
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp
import re
def toTimestamp(dt, tz):
	# str转为datetime
	timer = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S') 
	tz = re.search(r'UTC([+|-]\d+):(\d{2})', tz); # 拆分时区
	h = int(tz.group(1));
	m = int(tz.group(2));
	# 根据拆分的时、分创建UTC时间
	utc = timezone(timedelta(hours=h,minutes=m))
	# 强制转换成UTC时间
	time = timer.replace(tzinfo = utc);
	# 转为timestamp
	stamp = time.timestamp()
	return stamp;
print(toTimestamp("2015-1-21 9:01:30", 'UTC+5:00'));


# *****collections*****
# 集合模块，提供了许多有用的集合类。

# namedtuple
# namedtuple(name, 属性list[])是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，
# 并可以用属性而不是索引来引用tuple的某个元素。
from collections import namedtuple
# 可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用

# deque
# list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
d = deque(['a','b','c']);
d.append('q');
# append()和pop() 
# appendleft()和popleft() => 头部添加或删除元素

# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict
# **注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入
df = defaultdict(lambda: 'N/A');
df['key'] = 'qwe';
print(df['key']);
print(df['asd']);

# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict
# **注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
from collections import OrderedDict
# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdatedOrderedDict(OrderedDict):
	def __init__(self, capacity):
		super(LastUpdatedOrderedDict, self).__init__()
		self._capacity = capacity

	def __setitem__(self, key, value):
		containsKey = 1 if key in self else 0;
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last=False)
			print('remove:', last)
		if containsKey:
			del self[key]
			print('set:', (key, value))
		else:
			print('add:', (key, value))
			OrderedDict.__setitem__(self, key, value)

# ChainMap
# ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找
from collections import ChainMap

# Counter
# Counter是一个简单的计数器
from collections import Counter


# *****base64*****
# Base64是一种最常见的二进制编码方法。
# 好处是编码后的文本数据可以在邮件正文、网页等直接显示。
import base64
# 标准base64
#  => base64.b64encode() # 编码
#  => base64.b64decode() # 解码
# 编码后可能出现字符+和/，在URL中就不能直接作为参数，
# 所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
#  => base64.urlsafe_b64encode();
#  => base64.urlsafe_b64decode();
# Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。
# Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。

# 练习 
# 请写一个能处理去掉=的base64解码函数：用递归写
def safe_base64_decode(s):
	if len(s) % 4 == 0:
		return base64.b64decode(s);
	d = s + b'=';
	return self_base64_decode(d);


# *****struct*****
# Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，所以，字节数组＝二进制str。
# Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
import struct
# struct的pack函数把任意数据类型变成bytes
struct.pack('>I',10240099);
# pack的第一个参数是处理指令，
# '>I'的意思是：>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# 
# unpack()把bytes变成相应的数据类型
# byte类型也有切片：byte[0:30] => 取前30个字节

# BMP格式采用小端方式存储数据，文件头(前30个字节)的结构按顺序如下：

# 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
# 一个4字节整数：表示位图大小；
# 一个4字节整数：保留位，始终为0；
# 一个4字节整数：实际图像的偏移量；
# 一个4字节整数：Header的字节数；
# 一个4字节整数：图像宽度；
# 一个4字节整数：图像高度；
# 一个2字节整数：始终为1；
# 一个2字节整数：颜色数。

# 文件头解码
# struct.unpack('<ccIIIIIIHH', s)

# 练习
# 请编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。
def bmpInfo(data):
	file = open(data, 'rb');
	s = file.read(30); # 读取前30个字节即可知道文件格式
	h = struct.unpack('<ccIIIIIIHH', s);
	if h[0] == b'B' and (h[1] == b'M' or h[1] == b'A'):
		print(True);
	else:
		print(False);
	return {
		'width': h[6],
		'height': h[7],
		'color': h[9]
	}


# *****hashlib*****
# 摘要算法：又称哈希算法、散列算法。如MD5，SHA1等等，它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
# 摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。
# 而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。
import hashlib

# 不能用于加密（因为无法通过摘要反推明文），只能用于防篡改

# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
# 
# 有没有可能两个不同的数据通过某个摘要算法得到了相同的摘要？
# 有，因为任何摘要算法都是把无限多的数据集合映射到一个有限的集合中。这种情况称为碰撞

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

# 练习
# 根据用户输入的口令，计算出存储在数据库中的MD5口令
def calcMd5(password):
	md5 = hashlib.md5();
	md5.update(password.encode('utf-8'));
	h = md5.hexdigest();
	return h;

# 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：
def login(user, password):
	if calcMd5(password) == db[user]:
		print(True);
	else:
		print(False);
login('michael', '123456');

# 对简单口令加强保护 => 通过对原始口令加一个复杂字符串来实现，俗称“加盐”
#
#2、根据修改后的MD5算法实现用户登录的验证：
import random
def get_md5(s):
	return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
	def __init__(self, username, password):
		self.username = username
		self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
		self.password = get_md5(password + self.salt)
dbUp = {
	'michael': User('michael', '123456'),
	'bob': User('bob', 'abc999'),
	'alice': User('alice', 'alice2008')
}

def login(username, password):
	user = dbUp[username];
	salt = user.salt;
	password = password + salt;
	return user.password == get_md5(password);

# *****hmac*****
# Hmac算法: 计算一段message的哈希时，根据不通口令计算出不同的哈希。要验证哈希值，必须同时提供正确的口令。
# Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA-1。采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。
import hmac
# **需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。

# 练习
# 将上一节的salt改为标准的hmac算法，验证用户口令：
def hamcMd5(key, s):
	return hamc.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5');

def loginByHmac(username, password):
	user = dbUp[username];
	return user.password == hamcMd5(user.key, password);

# *****itertools*****
# 提供了非常有用的用于操作迭代对象的函数。
import itertools
# “无限”迭代器
# => count() 无限的迭代器
# => cycle()会把传入的一个序列无限重复下去
# => repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
# 
# 无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，
# 事实上也不可能在内存中创建无限多个元素。
# 
# 常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
natuals = itertools.count(1);
ns = itertools.takewhile(lambda x: x <= 10, natuals);
list(ns);

# chain()
#  => 把一组迭代对象串联起来，形成一个更大的迭代器

# groupby()
# => 把迭代器中相邻的重复元素挑出来放在一起
# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。



# 练习
# 计算圆周率可以根据公式：
def pi(N):
    # ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    natuals = itertools.count(1);
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    ln = itertools.takewhile(lambda x: x < N+1, natuals);
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    lastN = list(ln);
    for n in range(len(lastN)):
    	lastN[n] = 2 * lastN[n] - 1; # 取得奇数序列
    	lastN[n] = 4 / lastN[n];
    	if n % 2 != 0:
    		lastN[n] = -lastN[n];
    # step 4: 求和:
    return sum(lastN);
p = pi(10)
print(p);

# *****contextlib*****
# 在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们。正确关闭文件资源的一个方法是使用try...finally(麻烦)
# with语句允许我们非常方便地使用资源，而不必担心资源没有关闭
# 实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。

# 实现上下文管理是通过__enter__和__exit__这两个方法实现的

# @contextmanager
# 编写__enter__和__exit__仍然很繁琐，contextlib提供了更简单的写法
from contextlib import contextmanager
# @contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了
# @contextmanager让我们通过编写generator来简化上下文管理。

# @closing
# 作用就是把任意对象变为上下文对象，并支持with语句

# *****urllib*****
# urllib提供了一系列用于操作URL的功能
from urllib import request

# urllib.request：可以用来发送request和获取request的结果
# urllib.error：包含了urllib.request产生的异常
# urllib.parse：用来解析和处理URL
# urllib.robotparse：用来解析页面的robots.txt文件


# Get
# urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应

# Post
# 以POST发送一个请求，只需要把参数data以bytes形式传入。
# 
# 模拟微博登录：
from urllib import request, parse

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

# Handler
# 如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理

# 练习
# 利用urllib读取JSON，然后将JSON解析为Python对象
import json
def fetchDate(url):
	with request.urlopen(url) as u:
		data = json.loads(u.read().decode('utf-8'));
		return data;


# *****XML*****
# DOM vs SAX
# 操作XML有两种方法：DOM和SAX。（正常情况下，优先考虑SAX，因为DOM实在太占内存）
# DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
# SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。

# 练习
# 请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：
# https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml
from xml.parsers.expat import ParserCreate

class WeatherHandler(object):
	def __init__(self):
		self.data = {'forecast':[]}

	def start_element(self, name, attrs):
		if name == 'yweather:location':
			self.data['city'] = attrs['city'];
			self.data['country'] = attrs['country'];
		elif name == 'yweather:forecast':
			self.data['forecast'].append({
				'date': attrs['date'],
				'high': attrs['high'],
				'low': attrs['low']
				})
	def end_elemet(self, name):
		pass
	def char_data(self, text):
		pass

def parseXml(xml_str):
	handler = WeatherHandler();
	parse = ParserCreate();
	parse.StartElementHandler = handler.start_element;
	parse.EndElementHandler = handler.end_elemet;
	# parse.CharacterDateHandler = handler.char_data;
	parse.Parse(xml_str); # 解析XML文件

	print('City： ' + handler.data['city']);
	print('Weather: ');
	for x in handler.data['forecast']:
		print(x);
	return handler.data;

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
with request.urlopen(URL, timeout = 4) as f:
	data = f.read();
result = parseXml(data.decode('utf-8'));
assert result['city'] == 'Beijing';


# *****HTMLParser*****
# 如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，
# 第二步就是解析该HTML页面，看看里面的内容到底是新闻、图片还是视频。

from html.parser import HTMLParser
from html.entities import name2codepoint
# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
# 特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。

# 1、定义Parser(HTMLParser)处理类
# 2、parser = Parser();
#    parser.feed(html);