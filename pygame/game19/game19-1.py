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
    # tand等用的弧度
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
            edge_y = (y == 0 or y == CUBE_SIZE)

            for z in range(0, CUBE_SIZE + 1, 20):
                edge_z = (z == 0 or z == CUBE_SIZE)

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
    ball_center_x = ball_w / 2
    ball_center_y = ball_h / 2

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
        elif pressed_keys[K_RIGHT]:
            direction.x = +1.0

        if pressed_keys[K_UP]:
            direction.y = +1.0
        elif pressed_keys[K_DOWN]:
            direction.y = -1.0

        if pressed_keys[K_q]:
            direction.z = +1.0
        elif pressed_keys[K_a]:
            direction.z = -1.0

        if pressed_keys[K_w]:
            fov = min(179.0, fov+1.0)
            w = SCREEN_SIZE[0]
            # radians()角度转弧度
            viewing_distance = calculate_veiwing_distance(radians(fov), w)
        elif pressed_keys[K_s]:
            fov = max(1.0, fov-1.0)
            w = SCREEN_SIZE[0]
            viewing_distance = calculate_veiwing_distance(radians(fov), w)

        # 相机位置 = 方向 * 速度 * 时间
        camera_position += direction * camera_speed * time_passed_second

        # 绘制点
        for point in points:
            x, y, z = point - camera_position
            if z > 0:
                x = x * viewing_distance / z
                y = -y * viewing_distance / z
                x += center_x
                y += center_y
                screen.blit(ball, (x-ball_center_x, y-ball_center_y))

        # 绘制表
        diagram_width = SCREEN_SIZE[0] / 4
        col = (50, 255, 50)
        diagram_points = []
        diagram_points.append((diagram_width/2, 100+viewing_distance/4))
        diagram_points.append((0, 100))
        diagram_points.append((diagram_width, 100))
        diagram_points.append((diagram_width/2, 100+viewing_distance/4))
        diagram_points.append((diagram_width/2, 100))
        pygame.draw.lines(screen, col, False, diagram_points, 2)

        # 绘制文字
        white = (255, 255, 255)
        cam_text = font.render("camera = "+str(camera_position), True, white)
        screen.blit(cam_text, (5, 5))
        fov_text = font.render("field of view = %i" % int(fov), True, white)
        screen.blit(fov_text, (5, 35))
        txt = "viewing distance = %.3f" % viewing_distance
        d_txt = font.render(txt, True, white)
        screen.blit(d_txt, (5, 65))

        pygame.display.update()

if __name__ == '__main__':
    run()
