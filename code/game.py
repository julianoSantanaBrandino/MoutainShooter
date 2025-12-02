#!/usr/bin/python
# -*- coding: utf-8 -*-
# import de pygame
import pygame

# Chamando o codigo Menu
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        # comando para iniciar o py game
        pygame.init()

        # inicializa a janela que iria mostrar o jogo ou algum grafico
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        # LOOP para manter a janela aberta
        while True:
            menu = Menu(self.window)
            menu_return=menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, "Level1",menu_return)
                level_return = level.run()

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass

