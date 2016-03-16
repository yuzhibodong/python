#!flask/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2016-02-28 17:53:14
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon
# @Version : 1.0

from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, Im, oid
from .forms import LoginForm
from .models import User


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler  # 对Flask-OpenID声明是登陆函数
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template("login.html", title='Sign In', form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@Im.user_loader
def load_user(id):
    # id是unicode
    return User.query.get(int(id))


# resp参数传递给after_login, 包含从OpenID提供的返回信息
@oid.after_login
def after_login(resp):
    # 验证邮箱合法
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    # 从DB中搜索邮箱, 校验是否注册过
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        # 某些OpenID提供商没有nickname, 此处对此处理
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    # 设置默认
    remember_me = False
    # 从flask会话中加载r_m值
    if 'remember_me' in session:
        remember_me = session['remember_me']
        # 删除dict中的r_m, 如果没有, 返回None(默认KeyError)
        session.pop('remember_me', None)
    # 调用login_user注册此有效登陆
    login_user(user, remember=remember_me)
    # 如果next页未提供, 则重定向到首页
    return redirect(request.args.get('next') or url_for('index'))


# 辅助判断是否用户已登陆
# 任何使用before_request装饰器的函数在
# 接收请求前都会允许
@app.before_request
def before_request():
    # current_user是被Flask-Login设置的
    g.user = current_user
