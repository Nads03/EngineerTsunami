import pygame
import random
pygame.init()

# Configuración de la pantalla
W,H = 1000,600


# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Clase Obstacle
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.type = random.choice(["vertical_rect", "hole", "ball"])
        self.image = pygame.Surface((50, 50))
        self.speed = 5

        if self.type == "vertical_rect":
            self.image = pygame.Surface((20, 100))
            self.image.fill(RED)
            self.rect = self.image.get_rect(topleft=(W, 250))
        elif self.type == "hole":
            self.image = pygame.Surface((100, 151))
            self.image.fill(BLACK)
            self.rect = self.image.get_rect(topleft=(W, H - 151))
        elif self.type == "ball":
            self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
            pygame.draw.circle(self.image, BLUE, (15, 15), 15)
            self.rect = self.image.get_rect(topleft=(W, 400))

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
