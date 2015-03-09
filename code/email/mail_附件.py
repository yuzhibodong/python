#!/usr/bin/env python
# -*- coding:utf-8 -*-

from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
import smtplib

#格式化邮件地址, 如果邮件地址包含中文, 需要通过Header对象进行编码
def _format_addr(s):
    name, addr = parseaddr(s)
    #isinstance 判断变量是否为某个类型
    return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = 'j5088794@163.com'
password = 'jhb5088794'
to_addr = '357892250@qq.com'
smtp_server = 'smtp.163.com'

msg = MIMEText('<html><body><h1>Hello</h1>' + '<p>send by <a href="http://www.python.org">Python</a>...</p>' + '</body></html>', _subtype='html', _charset='utf-8')
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
# msg['To'] 接收的是字符串而不是list, 如果有多个地址 用,分隔即可
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来着SMTP的问候...', 'utf-8').encode()

server = smtplib.SMTP(host=smtp_server, port=25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
