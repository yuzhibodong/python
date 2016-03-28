#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-03-28 16:48:46
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

import pygame
from pygame.locals import *
from sys import exit
from lib.vec2d import *

background_image_filename = '../image/sushiplate.jpg'
sprite_image_filename = '../image/fugu.png'

pygame.init()

screen = pygame.display.set_mode((640, 480, 0, 32))

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()
