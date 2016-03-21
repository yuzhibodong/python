#!flask/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2016-02-28 17:49:33
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon
# @Version : 1.0

import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
# 定义哪个视图允许用户登陆 (不懂?)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models
