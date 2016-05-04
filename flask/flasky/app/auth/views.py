#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-25 23:12:05
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon


from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required

from . import auth
from .. import db
from ..models import User
from ..email import send_email
from .forms import LoginForm, RegistrationForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # 验证表单, 然后尝试登入
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            # 要登录的用户 及 记住我 的值
            login_user(user, form.remember_me.data)
            # next中为 之前访问的未授权的URL, 存在request.args字典中
            return redirect(request.args.get('next') or url_for('main1.index'))
        # 输入有误, 提示如下Flash信息, 跳出if后再次渲染表单
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    # 调用Flask-Login的函数, 删除并重设会话
    logout_user()
    flash('You have benn logged out.')
    return redirect(url_for('main1.index'))


# 注册
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data, password=form.password.data)
        db.session.add(user)
        # 提交数据库后才生成ID, 所以不能延后自动提交, 需手动
        db.session.commit()
        # 生成token
        token = user.generate_confirmation_token()
        # 发送确认邮件
        send_email(user.email, 'Confirm Your Account',
                   'auth/email/confirm', user=user, token=token)
        flash('A confirmation email has been sent to you by email.')
        return redirect(url_for('main1.index'))
    return render_template('auth/register.html', form=form)
