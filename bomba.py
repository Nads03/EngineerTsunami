from obstacle import Obstacle
from settings import Settings

sett = Settings()

class Bomba(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y, sett.bomba_img, sett.t_bloc // 2, sett.t_bloc // 2)
