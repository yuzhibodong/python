#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-04-21 15:19:40
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

"""
模拟小球下落的声音模拟
"""

import sys
sys.path.append('..')
from random import randint

import pygame
from pygame.locals import *

from lib.vec2d import Vec2d


SCREEN_SIZE = (640, 480)
# 重力因子, 单位 pixel/s*s
GRAVITY = 250.0
# 弹力系数, 反弹后剩余的能量, 不超过1
BOUNCINESS = 0.7


class Sprite(object):
    """docstring for Sprite"""

    def __init__(self):
        super(Sprite, self).__init__()

    def render(self):
        w, h = self.image.get_size()

        x, y = self.position
        x -= w / 2
        y -= h / 2
        return (x, y, w, h)


class Ball(Sprite):
    """docstring for Ball"""

    def __init__(self, position, speed, image, bounce_sound):
        super(Ball, self).__init__()
        self.position = Vec2d(position)
        self.speed = Vec2d(speed)
        self.image = image
        self.bounce_sound = bounce_sound
        self.age = 0.0

    def update(self, time_passed):
        x, y, w, h = super(Ball, self).render()
        screen_width, screen_height = SCREEN_SIZE
        # 是否反弹
        bounce = False

        # 判断是否碰壁
        if y + h >= screen_height:
            self.speed.y = -self.speed.y * BOUNCINESS
            self.position.y = screen_height - h / 2.0 - 1.0
            bounce = True
        if x + w >= screen_width:
            self.speed.x = -self.speed.x * BOUNCINESS
            self.position.x = screen_width - w / 2.0 - 1.0
            bounce = True
        elif x < 0:
            self.speed.x = -self.speed.x * BOUNCINESS
            self.position.x = w / 2.0 + 1.0
            bounce = True

        # s = vt 计算当前位置
        self.position += self.speed * time_passed
        # 根据重力计算速度
        self.speed.y += GRAVITY * time_passed

        if bounce:
            self.play_bounce_sound()

        self.age += time_passed

    def play_bounce_sound(self):
        channel = self.bounce_sound.play()

        if channel is not None:
            # 设置左右声道音量
            left, right = stero_pan(self.position.x, SCREEN_SIZE[0])
            channel.set_volume(left, right)

    def render(self, surface):
        x, y = super(Ball, self).render()[:2]
        surface.blit(self.image, (x, y))


def stero_pan(x_coord, screen_width):
    """根据求位置决定播放左右声道的音量"""
    right_volume = float(x_coord) / screen_width
    left_volume = 1.0 - right_volume
    return (left_volume, right_volume)


def run():
    # 初始化声音
    pygame.mixer.pre_init(44100)
    pygame.init()
    pygame.mixer.set_num_channels(8)
    screen = pygame.display.set_mode(SCREEN_SIZE, 0)

    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()

    ball_image = pygame.image.load('../media/balls.png').convert_alpha()
    mouse_image = pygame.image.load('../media/mousecursor.png').convert_alpha()

    # 加载声音文件
    bounce_sound = pygame.mixer.Sound('../media/bounce.ogg')
    balls = []

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == MOUSEBUTTONDOWN:
                # 给球初速度
                random_speed = (randint(-400, 400), randint(-300, 0))
                new_ball = Ball(
                    event.pos, random_speed, ball_image, bounce_sound)
                balls.append(new_ball)

        time_passed_seconds = clock.tick() / 1000.0
        screen.fill((255, 255, 255))
        # 防止球过多, 超时的去除
        dead_balls = []
        for ball in balls:
            ball.update(time_passed_seconds)
            ball.render(screen)
            # 设置超时时限
            if ball.age > 10.0:
                dead_balls.append(ball)
        for ball in dead_balls:
            balls.remove(ball)

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(mouse_image, mouse_pos)
        pygame.display.update()

if __name__ == '__main__':
    run()
