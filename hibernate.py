#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# *****切片*****
# 切片（Slice）操作符,取值时可省略第一个元素和最后一个索引
items = [1,2,3,4,5,6,7,8,9,10];
print(items[0:3]);
print(items[:3]); #即从第一个开始区到第三个
print(items[-2:]); #即去倒数第二个到最后一个元素
# 第三个数表示间隔
print(items[0:4:2]); #前4个数，每2个取一个
print(items[::3]) #所有数，每3个取一个
# 原样复制
print(items[:]);
# 翻转字符串
print(items[::-1]);
# |*****详解****|
# b = a[i:j:s]这种格式呢，i,j与上面的一样，但s表示步进，缺省为1.
# 所以a[i:j:1]相当于a[i:j]
# 当s<0时，i缺省时，默认为-1. j缺省时，默认为-len(a)-1
# 所以a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍。

# 练习：实现自定义trim()函数
def myTrim(s):
	i = 0;
	l = len(s);
	while i < l:
		if s[i] == ' ':
			i = i + 1;
		else :
			break;
	if i == len:
		return "";
	j = l - 1;
	while j >= 0:
		if s[j] == " ":
			j = j - 1;
		else :
			break;
	return s[i:j + 1];
print(myTrim("hello   "));
print(myTrim("     "));
print(myTrim("  ddd"));
print(myTrim(""));
print(myTrim("  ddas  "));

# *****迭代*****
# 迭代dict，默认是迭代key
# 迭代value: .values
d = {'a':1,'b':2,'c':3};
for key in d:
	print(key);
for val in d.values():
	print("value = ", val);
# 迭代key和value
for key, val in d.items():
	print("%s = %s" % (key,val));

# 判断是否为迭代对象：通过collections模块的Iterable类型判断
from collections import Iterable;
print(isinstance(d,Iterable));

# 练习：请使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(val):
	if len(val) == 0:
		return (None, None);
	mi = mx = val[0];
	for v1 in val:
		if v1 >= mi and v1 <= mx:
			continue;
		elif v1 > mx:
			mx = v1;
		elif v1 < mi:
			mi = v1;
	return (mi,mx);
print(findMinAndMax([]));
print(findMinAndMax([2]));
print(findMinAndMax([2,1,3,5,2,9,4]));

# *****列表生成式*****
# 即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
# 生成1-10
L = (range(1,11));
# 生成平方序列
Li = [x * x for x in range(1,11)];
# 写列表生成式时，把要生成的元素(x * x)放到前面，后面跟for循环，就可以把list创建出来
# ==>for循环后面还可以加上if判断
# 这样我们就可以筛选出仅偶数的平方：
Lis = [x * x for x in range(1,11) if x % 2 == 0];

# 两层循环，可以生成全排列
List = [m + n for m in "abc" for n in "opq"];

# 练习:把一个list中所有的字符串变成小写：
# 列表中的字符串才有效
L1 = ['Hello', 'World', 18, 'Apple', None];
L2 = [s.lower() for s in L1 if isinstance(s,str)];

# *****生成器generator*****
# generator函数的“调用”实际返回一个generator对象
# 方法一：把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(1,11));
# 使用next()方法获得generator的下一个返回值
# 也可以用for...in循环
 
# 方法二：如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。 
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
# 用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中 
print(sum((1,5)));
t = [1];
a = zip([0]+t, t+[0])
print(list(a));

# *****迭代器：Iterator*****
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器
#   ==>Iterator对象表示的是一个数据流,Iterator对象可以被next()函数调用
#   ==>并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
#   ==>可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
#   ==>只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，
#   ==>只有在需要返回下一个数据时它才会计算。
# 可迭代对象: Iterable  ==>如list、tuple、dict、set、str等,但他们不是Iterator
	# 凡是可作用于for循环的对象都是Iterable类型；
	# 凡是可作用于next()函数的对象都是Iterator类型
# Iterable变成Iterator可以使用iter()函数