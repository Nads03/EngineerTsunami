import pygame
from pygame.locals  import *
import random
from settings import Settings
from jugador import Jugador
from videojoc import Joc
import view

pygame.init()
pygame.font.init()

CLOCK = pygame.time.Clock()

sett = Settings()

pantalla = pygame.display.set_mode((sett.pant_width, sett.pant_height))
pygame.display.set_caption('ZombieNeer')

dades = sett.dades

jugador = Jugador(10,sett.pant_height -130)
joc = Joc(dades)

x = 0
game_over = sett.game_over

font = sett.font

run = True
while run:

    CLOCK.tick(sett.fps)

    if not game_over:
        view.moviment_pantalla(pantalla, sett.pant_width, x, sett.bg_img)
        dx_fons = -1
        x += dx_fons

        joc.mou_plataformes(dx_fons)
        joc.nova_plataforma()
        joc.dibuixa(pantalla)

        for bomba in joc.llista_bombes:
            bomba.update(dx_fons)

        for persona in joc.llista_persones:
            persona.update()

        game_over = jugador.update(joc)
        jugador.dibuixa(pantalla)

        puntuacio = font.render(f'Punts: {jugador.punts}', True, (0,0,0))
        pantalla.blit(puntuacio, (10,10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()