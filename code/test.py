#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib

def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()

db = {}

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')

def login(username, password):
    pwd_md5 = get_md5(password + username + 'the-Salt')
    if db[username] == pwd_md5:
        print True
    else:
        print False

username = raw_input('input your name:')
password = raw_input('input your password:')

register(username, password)
login(username, password)
