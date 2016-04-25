#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-25 23:12:05
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon


from flask import render_template

from . import auth


@auth.route('/login')
def login():
    return render_template('auth/login.html')
