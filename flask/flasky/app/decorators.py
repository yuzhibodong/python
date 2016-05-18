#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-05-17 11:18:14
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon


from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission


# 定义修饰器
def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)
