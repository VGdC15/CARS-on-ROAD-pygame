import pygame
from pygame.locals import *
from constantesCar import *
import random
from imagenes import *
from vehiculo import *
from carretera import *
from funciones_cars import *
from funcion__para_json import *
from nivel import Nivel
from ingreso import *

pygame.init()

# pantalla
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Cars on Road - Verónica Castillo")

# barra de score
barra_score = pygame.image.load(linea_score)
barra_score = pygame.transform.scale(barra_score, (ANCHO_VENTANA, 50))

carretera = Carretera()
entrada = Entrada()

# Coordenadas de los carriles
carril_izquierdo = 150
carril_central = 250
carril_derecho = 350
carriles = [carril_izquierdo, carril_central, carril_derecho]

# Coordenadas de inicio del jugador
player_x = 250
player_y = 400

# Configuraciones de tiempo
reloj = pygame.time.Clock()
fps = 120

# Configuraciones del juego
game_over = False
esperando_ingreso = False
ejecutar_juego = False
speed = 1.7
score = 0
ingreso = ""

nivel_actual = 0  # Iniciar desde el nivel 0
tiempo_nivel_actual = 0

# Grupos de sprites
player_group = pygame.sprite.Group()
vehicle_group = pygame.sprite.Group()

# Crea el auto del jugador
player = PlayerCar(player_x, player_y, scale=0.4)
player_group.add(player)

# Carga la imagen de colisión
explosion = pygame.image.load(explosion)
explosion = pygame.transform.scale(explosion, (ANCHO_EXPLOSION, ALTO_EXPLOSION))
rectangulo_choque = explosion.get_rect()

# Configuraciones de niveles
niveles = [
    Nivel(numero=1, rutas_enemigos=[auto_verde, auto_violeta, auto_amarillo],
          color_fondo=COLOR_NEGRO, tiempo_nivel=20000),
    Nivel(numero=2, rutas_enemigos=[auto_verde, camioneta, auto_amarillo, camion],
          color_fondo=COLOR_VERDE, tiempo_nivel=30000),
    Nivel(numero=3, rutas_enemigos=[bomberos, auto_violeta, ambulancia, camion],
          color_fondo=COLOR_PURPURA, tiempo_nivel=40000)
]

# Bucle principal del juego
run = True
while run:
    reloj.tick(fps)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == QUIT:
            run = False

        # Menú
        if not ejecutar_juego:
            opcion_seleccionada = dibujar_menu(screen, POSICION_IMAGEN)
            if opcion_seleccionada == "start":
                ejecutar_juego = True
                color_fondo = niveles[nivel_actual].color_fondo
                screen.fill(color_fondo)
            elif opcion_seleccionada == "ranking":
                ranking_ordenado = ordenar_puntuacion_descendente("programacion\ejercicios\juego_2\data.json", "score")
                ejecutar_pantalla_ranking(screen, POSICION_IMAGEN, ranking_ordenado)

    # Lógica del juego
    if ejecutar_juego:
        for evento in eventos:
            if evento.type == QUIT:
                run = False
            elif evento.type == KEYDOWN:
                if evento.key == K_LEFT and player.rect.center[0] > carril_izquierdo:
                    player.rect.x -= 100
                elif evento.key == K_RIGHT and player.rect.center[0] < carril_derecho:
                    player.rect.x += 100

        tiempo_nivel_actual += reloj.get_time()
        if nivel_actual < len(niveles):
            if tiempo_nivel_actual > niveles[nivel_actual].tiempo_nivel:
                nivel_completado = niveles[nivel_actual].cargar_niveles(nivel_actual)
                nivel_actual += 1
                tiempo_nivel_actual = 0

                # Verifica si aún hay niveles disponibles antes de acceder a ellos
                if nivel_actual < len(niveles):
                    color_fondo_nuevo = niveles[nivel_actual].color_fondo
                    screen.fill(color_fondo_nuevo)
        else:
            # Se ejecuta cuando se completa el último nivel
            esperando_ingreso = True
            game_over = True

            # Verifica si no hay colisiones antes de cambiar las coordenadas de la explosión
            if not pygame.sprite.spritecollide(player, vehicle_group, False):
                rectangulo_choque.center = (800, 800)

            dibujar_game_over(screen, explosion, rectangulo_choque, score, ingreso)

        # Actualiza la carretera independientemente de la dirección del jugador
        carretera.actualizar(speed)

        # Verifica si hay una colisión lateral después de cambiar de carril
        for vehiculo in vehicle_group:
            if pygame.sprite.collide_rect(player, vehiculo):
                game_over = True
                # Coloca el auto del jugador al lado del otro vehículo
                if evento.key == K_LEFT:
                    player.rect.left = vehiculo.rect.right
                elif evento.key == K_RIGHT:
                    player.rect.right = vehiculo.rect.left

                # Ajusta las coordenadas del rectángulo de la explosión al centro entre el jugador y el vehículo
                rectangulo_choque.centerx = (player.rect.centerx + vehiculo.rect.centerx) / 2
                rectangulo_choque.centery = (player.rect.centery + vehiculo.rect.centery) / 2
       
        carretera.dibujar(screen, carriles) # Dibuja la carretera       
        player_group.draw(screen) # Dibuja el auto del jugador

        # Agrega un vehículo
        if len(vehicle_group) < 2:
            # Asegura que haya suficiente espacio entre los vehículos
            agregar_vehiculo = True
            for vehiculo in vehicle_group:
                if vehiculo.rect.top < vehiculo.rect.height * 1.5:
                    agregar_vehiculo = False
            if agregar_vehiculo:
                carril = random.choice(carriles)  # Selecciona un carril al azar
                ruta_enemigo = random.choice(niveles[nivel_actual].rutas_enemigos)  # Selecciona una ruta de vehículo al azar del nivel actual
                vehiculo = VehiculoEnemigo(carril + 45, ALTO_VENTANA / -2, [ruta_enemigo], scale=0.5)
                vehicle_group.add(vehiculo)

        # Incrementa la velocidad después de pasar 3 vehículos
        if score > 0 and score % 30 == 0:
            speed += 0.003

        # Hace que los vehículos se muevan
        for vehiculo in vehicle_group:
            score = vehiculo.actualizar(speed, score, carriles)
      
        vehicle_group.draw(screen) # Dibuja los vehículos        
        screen.blit(barra_score, POSICION_IMAGEN) # Dibuja la barra de score

        # Muestra la puntuación
        fuente = pygame.font.SysFont('Bauhaus 93', 29)
        texto = fuente.render('Score: ' + str(score), False, COLOR_NEGRO)
        rectangulo_texto = texto.get_rect()
        rectangulo_texto.center = (410, 23)  # X , Y
        screen.blit(texto, rectangulo_texto)

        # Verifica si hay una colisión frontal
        colisionados = pygame.sprite.spritecollide(player, vehicle_group, True)
        if colisionados:
            game_over = True
            vehiculo = colisionados[0]  # para obtener el primer vehículo colisionado

            # Ajusta las coordenadas del rectángulo de la explosión al centro entre el jugador y el vehículo
            rectangulo_choque.centerx = (player.rect.centerx + vehiculo.rect.centerx) / 2
            rectangulo_choque.centery = (player.rect.centery + vehiculo.rect.centery) / 2

        # Muestra el mensaje de fin de juego
        if game_over:
            esperando_ingreso = True
            dibujar_game_over(screen, explosion, rectangulo_choque, score, ingreso)           
        
        pygame.display.update()
        while game_over:
            reloj.tick(fps)
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    game_over = True

                # Manejo de iniciales del usuario
                elif evento.type == pygame.KEYDOWN:
                    entrada.teclas([evento])
                    if evento.key == pygame.K_RETURN:
                        # Procesar el texto ingresado 
                        ingreso = entrada.caracteres[-1]
                        entrada.lineas = 0
                    elif evento.key == K_ESCAPE:
                        # Guardar datos y redirigir a la pantalla de ranking
                        ranking = leer_data("programacion\ejercicios\juego_2\data.json")
                        guardar_data(ranking, entrada.caracteres, score)
                        ranking_ordenado = ordenar_puntuacion_descendente("programacion\ejercicios\juego_2\data.json", "score")
                        ejecutar_pantalla_ranking(screen, POSICION_IMAGEN, ranking_ordenado)
                        game_over = False

            entrada.mensaje(screen)
            pygame.display.flip()

pygame.quit()
