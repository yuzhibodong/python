#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-03-15 13:16:58
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon
# @Version : 1.0

'''
实现类似回弹效果
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
x, y = 100., 100.
# 速度(pixel/s)
speed_x, speed_y = 133., 170.

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, y))

    # 限制帧数为30帧
    # 默认为获取上一帧到现在的时间
    # 30为过了30帧后的时间
    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    x += speed_x * time_passed_seconds
    y += speed_y * time_passed_seconds

    if x > 640 - sprite.get_width():
        speed_x = -speed_x
        x = 640 - sprite.get_width()
    elif x < 0:
        speed_x = -speed_x
        x = 0.

    if y > 480 - sprite.get_height():
        speed_y = -speed_y
        y = 480 - sprite.get_height()
    elif y < 0:
        speed_y = -speed_y
        y = 0.

    pygame.display.update()
