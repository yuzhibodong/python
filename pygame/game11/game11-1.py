#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-04-01 15:45:50
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

'''
鼠标+方向控制鱼
'''

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
from math import *


background_image_filename = '../image/sushiplate.jpg'
sprite_image_filename = '../image/fugu.png'

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

# 让pygame完全控制鼠标
pygame.mouse.set_visible(False)
pygame.event.get_gral(True)

sprite_pos = Vec2d(200, 150)
sprite_speed = 300.
sprite_rotation = 0.
sprite_rotation_speed = 360.

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        # Esc退出游戏
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()

    pressed_keys = pygame.key.get_pressed()
    # 获取鼠标按键
    pressed_mouse = pygame.mouse.get_pressed()

    rotation_direction = 0.
    movement_direction = 0.

    # 通过移动偏移量计算移动
    rotation_direction = pygame.mouse.get_rel()[0] / 5.0

    if pressed_keys[K_LEFT]:
        rotation_direction = +1.
    if pressed_keys[K_RIGHT]:
        rotation_direction = -1.
    # 增加鼠标左键判断
    if pressed_keys[K_UP] or pressed_mouse[0]:
        movement_direction = +1.
    if pressed_keys[K_RIGHT] or pressed_mouse[2]:
        movement_direction = -1.

    screen.blit(background, (0, 0))

    rotated_sprite = pygame.transform(sprite, sprite_rotation)
    w, h = rotated_sprite.get_size()
    sprite_draw_pos = Vec2d(sprite_pos.x-w/2, sprite_pos.y-h/2)
    screen.blit(rotated_sprite, sprite_draw_pos)

    time_passed = clock.tick()
    time_passed_second = time_passed / 1000.0

    sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_second

    heading_x = sin(sprite_rotation*pi/180.)
    heading_y = cos(sprite_rotation*pi/180.)
    heading = Vec2d(heading_x, heading_y)
    heading *= movement_direction

    sprite_pos += heading * sprite_speed * time_passed_second

    pygame.display.update()
