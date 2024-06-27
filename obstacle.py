import pygame
import random
from pygame.locals import *
from settings import Settings
from pygame.sprite import Sprite

sett = Settings()

#Classe obstacle
class Bomba(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.imatge = pygame.transform.scale(sett.bomba_img, (sett.t_bloc//2, sett.t_bloc//2))
        self.rect = self.imatge.get_rect()
        self.rect.x = x
        self.rect.y = y

    def visible(self):
        return self.rect.right > 0