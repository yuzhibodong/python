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
from random import randint

import pygame
from pygame.locals import *

from lib.vec2d import Vec2d


SCREEN_SIZE = (640, 480)
NEST_POSITION = (320, 240)
ANT_COUNT = 20
NEST_SIZE = 100.0


class State():
    """docstring for State"""

    def __init__(self, name):
        self.name = name

    def do_actions(self):
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
        self.active_state = None    # 当前有效状态

    def add_state(self, state):
        # 增加状态
        self.states[state.name] = state

    def think(self):
        if self.active_state is None:
            return
        # 执行有效状态的动作, 并做转移检查
        self.active_state.do_actions()
        new_state_name = self.active_state.check_conditions()
        if new_state_name is not None:
            self.set_state(new_state_name)

    def set_state(self, new_state_name):
        # 更改状态, 执行进入/退出动作
        if self.active_state is not None:
            # 退出当前活动状态
            self.active_state.exit_actions()
        # 将新状态设为活动
        self.active_state = self.states[new_state_name]
        # 进入
        self.active_state.entry_actions()


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
            heading = vec_to_destination.normalized()
            # 防止位移超出
            travel_distance = min(distance_to_destination,
                                  time_passed * self.speed)
            self.location += travel_distance * heading


class World(object):
    """docstring for World"""

    def __init__(self):
        self.entities = {}  # Store all the entities
        self.entity_id = 0  # Last entity id assigned
        # 创建一个surface
        self.background = pygame.Surface(SCREEN_SIZE).convert()
        self.background.fill((255, 255, 255))
        # 画一个圈作为蚁穴, int(半径)
        pygame.draw.circle(
            self.background, (200, 255, 200), NEST_POSITION, int(NEST_SIZE))

    def add_entity(self, entity):
        # 增加一个新的实体
        self.entities[self.entity_id] = entity
        entity.id = self.entity_id
        self.entity_id += 1

    def remove_entity(self, entity):
        del self.entities[entity.id]

    def get(self, entity_id):
        # 通过id给出实体, 没有的话返回None
        if entity_id in self.entities:
            return self.entities[entity_id]
        else:
            return None

    def process(self, time_passed):
        # 处理世界中的每一个个体
        time_passed_seconds = time_passed / 1000.0
        for entity in list(self.entities.values()):
            entity.process(time_passed_seconds)

    def render(self, surface):
        # 绘制背景和每一个实体
        surface.blit(self.background, (0, 0))
        for entity in self.entities.values():
            entity.render(surface)

    def get_close_entity(self, name, location, range=100.0):
        # 通过一个范围寻找之内的所有实体
        location = Vec2d(*location)
        for entity in list(self.entities.values()):
            # entity中找所有name相等的
            if entity.name == name:
                distance = location.get_distance(entity.location)
                if distance < range:
                    return entity
        return None


class Leaf(GameEntity):
    """docstring for Leaf"""

    def __init__(self, world, image):
        super(Leaf, self).__init__(world, 'leaf', image)


class Spider(GameEntity):
    """docstring for Spider"""

    def __init__(self, world, image):
        super(Spider, self).__init__(world, 'spider', image)
        # 死亡图像 为y向反转图片
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
        super(Spider, self).render(surface)
        x, y = self.location
        w, h = self.image.get_size()
        bar_x = x - 12
        bar_y = y + h / 2
        # 绘制红色背景条
        surface.fill((255, 0, 0), (bar_x, bar_y, 25, 4))
        # 绘制绿色血条
        surface.fill((0, 255, 0), (bar_x, bar_y, self.health, 4))

    def process(self, time_passed):
        x, y = self.location
        if x > SCREEN_SIZE[0] + 2:
            self.world.remove_entity(self)
            return
        super(Spider, self).process(time_passed)


class Ant(GameEntity):
    """docstring for Ant"""

    def __init__(self, world, image):
        # 执行基类构造方法
        super(Ant, self).__init__(world, 'ant', image)
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
        super(Ant, self).render(surface)
        # 额外绘制carry_image
        if self.carry_image:
            x, y = self.location
            w, h = self.carry_image.get_size()
            surface.blit(self.carry_image, (x - w, y - h / 2))


class AntStateExploring(State):
    """docstring for AntStateExploring"""

    def __init__(self, ant):
        super(AntStateExploring, self).__init__('exploring')
        self.ant = ant

    def random_destination(self):
        w, h = SCREEN_SIZE
        # 窗口内随机一点定为目的地
        self.ant.destination = Vec2d(randint(0, w), randint(0, h))

    def do_actions(self):
        if randint(1, 20) == 1:
            self.random_destination()

    def check_conditions(self):
        # 查找范围内是否有叶子
        leaf = self.ant.world.get_close_entity('leaf', self.ant.location)
        if leaf is not None:
            self.ant.leaf_id = leaf.id
            return 'seeking'
        # 查找巢穴内是否有蜘蛛
        spider = self.ant.world.get_close_entity(
            'spider', NEST_POSITION, NEST_SIZE)
        if spider is not None:
            if self.ant.location.get_distance(spider.location) < 100.0:
                self.ant.spider_id = spider.id
                return 'hunting'
        return None

    def entry_actions(self):
        self.ant.speed = 120.0 + randint(-30, 30)
        self.random_destination()


class AntStateSeeking(State):
    """docstring for AntStateSeeking"""

    def __init__(self, ant):
        super(AntStateSeeking, self).__init__('seeking')
        self.ant = ant
        self.leaf_id = None

    def check_conditions(self):
        leaf = self.ant.world.get(self.ant.leaf_id)
        if leaf is None:
            return 'exploring'
        if self.ant.location.get_distance(leaf.location) < 5.0:
            self.ant.carry(leaf.image)
            self.ant.world.remove_entity(leaf)
            return 'delivering'

    def entry_actions(self):
        leaf = self.ant.world.get(self.ant.leaf_id)
        if leaf is not None:
            self.ant.destination = leaf.location
            self.ant.speed = 160.0 + randint(-20, 20)


class AntStateDelivering(State):
    """docstring for AntStateDelivering"""

    def __init__(self, ant):
        super(AntStateDelivering, self).__init__('delivering')
        self.ant = ant

    def check_conditions(self):
        if Vec2d(*NEST_POSITION).get_distance(self.ant.location) \
                < NEST_SIZE:
            if (randint(1, 10) == 1):
                self.ant.drop(self.ant.world.background)
                return 'exploring'

        return None

    def entry_actions(self):
        self.ant.speed = 60.0
        random_offset = Vec2d(randint(-20, 20), randint(-20, 20))
        self.ant.destination = Vec2d(*NEST_POSITION) + random_offset


class AntStateHunting(State):
    """docstring for AntStateHunting"""

    def __init__(self, ant):
        super(AntStateHunting, self).__init__('hunting')
        self.ant = ant
        self.got_kill = False

    def do_actions(self):
        spider = self.ant.world.get(self.ant.spider_id)
        if spider is None:
            return
        self.ant.destination = spider.location
        if self.ant.location.get_distance(spider.location) < 15.0:
            if randint(1, 5) == 1:
                spider.bitten()
                # 蜘蛛死亡处理
                if spider.health <= 0.0:
                    self.ant.carry(spider.image)
                    self.ant.world.remove_entity(spider)
                    self.got_kill = True

    def check_conditions(self):
        if self.got_kill:
            return 'delivering'
        spider = self.ant.world.get(self.ant.spider_id)
        if spider is None:
            return 'exploring'
        # 离开巢穴3倍距离, 放弃攻击
        if spider.location.get_distance(NEST_POSITION) > NEST_SIZE * 3:
            return 'exploring'
        return None

    def entry_actions(self):
        self.speed = 160.0 + randint(0, 50)

    def exit_actions(self):
        self.got_kill = False


def run():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    world = World()
    w, h = SCREEN_SIZE
    clock = pygame.time.Clock()
    ant_image = pygame.image.load('../image/ant.png').convert_alpha()
    leaf_image = pygame.image.load('../image/leaf.png').convert_alpha()
    spider_image = pygame.image.load('../image/spider.png').convert_alpha()

    for ant_no in range(ANT_COUNT):
        ant = Ant(world, ant_image)
        ant.location = Vec2d(randint(0, w), randint(0, h))
        ant.brain.set_state('exploring')
        world.add_entity(ant)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        # 还是读取帧间隔时间, 但是限制最高30fps
        time_passed = clock.tick(30)

        if randint(1, 10) == 1:
            leaf = Leaf(world, leaf_image)
            leaf.location = Vec2d(randint(0, w), randint(0, h))
            world.add_entity(leaf)

        if randint(1, 100) == 1:
            spider = Spider(world, spider_image)
            spider.location = Vec2d(-50, randint(0, h))
            spider.destination = Vec2d(w + 50, randint(0, h))
            world.add_entity(spider)

        world.process(time_passed)
        world.render(screen)

        pygame.display.update()

if __name__ == '__main__':
    run()
