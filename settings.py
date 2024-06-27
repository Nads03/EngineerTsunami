import pygame

class Settings():
    def __init__(self):
        self.fps = 100

        self.pant_width = 700
        self.pant_height = 600

        # Carreguem imatges
        self.bg_img = pygame.image.load('imatges/cel.jpg')
        self.bloc_img = pygame.image.load('imatges/bloc.JPG')
        self.zombie_img = pygame.image.load('imatges/zombie.png')
        self.bomba_img = pygame.image.load('imatges/bomba.png')

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



