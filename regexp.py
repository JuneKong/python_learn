#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name:正则表达式

# \d => 可以匹配一个数字
# \w => 可以匹配一个字母或数字
# . => 可以匹配任意字符
# \s => 可以匹配一个空格（也包括Tab等空白符）
# 要匹配变长的字符:
# * => 表示任意个字符（包括0个）
# + => 表示至少一个字符
# ? => 表示0个或1个字符
# {n} => 表示n个字符
# {n,m} => 表示n-m个字符

# 进阶
# 要做更精确地匹配，可以用[]表示范围
# A|B => 可以匹配A或B
# ^ => 表示行的开头。
# $ => 表示行的结束。

# re模块
# r前缀，就不用考虑转义的问题
s = r'ASD\-1332';

import re
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
if re.match(r'^\w{2}', s):
	print('ok');
else:
	print('failed');

# 切分字符串
# re.split(reg,str)

# 分组
# 用()表示的就是要提取的分组（Group）
# 如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来
# **注意到group(0)永远是原始字符串
# groups() 提取所有子串
r = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(r.group(0));
print(r.groups());

# 贪婪匹配
# **正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
# 加个?就可以让reg采用非贪婪匹配

# 编译
# re.compile()预编译该正则表达式,返回Regular Expression对象，包含编译后的正则表达式，
# 匹配时不用再添加正则表达式
re = re.compile(r'^(\d{3})-(\d{3,8})$');
re.match('010-123456');

# 练习1
# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email
def is_valid_email(addr):
    r = r'(^[0-9a-zA-Z])([0-9a-zA-Z.]*)@([0-9a-zA-Z]*).(com|cn|org)$';
    if re.match(r, addr):
        return True
    else :
        return False

# 练习2
# 可以提取出带名字的Email地址
def name_of_email(addr):
    reg = r'^<?([0-9a-zA-Z\s]*)>?([0-9a-zA-Z.\s]*)@([0-9a-zA-Z]*).(com|cn|org)$'
    g = re.match(reg, addr);
    if g!= None:
        return g.group(1);
    return None