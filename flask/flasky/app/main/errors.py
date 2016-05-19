#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-21 21:12:38
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon


from flask import render_template
from . import main


@main.app_errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403


# errorhandler只有蓝本中错误才能触发
# app_errorhandler才能注册为全局的错误处理程序
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
