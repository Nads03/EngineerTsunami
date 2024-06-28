import random
from objecte import Objecte
from settings import Settings

sett = Settings()

class ObjecteAeri(Objecte):
    def __init__(self, x, y):
        super().__init__(x, y, sett.aeri_img, sett.t_bloc // 2, sett.t_bloc // 2)
        self.velocitat = 3

    def update(self):
        self.rect.x -= self.velocitat
        if self.rect.right < 0:
            self.kill()