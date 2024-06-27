from obstacle import Obstacle
from settings import Settings

sett = Settings()

class Persona(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y, sett.person_img, sett.zombie_x, sett.zombie_y)
