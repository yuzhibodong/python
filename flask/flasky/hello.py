#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-22 22:26:37
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

from flask import Flask, render_template, session, redirect, url_for, flash
from flask.ext.script import Manager, Server
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


# Flask类的构造函数必填参数只有一个, 即程序主模块或包的名字
# 在大多数情况下, Python的__name__变量即为所需值
# Flask用此参数决定程序的根目录, 以便找资源文件的相对位置
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

# 命令行可执行启动参数
manager = Manager(app)
# 调试模式
# manager.add_command("runserver", Server(use_debugger=True))

# 用户界面插件
bootstrap = Bootstrap(app)
# 本地化时间
moment = Moment(app)


# 定义表单类
class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


# 程序实例需要知道对每个URL请求运行哪些代码, 所以保存一个URL到Python函数的映射关系
# 处理URL和函数间关系的程序称为路由
# 使用修饰器把函数注册为事件的处理程序
@app.route('/', methods=['GET', 'POST'])
# 视图函数(view function)
def index():
    # 加入datetime变量
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.datass
        return redirect(url_for('index'))
        form.name.data = ''
    return render_template('index.html', form=form, name=session.get('name'))


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
