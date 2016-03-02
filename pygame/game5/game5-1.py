#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-03-01 14:12:09
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon
# @Version : 1.0

import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))

all_colors = pygame.Surface((4096, 4096), depth=24)

for r in range(256):
    print(r + 1, "out of 256")
    # 下列2种方法等价%16
    x = (r & 15) * 256
    y = (r >> 4) * 256
    for g in range(256):
        for b in range(256):
            all_colors.set_at((x + g, y + b), (r, g, b))

pygame.image.save(all_colors, "allcolors.bmp")
