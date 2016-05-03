#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-25 23:03:40
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon


import unittest

from app import create_app, db
from app.models import User


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        # 使用测试配置创建程序
        self.app = create_app('testing')
        # 激活上下文, 确保能在测试中使用current_app
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # u.username为空
    # 测试pw只写方法
    def test_password_setter(self):
        u = User(password='cat')
        self.assertTrue(u.password_hash is not None)

    # 测试pw只读方法, 使用u.password返回AttributeError
    def test_no_password_getter(self):
        u = User(password='cat')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verifycation(self):
        u = User(password='cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))

    def test_password_salts_are_random(self):
        u = User(password='cat')
        u2 = User(password='cat')
        self.assertTrue(u.password_hash != u2.password_hash)

    def test_confirmed(self):
        pass
