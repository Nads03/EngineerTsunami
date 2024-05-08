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
        self.temps_salt = 10
        self.altura_salt = 100

    def dibuixa_quiet(self):
        PANTALLA.blit(self.image, (self.x,self.y))

    def salta (self):
        if not self.salt:
            self.salt = True

    def actualitzar(self):
        if self.salt:
            if self.altura_salt >= 0:
                self.y -= self.vel_salt
                self.altura_salt -= self.vel_salt
            else:
                self.salt = False
                self.altura_salt = 100
        else:
            self.y += self.temps_salt
