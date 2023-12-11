import pygame
from pygame.locals import *
from constantesCar import *


class Nivel():
    # Constructor de la clase Nivel
    def __init__(self, numero, rutas_enemigos, color_fondo, tiempo_nivel, player_x=250, player_y=400):
        # Inicializa atributos del nivel
        self.numero = numero
        self.rutas_enemigos = rutas_enemigos
        self.color_fondo = color_fondo
        self.tiempo_nivel = tiempo_nivel
        self.player_x = player_x
        self.player_y = player_y
  
    def cargar_niveles(self, nivel: int):
        rutas_enemigos = []
        tiempo_nivel = 0
        color_fondo = None

        # Configura los niveles
        if nivel == 1:
            rutas_enemigos = ['programacion\ejercicios\juego_2\imagenes\carVerde.png', 'programacion\ejercicios\juego_2\imagenes\carPremio.png']
            color_fondo = COLOR_NEGRO
            tiempo_nivel = 10000  # 20000 20 segundos en milisegundos
        elif nivel == 2:
            rutas_enemigos = ['programacion\ejercicios\juego_2\imagenes\carVerde.png', 'programacion\ejercicios\juego_2\imagenes\camioneta.png', 'programacion/ejercicios/pygame/carAmarillo.png', 'programacion\ejercicios\juego_2\imagenes\camion.png']
            color_fondo = COLOR_VERDE
            tiempo_nivel = 10000  # 30000 30 segundos en milisegundos
        elif nivel == 3:
            rutas_enemigos = ['programacion\ejercicios\juego_2\imagenes\car_fire.png', 'programacion\ejercicios\juego_2\imagenes\carPremio.png', 'programacion\ejercicios\juego_2\imagenes\sanidad.png', 'programacion\ejercicios\juego_2\imagenes\camion.png']
            color_fondo = COLOR_PURPURA
            tiempo_nivel = 10000  # 40000 40 segundos en milisegundos

        return rutas_enemigos, color_fondo, tiempo_nivel
    


   
    
    

