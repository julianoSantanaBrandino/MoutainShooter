#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOOT_DELAY
from code.entity import Entity
from code.playerShot import PlayerShoot


class Player(Entity):
    def __init__(self, name: str, postion: tuple):
        super().__init__(name, postion)
        self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

        pass

    def shoot(self):
        self.shoot_delay -= 1
        if self.shoot_delay == 0:
            pressed_key = pygame.key.get_pressed()
            self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]
            key_shoot = PLAYER_KEY_SHOOT[self.name]

            if pressed_key[key_shoot]:
                # Reseta o tempo de recarga
                self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]
                if self.name == "Player1":
                    pos1 = (self.rect.right - 10, self.rect.centery - 10)
                    shoot1 = PlayerShoot(name=f"{self.name}shoot", position=pos1)
                    pos2 = (self.rect.right - 15, self.rect.centery)
                    shoot2 = PlayerShoot(name=f"{self.name}shoot", position=pos2)
                    return [shoot1, shoot2]

                elif self.name == "Player2":
                    pos3 = (self.rect.right - 15, self.rect.centery)
                    shoot3 = PlayerShoot(name=f"{self.name}shoot", position=pos3)
                    return [shoot3]
