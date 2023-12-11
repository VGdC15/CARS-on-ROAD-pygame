import pygame
from constantesCar import *


class Carretera:
    # Constructor de la clase
    def __init__(self):
        # Defino marcadores en el carril izquierdo (carril 1)
        self.marcadores = [(95, 0, ANCHO_MARCADOR, ALTO_VENTANA), (395, 0, ANCHO_MARCADOR, ALTO_VENTANA)]
        # Color de los marcadores en el carril izquierdo
        self.marcador_color = COLOR_AMARILLO

        # Defino marcadores en el carril derecho (carril 2)
        self.marcadores_dos = [(75, 0, ANCHO_MARCADOR, ALTO_VENTANA), (415, 0, ANCHO_MARCADOR, ALTO_VENTANA)]
        # Color de los marcadores en el carril derecho
        self.marcador_color_dos = COLOR_BLANCO

        # Inicialización del movimiento vertical y del marcador
        self.movimiento_y_marcador = 0

    # Método para actualizar la posición de los marcadores y el movimiento vertical
    def actualizar(self, speed):
        # Actualiza el movimiento vertical basado en la velocidad del juego
        self.movimiento_y_marcador += speed * 2
        # Reinicia el movimiento si ha superado la altura de dos marcadores consecutivos
        if self.movimiento_y_marcador >= ALTO_MARCADOR * 2:
            self.movimiento_y_marcador = 0

    # Método para dibujar la carretera en la pantalla
    def dibujar(self, screen, carriles):
        # Dibuja el camino principal (rectángulo gris)
        pygame.draw.rect(screen, COLOR_GRIS, (100, 0, ANCHO_CAMINO, ALTO_VENTANA))
        
        # Dibuja marcadores en los carriles
        for i in range(ALTO_MARCADOR * -2, ALTO_VENTANA, ALTO_MARCADOR * 2):
            for carril in carriles:
                pygame.draw.rect(screen, COLOR_BLANCO, (carril + 45, i + self.movimiento_y_marcador, ANCHO_MARCADOR, ALTO_MARCADOR))
        
        # Dibuja marcadores en el carril izquierdo
        for marcador in self.marcadores:
            pygame.draw.rect(screen, self.marcador_color, marcador)
        
        # Dibuja marcadores en el carril derecho
        for marcador in self.marcadores_dos:
            pygame.draw.rect(screen, self.marcador_color_dos, marcador)




