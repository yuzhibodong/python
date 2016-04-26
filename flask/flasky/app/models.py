#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-21 23:24:27
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon


# 使用Werkzeug中security模块实现 密码散列
from werkzeug.security import generate_password_hash, check_password_hash
# 用于登陆
from flask.ext.login import UserMixin

from . import db
from . import login_manager


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    # 设置密码
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 校验密码的hash, 返回True即密码正确
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username


# 加载用户的回调函数?
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
