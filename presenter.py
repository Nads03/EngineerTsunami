import pygame
from pygame.locals  import *
from settings import Settings
from jugador import Jugador
from videojoc import Joc
from boto import Boto
from instruccions import Instruccions
from idioma import Idioma
import view

pygame.init()
pygame.font.init()

CLOCK = pygame.time.Clock()

sett = Settings()

bg_inici  = pygame.transform.scale(sett.inici_img, (sett.pant_width, sett.pant_height))

pantalla = pygame.display.set_mode((sett.pant_width, sett.pant_height))
pygame.display.set_caption('ZombieNeer')
pygame.display.set_icon(sett.zombie_img)

dades = sett.dades

jugador = Jugador(10,sett.pant_height -130)
joc = Joc(dades)

idioma = Idioma(pantalla)
instruccions = Instruccions(pantalla, idioma.selected)

# Botons
play_boto = Boto(sett.pant_width // 2 - 50, sett.pant_height // 2 - 150, 'Juga')
menu_boto = Boto(sett.pant_width // 2 - 50, sett.pant_height // 2 - 25, 'Menú')
restart_boto = Boto(sett.pant_width // 2 - 50, sett.pant_height // 2 + 50, 'Reinicia')
instruccions_boto = Boto(sett.pant_width // 2 - 50, sett.pant_height // 2 - 75, 'Instruccions')
idioma_boto = Boto(sett.pant_width // 2 - 50, sett.pant_height // 2, 'Idioma')
ok_boto = Boto(sett.pant_width // 2 - 50, sett.pant_height // 2 - 75, 'Ok')

# Control del joc
estat_joc = 'inici'
mostrar_idioma = False
seleccio_idioma = None

x = 0
game_over = sett.game_over

font = sett.font

run = True
while run:

    CLOCK.tick(sett.fps)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            if estat_joc == 'inici':
                if play_boto.premut(mouse_pos):
                    estat_joc = 'jugant'

                elif menu_boto.premut(mouse_pos):
                    estat_joc = 'menu'

            elif estat_joc == 'game_over':
                if restart_boto.premut(mouse_pos):
                    jugador = Jugador(10, sett.pant_height - 130)
                    joc = Joc(sett.dades)
                    game_over = False
                    x = 0
                    estat_joc = 'jugant'

                elif menu_boto.premut(mouse_pos):
                    estat_joc = 'menu'

            elif estat_joc == 'menu':
                if play_boto.premut(mouse_pos):
                    estat_joc = 'jugant'

                elif instruccions_boto.premut(mouse_pos):
                    estat_joc = 'instruccions'

                elif idioma_boto.premut(mouse_pos):
                    estat_joc = 'idioma'

            elif estat_joc == 'instruccions':
                if instruccions.ok_boto.premut(mouse_pos):
                    estat_joc = 'menu'

            elif estat_joc == 'idioma':
                selected_idioma = idioma.tria(mouse_pos)
                if selected_idioma:
                    idioma.selected= selected_idioma
                    instruccions.idioma = selected_idioma
                    estat_joc = 'menu'

    if estat_joc == 'inici':
        pantalla.blit(bg_inici, (0,0))
        menu_boto.dibuixa(pantalla)

    elif estat_joc == 'menu':
        pantalla.fill((245, 245, 220))
        play_boto.dibuixa(pantalla)
        instruccions_boto.dibuixa(pantalla)
        idioma_boto.dibuixa(pantalla)

    elif estat_joc == 'jugant':
        if not game_over:
            view.moviment_pantalla(pantalla, sett.pant_width, x, sett.bg_img)
            dx_fons = -1
            x += dx_fons

            joc.mou_plataformes(dx_fons)
            joc.nova_plataforma()
            joc.dibuixa(pantalla)
            joc.update_objectes_aeris()

            for bomba in joc.llista_bombes:
                bomba.update(dx_fons)

            for persona in joc.llista_persones:
                persona.update()

            game_over = jugador.update(joc)
            jugador.dibuixa(pantalla)

            puntuacio = font.render(f'Punts: {jugador.punts}', True, (0,0,0))
            pantalla.blit(puntuacio, (10,10))

        else:
            estat_joc = 'game_over'

    elif estat_joc == 'game_over':
        restart_boto.dibuixa(pantalla)
        menu_boto.dibuixa(pantalla)

    elif estat_joc == 'instruccions':
        instruccions.dibuixa()

    elif estat_joc == 'idioma':
        idioma.dibuixa()

    pygame.display.update()

pygame.quit()