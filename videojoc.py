import pygame, sys
from pygame.locals import *
from jugador import Jugador

#Iniciació pygame
pygame.init()

#Pantalla
W,H = 1000,600
PANTALLA = pygame.display.set_mode((W,H))
FPS = 150
CLOCK = pygame.time.Clock()

#Fons
fons = pygame.image.load("imatges/fondo2.jpg").convert()
fons_redi = pygame.transform.scale(fons, (W,H))
x = 0

#ICONA I TÍTOL
pygame.display.set_caption('ZOMBIENEER')
icona = pygame.image.load("imatges/icono_personatge.png")
pygame.display.set_icon(icona)

#Bucle del joc
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    x_relativa = x % fons_redi.get_rect().width
    PANTALLA.blit(fons_redi, (x_relativa - fons_redi.get_rect().width, 0))
    if x_relativa < W:
        PANTALLA.blit(fons_redi,(x_relativa,0))
    x -= 1

    # Personatge
    personatge = Jugador(50, 360)
    personatge.dibuixa_quiet()

    pygame.display.flip()
    CLOCK.tick(FPS)



