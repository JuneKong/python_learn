#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name:IO编程（主要是同步IO）

# Input Stream就是数据从外面（磁盘、网络）流进内存，Output Stream就是数据从内存流到外面去。
# 由于CPU和内存的速度远远高于外设的速度，所以，在IO编程中，就存在速度严重不匹配的问题。
# 有两种方法解决：
# 1、CPU等着，也就是程序暂停执行后续代码，等100M的数据在10秒后写入磁盘，再接着往下执行，这种模式称为同步IO；
# 2、CPU不等待，只是告诉磁盘，“您老慢慢写，不着急，我接着干别的事去了”，于是，后续代码可以立刻接着执行，这种模式称为异步IO。
# 同步和异步的区别就在于是否等待IO执行的结果。
# 使用异步IO来编写程序性能会远远高于同步IO，但是异步IO的缺点是编程模型复杂。

# 打开文件： open(文件名，标识符)

# 读文件
# （读写操作都是有操作系统完成的，我们仅仅只是调用接口）
# 标识符：r => 读（UTF-8编码的文本文件）
# 读取文件： Python把内容读到内存，用一个str对象表示
# 	read() => 全部 == 文件小
# 	read(size) => 最多size个字节 == 不确定大小
# 	readline() => 每次读取一行
# 	readlines() => 一次读取所有内容并按行返回list == 配置文件
# 			
# 关闭文件： close() => 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
# **with语句：自动帮我们调用close()方法
#   防止读取或写入的时候出现错误，导致没有执行close()方法，而占用操作系统或无法写全
# 
# file-like Object: 只要写个read()方法就可以是给对象（类）。
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。

# 二进制文件： 标识符 rb

# 字符编码
# 读取非UFT-8编码的文本文件：open中传入参数encoding
# open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略errors='ignore'

# 写文件 write()
# 标识符: w 或 wb => 写文本文件或写二进制文件（如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。）
#        a => 追加到文件末尾(写到文件尾部)
# 务必要调用close()来关闭文件。
# 当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
# 只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
# 此时，open()函数传入encoding参数，将字符串自动转换成指定编码。

# StringIO: 就是在内存中读写str(只能是str)
# 先创建StringIO，再写入
# getvalue()方法用于获得写入后的str

# BytesIO: 在内存中读写bytes(操作二进制数据)

# 操作文件和目录
# Python内置的os模块也可以直接调用操作系统提供的接口函数
import os
print(os.name);

# 环境变量
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看
# 要获取某个环境变量的值，可以调用os.environ.get('key')

# *****操作文件和目录*****
# **注意: 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
# ==>
# 查看当前目录的绝对路径:
# >>> os.path.abspath('.')
# '/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# >>> os.path.join('/Users/michael', 'testdir')
# '/Users/michael/testdir'
# 然后创建一个目录:
# >>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
# >>> os.rmdir('/Users/michael/testdir')

# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便
# >>> os.path.splitext('/path/to/file.txt')
# ('/path/to/file', '.txt')

# 文件重命名： os.rename()
# 删除文件： os.remove()
# os模块没有复制文件，shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
# 过滤文件：for...in之后加if做判断

# 练习1：
# 利用os模块编写一个能实现dir -l输出的程序。(遍历当前路径中所有文件)
def dir_l(path = '.'):
    L = os.listdir(os.path.abspath(path)) # 用于返回指定的文件夹包含的文件或文件夹的名字的列表。
    for file in L:
        print(file)
dir_l();

# 练习2：
# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
def findFile(fileName):
	path = os.path.abspath('.')
	dirlist = os.walk(path);
	find = list();
	for parent, dirs, files in dirlist:
		for file in files:
			if fileName in file:
				relPath = parent.replace(path, '.');
				joinPath = os.path.join(relPath, file);
				print(joinPath);
				find.append(joinPath);
	if len(find) == 0:
		print("Not found");
		return;
	return find;
findFile("error.py");
findFile("eee");
# os.walk()用于通过在目录树中游走输出在目录中的文件名，向上或者向下。
# 		   是一个简单易用的文件、目录遍历器

# *****序列化*****
# 把变量从内存中变成可存储或传输的过程称之为序列化
# 把变量内容从序列化的对象重新读到内存里称之为反序列化
# pickle模块来实现序列化。
import pickle
# pickle.dumps()方法 => 把任意对象序列化成一个bytes
# pickle.dump() => 直接把对象序列化后写入一个file-like Object
d = dict(name='joy', age='35', score='85');
pd = pickle.dumps(d);
print(pd);
f = open('dump.txt','wb');
pickle.dump(d, f);
f.close();
# pickle.loads()方法反序列化出对象，要把对象从磁盘读到内存。
# pickle.load()方法从一个file-like Object中直接反序列化出对象。
r = open('dump.txt', 'rb');
l = pickle.load(r);
r.close();
print(l);
# **Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容
# 因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

# JSON
# json模块提供了非常完善的Python对象到JSON格式的转换。
import json
j = json.dumps(d);
print('json: ' + j);
# Python对象 => JSON
# dumps()方法返回一个str，内容就是标准的JSON。
# dump()方法可以直接把JSON写入一个file-like Object
# JSON => Python对象
# loads() JSON的字符串反序列化
# load()方法，从file-like Object中读取字符串并反序列化

# JSON进阶
# dict对象可以直接序列化为JSON的{}，但常用class表示对象
# class => JSON
class Student(object):
	def __init__(self, name, age, score):
		self.name = name;
		self.age = age;
		self.score = score;
s = Student('joy', 23, 87);
# 此时转为JSON会报错，因为Student对象不是可序列化为JSON的对象
# dumps()方法的参数中有个default参数 => 把任意一个对象变成一个可序列为JSON的对象
# 为Student添加一个转换函数
def stu2dict(std):
	return {
		'name': std.name,
		'age': std.age,
		'score': std.score
	}
print(json.dumps(s, default=stu2dict));
# 把任意class的实例变为dict
def arbitrary(obj):
	return obj.__dict__;
print(json.dumps(s,default=arbitrary));
# JSON => class
# loads()方法的object_hook参数负责把dict转换为Student实例
def dict2stu(ds):
	return Student(ds['name'],ds['age'],ds['score']);
json_str = '{"name":"joe","age":34,"score":75}'; # 注：要用双引号标识字符
print(json.loads(json_str, object_hook=dict2stu));


# 序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。
# 既做到了接口简单易用，又做到了充分的扩展性和灵活性。