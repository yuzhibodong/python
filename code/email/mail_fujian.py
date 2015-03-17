#!/usr/bin/env python
# -*- coding:utf-8 -*-

from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib
import Base64

#格式化邮件地址, 如果邮件地址包含中文, 需要通过Header对象进行编码
def _format_addr(s):
    name, addr = parseaddr(s)
    #isinstance 判断变量是否为某个类型
    return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = 'j5088794@163.com'
password = 'jhb5088794'
to_addr = '357892250@qq.com'
smtp_server = 'smtp.163.com'

# 邮件对象
msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
# msg['To'] 接收的是字符串而不是list, 如果有多个地址 用,分隔即可
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候......', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', _subtype='plain', _charset='utf-8'))

# 添加附件就是加上一个MIMEBase, 从本地读取一个图片:
with open('/home/blue/github/python/code/email/20.jpg', 'rb') as f:
    # 设置附件的MIME和文件名:
    mime = MIMEBase('image', 'jpg', filename='20.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='20.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
<<<<<<< HEAD:code/email/mail_fujian.py
    # 添加到MIMEMultipart:
    msg.attach(mime)
=======
>>>>>>> c15a71aaad79c0029538eafa68dcbf268d1cbffe:code/email/mail_附件.py

server = smtplib.SMTP(host=smtp_server, port=25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
