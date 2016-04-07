#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-04-06 15:13:37
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

"""
完整AI程序
"""
import sys
sys.path.append('..')
from random import randint, choice

import pygame
from pygame.locals import *

from lib.vec2d import Vec2d


SCREEN_SIZE = (640, 480)
NEST_POSITION = (320, 240)
ANT_COUNT = 10
NEST_SIZE = 50.0


class GameEntity(object):
    """docstring for GameEntity"""

    def __init__(self, world, name, image):
        self.world = world
        self.name = name
        self.image = image
        self.location = Vec2d(0, 0)
        self.destination = Vec2d(0, 0)
        self.speed = 0.
        self.brain = StateMachine()
        self.id = 0

    def render(self, surface):
        x, y = self.location
        w, h = self.image.get_size()
        surface.blit(self.image, (x - w / 2, y - h / 2))

    def process(self, time_passed):
        self.brain.think()
        if self.speed > 0 and self.location != self.destination:
            vec_to_destination = self.destination - self.location
            distance_to_destination = vec_to_destination.get_length()
            heading = vec_to_destination.get_normalized()
            # 防止位移超出
            travel_distance = min(distance_to_destination,
                                  time_passed * self.speed)
            self.location += travel_distance * heading


class World(object):
    """docstring for World"""

    def __init__(self):
        self.entities = {}  # Store all the entities
        self.entity_id = 0  # Last entity id assigned
        # 画一个圈作为蚁穴
        self.background = pygame.surface.Surface(SCREEN_SIZE).convert()
        self.background.fill((255, 255, 255))
        pygame.draw.circle(
            self.background, (200, 255, 200), NEST_POSITION, int(NEST_SIZE))

    def add_entity(self, entity):
        # 增加一个新的实体
        self.entities[self.entity_id] = entity
        entity.id = self.entity_id
        self.entity_id += 1

    def remove_entity(self, entity):
        del self.entities[entity_id]

    def get(self, entity_id):
        # 通过id给出实体, 没有的话返回None
        if entity_id in self.entities:
            return self.entities['entity_id']
        else:
            return None

    def process(self, time_passed):
        # 处理世界中的每一个个体
        time_passed_seconds = time_passed / 1000.0
        for entity in self.entities.itervalue():
            entity.process(time_passed_seconds)

    def render(self, surface):
        # 绘制背景和每一个实体
        surface.blit(self.background, (0, 0))
        for entity in self.entities.values():
            entity.render(surface)

    def get_close_entity(self, name, location, range=100.0):
        # 通过一个范围寻找之内的所有实体
        location = Vec2d(*location)
        for entity in self.entities.values():
            if entity.name == name:
                distance = location.get_distance_to(entity.location)
                if distance < range:
                    return entity
        return None


class Ant(GameEntity):
    """docstring for Ant"""

    def __init__(self, world, image):
        # 执行基类构造方法
        super(Ant, self).__init__(self, world, "ant", image)
        # 创建各种状态
        exploring_state = AntStateExploring(self)
        seeking_state = AntStateSeeking(self)
        delivering_state = AntStateDelivering(self)
        hunting_state = AntStateHunting(self)
        self.brain.add_state(exploring_state)
        self.brain.add_state(seeking_state)
        self.brain.add_state(delivering_state)
        self.brain.add_state(hunting_state)
        self.carry_image = None

    def carry(self, image):
        self.carry_image = image

    def drop(self, surface):
        # 放下carry图像
        if self.carry_image:
            x, y = self.location
            w, h = self.carry_image.get_size()
            surface.blit(self.carry_image, (x - w, y - h / 2))
            self.carry_image = None

    def render(self, surface):
        # 先调用基类的render方法
        super(Ant, self).render(self, surface)
        # 额外绘制carry_image
        if self.carry_image:
            x, y = self.location
            w, h = self.carry_image.get_size()
            surface.blit(self.carry_image, (x - w, y - h / 2))


class State():
    """docstring for State"""

    def __init__(self, name):
        self.name = name

    def do_action(self):
        pass

    def check_conditions(self):
        pass

    def entry_actions(self):
        pass

    def exit_actions(self):
        pass


class StateMachine():
    """docstring for StateMachine"""

    def __init__(self):
        self.states = {}     # 存储状态
        self.active_state = None    # d当前有效状态

    def add_state(self, state):
        # 增加状态
        self.states[state.name] = state

    def think(self):
        if self.active_state is None:
            return
        # 执行有效状态的动作, 并做转移检查
        self.active_state.do_action()
        new_state_name = self.active_state.check_conditions()
        if new_state_name is not None:
            self.set_state(new_state_name)

    def set_state(self, new_state_name):
        # 更改状态, 执行进入/退出动作
        if self.active_state is not None:
            self.active_state.exit_actions()
        self.active_state = self.states[new_state_name]
        self.active_state.entry_actions()


class Leaf(GameEntity):
    """docstring for Leaf"""

    def __init__(self, world, image):
        super(Leaf, self).__init__(self, world, "leaf", image)


class Spider(GameEntity):
    """docstring for Spider"""

    def __init__(self, world, image):
        super(Spider, self).__init__(self, world, "spider", image)
        self.dead_image = pygame.transform.flip(image, 0, 1)
        self.health = 25
        self.speed = 50.0 + randint(-20, 20)

    def bitten(self):
        self.health -= 1
        if self.health <= 0:
            self.speed = 0.0
            self.image = self.dead_image
        self.speed = 140.0

    def render(self, surface):
        super.render(self, surface)
        x, y = self.location
        w, h = self.image.get_size()
        bar_x = x - 12
        bar_y = y + h / 2
        surface.fill((255, 0, 0), (bar_x, bar_y, 25, 4))
        surface.fill((0, 255, 0), (bar_x, bar_y, self.health, 4))

    def process(self, time_passed):
        x, y = self.location
        if x > SCREEN_SIZE[0] + 2:
            self.world.remove_entity(self)
            return
        super.process(self. time_passed)


def run():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0 ,32)
    world = World()
    w, h = SCREEN_SIZE
    clock = pygame.time.Clock
    ant_image = pygame.image.load('../image/ant.png').convert_alpha()
    leaf_image = pygame.image.load('../image/leaf.png').convert_alpha()
    spider_image = pygame.image.load('../image/spider.png').convert_alpha()

    for ant_no in range(ANT_COUNT:
        ant = Ant(world, ant_image)
        ant.location = Vec2d(randint(0, w), randint(0, h))
        ant.brain.set_state('exploring_state')
        world.add_entity(ant)

    while :
        pass
