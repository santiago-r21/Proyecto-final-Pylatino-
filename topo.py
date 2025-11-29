import Constantes
import pygame
import random


Tiempo_asomado = 2000
Tiempo_escondido = 4000


topos = {}
Posiciones_topos = []


class Topo(pygame.sprite.Sprite):
    def __init__(self, posicion_id):
        super().__init__()

        self.posicion_id = posicion_id
        x, y = Posiciones_topos[posicion_id]
        self.estado = "Escondido"
        self.image = topos["escondido"]
        self.rect = self.image.get_rect(center=(x, y))
        self.tiempo_actual = 0
        self.tiempo_cambio = random.randint(500, Tiempo_escondido)

    def aparecer(self):
        self.estado = "Arriba"
        self.image = topos["arriba"]
        self.tiempo_actual = 0

    def golpear(self):
        if self.estado == "Arriba":
            self.estado = "Golpeado"
            self.image = topos["golpeado"]
            self.tiempo_actual = 0
            return True
        return False

    def esconder(self):
        self.estado = "Escondido"
        self.image = topos["escondido"]
        self.tiempo_cambio = random.randint(500, Tiempo_escondido)
        self.tiempo_actual = 0

    def update(self, tt):
        #  tiempo transcurrido
        self.tiempo_actual += tt
        if self.estado == "Arriba":
            if self.tiempo_actual >= Tiempo_asomado:
                self.esconder()
        elif self.estado == "Golpeado":
            if self.tiempo_actual >= 300:
                self.esconder()
        elif self.estado == "Escondido":
            if self.tiempo_actual >= self.tiempo_cambio:
                self.aparecer()


def cargar_assets():
    global topos, Posiciones_topos
    TamañoTopos = (Constantes.ANCHO_TOPO, Constantes.ALTO_TOPO)

    imgescondido = pygame.image.load("imagenes/Topo_escondido.png").convert_alpha()
    imgarriba = pygame.image.load("imagenes/Topo.png").convert_alpha()
    imggolpeado = pygame.image.load("imagenes/Golpeado.png").convert_alpha()
    topos["escondido"] = pygame.transform.scale(imgescondido, TamañoTopos)
    topos["arriba"] = pygame.transform.scale(imgarriba, TamañoTopos)
    topos["golpeado"] = pygame.transform.scale(imggolpeado, TamañoTopos)
    Posiciones_topos.extend([
        (200, 370),  # arriba izquierda
        (510, 370),  # centro arriba
        (830, 370),  # derecha arriba
        (200, 630),  # abajo izquierda
        (510, 630),  # centro abajo
        (830, 630),  # abajo derecha
    ])
