import pygame
import random
from settings import Settings

sett = Settings()
class Joc():
    def __init__(self, dades):
       self.llista_blocs = []

       f_cont = 0
       for fila in dades:
           col_cont = 0
           for bloc in fila:
               if bloc == 1:
                   imatge = pygame.transform.scale(sett.bloc_img, (sett.t_bloc, sett.t_bloc))
                   imatge_rect = imatge.get_rect()
                   imatge_rect.x = col_cont * sett.t_bloc
                   imatge_rect.y = f_cont * sett.t_bloc
                   bloc = (imatge,imatge_rect)
                   self.llista_blocs.append(bloc)
               col_cont += 1
           f_cont += 1

    def dibuixa(self, pantalla):
       for bloc in self.llista_blocs:
           pantalla.blit(bloc[0], bloc[1])

    def mou_plataformes(self, dx_fons):
        for bloc in self.llista_blocs:
            bloc[1].x += dx_fons

        #Optimització del joc: eliminem plataformes fora de pantalla
        self.llista_blocs = [bloc for bloc in self.llista_blocs if bloc[1].right > 0]

    def nova_plataforma(self):
        if self.llista_blocs and self.llista_blocs[-1][1].right < sett.pant_width:
            valors_x = [0, 100, 200, 300]
            x = self.llista_blocs[-1][1].right + random.choice(valors_x)
            y = sett.pant_height - sett.t_bloc
            imatge = pygame.transform.scale(sett.bloc_img, (sett.t_bloc, sett.t_bloc))
            imatge_rect = imatge.get_rect()
            imatge_rect.x = x
            imatge_rect.y = y
            bloc = (imatge, imatge_rect)
            self.llista_blocs.append(bloc)
