import sys
import pygame
from pygame import *
from constantesCar import *

class Entrada():
    def __init__(self) -> None:
        # Inicializa las variables de la clase
        self.lineas = 0  
        self.caracteres = [' ',]  
        self.fuente = pygame.font.SysFont('Bauhaus 93', 30)  

        # Configuraciones de posición y distancia entre líneas
        self.distancia = 20
        self.posx = 50
        self.posy = 50

    def teclas(self, evento):
        # Maneja eventos de teclado
        for accion in evento:
            if accion.type == KEYDOWN:
                if accion.key == K_RETURN:
                    # Cuando se presiona Enter, agrega una nueva línea si la longitud actual es menor que 4
                    if len(self.caracteres[self.lineas]) < 4:
                        self.caracteres.append('')
                        self.lineas += 1
                elif accion.key == K_BACKSPACE:
                    # Cuando se presiona Backspace, elimina el último caracter o la última línea si está vacía
                    if self.caracteres[self.lineas] == '' and self.lineas > 0:
                        self.caracteres = self.caracteres[0:-1]
                        self.lineas -= 1
                    else:
                        self.caracteres[self.lineas] = self.caracteres[self.lineas][0:-1]
                else:
                    # Cuando se presiona cualquier otra tecla, agrega el carácter a la línea actual si la longitud es menor que 4
                    if len(self.caracteres[self.lineas]) < 4:
                        self.caracteres[self.lineas] = str(self.caracteres[self.lineas] + accion.unicode)

    def mensaje(self, surface):
        # Dibuja un rectángulo blanco en la superficie para mostrar el texto
        pygame.draw.rect(surface, COLOR_BLANCO, (POSICION_X_RECTANGULO, POSICION_Y_RECTANGULO, ANCHO_RECTANGULO, ALTO_RECTANGULO))

        # Itera sobre las líneas ingresadas y dibuja el texto en el rectángulo blanco
        for self.lineas in range(len(self.caracteres)):
            Img_letra = self.fuente.render(self.caracteres[self.lineas], False, COLOR_NEGRO)
            surface.blit(Img_letra, (POSICION_X_RECTANGULO, POSICION_Y_RECTANGULO + self.distancia * self.lineas))


        