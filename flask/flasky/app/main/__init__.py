#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-20 22:50:13
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

"""
创建蓝本
"""
from flask import Blueprint


#               蓝本名称, 蓝本所在包或模块
main = Blueprint('main', __name__)

from . import views, errors


