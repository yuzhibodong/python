#!/usr/bin/python
# -*- coding:utf-8 -*-
import functools
def log(text):
    if isinstance(text,str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print 'prog beginning...'
                print '%s %s...' % (text,func.__name__)
                func(*args,**kw)
                print 'prog endding...'
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args,**kw):
            print 'prog begging...'
            text(*args,**kw)
            print 'prog endding...'
        return wrapper
@log('execute')
def now(date):
    print date
now('20141107')
print '================================================'
@log
def today(date):
    print date
today('20141107')
