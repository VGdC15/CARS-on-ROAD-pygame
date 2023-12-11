import pygame 
from pygame.locals import *
from constantesCar import *
from imagenes import *
from carretera import *
from vehiculo import *
from boton import *
from funcion__para_json import *

def dibujar_game_over(screen, explosion, rectangulo_choque, score, ingreso:str):
    # Muestra la explosión en el centro
    screen.blit(explosion, rectangulo_choque)
    
    pygame.draw.rect(screen, COLOR_ROSA, (0, 200, ANCHO_VENTANA, 150))
    fuente = pygame.font.SysFont('Bauhaus 93', 45)
    texto_game_over = fuente.render('G A M E  O V E R', False, COLOR_NEGRO)
    rectangulo_texto_game_over = texto_game_over.get_rect()
    rectangulo_texto_game_over.center = (ANCHO_VENTANA / 2, 225)
    screen.blit(texto_game_over, rectangulo_texto_game_over)

    # Muestra la palabra "score" y el puntaje acumulado
    fuente_score = pygame.font.SysFont('Bauhaus 93', 30)
    texto_score = fuente_score.render(f'Score: {score}', False, COLOR_NEGRO)
    rectangulo_texto_score = texto_score.get_rect()
    rectangulo_texto_score.midtop = (ANCHO_VENTANA / 2, rectangulo_texto_game_over.bottom + 10)
    screen.blit(texto_score, rectangulo_texto_score)

    # Muestra el texto "Inserte sus iniciales:"
    fuente_iniciales = pygame.font.SysFont('Bauhaus 93', 25)
    texto_iniciales = fuente_iniciales.render('Inserte sus iniciales:', False, COLOR_NEGRO)
    rectangulo_texto_iniciales = texto_iniciales.get_rect()
    rectangulo_texto_iniciales.midtop = (ANCHO_VENTANA / 2 - 80, rectangulo_texto_score.bottom + 14)
    screen.blit(texto_iniciales, rectangulo_texto_iniciales)

    # Dibuja un rectángulo blanco como fondo para el campo de texto de iniciales
    pygame.draw.rect(screen, COLOR_BLANCO, (POSICION_X_RECTANGULO, POSICION_Y_RECTANGULO, ANCHO_RECTANGULO, ALTO_RECTANGULO))

    # Muestra el texto "Presione ESC para volver al menú"
    fuente_esc = pygame.font.SysFont('Bauhaus 93', 20)
    texto_esc = fuente_esc.render('Presione ESC para volver al menú', False, COLOR_NEGRO)
    rectangulo_texto_esc = texto_esc.get_rect()
    rectangulo_texto_esc.midtop = (ANCHO_VENTANA / 2, rectangulo_texto_iniciales.bottom + 21)
    screen.blit(texto_esc, rectangulo_texto_esc)


def ejecutar_pantalla_ranking(screen, POSICION_IMAGEN, ranking):
    # Carga y ajusta la imagen de fondo
    imagen_fondo = pygame.image.load("programacion\ejercicios\juego_2\imagenes\pantalla_ranking.png")
    imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

    # Crea una instancia de la clase Boton
    boton_menu_principal = Boton("programacion\ejercicios\juego_2\imagenes\menu_principal.png", (60, 440), (ANCHO_BOTON, ALTO_BOTON))

    menu_principal = False  # variable que indica si se debe ir al menú principal
    
    run = True
    while run:
        # Dibuja la imagen de fondo y el botón del menú principal en la pantalla
        screen.blit(imagen_fondo, POSICION_IMAGEN)
        screen.blit(boton_menu_principal.surface, boton_menu_principal.rect)

        # Manejo de eventos
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                run = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Verifica si se hizo clic en el botón del menú principal
                posicion_click = list(evento.pos)
                if boton_menu_principal.rect.collidepoint(posicion_click):
                    menu_principal = True
                    run = False

        # Verifica si el objeto JSON tiene la clave 'ranking' y no está vacío antes de intentar acceder a sus elementos
        if 'ranking' in ranking and ranking['ranking']:
            # Crea una fuente para mostrar el nombre y la puntuación en el ranking
            font_data = pygame.font.SysFont('Bauhaus 93', 30)
            for i, item in enumerate(ranking['ranking']):
                # Renderiza el nombre del jugador en el ranking
                texto_name = font_data.render(str(item["name"]), True, COLOR_NEGRO)
                imagen_fondo.blit(texto_name, (160, 170 + i * 60))

                # Renderiza la puntuación del jugador en el ranking
                texto_score = font_data.render(str(item["score"]), True, COLOR_NEGRO)
                imagen_fondo.blit(texto_score, (310, 170 + i * 60))

        # Actualiza la pantalla
        pygame.display.flip()

    # Si se debe ir al menú principal, llama a la función ejecutar_menu
    if menu_principal:
        ejecutar_menu(screen, POSICION_IMAGEN, ranking)


def dibujar_menu(screen, POSICION_IMAGEN):
    # Carga y ajusta la imagen de fondo del menú principal
    imagen_fondo = pygame.image.load("programacion\ejercicios\juego_2\imagenes\menu.png")
    imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

    # Crear botones
    boton_start = Boton("programacion\ejercicios\juego_2\imagenes\start.png", (-45, 370), (ANCHO_BOTON, ALTO_BOTON))
    boton_ranking = Boton("programacion\ejercicios\juego_2\imagenes\score.png", (160, 370), (ANCHO_BOTON, ALTO_BOTON))

    # Bucle principal para el menú
    while True:
        # Dibuja la imagen de fondo y los botones en la pantalla
        screen.blit(imagen_fondo, POSICION_IMAGEN)
        screen.blit(boton_start.imagen, boton_start.rect)
        screen.blit(boton_ranking.imagen, boton_ranking.rect)

        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Obtiene la posición del clic del ratón
                posicion_click = list(evento.pos)
                # Verifica si se hizo clic en algún botón
                if boton_start.rect.collidepoint(posicion_click):
                    return "start"
                elif boton_ranking.rect.collidepoint(posicion_click):
                    return "ranking"

        # Actualiza la pantalla
        if pygame.display.get_init():
            pygame.display.flip()
        else:
            break

def ejecutar_menu(screen, POSICION_IMAGEN, ranking=None):
    ejecutar_juego = False
    if not ejecutar_juego:
        # Llama a la función dibujar_menu para mostrar el menú principal
        opcion_seleccionada = dibujar_menu(screen, POSICION_IMAGEN)
        if opcion_seleccionada == "start":
            # Si se selecciona "start", establece el color de fondo y marca la variable ejecutar_juego como Verdadero
            color_fondo = COLOR_NEGRO
            screen.fill(color_fondo)
            ejecutar_juego = True
        elif opcion_seleccionada == "ranking":
            # Si se selecciona "ranking", lee los datos del archivo JSON y ejecuta la pantalla de ranking
            ranking = leer_data("programacion\ejercicios\cars_on_road\data.json")
            ejecutar_pantalla_ranking(screen, POSICION_IMAGEN, ranking)
