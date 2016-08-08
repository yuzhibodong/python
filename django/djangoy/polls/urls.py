#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-08 15:37:12
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

from django.conf.urls import url

from .views import index

urlpatterns = [
    url(r'^$', index, name='index1')
]
