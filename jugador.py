import pygame, sys
from pygame.locals import *

#Iniciació pygame
pygame.init()

#Pantalla
W,H = 1000,600
PANTALLA = pygame.display.set_mode((W,H))

#Classe jugador, personatge
class Jugador:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        imatge = pygame.image.load("imatges/icono_personatge3.png").convert_alpha()
        self.image = imatge
        x = 0
        self.salt = False
        self.temps_salt = 0
        self.altura_salt = 100
        self.vel_salt = 5

    def dibuixa_quiet(self):
        PANTALLA.blit(self.image, (self.x,self.y))

    def salta (self, x, y):
        PANTALLA.blit(self.image, (self.x,self.y))
        z = 800
        if self.salt:
            z = 360
            while z < 800:
                self.y = z
                z += 1
        else:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.salt = True


