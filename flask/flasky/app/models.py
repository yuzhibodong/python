#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-21 23:24:27
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon


# 使用Werkzeug中security模块实现 密码散列
from werkzeug.security import generate_password_hash, check_password_hash
# 令牌
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# 用于登陆
from flask import current_app
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


# 继承UserMinxin, 里面包含了
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    # 是否邮件激活
    confirmed = db.Column(db.Boolean, default=False)

    # 只读属性, 密码散列, 原密码不存在, 返回错误
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    # 只写属性, 设置密码
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 校验密码的hash, 返回True即密码正确
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # 注册 生成token, 默认有效1h
    def generate_confirmation_token(self, expiration=3600):
        # 创建序列化器
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        # 用当然用户ID生成token
        return s.dumps({'confirm': self.id})

    # 注册 确认
    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            # 还原数据
            data = s.loads(token)
        except:
            return False
        # 检查ID是否已存在db中, token被破, 也无法确认他人账户
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    # 重置密码 生成token
    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id})

    # 重置密码 设置新密码
    def reset_password(self, token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_password
        db.session.add(self)
        return True

    # 更换邮箱 生成token
    def generate_email_change_token(self, new_email, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'change_email': self.id, 'new_email': new_email})

    # 更换邮箱
    def change_email(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        db.session.add(self)
        return True

    def __repr__(self):
        return '<User %r>' % self.username


# 加载用户的回调函数
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
