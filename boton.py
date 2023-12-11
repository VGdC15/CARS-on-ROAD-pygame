import pygame
from constantesCar import *


class Boton(pygame.sprite.Sprite):
    def __init__(self, imagen_path, posicion, dimensiones):
        # Inicializa la clase base de pygame.sprite.Sprite
        super().__init__()

        # Carga la imagen del botón y la ajusta según las dimensiones proporcionadas
        self.imagen = pygame.image.load(imagen_path)
        self.imagen = pygame.transform.scale(self.imagen, dimensiones)

        # Obtiene el rectángulo de la imagen y establece sus coordenadas de posición
        self.rect = self.imagen.get_rect()
        self.rect.x, self.rect.y = posicion

        # Guarda la imagen original sin escalar en self.surface (no se utiliza en este código)
        self.surface = self.imagen
