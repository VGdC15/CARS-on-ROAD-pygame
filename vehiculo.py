import pygame
from constantesCar import *
import random

# clase Vehiculo que hereda de pygame.sprite.Sprite
class Vehiculo(pygame.sprite.Sprite):

    # Constructor de la clase, recibe una imagen, coordenadas (x, y) y una escala opcional
    def __init__(self, image, x, y, scale=1.0):
        # Llama al constructor de la clase base (pygame.sprite.Sprite)
        pygame.sprite.Sprite.__init__(self)

        # Calcula las nuevas dimensiones de la imagen según la escala
        nuevo_ancho = int(image.get_rect().width * scale)
        nuevo_alto = int(image.get_rect().height * scale)
        
        # Escala la imagen
        self.image = pygame.transform.scale(image, (nuevo_ancho, nuevo_alto))

        # Obtiene el rectángulo que rodea la imagen y centrarlo en las coordenadas (x, y)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

# Define una subclase llamada PlayerCar que hereda de la clase Vehiculo
class PlayerCar(Vehiculo):

    # Constructor de la subclase, recibe las coordenadas (x, y) y una escala opcional
    def __init__(self, x, y, scale=1.0):
        # Carga la imagen del jugador desde un archivo
        image = pygame.image.load('programacion\ejercicios\pygame\PlayerCar.png')
        # Llama al constructor de la clase base (Vehiculo) y pasar la imagen, coordenadas y escala
        super().__init__(image, x, y, scale)


# clase VehiculoEnemigo que hereda de la clase Vehiculo
class VehiculoEnemigo(Vehiculo):

    # Constructor de la clase, que llama al constructor de la clase base (Vehiculo)
    def __init__(self, x, y, rutas_enemigos, scale=1.2):
        # Llama al constructor de la clase base y pasar la imagen aleatoria
        if rutas_enemigos and len(rutas_enemigos) > 0:
            super().__init__(self.obtener_imagen_aleatoria(rutas_enemigos), x, y, scale)

    # Método para obtener una imagen aleatoria de la lista de rutas de enemigos
    def obtener_imagen_aleatoria(self, rutas_enemigos):
        # Selecciona aleatoriamente una ruta de la lista
        nombre_archivo = random.choice(rutas_enemigos)
        # Carga la imagen correspondiente a la ruta seleccionada
        return pygame.image.load(nombre_archivo)

    # Método para mover el vehículo hacia abajo en la pantalla
    def mover_vehiculo(self, speed, carriles):
        self.rect.y += speed

        # Limitar el vehículo al carril izquierdo, central o derecho
        carril_destino = min(carriles, key=lambda x: abs(x - self.rect.center[0]))
        self.rect.center = (carril_destino, self.rect.centery)

    # Método para actualizar la posición del vehículo y la puntuación del juego
    def actualizar(self, speed, score, carriles):
        # Mover el vehículo hacia abajo y limitarlo al carril
        self.mover_vehiculo(speed, carriles)
        
        # Quita el vehículo de la pantalla una vez que sale de la pantalla
        if self.rect.top >= ALTO_VENTANA:
            self.kill()  # Elimina el objeto de la lista de sprites
            # Suma a la puntuación del jugador
            score += 10
            
        return score  # Devuelve la puntuación actualizada

