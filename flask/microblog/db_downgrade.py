#!flask/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2016-03-10 21:11:00
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO


v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)
print('Current database version: ' + str(api.db_version(
    SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)))
