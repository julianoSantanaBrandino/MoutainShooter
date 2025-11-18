# import de pygame
import pygame

# comando para iniciar o py game
pygame.init()

# inicializa a janela que iria mostrar o jogo ou algum grafico
window = pygame.display.set_mode(size=(600, 480))

# Luping para manter a janela aberta
while True:
    # Check para todos os evento
    for event in pygame.event.get():
        # evento de fechar janela clicando no "x"
        if event.type == pygame.QUIT:
            pygame.quit()  # Fechar janela
            quit()  # End pygame
