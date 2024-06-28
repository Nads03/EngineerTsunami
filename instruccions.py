from settings import Settings
from boto import Boto

sett = Settings()

class Instruccions:
    def __init__(self, pantalla, idioma):
        self.pantalla = pantalla
        self.font = sett.font
        self.idioma = idioma
        self.ok_boto = Boto(sett.pant_width // 2 - 50, sett.pant_height - 100, 'Ok')

    def dibuixa(self):
        self.pantalla.fill((245,245,220))
        text_instruccions = {
            'català': "Instruccions: Utilitza l'espai per saltar. \nEvita els forats i les bombes. \nFaràs punts menjant-te persones.",
            'castellà': "Instrucciones: Utiliza el espacio para saltar. \nEvita los agujeros y las bombas. \nHarás puntos comiéndote personas.",
            'anglès': "Instructions: Use the space to jump. \nAvoid the holes and the bombs. \nYou will make points eating people."
        }
        text = text_instruccions[self.idioma]
        linies = text.split('\n')
        vert_pos = 50
        for linia in linies:
            rendered_text = self.font.render(linia, True, (0,0,0))
            self.pantalla.blit(rendered_text, (50, vert_pos))
            vert_pos += rendered_text.get_height() + 10

        self.ok_boto.dibuixa(self.pantalla)
