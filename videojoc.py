import pygame
import random
import sys
from pygame.locals import *
from jugador import Jugador
from obstacle import Obstacle
from Settings import Settings

#Iniciació pygame
pygame.init()

# Colores
BLACK = (0, 0, 0)

#Pantalla
W,H = 1000,600
PANTALLA = pygame.display.set_mode((W,H))
FPS = 100
CLOCK = pygame.time.Clock()

#Fons
fons = pygame.image.load("imatges/fondo2.jpg").convert()
fons_redi = pygame.transform.scale(fons, (W,H))
z = 0

#ICONA I TÍTOL
pygame.display.set_caption('ZOMBIENEER')
icona = pygame.image.load("imatges/icono_personatge.png")
pygame.display.set_icon(icona)


settings = Settings()

#Inicialització personatge
posicio_x = 50
posicio_y = 360

salt = False

gravetat = 1
altura_salt = 15
salt_y = altura_salt
tiempo_anterior = pygame.time.get_ticks()

#Obstacle
obstacle_timer = 0
obstacles = pygame.sprite.Group()
#Bucle del joc
while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # Agregar nuevos obstáculos en intervalos aleatorios
    if obstacle_timer == 0:
        obstacles.add(Obstacle())
        obstacle_timer = random.randint(50, 150)  # Generar un obstáculo nuevo después de un intervalo aleatorio
    else:
        obstacle_timer -= 1



    z_relativa = z % fons_redi.get_rect().width
    PANTALLA.blit(fons_redi, (z_relativa - fons_redi.get_rect().width, 0))
    if z_relativa < W:
        PANTALLA.blit(fons_redi,(z_relativa,0))
    z -= 1


    # Moviment personatge
    personatge = Jugador(posicio_x, posicio_y)

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_SPACE]:
        salt = True


    if salt:
        posicio_y -= salt_y
        salt_y -= gravetat

        #Acabament salt
        if salt_y < -altura_salt:
            salt = False
            salt_y = altura_salt
        personatge.dibuixa()


    else:
        posicio_x = 50
        posicio_y = 360
        personatge.dibuixa()
      # Actualizar y dibujar obstáculos

    obstacles.update()
    obstacles.draw(PANTALLA)


    pygame.display.flip()
    CLOCK.tick(FPS)



