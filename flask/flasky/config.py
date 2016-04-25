#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-17 14:09:52
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

import os


# 当前文件的目录(文件夹名称)的绝对路径
basedir = os.path.abspath(os.path.dirname(__file__))


# 基类, 包含通用配置
class Config:
    # 防止CSRF, wtf使用的密匙
    SECRET_KEY = os.environ.get(
        'SECRET_KEY', default=None) or 'hard to guess string'
    # True, 每次请求结束, 自动提交数据库中变动
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 邮件标题前缀
    FLASKY_MAIL_SUBJECT_PREFIX = '[FLASKY]'
    # 发送者
    FLASKY_MAIL_SENDER = 'Flasky Admin <j5088794@163.com>'
    # 管理员, 接收者
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN', default='j5088794@163.com')

    # 如果设置成True，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存
    # 2.1中默认None, 未来默认False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 基类为空
    # 配置类可以实例化, 执行对当前环境变量的配置初始化
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', default=None)
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', default=None)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or (
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite'))


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or (
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite'))


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or (
        'sqlite:///' + os.path.join(basedir, 'data.sqlite'))


# config字典注册不同的配置环境
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
