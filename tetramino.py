from globals import *
from collision import *

# def dessiner_tetramino(tetramino):
#     draw_x = grid_start_x + get_tetraminos_x() * tile_size
#     draw_y = 0 + get_tetraminos_y() * tile_size
#     taille_cote = 20
#     for coord in tetramino:
#         rect_x = draw_x + coord[1] * taille_cote
#         rect_y = draw_y + coord[0] * taille_cote
#         Py.draw.rect(screen, 'blue', (rect_x, rect_y, taille_cote, taille_cote))
#     if test_collision((0, 1), tetramino):
#         set_tetraminos_y(1)
#     else:
#         set_grid(tetramino, draw_x, draw_y, taille_cote)
#         set_tetraminos_y(0)
#         set_tetraminos_x(10)
#         dessiner_tetramino(tetramino)
        # La piece est arrivée en bas; la rentrer dans la grille et générer une nouvelle pièce
def dessiner_tetramino():
    draw_x = grid_start_x + get_tetraminos_x() * tile_size
    draw_y = 0 + get_tetraminos_y() * tile_size
    taille_cote = 20
    tetramino = get_tetramino()
    dessiner_tetramino_aux(tetramino, draw_x, draw_y, taille_cote)
    if test_collision((0, 1), tetramino):
        set_tetraminos_y(1)
    else:
        set_grid(tetramino, draw_x, draw_y, taille_cote)
        set_tetramino(tetraminos)
        set_tetraminos_y(0)
        set_tetraminos_x(10)
        dessiner_tetramino_aux(tetramino, draw_x, draw_y, taille_cote)

def dessiner_tetramino_aux(tetramino, draw_x, draw_y, taille_cote):
    for coord in tetramino:
        rect_x = draw_x + coord[1] * taille_cote
        rect_y = draw_y + coord[0] * taille_cote
        Py.draw.rect(screen, 'blue', (rect_x, rect_y, taille_cote, taille_cote))
