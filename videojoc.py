#VIEW
import pygame, sys
from pygame.locals import *
from jugador import Jugador
from settings import Settings

def run_game():
    #Inicialitzem pygame, els settings i la pantalla
    pygame.init()
    vg_settings = Settings()
    PANTALLA = pygame.display.set_mode((vg_settings.W, vg_settings.H))
    pygame.display.set_caption('ZOMBIENEER')
    CLOCK = pygame.time.Clock()

    # Fons
    fons = pygame.image.load(vg_settings.bg_image).convert()
    fons_redi = pygame.transform.scale(fons, (vg_settings.W, vg_settings.H))

    # Icona i títol
    icona = pygame.image.load(vg_settings.icon)
    pygame.display.set_icon(icona)

    # Ínicialització personatge
    personatge = Jugador(50,360)

    # Inicialització variable moviment pantalla
    z = 0

    # Bucle del joc
    while True:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Funció moviment pantalla
        moviment_pantalla(PANTALLA, fons_redi, vg_settings, z)
        z -= 1

        #Moviment personatge?
        personatge.space_pressed()

        #Dibuix personatge si hi ha moviment
        personatge.salta()

        pygame.display.flip()
        CLOCK.tick(vg_settings.fps)

def moviment_pantalla(PANTALLA, fons_redi, vg_settings, z):
    z_relativa = z % fons_redi.get_rect().width
    PANTALLA.blit(fons_redi, (z_relativa - fons_redi.get_rect().width, 0))
    if z_relativa < vg_settings.W:
        PANTALLA.blit(fons_redi, (z_relativa, 0))

if __name__ == '__main__':
    run_game()

