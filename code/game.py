#!/usr/bin/python
# -*- coding: utf-8 -*-
# import de pygame
import pygame

# Chamando o codigo Menu
from code.menu import Menu


class Game:
    def __init__(self):
        # comando para iniciar o py game
        pygame.init()

        # inicializa a janela que iria mostrar o jogo ou algum grafico
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self, ):
        # Luping para manter a janela aberta
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # Check para todos os evento
        #    for event in pygame.event.get():
        # evento de fechar janela clicando no "x"
        #        if event.type == pygame.QUIT:
        #            pygame.quit()  # Fechar janela
        #           quit()  # End pygame
