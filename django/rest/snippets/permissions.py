#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2016-10-18 18:12
# @Author   : Bluethon (j5088794@gmail.com)
# @Link     : http://github.com/bluethon

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


