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
        self.velocitat = 5


    def dibuixa(self):
        PANTALLA.blit(self.image, (self.x,self.y))