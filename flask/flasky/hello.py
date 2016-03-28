#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-22 22:26:37
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap


# Flask类的构造函数必填参数只有一个, 即程序主模块或包的名字
# 在大多数情况下, Python的__name__变量即为所需值
# Flask用此参数决定程序的根目录, 以便找资源文件的相对位置
app = Flask(__name__)

# 命令行可执行启动参数
manager = Manager(app)
# 用户界面插件
bootstrap = Bootstrap(app)


# 程序实例需要知道对每个URL请求运行哪些代码, 所以保存一个URL到Python函数的映射关系
# 处理URL和函数间关系的程序称为路由
# 使用修饰器把函数注册为事件的处理程序
@app.route('/')
# 视图函数(view function)
def index():
    return render_template('index.html')


# 动态路由
# 默认使用字符串
# Flask支持使用int, float, path类型
# path类型也是字符串, 只是不把斜线视作分隔符, 而是当做动态片段的一部分
# eg: /user/<int:id> 只匹配片段id为整数的URL
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# 自定义错误页面
# 404, 客户端请求未知页面或路由
@app.errorhandler(404)
def page_not_found(e):
    # 除正常返回响应外, 还返回与该错误对应的数字状态码
    return render_template('404.html'), 404


# 500, 有未处理的异常
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# 此处写法确保执行这个脚本时才启动开发服务器
if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()
