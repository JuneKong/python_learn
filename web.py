#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name:Web开发


# *****使用Web框架*****
# 比较流行的Web框架——Flask来使用。
# 
# 处理3个URL，分别是：
# GET /：首页，返回Home；
# GET /signin：登录页，显示登录表单；
# POST /signin：处理登录表单，显示登录结果。
# **注意噢，同一个URL/signin分别有GET和POST两种请求，映射到两个处理函数中。
# 
# **Flask通过Python的装饰器在内部自动地把URL和函数给关联起来
from flask import Flask
from flask import request

app = Flask(__name__);

@app.route('/', methods=['GET', 'POST'])
def home():
	return '<h1>Home</h1>';

@app.route('/signin', methods=['GET'])
def signin_form():
	return '''<form action="/signin" method="post">
				<p><input name="username"></p>
				<p><input name="password" type="password"></p>
				<p><button type="submit">Sign In</button></p>
			  </form>''';

@app.route('/signin', methods=['POST'])
def signin():
	# 需要从request对象读取表单内容
	if request.form['username'] == 'admin' and request.form['password'] == 'password':
		return '<h3>Hello, admin!</h3>';
	return '<h3>Bad username or password</h3>';

if __name__ == '__main__':
	app.run();

# Django框架
# => Django 自带的后台管理系统，方便对于文章、用户及其他动态内容的管理
# => 文章分类、标签、浏览量统计以及规范的 SEO 设置
# => 用户认证系统，在 Django 自带的用户系统的基础上扩展 Oauth 认证，支持微博、Github 等第三方认证
# => 文章评论系统，炫酷的输入框特效，支持 markdown 语法，二级评论结构和回复功能
# => 信息提醒功能，登录和退出提醒，收到评论和回复提醒，信息管理
# => 强大的全文搜索功能，只需要输入关键词就能展现全站与之关联的文章
# => RSS 博客订阅功能及规范的 Sitemap 网站地图
# => django-redis 支持的缓存系统，遵循缓存原则，加速网站打开速度
# => 实用的在线工具
# => 友情链接和推荐工具网站的展示




# *****使用模板*****
# MVC：Model-View-Controller，中文名“模型-视图-控制器”。
# 处理URL的函数就是C：Controller，Controller负责业务逻辑，比如检查用户名是否存在，取出用户信息等等；
# 包含变量{{ name }}的模板就是V：View，View负责显示逻辑，通过简单地替换一些变量，View最终输出的就是用户看到的HTML。
# Model是用来传给View的，这样View在替换变量的时候，就可以从Model中取出相应的数据。

# Flask通过render_template()函数来实现模板的渲染。
from flask import render_template

# 使用模板的另一大好处是，模板改起来很方便，而且，改完保存后，刷新浏览器就能看到最新的效果，这对于调试HTML、CSS和JavaScript的前端工程师来说实在是太重要了。