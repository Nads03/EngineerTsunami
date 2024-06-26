import pygame
from settings import Settings
from pygame.sprite import Sprite

sett = Settings()

class Jugador(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.imatge = pygame.transform.scale(sett.zombie_img, (sett.zombie_x, sett.zombie_y))
        self.rect = self.imatge.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.imatge.get_width()
        self.height = self.imatge.get_height()
        self.vel = 0
        self.salt = False
        self.punts = 0

    def update(self, joc):
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.salt == False:
            self.vel = -15
            self.salt = True

        if key[pygame.K_SPACE] == False:
            self.salt = False

        # Gravetat
        self.vel += 1
        if self.vel > 10:
            self.vel = 10
        dy += self.vel

        # Colisió
        for bloc in joc.llista_blocs:
            if bloc[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            if bloc[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                dy = bloc[1].top - self.rect.bottom
                self.vel = 0

        self.rect.x += dx
        self.rect.y += dy

        for persona in joc.llista_persones:
            if self.rect.colliderect(persona.rect):
                self.punts += 1
                joc.llista_persones.remove(persona)

        for objecte_aeri in joc.llista_objectes_aeris:
            if objecte_aeri.rect.colliderect(self.rect):
                return True

        if self.rect.bottom > sett.pant_height:
            self.rect.bottom = sett.pant_height
            return True

        for bomba in joc.llista_bombes:
            if bomba.rect.colliderect(self.rect):
                return True

        return False

    def dibuixa(self, pantalla):
        pantalla.blit(self.imatge, self.rect)