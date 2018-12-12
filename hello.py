#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# //输入
name = input("please enter your name:");
# //输出
print("hello,",name);
# //获取字符的整数表示
ord("A"); #//65
# //把编码转换为对应的字符
chr(66); #//B
# *************************
# //bytes类型的数据是带b前缀的单引号或双引号表示
# //x = b'abc';
# *************************
# //以Unicode表示的str通过encode()方法可以编码为指定的bytes
"abc".encode("ascii"); #b"abc"
"中文".encode("utf-8"); #b'\xe4\xb8\xad\xe6\x96\x87'
# //要把bytes变为str，就需要用decode()
b"ABC".decode("ascii"); #ABC
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'); #中文

# //计算有多少个字节
# str时为字符数，bytes时为字节数
len("abc") #3

# **********格式化**********
# 方法一：%
print("hello,%s" % "world");
print("hello,%s, you have $%d." % ("asd",10000));
# 用%%来表示一个%
print("percent: %d %%" % 7);
# 方法二：format()
print("hello,{0},成绩提升了{1:.1f}%".format("xiao",12.356));

# 列表list：
# 可修改，直接赋值，用[]表示
list = ["qq","ww","ee"];
print("list: ",list);
# 用len()可以获得list的个数
print(len(list));
# 可用索引获得元素，获得最后一个元素：list[len(list) - 1] or list[-1];
# 即可以顺序获得也可以倒序获得
print(list[len(list) - 1],list[-1]);
# 添加
list.append("asd");
# 插入
list.insert(1,"jack");
# 删除:pop()删除末尾，pop(i)删除索引i
list.pop();

# 元祖tuple(另一种有序列表)
# 一旦初始化就不能修改，用()来表示,即tuple的每个元素，指向永远不变
tuple = ('aa','ss','dd');
# tuple陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
# 因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义
# 定义一个只有一个元素的tuple,必须加一个逗号“,”，来消除歧义
t1 = ("q",);
print(t1);
# 判断语句
# if,elif(else if的缩写),else
age = int(input('enter your age:'));
if age >= 18:
	print("adult");
elif age <18 and age >= 6:
	print("teenager");
else :
	print("kid");

# str不能直接和整数比较,把str转换成整数:int()

# 循环：
# for...in循环
for item in list:
	print("item:",item);
# 循环出index和value, 要使用enumerate()枚举;
for i,item in enumerate(list):
	print("item%s:%s" % (i,item));
# 生成整数序列：range()
# 转换成列表：list()

# while循环
n = 1;
while n < 10:
	print('n:',n);
	n = n + 1;
# break语句可以提前退出循环
# continue语句，跳过当前的这次循环，直接开始下一次循环

# 字典dict：也称为map，使用键-值（key-value）存储，具有极快的查找速度
# 
# ===>>>dict的key必须是不可变对象。<<<=== 可用字符串、整数等作为key，而list可变，不可作为key
# 
# 通过key计算位置的算法称为哈希算法（Hash）
d = {'a':1,'b':2,'c':3};
print(d['a']);
# 判断key是否存在：
# 方法一：in
print('a' in d);
# 方法二：get()---如果key不存在，可以返回None，或者自己指定的value
# 注意：返回None的时候Python的交互环境不显示结果。
print(d.get('d')); #//None
print(d.get('d',-1)); #//-1
# 删除pop(key)
d.pop('a');
print(d);

# ************list与dict的比较***************
# 和list比较，dict有以下几个特点：
# 	1、查找和插入的速度极快，不会随着key的增加而变慢；
# 	2、需要占用大量的内存，内存浪费多。
# 而list相反：
# 	1、查找和插入的时间随着元素的增加而增加；
# 	2、占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。
# *******************************************


# set：一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# key值不可变对象，即不可以为list
s = set([1,2,3]);
print(s); #{1,2,3}
# 重复元素在set中自动被过滤：(有自动排序功能)
s1 = set([2,5,2,1,2,3]);
print(s1); #{1,2,3,5}
# 添加,可重复添加但无效果
s.add(4);
# 删除
s.remove(1);
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
print(s & s1);
print(s | s1);

# *********set和dict的区别************
# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，
# 因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
# ************************************