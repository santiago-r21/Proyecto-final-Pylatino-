import pygame
import random

Tiempo_asomado = 2000
Tiempo_escondido = 4000

topos = {}
Posiciones_topos = []


class Topo(pygame.sprite.Sprite):
    def __init__(self, posicion_id):
        super().__init__()

        self.posicion_id = posicion_id  # les damos una posicion
        x, y = Posiciones_topos[posicion_id]
        self.estado = "Escondido"
        self.image = topos["escondido"]  # le damos imagen inial y estado
        self.rect = self.image.get_rect(center=(x, y))
        self.tiempo_actual = 0  # tiempo del estado
        self.tiempo_cambio = random.randint(500, Tiempo_escondido)


def aparecer(self):
    self.estado = "Arriba"
    self.image = topos["arriba"]
    self.tiempo_actual = 0


def golpear(self):
    if self.estado == "Arriba":
        self.estado = "Golpeado"
        self.image = topos["golpeado"]
        self.tiempo_actual = 1000
        return True
    return False


def esconder(self):
    self.estado = "Escondido"
    self.image = topos["escondido"]
    self.tiempo_cambio = random.randint(500, Tiempo_escondido)
    self.tiempo_actual = 0


def update(self, tt):
    self.tiempo_actual += tt  # tiempo transcurrido
    if self.estado == "Arriba":
        if self.tiempo_actual >= Tiempo_asomado:
            self.esconder()
    elif self.estado == "Golpeado":
        if self.tiempo_actual >= 300:
            self.esconder()
    elif self.estado == "Escondido":
        if self.tiempo_actual >= self.tiempo_proximo_cambio:
            self.aparecer()


def cargar_assets():
    global IMAGENES_TOPO, POSICIONES_AGUJEROS
    #  Carga de Imágenes
    topos["escondido"] = pygame.image.load("imagenes/Topo_escondido.png").convert_alpha()
    topos["arriba"] = pygame.image.load("imagenes/Topo.png").convert_alpha()
    topos["golpeado"] = pygame.image.load("imagenes/Golpeado.png").convert_alpha()
    Posiciones_topos = [
        (200, 350),  # arriba izquierda
        (400, 350),  # centro arriba
        (600, 350),  # derecha arriba
        (200, 500),  # abajo izquierda
        (400, 500),  # centro abajo
        (600, 500),  # abajo derecha
    ]
