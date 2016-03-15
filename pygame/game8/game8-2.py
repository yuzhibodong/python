#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-03-15 13:16:58
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon
# @Version : 1.0

'''
通过s=vt 方法, 限制显示效果
这种通过实践控制要不直接调节帧率效果好
每秒移动250pixel, 刷新快的机子, 返回时间小
每次移动慢, 核心就是将移动与时间挂钩,
不与帧率挂钩, 就可以造成恒定的显示效果
'''

import pygame
from pygame.locals import *
from sys import exit


background_image_filename = '../image/sushiplate.jpg'
sprite_image_filename = '../image/fugu.png'

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

# Clock对象
clock = pygame.time.Clock()

# sprite的起始x坐标
x = 0.
# 速度(pixel/s)
speed = 250.

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, 100))

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    distance_moved = time_passed_seconds * speed
    x += distance_moved

    # 如果移动出屏幕, 搬到开始位置继续
    if x > 640:
        x -= 640.

    pygame.display.update()
