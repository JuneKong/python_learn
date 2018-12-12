#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name:访问数据库

# *****使用SQLite*****
# SQLite是一种嵌入式数据库，它的数据库就是一个文件。
# 表是数据库中存放关系数据的集合
# 一个数据库里面通常都包含多个表
# 表和表之间通过外键关联。
# 
# 要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；
# 连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。
# Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。
import sqlite3
# 创建表和插入数据
# conn = sqlite3.connect('test.db');
# cursor = conn.cursor();
# # 执行SQL语句
# cursor.execute('create table student (id varchar(20) primary key, name varchar(20))');
# cursor.execute('insert into student (id, name) values (\'1\', \'Michael\')');
# row = cursor.rowcount;
# cursor.close();
# conn.commit();
# conn.close();

# # 查询记录
# cursor.execute('select * from user where id=?', ('1',));
# # 获得查询结果集:
# val = cursor.fetchall();
# print(val);
# cursor.close();
# conn.commit();
# conn.close();
# **Connection和Cursor对象，打开后一定记得关闭
# 使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。
# 使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
# 如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数， 用and连接
# 'select * from user where name=? and pwd=?', ('abc', 'password')

# sql语句
# 用 DESC 表示按倒序排序(即：从大到小排序) ---降序排列
# 用 ACS   表示按正序排序(即：从小到大排序)---升序排列

# *****使用MySQL*****
# 
# MySQL 与 SQLite 的区别：
# SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用。
# 而MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite。
# import mysql.connector
# con = mysql.connector.connect(user='root', password='root', database='test');
# cur = con.cursor();
# cur.execute('create table people (id varchar(20) primary key, name varchar(20))');
# #  插入一行记录，
# #  **注意MySQL的占位符是%s:
# #  
# #  删除数据表
# # cur.execute("DROP TABLE IF EXISTS people")
# cur.execute('insert into people (id, name) values (%s, %s)', ['1', 'Michael']);
# cur.rowcount;
# con.commit();

# cur = con.cursor();
# cur.execute('select * from people where id = %s', ('1',))
# value = cur.fetchall()
# print(value);
# cur.close();
# con.close();

# *****使用SQLAlchemy*****
# ORM框架：Object-Relational Mapping，把关系数据库的表结构映射到对象上。
# 在Python中，最有名的ORM框架是SQLAlchemy。
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 完成SQLAlchemy的初始化和具体每个表的class定义:
Base = declarative_base();
class Poeple(Base):
	__tablename__ = 'people';

	id = Column(String(20), primary_key=True)
	name = Column(String(20))

# create_engine()用来初始化数据库连接。
# **SQLAlchemy用一个字符串表示连接信息：
# **'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:root@localhost:8080/test')
# DBSession对象可视为当前数据库连接。
DBSession = sessionmaker(bind=engine);

# 创建
session = DBSession();
new = Poeple(id='3', name='Bob');
# 添加
session.add(new);
session.commit();
session.close();

session = DBSession();
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
people = session.query(Poeple).filter(Poeple.id=="3").one();
print('type:', type(people))
print('name:', people.name)
session.close();