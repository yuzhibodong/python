#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-04-15 10:08:04
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

"""
3D效果
"""
import sys
sys.path.append('..')
from math import tan
from random import randint

import pygame
from pygame.locals import *
from lib.vec3d import Vec3d


SCREEN_SIZE = (640, 480)
CUBE_SIZE = 300


# 计算视距, fov为视角大小
def calculate_veiwing_distance(fov, screen_width):
    d = (screen_width / 2.0) * tan(fov / 2.0)
    return d


def run():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0)

    # 获取系统字体
    default_font = pygame.font.get_default_font()
    # 创建字体对象
    font = pygame.font.SysFont(default_font, 24)

    ball = pygame.image.load('../image/ball.png').convert_alpha()

    # 3D points()
    points = []

    # Field of view
    fov = 90.0
    viewing_distance = calculate_veiwing_distance(fov, SCREEN_SIZE[0])

    # 边沿的一系列点
    for x in range(0, CUBE_SIZE + 1, 20):
        edge_x = (x == 0 or x == CUBE_SIZE)

        for y in range(0, CUBE_SIZE + 1, 20):
            edge_y = (y == 0 or y=CUBE_SIZE)

            for z in range(0, CUBE_SIZE + 1, 20):
                edge_z = (z == 0 or z=CUBE_SIZE)

                if sum((edge_x, edge_y, edge_z)) >= 2:
                    point_x = float(x) - CUBE_SIZE / 2
                    point_y = float(y) - CUBE_SIZE / 2
                    point_z = float(z) - CUBE_SIZE / 2

                    points.append(Vec3d(point_x, point_y, point_z))

    # 以z序存储, 类似于css中的z-index
    def point_z(point):
        return point.z
    points.sort(key=point_z, reverse=True)

    center_x, center_y = SCREEN_SIZE
    center_x /= 2
    center_y /= 2

    ball_w, ball_h = ball.get_size()
    ball_center_x = ball_w /= 2
    ball_center_y = ball_h /= 2

    camera_position = Vec3d((0.0, 0.0, -700.0))
    camera_speed = Vec3d((300.0, 300.0, 300.0))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.fill((0, 0, 0))

        pressed_keys = pygame.key.get_pressed()

        time_passed = clock.tick()
        time_passed_second = time_passed / 1000.0

        direction = Vec3d()
        if pressed_keys[K_LEFT]:
            direction.x = -1.0
