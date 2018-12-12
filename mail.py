#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name:电子邮件

# MUA：Mail User Agent——邮件用户代理。
# MTA：Mail Transfer Agent——邮件传输代理
# MDA：Mail Delivery Agent——邮件投递代理
# 过程
# 发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人
# 
# 发邮件时，MUA和MTA使用的协议就是SMTP：Simple Mail Transfer Protocol
# 收邮件时，MUA和MDA使用的协议有两种：
# POP：Post Office Protocol，目前版本是3，俗称POP3；
# IMAP：Internet Message Access Protocol，优点是不但能取邮件，还可以直接操作MDA上存储的邮
# 
# **特别注意，目前大多数邮件服务商都需要手动打开SMTP发信和POP收信的功能，否则只允许在网页登录

# *****SMTP发送邮件*****
# 可以发送纯文本邮件、HTML邮件以及带附件的邮件
# Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
from email.mime.text import MIMEText
msg = MIMEText("hello, As the saying that nobody's life goes on well all the time, so we will meet some difficulties sometimes. When we meet the setback, we are easy to feel lost. We have to face the hard time and learn from the experience, so that we will grow up. If we never give up, we can realize our dreams someday. ...", 'plain', 'utf-8');
# MIMEText() => 第一个参数就是邮件正文，
#               第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，
#               最后一定要用utf-8编码保证多语言兼容性。

from_addr = input('from: ')
password = input('password: ')
to_addr = input('to: ')
smtp_server = input('STMP server: ')

#发送邮箱地址
msg['from'] = from_addr
#收件箱地址
msg['to'] = to_addr
#主题
msg['subject'] = 'the frist mail'

import smtplib


# 注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码
from email.header import Header

# 发送HTML邮件
# 在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了
# m = MIMEText(html字符串,'html', 'utf-8')
m = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8');

# 发送附件
# 带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，
# 可以构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，
# 再继续往里面加上表示附件的MIMEBase对象即可
from email import encoders
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
# 格式化邮件信息
def _format_addr(s):
    name, addr = parseaddr(s);
    return formataddr(Header(name, 'utf-8').encode(), addr);
massage = MIMEMultipart();
massage['From'] = from_addr
massage['To'] = to_addr
massage['Subject'] = Header('来自SMTP的问候','utf-8').encode()
# 邮件正文是MIMEText
massage.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'));
# 附件MIMEBase
with open('D:/dmImage/a.jpg','rb') as f:
	mi = MIMEBase('image','jpg', filename='a.jpg')
	# 加上必要的头信息:
	mi.add_header('Content-Disposition', 'attachment', filename='test.png')
	mi.add_header('Content-ID', '<0>')
	mi.add_header('X-Attachment-Id', '0')
	# 把附件的内容读进来:
	mi.set_payload(f.read())
	encoders.encode_base64(mi);
	massage.attach(mi);

# **发送邮件
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1); # set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
server.login(from_addr, password) # login()方法用来登录SMTP服务器
# sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], massage.as_string())
server.quit();

# 发送图片
# 大部分邮件服务商都会自动屏蔽带有外链的图片，因为不知道这些链接是否指向恶意网站。
# 要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。
# 如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。

# 同时支持HTML和Plain格式
# 当无法查看HTML格式时，可降为查看plain 
# 在发送HTML的同时再附加一个纯文本，如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件。
# **要注意指定subtype是alternative
# msg = MIMEMultipart('alternative')

# 加密SMTP
# 加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。
# 只需要在创建SMTP对象后，立刻调用starttls()方法，就创建了安全连接。后面的代码和前面的发送邮件代码完全一样


# 继承关系
# Message
# +- MIMEBase
#    +- MIMEMultipart
#    +- MIMENonMultipart
#       +- MIMEMessage
#       +- MIMEText
#       +- MIMEImage


# *****POS3收取邮件*****
# 收取邮件就是编写一个MUA作为客户端，从MDA把邮件获取到用户的电脑或者手机上
import poplib
# **注意到POP3协议收取的不是一个已经可以阅读的邮件本身，而是邮件的原始文本，这和SMTP协议很像，SMTP发送的也是经过编码后的一大段文本。
# 因此，收取邮件分两步：
# 第一步：用poplib把邮件的原始文本下载到本地；
# 第二部：用email解析原始文本，还原为邮件对象。

# 要获取所有邮件，只需要循环使用retr()把每一封邮件内容拿到即可。
# 真正麻烦的是把邮件的原始内容解析为可以阅读的邮件对象。

# 通过POP3下载邮件
# 见pop3.py

# 解析邮件
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr