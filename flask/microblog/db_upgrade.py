#!flask/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2016-03-09 23:04:32
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' +
      str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)))
