#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-27 20:57:17
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon


from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

from ..models import User


class LoginForm(Form):
    email = StringField(
        'Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegistrationForm(Form):
    email = StringField(
        'Email', validators=[Required(), Length(1, 64), Email()])
    # Regexp后两个参数: 旗标 和 验证失败显示的错误消息
    username = StringField('Username', validators=[Required(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, numbers, dots or underscores')])
    # EqualTo验证器中, 另一个字段pass2作为参数传入
    password = PasswordField('Password', validators=[
        Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            # 自定义验证函数, 抛出的VE异常, 参数即为错误消息
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
