import pygame
import random
from settings import Settings
from obstacle import Bomba

sett = Settings()
class Joc():
    def __init__(self, dades):
       self.llista_blocs = []
       self.llista_bombes = []

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
       for bomba in self.llista_bombes:
           pantalla.blit(bomba.imatge, bomba.rect)

    def mou_plataformes(self, dx_fons):
        for bloc in self.llista_blocs:
            bloc[1].x += dx_fons
        #Optimització del joc: eliminem plataformes fora de pantalla
        self.llista_blocs = [bloc for bloc in self.llista_blocs if bloc[1].right > 0]

        for bomba in self.llista_bombes:
            bomba.rect.x += dx_fons
        self.llista_bombes = [bomba for bomba in self.llista_bombes if bomba.rect.right > 0]

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

        if random.random() < 0.003:
            bomba_x = 0
            bomba_y = 0
            if self.llista_blocs:
                bomba_x = self.llista_blocs[-1][1].x + sett.t_bloc // 2 - sett.t_bomba // 2
                bomba_y = sett.pant_height - sett.t_bloc - sett.t_bloc // 2
            bomba = Bomba(bomba_x, bomba_y)
            self.llista_bombes.append(bomba)
