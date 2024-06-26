import pygame
import random
from pygame.locals import *
from settings import Settings
from pygame.sprite import Sprite

sett = Settings()

#Classe obstacle
class Obstacle(Sprite):
    def __init__(self):
        super().__init__()
        self.type = random.choice(["vertical_rect", "hole", "ball"])
        self.image = pygame.Surface((50,50))
        self.speed = 5

        if self.type == "vertical_rect":
            self.image = pygame.Surface((20,100))
            self.image.fill((255,0,0))
            self.rect = self.image.get_rect(topleft=(sett.pant_width, 250))
        elif self.type == "hole":
            self.image = pygame.Surface((100, 151))
            self.image.fill((0, 0, 0))
            self.rect = self.image.get_rect(topleft=(sett.pant_width, sett.pant_height-151))
        elif self.type == "ball":
            self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
            pygame.draw.circle(self.image, (0, 0, 255), (15, 15), 15)
            self.rect = self.image.get_rect(topleft = (sett.pant_width, 400))
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()