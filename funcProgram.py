#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# *****函数式编程*****
# 特点之一就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！ 

# *****高阶函数*****
# 函数本身也可以赋值给变量，即：变量可以指向函数。
s = abs(-10);
f = abs;

# ===>>> map()和reduce()
# 
# 1.map()函数接收两个参数，一个是函数，一个是Iterable，
# 	map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def fx(x):
	return x * x;
m = map(fx, [1,2,3,4,5,6]);
print(list(m));
# 2.randuce()这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
def fn(x,y):
	return x * 10 + y;
r = reduce(fn, [1,2,3,4,5,6]);
print(r);

# 练习
# 1.英文名首字母大写
def normalize(name):
	n = name[0].upper();
	l = len(name);
	n = n + name[1:l].lower();
	return n;

L1 = ['adam', 'LISA', 'barT'];
L2 = list(map(normalize, L1));
print(L2);

# 2.接受一个list并利用reduce()求积
def prod(L):
	def lam(x, y):
		return x * y;
	return reduce(lam,L);
print(prod([3,5,7,9])); 

# 3.字符串转换成浮点数
# 
CHART_TO_FLOAT = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,".":-1}; 
def str2float(s):
	nums = map(lambda ch: CHART_TO_FLOAT[ch], s);
	point = 0;
	def to_float(f,n):
		nonlocal point;
		if n == -1:
			point = 1;
			return f;
		if point == 0:
			return f * 10 + n;
		else:
			point = point * 10;
			return f + n / point;
	return reduce(to_float, nums, 0.0);

print(str2float("23.1"));

# 注意：
# global关键字表示声明全局变量
# nonlocal关键字表示用来在函数或其他作用域使用外层(非全局)变量;

# ===>>>filter()过滤列表
# 接收一个函数和一个序列；
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。
# ***注意***到filter()函数返回的是一个Iterator，也就是一个惰性序列，
# 所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

# 练习
# 筛选出回数

# ***解决递归深度出现的错误***
# import sys   
# sys.setrecursionlimit(1000000);  设置深度为1000000

# 使用切片slice实现
def palindrome(num):
	return str(num) == str(num)[::-1];
l = list(filter(palindrome, range(1,200)));
print(l);

# ===>>>sorted()
# 排序算法
 
# 练习
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def byName(t):
	return t[0];
L2 = sorted(L, key=byName)
print(L2);

# *****返回函数*****
# 每次调用都会返回一个新的函数，即使传入相同的参数
# 返回的函数f并没有立即执行，而是调用了f()才执行
# **注意**
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数
# 法一：
# def count():
# 	n = 0;
# 	def add():
# 		nonlocal n;
# 		n = n + 1;
# 		return n;
# 	return add;
# 法二：创建序列
def count():
	s = [0];
	def add():
		s[0] = s[0] + 1;
		return s[0];
	return add;
counterA = count();
print(counterA(), counterA(), counterA(), counterA(), counterA());

# *****匿名函数*****
# 关键字lambda表示匿名函数, lambda 参数：表达式
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
# 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
 
# *****装饰器*****
# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# 函数对象有一个__name__属性
# 
# 借助Python的@语法，把decorator置于函数的定义处
def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper
@log
def now():
	print("2012-12-12");
now(); # 但此时的__name__指向wrapper，因为返回的是wrapper

# 把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数,三层嵌套
# 使用时@log(参数)
# 相当于now = log(参数)(now)

# 让其__name__属性指向回自己本身
# 使用Python内置的functools.wraps
# 在返回函数之前加上@functools.wraps(func);
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper
# 法1:
def log(*text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			if text == None:
				print('call: %s():' % (func.__name__))
			else :
				print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
@log()
def f():
	print("1");
f();
@log("dd")
def f1():
	print("2");
f1();
# 法2：
def log(param):
	if callable(param):
		def wrapper(*args, **kw):
			print('%s function()' % (param.__name__,))
			param(*args, **kw)
		return wrapper
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (param, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
@log
def now():
	print("2018")
@log("测试")
def now2():
	print("2018")
now() 
now2()

# *****偏函数partial*****
# 是functools模块下提供的函数
# 要引入functools模块
# 把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
int2 = functools.partial(int, base=2);
print(int2("1000100"));
# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数