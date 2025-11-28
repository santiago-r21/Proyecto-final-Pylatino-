import pygame
import Constantes
import jugador
import boton
import topo
pygame.init()
ventana = pygame.display.set_mode((Constantes.ancho, Constantes.alto))
run = True
tiempo = pygame.time.Clock()

background = pygame.image.load("imagenes/Menu.png").convert()
titulo = pygame.image.load("imagenes/Titulo.png")
jugador.cargarima()
topo.cargar_assets()
Ttopos = pygame.sprite.Group()
for i in range(len(topo.Posiciones_topos)):
    nuevo_topo = topo.Topo(i)
    Ttopos.add(nuevo_topo)
Puntos = 0
pygame.mouse.set_visible(0)
ESPACIO_ENTRE_BOTONES = 40
estado = "MENU"
boton.cargar_botones()
BOTON_H = (Constantes.ancho / 2) - (Constantes.ANCHO_BOTON / 2)-125
BOTON_V = (Constantes.alto * 0.85)
posBtn1 = BOTON_H
btn_jugar = pygame.Rect(posBtn1, BOTON_V, Constantes.ANCHO_BOTON, Constantes.ALTO_BOTON)
posBtn2 = BOTON_H+Constantes.ANCHO_BOTON+ESPACIO_ENTRE_BOTONES
btn_salir = pygame.Rect(posBtn2, BOTON_V, Constantes.ANCHO_BOTON, Constantes.ALTO_BOTON)
# !bucle ventana
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            # Se detecta si se hace click en menu
        if estado == "MENU" and event.type == pygame.MOUSEBUTTONDOWN:
            pos_click = event.pos  # posicion mouse
            if btn_jugar.collidepoint(pos_click):
                estado_juego = "JUGANDO"  # inicia el juega
            if btn_salir.collidepoint(pos_click):
                run = False  # Salir del bucle y del juego
        if estado == "JUGANDO" and event.type == pygame.MOUSEBUTTONDOWN:
            pos_click = event.pos
            for un_topo in Ttopos:
                if un_topo.rect.collideonpoint(pos_click):
                    if un_topo.golpear():
                        Puntos += 10

    jugador.actposicion()
    tt = tiempo.get_time()
    # posicion cursor
    ventana.blit(background, [0, 0])  # se muestra la imagen de fondo
    ventana.blit(titulo, [250, 80])

    if estado == "MENU":
        posicion_mouse = pygame.mouse.get_pos()
        ventana.blit(boton.boton_jugar, btn_jugar.topleft)

        ventana.blit(boton.boton_salir, btn_salir.topleft)
    elif estado == "JUGANDO":
        Ttopos.update(tt)
        Ttopos.draw(ventana)
    ventana.blit(jugador.jugador_imagen, [jugador.x, jugador.y])
    pygame.display.flip()
    tiempo.tick(60)
pygame.quit()
