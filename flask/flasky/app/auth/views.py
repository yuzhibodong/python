#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-25 23:12:05
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon


from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required, \
    current_user

from . import auth
from .. import db
from ..models import User
from ..email import send_email
from .forms import LoginForm, RegistrationForm, ChangePasswordForm


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
    flash('You have been logged out.')
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
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
# 要去已登录
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main1.index'))
    if current_user.confirm(token):
        flash('You have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('main1.index'))


# @auth.before_request钩子针对属于anth蓝本的请求
# @auth.before_app_request钩子针对全局请求
# 拦截满足以下条件的请求
# 在调用原请求的视图函数前先执行如下函数
@auth.before_app_request
def before_request():
    if current_user.is_authenticated \
            and not current_user.confirmed \
            and request.endpoint[:5] != 'auth.' \
            and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirmed'))


# 处理未激活的账户
@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main1.index'))
    return render_template('auth/unconfirmed.html')


@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Confirm Your Account',
               'auth/email/confirm', user=current_user, token=token)
    flash('A new confirmation email has been sent to you by email.')
    return redirect(url_for('main1.index'))


# 修改密码
@auth.route('/change-password', methods=['POST', 'GET'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data
            db.session.add(current_user)
            flash('Your password has been updated.')
            return redirect(url_for('main1.index'))
        else:
            flash('Invalid password.')
    return render_template('auth/change_password.html', form=form)
