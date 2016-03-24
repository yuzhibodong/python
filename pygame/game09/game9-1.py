#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-03-18 14:24:57
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

'''
向量
'''
import math

# 向量定义


class Vector2(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    @classmethod
    def from_points(cls, p1, p2):
        return cls(p2[0] - p1[0], p2[1] - p1[1])

# 计算两点间向量
A = (10.0, 20.0)
B = (30.0, 35.0)
AB = Vector2.from_points(A, B)
print(AB)


# 大小
def get_magnitude(self):
    return math.sqrt(self.x**2 + self.y**2)


# 单位向量
def normalize(self):
    magnitude = self.get_magnitude()
    self.x /= magnitude
    self.y /= magnitude


# 加减
# "__"一般意为重载
def __add__(self, rhs):
    return Vector2(self.x + rhs.x, self.y + rhs.y)


def __sub__(self, rhs):
    return Vector2(self.x - rhs.x, self.y - rhs.y)


# 乘除
# 意为缩放倍数
def __mul__(self, scalar):
    return Vector2(self.x * scalar, self.y * scalar)


def __div__(self, scalar):
    return Vector2(self.x / scalar, self.y / scalar)
