#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        print 'self._path:{0}\tpath:{1}'.format(self._path, path)
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

print Chain().status.user.timeline.list

class Chain2(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        print 'self._path:{0}\tpath:{1}'.format(self._path, path)
        #返回一个完整的字符串作为新的Chain2的输入
        return Chain2('%s/%s' % (self._path, path))

    #返回用户看到的字符串  print
    def __str__(self):
        return self._path

    #返回开发者看到的字符串
    def __repr__(self):
        return self._path
    #因通常与__str__代码保持一致, 可以简写为
    #__repr__ = __str__

    def __call__(self, user):
        print 'self._path:{0}\tuser:{1}'.format(self._path, user)
        return Chain2('%s/%s' % (self._path, user))

print Chain2().users('michael').repos
