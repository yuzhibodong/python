#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-03-03 16:47:29
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon
# @Version : 1.0

import pygame
from pygame.locals import *
from sys import exit


pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

color1 = (221, 99, 20)
color2 = (96, 130, 51)
factor = 0.


def blend_color(color1, color2, blend_factor):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    r = r1 + (r2 - r1) * blend_factor
    g = g1 + (g2 - g1) * blend_factor
    b = b1 + (b2 - b1) * blend_factor
    return int(r), int(g), int(b),

while True:

    for event in pygame.event.get():
        if event.ty:
            pass
