import pygame, sys
from pygame.locals import *
from jugador import Jugador

#Iniciació pygame
pygame.init()

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

#Inicialització personatge
posicio_x = 50
posicio_y = 360

salt = False

gravetat = 1
altura_salt = 15
salt_y = altura_salt

#Bucle del joc
while True:
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

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

    pygame.display.flip()
    CLOCK.tick(FPS)



