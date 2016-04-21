#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-21 21:12:38
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon


from flask import render_template
from . import main


# errorhandler只有蓝本中错误才能出发
# app_errorhandler才能注册位全局错误处理程序
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
