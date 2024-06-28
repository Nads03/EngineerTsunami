import pygame
import random
from settings import Settings
from bomba import Bomba
from persona import Persona
from objecte_aeri import ObjecteAeri

sett = Settings()
class Joc():
    def __init__(self, dades):
       self.llista_blocs = []
       self.llista_bombes = []
       self.llista_persones = []
       self.llista_objectes_aeris = []

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
       for persona in self.llista_persones:
           pantalla.blit(persona.imatge, persona.rect)
       for objecte_aeri in self.llista_objectes_aeris:
           pantalla.blit(objecte_aeri.imatge, objecte_aeri.rect)

    def mou_plataformes(self, dx_fons):
        for bloc in self.llista_blocs:
            bloc[1].x += dx_fons
        #Optimització del joc: eliminem plataformes fora de pantalla
        self.llista_blocs = [bloc for bloc in self.llista_blocs if bloc[1].right > 0]

        for bomba in self.llista_bombes:
            bomba.rect.x += dx_fons
        self.llista_bombes = [bomba for bomba in self.llista_bombes if bomba.rect.right > 0]

        for persona in self.llista_persones:
            persona.rect.x += dx_fons
        self.llista_persones = [persona for persona in self.llista_persones if persona.rect.right > 0]

        for objecte_aeri in self.llista_objectes_aeris:
            objecte_aeri.rect.x += dx_fons
        self.llista_objectes_aeris = [objecte_aeri for objecte_aeri in self.llista_objectes_aeris if objecte_aeri.rect.right > 0]

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

        if random.random() < 0.004:
            bomba_x = 0
            bomba_y = 0
            if self.llista_blocs:
                bomba_x = self.llista_blocs[-1][1].x + sett.t_bloc // 2 - sett.t_bomba // 2
                bomba_y = sett.pant_height - sett.t_bloc - sett.t_bloc // 2
            bomba = Bomba(bomba_x, bomba_y)
            coincideix_persona = any(bomba.rect.colliderect(persona.rect) for persona in self.llista_persones)
            if not coincideix_persona:
                self.llista_bombes.append(bomba)

        if random.random() < 0.002:
            persona_x = 0
            persona_y = 0
            if self.llista_blocs:
                persona_x = self.llista_blocs[-1][1].x + sett.t_bloc // 2 - sett.t_bomba // 2
                persona_y = sett.pant_height - 1.75*sett.t_bloc
            persona = Persona(persona_x, persona_y)
            marge = sett.zombie_x
            coincideix_bomba = any(persona.rect.colliderect(bomba.rect) for bomba in self.llista_bombes)
            coincideix_persona = any(persona.rect.colliderect(altre_persona.rect) for altre_persona in self.llista_persones if abs(persona.rect.x - altre_persona.rect.x) < marge)
            if not coincideix_bomba and not coincideix_persona:
                self.llista_persones.append(persona)

        if random.random() < 0.003:
            objecte_aeri_x = sett.pant_width
            objecte_aeri_y = random.randint(0, sett.pant_height - sett.t_bloc*1.25)
            objecte_aeri = ObjecteAeri(objecte_aeri_x, objecte_aeri_y)
            self.llista_objectes_aeris.append(objecte_aeri)

    def update_objectes_aeris(self):
        for objecte_aeri in self.llista_objectes_aeris:
            objecte_aeri.update()

