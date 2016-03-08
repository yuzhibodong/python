#!flask/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2016-03-08 21:18:09
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

import imp
from migrate.versioning import api
from app import db
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO


migration = SQLALCHEMY_MIGRATE_REPO + '/versions/%03d_migration.py' % (
    api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO) + 1)
tmp_module
