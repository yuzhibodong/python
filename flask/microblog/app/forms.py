#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-02 22:41:04
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
