#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-18 20:46:58
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon


from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy

from config import config


# 初始化__init__内也是调用init_app()
# 此处先生成空对象
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # 原代码有, 但是init_app为空, 此时感觉没用
    # config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # 导入蓝本, 开始定义路由, 因为否则无法使用app.route等修饰器
    from .main import main as main_blueprint
    # 蓝本中定义的路由处于休眠状态, 直到蓝本注册到app上后, 路由才真正成为app的一部分
    app.register_blueprint(main_blueprint)

    # 附加路由和自定义的错误页面
    # 已被分解到main中

    return app
