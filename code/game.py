#!/usr/bin/python
# -*- coding: utf-8 -*-
# import de pygame
import pygame

# Chamando o codigo Menu
from code.const import WIN_WIDTH, WIN_HEIGHT
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
            menu.run()
            pass


