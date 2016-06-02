#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-21 23:17:20
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon


import os

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from app.models import User, Role, Permission, Post

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
# 导入的db开始为空对象, 上面create_app初始化完成
migrate = Migrate(app, db)


# 下列都用在(python xx.py ____)这里
# 注册app, db, User, Role
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Permission=Permission,
                Post=Post)


# shell 注册make_context回调函数, 自动导入app等对象
manager.add_command('shell', Shell(make_context=make_shell_context))
# 添加一个db命令
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    # 下列说明会在shell帮助中显示
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
