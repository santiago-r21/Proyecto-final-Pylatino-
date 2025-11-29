import pygame
import Constantes
import jugador
import boton
import topo
pygame.init()
pygame.font.init()
ventana = pygame.display.set_mode((Constantes.ancho, Constantes.alto))
run = True
tiempo = pygame.time.Clock()
background = pygame.image.load("imagenes/Menu.png").convert()
titulo = pygame.image.load("imagenes/Titulo.png")
Fondo = pygame.image.load("imagenes/Fondo.png").convert()
FondoJuego = pygame.transform.scale(Fondo, (Constantes.ancho, Constantes.alto))
jugador.cargarima()
topo.cargar_assets()
Ttopos = pygame.sprite.Group()
for i in range(len(topo.Posiciones_topos)):
    nuevo_topo = topo.Topo(i)
    Ttopos.add(nuevo_topo)
Puntos = 0
Puntaje = pygame.font.SysFont("comicsans", 40)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
DuracionP = 10000
global TiempoR
TiempoR = DuracionP
fuente_fin = pygame.font.SysFont("comicsans", 80, bold=True)
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
                estado = "JUGANDO"
                TiempoR = DuracionP
                Puntos = 0
            if btn_salir.collidepoint(pos_click):
                run = False  # Salir del bucle y del juego
        if estado == "JUGANDO" and event.type == pygame.MOUSEBUTTONDOWN:
            pos_click = event.pos
            for un_topo in Ttopos:
                if un_topo.rect.collidepoint(pos_click):
                    if un_topo.golpear():
                        Puntos += 10
        if estado == "FIN_JUEGO" and event.type == pygame.MOUSEBUTTONDOWN:
            pos_click = event.pos
            if btn_jugar.collidepoint(pos_click):

                TiempoR = DuracionP
                Puntos = 0
                estado = "JUGANDO"
                pygame.mouse.set_visible(0)
            if btn_salir.collidepoint(pos_click):
                run = False
    jugador.actposicion()
    tt = tiempo.get_time()
    ventana.blit(background, [0, 0])
    ventana.blit(titulo, [250, 80])

    if estado == "MENU":
        ventana.blit(background, [0, 0])
        ventana.blit(titulo, [250, 80])
        ventana.blit(boton.boton_jugar, btn_jugar.topleft)
        ventana.blit(boton.boton_salir, btn_salir.topleft)

    elif estado == "JUGANDO":
        ventana.blit(FondoJuego, [0, 0])
        TiempoR -= tt
        if TiempoR <= tt:
            TiempoR = 0
            estado = "FIN_JUEGO"
        Ttopos.update(tt)
        Ttopos.draw(ventana)
        segundos = int(TiempoR/1000)
        MostrarPuntaje = Puntaje.render(f"Tus Puntos: {Puntos}", True, NEGRO)
        ventana.blit(MostrarPuntaje, (10, 10))
        texto_tiempo = Puntaje.render(f"TIEMPO: {segundos}", True, NEGRO)
        x_tiempo = Constantes.ancho - texto_tiempo.get_width() - 10
        ventana.blit(texto_tiempo, (x_tiempo, 10))
    elif estado == "FIN_JUEGO":
        ventana.blit(Fondo, [0, 0])
        texto_fin = fuente_fin.render("¡TIEMPO AGOTADO!", True, NEGRO)
        x_fin = (Constantes.ancho / 2) - (texto_fin.get_width() / 2)
        ventana.blit(texto_fin, (x_fin, Constantes.alto / 4))
        texto_puntaje = Puntaje.render(f"PUNTUACIÓN FINAL: {Puntos}", True, NEGRO)
        x_puntaje = (Constantes.ancho / 2) - (texto_puntaje.get_width() / 2)
        ventana.blit(texto_puntaje, (x_puntaje, Constantes.alto / 2.5))
        ventana.blit(boton.boton_jugar, btn_jugar.topleft)
        ventana.blit(boton.boton_salir, btn_salir.topleft)
        if estado == "JUGANDO":
            ventana.blit(jugador.jugador_imagen, [jugador.x, jugador.y])
    ventana.blit(jugador.jugador_imagen, [jugador.x, jugador.y])
    pygame.display.flip()
    tiempo.tick(60)

pygame.quit()
