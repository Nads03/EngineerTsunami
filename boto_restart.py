import pygame
from settings import Settings

sett = Settings()
class Boto():
    def __init__(self, x, y, text):
        self.rect = pygame.Rect(x, y, sett.b_width, sett.b_height)
        self.color = sett.b_color
        self.text = text
        self.font = sett.font
        self.color_text = sett.b_color_text

    def dibuixa(self, pantalla):
        pygame.draw.rect(pantalla, self.color, self.rect)
        text_sup = self.font.render(self.text, True, self.color_text)
        text_rect = text_sup.get_rect(center=self.rect.center)
        pantalla.blit(text_sup, text_rect)
