#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-22 22:26:37
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

from flask import Flask

# Flask类的构造函数必填参数只有一个, 即程序主模块或包的名字
# 在大多数情况下, Python的__name__变量即为所需值
# Flask用此参数决定程序的根目录, 以便找资源文件的相对位置
app = Flask(__name__)


# 程序实例需要知道对每个URL请求运行哪些代码, 所以保存一个URL到Python函数的映射关系
# 处理URL和函数间关系的程序称为路由
# 使用修饰器把函数注册为事件的处理程序
@app.route('/')
# 视图函数(view function)
def index():
    return '<h1>Hello World!</h1>'


# 动态路由
# 默认使用字符串
# Flask支持使用int, float, path类型
# path类型也是字符串, 只是不把斜线视作分隔符, 而是当做动态片段的一部分
# eg: /user/<int:id> 只匹配片段id为整数的URL
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

# 此处写法确保执行这个脚本时才启动开发服务器
if __name__ == '__main__':
    app.run(debug=True)
