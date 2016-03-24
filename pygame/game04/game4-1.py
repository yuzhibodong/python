#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-02-25 14:22:15
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon
# @Version : 1.0

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

font = pygame.font.SysFont("汉仪中等线简", 40)
# font = pygame.font.Font("simsun.ttc", 40)
text_surface = font.render(u"你好", True, (0, 0, 255))


x = 0
y = (480 - text_surface.get_height())/2

background = pygame.image.load("sushiplate.jpg").convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))

    x -= 0.5  # 调节文字滚动速度
    if x < -text_surface.get_width():
        x = 640 - text_surface.get_width()

    screen.blit(text_surface, (x, y))

    pygame.display.update()
