import pygame, sys
from pygame.locals import *
from jugador import Jugador

#Iniciació pygame
pygame.init()

#Pantalla
W,H = 1000,600
PANTALLA = pygame.display.set_mode((W,H))
#Control de FPS
FPS = 500
CLOCK = pygame.time.Clock()

#Fons
fons = pygame.image.load("imatges/fondo2.jpg").convert()
fons_redi = pygame.transform.scale(fons, (1000,600))


#Icona i títol
pygame.display.set_caption('ZOMBIENEER')
icona = pygame.image.load("imatges/icono_personatge.png")
pygame.display.set_icon(icona)

#Personatge
personatge = Jugador(100,100)

#Moviment
def pantalla():
#Fons en moviment
    x = 0
    x_relativa = x % fons_redi.get_rect().width
    PANTALLA.blit(fons_redi, (x_relativa - fons_redi.get_rect().width, 0))
    if x_relativa < W:
        PANTALLA.blit(fons_redi,(x_relativa,0))
    x -= 1

#Execució del joc
executa = True

while executa:

    #Control FPS
    CLOCK.tick(FPS)

    #Bucle del joc
    for event in pygame.event.get():
        if event.type == QUIT:
            executa = False

    #Actualiltzació pantala
    pygame.display.update()

    #Funció actualitzar pantalla
    pantalla()

#Exit
pygame.quit()
