#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font


from code.const import WIN_HEIGHT, COLOR_WHITE, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME
from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 2000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity("Level1Bg"))
        self.entity_list.append(EntityFactory.get_entity("Player1"))

        if game_mode in[MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity("Player2"))

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)




    def run(self,):
        pygame.mixer_music.load(f"./asset/{self.name}.mp3")
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(("Enemy1", "Enemy2"))
                    self.entity_list.append(EntityFactory.get_entity(choice))



            pygame.display.flip()
        pass


