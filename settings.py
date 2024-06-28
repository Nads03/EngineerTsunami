import pygame

pygame.font.init()

class Settings():
    def __init__(self):
        self.fps = 100

        self.pant_width = 700
        self.pant_height = 600

        # Carreguem imatges
        self.inici_img = pygame.image.load('imatges/inici.png')
        self.bg_img = pygame.image.load('imatges/cel.jpg')
        self.bloc_img = pygame.image.load('imatges/bloc.JPG')
        self.zombie_img = pygame.image.load('imatges/zombie.png')
        self.bomba_img = pygame.image.load('imatges/bomba.png')
        self.person_img = pygame.image.load('imatges/enginyer.png')

        self.t_bloc = 100
        self.zombie_x = 60
        self.zombie_y = 75
        self.t_bomba = 65

        self.game_over = False

        self.dades = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]]

        # text
        self.font = pygame.font.SysFont('Arial', 24)

        # botons
        self.b_color = (255,0,255)
        self.b_width = 120
        self.b_height = 50
        self.b_color_text = (0,0,0)

        # idiomes
        self.hor_pos = 50

