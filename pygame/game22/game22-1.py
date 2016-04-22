#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-04-22 10:13:52
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

"""
音乐播放器
"""

import os
import os.path
from math import sqrt

import pygame
from pygame.locals import *


SCREEN_SIZE = (800, 600)
MUSIC_PATH = r'E:\jhb\MUSIC'


def get_music(path):
    # 从文件夹读取所有文件
    raw_filenames = os.listdir(path)

    music_files = []
    for filename in raw_filenames:
        if filename.lower().endswith('.ogg') or \
                filename.lower().endswith('.mp3'):
            music_files.append(os.path.join(MUSIC_PATH, filename))

    return sorted(music_files)


class Button(object):
    """docstring for Button"""

    def __init__(self, image_filename, position):

        self.image = pygame.image.load(image_filename)
        self.position = position

    def render(self, surface):
        x, y = self.position
        w, h = self.image.get_sieze()
        x -= w / 2
        y -= h / 2
        surface.blit(self.image, (x, y))

    def is_over(self, point):
        # 若point在自身范围内, 返回True
        point_x, point_y = point

        x, y = self.position
        w, h = self.image.get_size()
        x -= w / 2
        y -= h / 2
        int_x = point_x >= x and point <= x + w
        int_y = point_y >= y and point <= y + h
        return int_x and int_y


def run():

    pygame.mixer.init(44100)
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0)

    default_font = pygame.font.get_default_font()
    font = pygame.font.SysFont(default_font, 50)

    x = 100
    y = 240
    button_width = 150
    buttons = {}
    buttons['prev'] = Button('prev.png', (x, y))
    buttons['pause'] = Button('prev.png', (x + button_width * 1, y))
    buttons['stop'] = Button('stop.png', (x + button_width * 2, y))
    buttons['play'] = Button('prev.png', (x + button_width * 3, y))
    buttons['next'] = Button('next.png', (x + button_width * 4, y))

    music_filenames = get_music(MUSIC_PATH)
    if len(music_filenames) == 0:
        print('No music files found in ', MUSIC_PATH)
        return

    white((255, 255, 255))
    label_surfaces = []
    # 一系列的文件名render
    for filename in music_filenames:
        txt = os.path.split(filename)[-1]
        print('Track:', txt)
        # zh-cn下Windows的文件编码, 酌情调整
        txt = txt.split('.')[0].decode('gb2312')
        # 2nd 抗锯齿
        surface = font.render(txt, True, (100, 0, 100))
        label_surfaces.append(surface)

    current_track = 0
    max_tracks = len(music_filenames)
    pygame.mixer.music.load(music_filenames[current_track])

    clock = pygame.time.Clock()
    playing = False
    paused = False

    # 所有事件类型都有类型标识符(int), 用户自定义的应大于等于USEREVENT
    TRACK_END = USEREVENT + 1
    pygame.mixer.music.set_endevent(TRACK_END)

    while True:

        button_pressed = None

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == MOUSEBUTTONDOWN:
                for button_name, button in buttons.iteritems():
                    if button.is_over(event.pos):
                        print(button_name, 'pressed')
                        button_pressed = button_name
                        break
            if event.type == TRACK_END:
                # 歌曲结束, 模拟按'next'
                button_pressed = 'next'

        if button_pressed is not None:
            if button_pressed == 'next':
                # 全部循环
                current_track = (current_track + 1) % max_tracks
                pygame.mixer.music.load(music_filenames[current_track])
                if playing:
                    pygame.mixer.music.play()
            elif button_pressed == 'prev':
                # 已经播放超过3s, 则重新播放, 否则上一曲
                if pygame.mixer.music.get_pos() > 3000:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.play()
                else:
                    current_track = (current_track - 1) % max_tracks
                    pygame.mixer.music.load(music_filenames[current_track])
                    if playing:
                        pygame.mixer.music.play()
            elif button_pressed == 'pause':
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True

            elif button_pressed == 'stop':
                pygame.mixer.music.stop()
                playing = False
            elif button_pressed == 'play':
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    if not playing:
                        pygame.mixer.music.play()
                        playing = True

        screen.fill(white)

