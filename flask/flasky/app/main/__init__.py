#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-20 22:50:13
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

"""
创建蓝本
"""
from flask import Blueprint


# 蓝本名称, 蓝本所在包或模块
main = Blueprint(name='main1', import_name=__name__)

# 放到main下面, 防止循环导入?
from . import views, errors
from ..models import Permission


# 避免render_template()每次调用都添加一个模板参数
# 上下文处理器能让变量在所有模板中全局可访问s
@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
