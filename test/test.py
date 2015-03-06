#!/usr/bin/env python
# -*- coding:utf-8 -*-

from email.mime.text import MIMEText

msg = MIMEText('hello, send by Python', _subtype='plain', _charset='utf-8')

from_addr = 'j5088794@163.com'
password = 'jhb5088794'

smtp_server = 'smtp.163.com'

to_addr = '357892250@qq.com'

import smtplib

server = smtplib.SMTP(host=smtp_server, port=25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
