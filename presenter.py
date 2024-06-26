import pygame
from settings import Settings
from jugador import Jugador
from videojoc import Joc
import view

pygame.init()

CLOCK = pygame.time.Clock()

sett = Settings()

pantalla = pygame.display.set_mode((sett.pant_width, sett.pant_height))
pygame.display.set_caption('ZombieNeer')

dades = sett.dades

jugador = Jugador(10,sett.pant_height -130)
joc = Joc(dades)

x = 0
game_over = sett.game_over

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

        game_over = jugador.update(joc)
        pantalla.blit(jugador.imatge, jugador.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()