import pygame, sys
from pygame.locals import *
from jugador import Jugador

#Iniciació pygame
pygame.init()

#inicialitzacions
vel = 0
salt = 10
isSalt = False
y = 360

#Pantalla
W,H = 1000,600
PANTALLA = pygame.display.set_mode((W,H))
FPS = 100
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
    personatge = Jugador(50, 360)
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == K_SPACE:
               isSalt = True

            if personatge.y != 360:
                isSalt = False

            if isSalt:
                while personatge.y <= 360 and y > 300:
                    y -= 1
                    personatge.y = y
                    print (personatge.y)
                """if personatge.y == 300:
                    while personatge.y < 360:
                        y += 1
                        personatge.y = y"""


    personatge.y = y

    x_relativa = x % fons_redi.get_rect().width
    PANTALLA.blit(fons_redi, (x_relativa - fons_redi.get_rect().width, 0))
    if x_relativa < W:
        PANTALLA.blit(fons_redi,(x_relativa,0))
    x -= 1

    # Personatge funcions
    personatge.dibuixa_quiet()
    #personatge.salta()
    #personatge.actualitzar()

    pygame.display.flip()
    CLOCK.tick(FPS)



