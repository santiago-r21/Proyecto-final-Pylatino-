import pygame

jugador_imagen = None
x = 0
y = 0


def cargarima():
    global jugador_imagen
    cursor_original = pygame.image.load("Proyecto-final-Pylatino-/imagenes/cursor.png").convert_alpha()
    nuevo_ancho = 100
    nuevo_alto = 100
    jugador_imagen = pygame.transform.scale(cursor_original, (nuevo_ancho, nuevo_alto))


def actposicion():
    global x, y
    if jugador_imagen:
        offset_x = jugador_imagen.get_width() // 2
        offset_y = jugador_imagen.get_height() // 2
        posicion_mouse = pygame.mouse.get_pos()
        x = posicion_mouse[0] - offset_x
        y = posicion_mouse[1] - offset_y
