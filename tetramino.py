from globals import *
import random
from collision import *

def dessiner_tetramino(tetramino):
    draw_x = grid_start_x + get_tetraminos_x() * tile_size
    draw_y = 0 + get_tetraminos_y() * tile_size
    taille_cote = 20
    for coord in tetramino:
        rect_x = draw_x + coord[1] * taille_cote
        rect_y = draw_y + coord[0] * taille_cote
        Py.draw.rect(screen, 'blue', (rect_x, rect_y, taille_cote, taille_cote))
    if test_collision((0, 1), tetramino):
        set_tetraminos_y()
    else:
        pass
        # La piece est arrivée en bas; la rentrer dans la grille et générer une nouvelle pièce

def random_tetramino(tetraminos):
    tetramino = random.choice(tetraminos)
    return tetramino