import pygame
from settings import Settings

sett = Settings()

class Idioma:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.font = sett.font
        self.idiomes = ['català', 'castellà', 'anglès']
        self.selected = 'català'

    def dibuixa(self):
        vert_pos = 50
        for idioma in self.idiomes:
            text = self.font.render(idioma.capitalize(), True, (0,0,0))
            self.pantalla.blit(text, (50, vert_pos))
            vert_pos += 50

    def tria(self, mouse_pos):
        vert_pos = 50
        for idioma in self.idiomes:
            text_rect = pygame.Rect(sett.hor_pos, vert_pos, 200, 36)
            if text_rect.collidepoint(mouse_pos):
                self.selected = idioma
                return idioma
            vert_pos += 50
        return None

