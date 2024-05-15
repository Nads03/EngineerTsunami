import pygame, sys
from pygame.locals import *

#Iniciació pygame
pygame.init()

#Pantalla
W,H = 1000,600
PANTALLA = pygame.display.set_mode((W,H))

#Classe obstacle
class Obstacle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        imatge = pygame.image.load("imatges/bomba.png").convert_alpha()
        self.image = imatge