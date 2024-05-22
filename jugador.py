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
        self.gravetat = 1
        self.altura_salt = 15
        self.salt_y = self.altura_salt
        self.salt = False
        #Definim rectangle per la imatge del jugador
        #self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def dibuixa(self):
        PANTALLA.blit(self.image, (self.x,self.y))

    def space_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[K_SPACE] and not self.salt:
            self.salt = True

    def salta(self):
        if self.salt:
            self.y -= self.salt_y
            self.salt_y -= self.gravetat

            # Acabament salt
            if self.salt_y < -self.altura_salt:
                self.salt = False
                self.salt_y = self.altura_salt
            self.dibuixa()

        else:
            self.x = 50
            self.y = 360
            self.dibuixa()

