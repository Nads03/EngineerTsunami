import pygame
import random
from pygame.locals import *
from settings import Settings
from pygame.sprite import Sprite

sett = Settings()

#Classe objecte

class Objecte(Sprite):
    def __init__(self, x, y, imatge, width, length):
        super().__init__()
        self.imatge = pygame.transform.scale(imatge, (width, length))
        self.rect = self.imatge.get_rect()
        self.rect.x = x
        self.rect.y = y

    def visible(self):
        return self.rect.right > 0