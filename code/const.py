# C
from typing import Tuple

import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_WHIT = (255, 255, 255)
COLOR_GREEN = (0, 128, 0)
COLOR_CYAN = (0, 128, 128)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    "Level1Bg0": 1,
    "Level1Bg1": 2,
    "Level1Bg2": 3,
    "Level1Bg3": 4,
    "Level1Bg4": 5,
    "Level2Bg0": 0,
    "Level2Bg1": 1,
    "Level2Bg2": 2,
    "Level2Bg3": 2,
    "Level2Bg4": 2,
    "Player1": 3,
    "Player2": 3,
    "Enemy1": 7,
    "Enemy2": 6,
    "Player1shoot": 5,
    "Player2shoot": 5,

}
ENTITY_DAMAGE = {
    "Level1Bg0": 0,
    "Level1Bg1": 0,
    "Level1Bg2": 0,
    "Level1Bg3": 0,
    "Level1Bg4": 0,
    "Level2Bg0": 0,
    "Level2Bg1": 0,
    "Level2Bg2": 0,
    "Level2Bg3": 0,
    "Level2Bg4": 0,
    "Player1": 1,
    "Player2": 1,
    "Player1shoot": 10,
    "Player2shoot": 20,
    "Enemy1": 1,
    "Enemy2": 1,

}
ENTITY_SCORE = {
    "Level1Bg0": 0,
    "Level1Bg1": 0,
    "Level1Bg2": 0,
    "Level1Bg3": 0,
    "Level1Bg4": 0,
    "Level2Bg0": 0,
    "Level2Bg1": 0,
    "Level2Bg2": 0,
    "Level2Bg3": 0,
    "Level2Bg4": 0,
    "Player1": 0,
    "Player2": 0,
    "Player1shoot": 0,
    "Player2shoot": 0,
    "Enemy1": 100,
    "Enemy2": 125,

}

ENTITY_HEALTH = {
    "Level1Bg0": 999,
    "Level1Bg1": 999,
    "Level1Bg2": 999,
    "Level1Bg3": 999,
    "Level1Bg4": 999,
    "Level2Bg0": 999,
    "Level2Bg1": 999,
    "Level2Bg2": 999,
    "Level2Bg3": 999,
    "Level2Bg4": 999,
    "Player1": 300,
    "Player1shoot": 1,
    "Player2": 300,
    "Player2shoot": 1,
    "Enemy1": 50,
    "Enemy2": 60,

}
ENTITY_SHOOT_DELAY = {
    "Player1": 15,
    "Player2": 15,
    "Enemy1": 50,
    "Enemy2": 50,
}
# M
MENU_OPTION = ("NEW GAME 1P",
               "NEW GAME 2P - COOPERATIVE",
               "NEW GAME 2P - COMPETITIVE",
               "SCORE",
               "EXIT")

# P
PLAYER_KEY_UP = {"Player1": pygame.K_UP,
                 "Player2": pygame.K_w}

PLAYER_KEY_DOWN = {"Player1": pygame.K_DOWN,
                   "Player2": pygame.K_s}

PLAYER_KEY_LEFT = {"Player1": pygame.K_LEFT,
                   "Player2": pygame.K_a}

PLAYER_KEY_RIGHT = {"Player1": pygame.K_RIGHT,
                    "Player2": pygame.K_d}

PLAYER_KEY_SHOOT = {"Player1": pygame.K_SPACE,
                    "Player2": pygame.K_LCTRL}
# t
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 40000

# s
SPAWN_TIME = 500

# w
WIN_WIDTH = 576
WIN_HEIGHT = 324
