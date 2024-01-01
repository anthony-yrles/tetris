from globals import *
from globales import *
from collision import *
from remplissage import *
from json_save import *

def dessiner_tetramino(tile_size, new_score):
    menu = get_menu()
    if menu == 1:
        draw_x = grid_start_x + get_tetraminos_x() * tile_size
        draw_y = 0 + get_tetraminos_y() * tile_size
        tetramino = get_tetramino_normal()
    elif menu == 2:
        tile_size = survival_tile_size
        draw_x = survival_grid_start_x + get_survival_tetraminos_x() * survival_tile_size
        draw_y = 0 + get_tetraminos_y() * tile_size
        tetramino = get_tetramino_survival()
    dessiner_tetramino_aux(tetramino, draw_x, draw_y, tile_size)
    if test_collision((0, 1), tetramino):
        set_tetraminos_y(1)
    else:
        if not test_loose():
            if menu == 1:
                set_grid(tetramino, draw_x, draw_y, tile_size)
                set_tetramino_normal(random_tetramino(tetraminos_normal))
                set_tetraminos_x(10)
            elif menu == 2:
                set_survival_grid(tetramino, draw_x, draw_y, tile_size)
                set_tetramino_survival(random_tetramino(tetraminos_survival))
                set_survival_tetraminos_x(7)    
            set_tetraminos_y(0)
            test_ligne()
            dessiner_tetramino_aux(tetramino, draw_x, draw_y, tile_size)
        else:
            if menu == 1:
                save_score(new_score)
            if menu == 2:
                save_time(new_score)
            set_initial_value()
            set_game_end()

def dessiner_tetramino_aux(tetramino, draw_x, draw_y, tile_size):
    if menu == 1:
        tile_size = tile_size
    elif menu == 2:
        tile_size = survival_tile_size
    for coord in tetramino:
        rect_x = draw_x + coord[1] * tile_size
        rect_y = draw_y + coord[0] * tile_size
        Py.draw.rect(screen, get_color(), (rect_x, rect_y, tile_size, tile_size))