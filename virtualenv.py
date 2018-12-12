#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name:virtualenv and 图形界面

# virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。
# 
# virtualenv是如何创建“独立”的Python运行环境的呢？
# 原理很简单，就是把系统Python复制一份到virtualenv的环境，用命令source venv/bin/activate进入一个virtualenv环境时，
# virtualenv会修改相关环境变量，让命令python和pip均指向当前的virtualenv环境。
 




# name: 图形界面
# Tkinter:Python自带的图形界面库

# 第一个GUI程序
from tkinter import *
# 在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
# pack()方法把Widget加入到父容器中，并实现布局。
# pack()是最简单的布局，grid()可以实现更复杂的布局。
class Application(Frame):
	def __init__(self, master = None):
		Frame.__init__(self,master)
		self.pack();
		self.createWidgets();
	def createWidgets(self):
		self.helloLabel = Label(self, text='Hello, World!')
		self.helloLabel.pack();
		self.quitBtn = Button(self, text='Quit', command=self.quit)
		self.quitBtn.pack();
# app = Application();
# app.master.title('Hello World')
# app.mainloop();

# 输入文本
# 加入一个文本框，让用户可以输入文本，然后点按钮后，弹出消息对话框。
import tkinter.messagebox as messagebox
class ApplicationToInput(Frame):
	def __init__(self, master=None):
		Frame.__init__(self,master);
		self.pack();
		self.createWidgets();

	def createWidgets(self):
		self.nameInput = Entry(self);
		self.nameInput.pack();
		self.alertBtn = Button(self, text='Hello', command=self.hello);
		self.alertBtn.pack();
	def hello(self):
		name = self.nameInput.get() or 'World';
		messagebox.showinfo('Message', 'Hello, %s' % name);
app_in = ApplicationToInput();
app_in.master.title('Hello World');
app_in.mainloop()
# 当用户点击按钮时，触发hello()，通过self.nameInput.get()获得用户输入的文本后，使用tkMessageBox.showinfo()可以弹出消息对话框。
		