#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-03-28 16:48:46
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

'''
使用向量实现方向键控制图片移动
'''

import sys
sys.path.append('..')
import pygame
from pygame.locals import *
from sys import exit
from lib.vec2d import *

background_image_filename = '../image/sushiplate.jpg'
sprite_image_filename = '../image/fugu.png'

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

sprite_pos = Vec2d(200, 150)
sprite_speed = 300.

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pressed_keys = pygame.key.get_pressed()

    key_direction = Vec2d(0, 0)
    if pressed_keys[K_LEFT]:
        key_direction.x = -1
    if pressed_keys[K_RIGHT]:
        key_direction.x = 1
    if pressed_keys[K_DOWN]:
        key_direction.y = 1
    if pressed_keys[K_UP]:
        key_direction.y = -1

    key_direction.normalized()

    screen.blit(background, (0, 0))
    screen.blit(sprite, sprite_pos)

    time_passed = clock.tick(30)
    time_passed_second = time_passed / 1000.0

    sprite_pos += key_direction * sprite_speed * time_passed_second

    pygame.display.update()
