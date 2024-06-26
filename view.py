#Funcions del view

def moviment_pantalla(pantalla, pant_width, x, bg_img):
    x_rel = x % pant_width
    pantalla.blit(bg_img, (x_rel - pant_width, 0))
    if x_rel < pant_width:
        pantalla.blit(bg_img, (x_rel, 0))