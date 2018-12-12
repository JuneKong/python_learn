#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# name:面向对象高级编程


class Student(object):
    pass

# 给实例绑定一个方法
def set_age(self, age):
    self.age = age

from types import MethodType
# 仅是当前实例有效，对其他实例无效
s = Student()
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# 若对所有实例都有效，则给class绑定方法

def set_score(self, score):
    self.score = score
Student.set_score = set_score
s1 = Student()
s1.set_score(60)
print(s1.score)
# 动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。


# *****使用__slots__*****
# 在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性,使用tuple类型定义
# **使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

# *****使用@property*****
# Python内置的@property装饰器就是负责把一个方法变成属性调用的
#   把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@方法名.setter，
#   负责把一个setter方法变成属性赋值
#
# 只定义getter方法，不定义setter方法就是一个只读属性
#
class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# 使用@property时
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# *****多重继承MixIn*****
# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承
# 来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。


# *****定制类*****
# __str__():返回用户看到的字符串,当打印print类时，所输出的字符串可用给方法进行修改
# __repr__():返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
#
# __iter__():如果一个类想被用于for...in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 			 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法
# 			 拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
# 以斐波那契数列为例:
class Fib(object):
    """docstring for Fib"""

    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:  # 退出循环条件
            raise StopIteration()
        return self.a  # 返回下一个值
for n in Fib():
    print(n)

# 仅用__iter__()方法还不能完全像list，tuple或dict那样对元素获得和设置
# 还有加上以下一些方法：
# __getitem__:需要实现__getitem__()方法,才能像list那样按照下标取出元素
# 对切片方法的编程：

class Fib(object):

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
print(Fib()[2])
print(Fib()[1:3])
# 但没有对step参数和负数做处理，所以还是很不完善的
# 如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。
# 最后，还有一个__delitem__()方法，用于删除某个元素。
#
# __getattr__():动态返回一个属性,也可以返回一个函数(调用的时候必须加（）)，避免调用不存在的属性产生的错误
# **注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
#
# 可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
# 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。
#
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
# __call__():就可以直接对实例进行调用。还可以定义参数。
# ?? 怎么判断一个变量是对象还是函数呢？
# 其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。


# *****使用枚举类*****
from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr'))
# 枚举类.__members__.items(): 获得枚举类型的所有成员；
# 枚举类.成员name.value: 获得成员值；
# 枚举类(value): 根据值获得枚举常量；
# ...
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
print(Month.Jan.value)
print(Month(3))
# @unique装饰器可以帮助我们检查保证没有重复值。
# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：


@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# *****使用元类*****
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
#
# type(): 函数可以查看一个类型或变量的类型，
# type()函数既可以返回一个对象的类型，又可以创建出新的类型
# 一个class，它的类型就是‘type’，一个实例，它的类型就是‘class 类名’
# class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
#
# 要创建一个class对象，type()函数依次传入3个参数：
# 1、class的名称；
# 2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

# metaclass：元类，控制类的创建行为
# 先定义metaclass，就可以创建类，最后创建实例。
# metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
# **metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。
# **不懂也没关系
