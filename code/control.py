#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect, font

from code.const import WIN_WIDTH, WIN_HEIGHT, COLOR_WHITE, COLOR_ORANGE, COLOR_YELLOW, COLOR_BLACK, COLOR_BLUE, \
    COLOR_RED


class Controls:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mouse.set_visible(False)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            self.window.blit(source=self.surf, dest=self.rect)

            # --- ESCREVE AS INSTRUÇÕES ---
            # Título
            self.draw_text("CONTROLS", 40, COLOR_YELLOW, (WIN_WIDTH / 2, 50))

            # Player 1
            self.draw_text("PLAYER 1 (DRAGON BLUE):", 25, COLOR_BLACK, (WIN_WIDTH / 2, 100))
            self.draw_text("Move: Arrow Keys (Up, Down, Left, Right)", 20, COLOR_BLUE, (WIN_WIDTH / 2, 125))
            self.draw_text("Shoot: Space Bar ", 20, COLOR_BLUE, (WIN_WIDTH / 2, 145))

            # Player 2
            self.draw_text("PLAYER 2 (DRAGON RED):", 25, COLOR_BLACK, (WIN_WIDTH / 2, 180))
            self.draw_text("Move: W, A, S, D", 20, COLOR_RED, (WIN_WIDTH / 2, 205))
            self.draw_text("Shoot: Left CTRL", 20, COLOR_RED, (WIN_WIDTH / 2, 225))

            # Voltar
            self.draw_text("Press ESC or ENTER to return", 15, COLOR_ORANGE, (WIN_WIDTH / 2, WIN_HEIGHT - 30))

            pygame.display.flip()

            # --- VERIFICA EVENTOS PARA SAIR ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # Se apertar ESC ou ENTER, sai do loop e volta pro Menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                        return  # Retorna para o game.py

    def draw_text(self, text, size, color, center_pos):
        # Função auxiliar para desenhar texto centralizado
        text_font = font.SysFont("Lucida Sans Typewriter", size)
        text_surf = text_font.render(text, True, color)
        text_rect = text_surf.get_rect(center=center_pos)
        self.window.blit(text_surf, text_rect)