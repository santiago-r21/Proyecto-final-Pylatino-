import pygame
import Constantes

pygame.init()
ventana = pygame.display.set_mode((Constantes.ancho, Constantes.alto))
run = True
while run:
    for event in pygame.event.get():
        if event.type:
            if event.type == pygame.QUIT:
                run = False
pygame.quit()
