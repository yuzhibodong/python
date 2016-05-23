#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-21 21:24:59
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon


from flask import render_template, abort

from . import main
from ..models import User


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)
