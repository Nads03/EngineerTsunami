from objecte import Objecte
from settings import Settings

sett = Settings()

class Persona(Objecte):
    def __init__(self, x, y):
        super().__init__(x, y, sett.person_img, sett.zombie_x, sett.zombie_y)
