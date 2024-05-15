import pygame, sys
from pygame.locals import *
from pygame.sprite import Sprite
from settings import Settings

#Pantalla
vg_settings = Settings()
PANTALLA = pygame.display.set_mode((vg_settings.W, vg_settings.H))

#Classe personatge
class Jugador(Sprite):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        imatge = pygame.image.load("imatges/icono_personatge3.png").convert_alpha()
        self.image = imatge

    def dibuixa(self):
        PANTALLA.blit(self.image, (self.x,self.y))

#Inicialització personatge
posicio_x = 50
posicio_y = 360

salt = False

gravetat = 1
altura_salt = 15
salt_y = altura_salt

# Moviment personatge
personatge = Jugador(posicio_x, posicio_y)

# Funció saltar (al model)
if salt:
    posicio_y -= salt_y
    salt_y -= gravetat

    # Acabament salt
    if salt_y < -altura_salt:
        salt = False
        salt_y = altura_salt
    personatge.dibuixa()

else:
    posicio_x = 50
    posicio_y = 360
    personatge.dibuixa()


    def check_which_keydown(keys_pressed):
        if keys_pressed[pygame.K_SPACE]:
            salt = True

