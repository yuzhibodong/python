#!flask/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2016-02-28 17:49:33
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon
# @Version : 1.0

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views
