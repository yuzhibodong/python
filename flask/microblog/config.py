#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-02 22:18:09
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

CSRF_ENABLED = True
SECRET_KEY = '123'

# OPENID_PROVIDERS = [
#     {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
#     {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
#     {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
#     {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
#     {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Flask-SQLAlchemy扩展必须, 数据库文件路径
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# SQLAlchemy-migrate数据文件存放地址
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
