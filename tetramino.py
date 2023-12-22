from globals import *
import random

def dessiner_tetramino(tetramino):
    x = get_x()
    y = get_y()
    taille_cote = 20
    for coord in tetramino:
        rect_x = x + coord[1] * taille_cote
        rect_y = y + coord[0] * taille_cote
        Py.draw.rect(screen, 'blue', (rect_x, rect_y, taille_cote, taille_cote))
    set_y()

def random_tetramino(tetraminos):
    tetramino = random.choice(tetraminos)
    return tetramino