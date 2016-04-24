#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-21 21:24:59
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon


import os

from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app
from flask import send_from_directory


from . import main
from .forms import NameForm
from .. import db
from ..models import User
from ..email import send_email


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        # form.name.data = ''
        # 蓝本中, Flask会为端点加上命名空间, 使不同蓝本可用相同端点定义视图, 且无冲突
        # 空间为蓝本的名字(Blueprint构造函数的第一个参数)
        # 所以端点名是main1.index
        return redirect(url_for('main1.index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow)
