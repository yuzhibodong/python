#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

# AF_INET指定使用IPv4协议, AF_INET6->IPv6
# SOCK_STREAM指定使用面向流的TCP协议
# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接 参数是一个tuple
s.connect(('www.sina.com.cn', 80))

# 发送数据:
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnetion: close\r\n\r\n')

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)

# 关闭连接:
s.close()

header, html = data.split('\r\n\r\n', 1)
print header
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)
