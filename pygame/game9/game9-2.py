#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-03-22 13:50:46
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

'''
使用向量的游戏动画demo
小鱼在鼠标周围游动, 若即若离
'''
import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2


background_image_filename = '../image/sushiplate.jpg'
sprite_image_filename = '../image/fugu.png'

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygamel.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

position = Vector2(100.0, 100.0)
heading = Vector2()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, position)

    time_passed = clock.tick()
    time_passed_second = time_passed / 1000.0

    # 参数前加*意味着把列表或元组展开
    destination = Vector2(*pygame.mouse.get_pos()) - \
        Vector2(*sprite.get_size()) / 2
    # 计算鱼当前位置到鼠标位置的向量
    vector_to_mouse = Vector2.from_points(position, destination)
    # 向量规格化
    vector_to_mouse.normalize()

    # 这个heading可以看做是鱼的速度, 但是由于这样的运算, 鱼的速度就不断改变了
    # 在没有到达鼠标时, 加速运动, 超过则减速. 因而鱼会在鼠标附近晃动
    heading = heading + (vector_to_mouse * 0.6)

    position += heading * time_passed_second
    pygame.display.update()
