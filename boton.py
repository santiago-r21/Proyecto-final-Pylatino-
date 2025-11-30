import Constantes
import pygame

boton_jugar = None
boton_salir = None


def cargar_botones():
    global boton_jugar
    global boton_salir

    original_jugar = pygame.image.load("Proyecto-final-Pylatino-/imagenes/Jugar.png").convert_alpha()
    original_salir = pygame.image.load("Proyecto-final-Pylatino-/imagenes/Salir.png").convert_alpha()
    boton_jugar = pygame.transform.scale(original_jugar, (Constantes.ANCHO_BOTON, Constantes.ALTO_BOTON))
    boton_salir = pygame.transform.scale(original_salir, (Constantes.ANCHO_BOTON, Constantes.ALTO_BOTON))
