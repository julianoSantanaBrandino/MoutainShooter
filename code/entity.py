#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC

import pygame.image

from code.const import ENTITY_HEALT, ENTITY_DAMAGE, ENTITY_SCORE


def abstractmethhod(args):
    pass


class Entity(ABC):
    def __init__(self, name: str, position: tuple, ):
        self.name = name
        self.surf = pygame.image.load("./asset/" + name + ".png").convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALT[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]

        self.last_dmg = "None"

    @abstractmethhod
    def move(self, ):
        pass
