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
from flask_login import UserMixin, AnonymousUserMixin

from . import db
from . import login_manager


class Permission:
    """ 权限常量 """
    FOLLOW = 0x01               # 关注其他用户
    COMMENT = 0x02              # 在他人撰写的文章中发布评论
    WRITE_ARTICLES = 0x04       # 写文章
    MODERATE_COMMENTS = 0x08    # 查处他人的不当评论
    ADMINISTER = 0x80           # 管理网站


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 创建用户默认属于哪个角色, 该角色此处为True,
    # 只有一个角色的default字段需要设为True
    default = db.Column(db.Boolean, default=False, index=True)
    # 权限, 用一个整型, 表示位标志, '0b 0000 0000'
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    # 静态方法, 类方法, 与实例无关, built-in函数, 不默认传入self
    @staticmethod
    def insert_roles():
        roles = {
            # 位或操作
            'User': (Permission.FOLLOW |
                     Permission.COMMENT |
                     Permission.WRITE_ARTICLES, True),
            'Moderator': (Permission.FOLLOW |
                          Permission.COMMENT |
                          Permission.WRITE_ARTICLES |
                          Permission.MODERATE_COMMENTS, False),
            'Administrator': (0xff, False)
        }
        # 查询角色是否存在, 不存在则创建, 即更新操作
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            # roles字典中key=r, value是个tuple, tuple中第一个, 即位或值
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name


# 继承UserMinxin, 里面包含了is_authenticated等的默认实现
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    # 是否邮件激活
    confirmed = db.Column(db.Boolean, default=False)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        # 若基类未定义角色
        if self.role is None:
            # 根据邮箱自动设为管理员
            if self.email == current_app.config['FLASKY_ADMIN']:
                self.role = Role.query.filter_by(permissions=0xff).first()
            # 否则设为默认角色(由角色default属性决定)
            if self.role is None:
                self.role = Role.query.filter_by(default=True)

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

    def can(self, permissions):
        """ 用户角色权限与 Permission.xx 验证 """
        # 位与操作
        return self.role is not None and \
            (self.role.permissions & permissions) == permissions

    # 检查管理员权限功能常用, 单独实现
    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    @property
    def __repr__(self):
        return '<User %r>' % self.username


# 一致性考虑, 实现匿名用户的验证方法
class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        False

    def is_administrator(self):
        False

# 匿名用户设为未登录时current_user的值
login_manager.anonymous_user = AnonymousUser


# 加载用户的回调函数
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
