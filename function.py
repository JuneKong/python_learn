#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 调用(内部)函数:参数个数要正确且类型也要正确
# 绝对值abs()
print(abs(-20));
# 最大值max()
print(max(2,5,-3));
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，
# 相当于给这个函数起了一个“别名”：
a = abs;
print(a(-1));
# 整数转为十六进制数：hex()
print(hex(255)); #//0xff

# 定义函数：
# 定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回
def myAbs(val):
	if val > 0:
		return val;
	elif val < 0:
		return -val;
	else:
		return 0;
print(myAbs(-2));

# 空函数
# pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，
# 就可以先放一个pass，让代码能运行起来。
def no():
	pass;
print(no());

# 参数检查
# 自定义的函数：如果参数不对可以检查出来
# 			   但参数类型出错则无法检查
# 内置函数则都可以检查出；
# 
# 数据类型检查可以用内置函数isinstance()实现
def oneAbs(val):
	if not isinstance(val,(int,float)):
		raise TypeError('bad operand type');
	if val >= 0:
		return val;
	else:
		return -val;

# 返回多个值
# 例：从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：
import math;
def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle);
	ny = y - step * math.sin(angle);
	return nx, ny;
print(move(100,100,60,math.pi / 6));
# 其实返回的值是一个tuple!!!在语法上，返回一个tuple可以省略括号，
# 而多个变量可以同时接收一个tuple，按位置赋给对应的值

# 练习
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0 的两个解。
def quadratic(a, b, c):
	dt = b*b - 4*a*c;
	if dt > 0:
		x1 = (-b + math.sqrt(dt))/(2*a);
		x2 = (-b - math.sqrt(dt))/(2*a);
		return x1,x2;
	elif dt == 0:
		x = (-b)/(2*a);
		return x;
	else :
		return;
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
	print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
	print('测试失败')
else:
	print('测试成功')


# *****参数*****
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 1位置参数
# 2默认参数
# 设置默认参数时，有几点要注意：
# 	一是必选参数在前，默认参数在后，否则Python的解释器会报错；
# 	二是如何设置默认参数。
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。
# 变化小的参数就可以作为默认参数。
# 使用默认参数最大的好处是能降低调用函数的难度。
# *****
# ==>>>定义默认参数要牢记一点：默认参数必须指向不变对象！<<<==
# *****
# 3可变参数 -----可变参数在函数调用时自动组装为一个tuple
# 在参数前面加了*号
# 请计算a*a + b*b + c*c + ……。
def  calc(*numbers):
	sum = 0;
	for num in numbers:
		sum = sum + num * num;
	return sum;
# 4关键字参数 ----- 关键字参数在函数内部自动组装为一个dict
# 在参数面前加**号
def person(name, age, **kw):
	pass
# 关键字参数有什么用？它可以扩展函数的功能

# 5命名关键字参数
# 命名关键字中没有可选参数时，参数必须要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def people(name, age, *, city,job):
	pass
# 调用要写上命名关键字
people("jack",25,city="beijing",job="engineer")

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def people1(name, age, *args, city, job):
	pass

# 参数组合


# 递归函数
# 递归函数的优点是定义简单，逻辑清晰。
# 使用递归函数需要注意防止栈溢出。
def fact(n):
 	if n == 1:
 		return 1;
 	return n * fact(n-1);
# 尾递归
# 解决递归调用栈溢出的方法是通过尾递归优化
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
def fact_tail(n, sum):
	if n == 1:
		return sum;
	return fact_tail(n-1, n*sum);
