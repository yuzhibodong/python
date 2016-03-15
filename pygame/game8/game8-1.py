#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-03-15 13:16:58
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon
# @Version : 1.0

background_image_filename = '../image/sushiplate.jpg'
sprite_image_filename = '../image/fugu.png'

import pygame
from pygame.locals import *
from sys import exit


pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

# sprite的起始x坐标
x = 0.

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, 100))
    x += 1.         # 如果性能太好看不清, 调小数字

    # 如果移动出屏幕, 搬到开始位置继续
    if x > 640:
        x = 0.

    pygame.display.update()

